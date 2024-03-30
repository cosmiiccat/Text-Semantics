
from sentence_transformers import (
    SentenceTransformer, 
    util)
from collections import Counter
import argparse
import string
import re
import os
import json

# from dotenv import load_dotenv

# load_dotenv("config.env")

# EMBEDDING_MODEL_NAME = os.getenv('EMBEDDING_MODEL_NAME')

EMBEDDING_MODEL_NAME = 'all-MiniLM-L6-v2'

class SemanticSimilarity:

    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL_NAME)
        self.weightage = [
            1.0,
            1.0,
            1.0
        ]
        self.max_weight_dist = sum(
            self.weightage
        )

    def normalize_answer(self, s):

        def remove_articles(text):
            return re.sub(r"\b(a|an|the)\b", " ", text)

        def white_space_fix(text):
            return " ".join(text.split())

        def remove_punc(text):
            exclude = set(string.punctuation)
            return "".join(ch for ch in text if ch not in exclude)

        def lower(text):
            return text.lower()

        return white_space_fix(remove_articles(remove_punc(lower(s))))


    def token_f1_score(self, prediction, ground_truth):
    
        prediction_tokens = self.normalize_answer(prediction).split()
        ground_truth_tokens = self.normalize_answer(ground_truth).split()
        common = Counter(prediction_tokens) & Counter(ground_truth_tokens)
        num_same = sum(common.values())
        if num_same == 0:
            return 0
        precision = 1.0 * num_same / len(prediction_tokens)
        recall = 1.0 * num_same / len(ground_truth_tokens)
        f1 = (2 * precision * recall) / (precision + recall)
        return f1


    def paragraph_f1_score(self, prediction, ground_truth):
        if not ground_truth and not prediction:
            return 1.0
        num_same = len(set(ground_truth).intersection(set(prediction)))
        if num_same == 0:
            return 0.0
        precision = num_same / len(prediction)
        recall = num_same / len(ground_truth) 
        f1 = (2 * precision * recall) / (precision + recall)
        return f1

    def embeddingSimilarity(self, prediction, ground_truth):

        embedding1 = self.model.encode(prediction, convert_to_tensor=True)
        embedding2 = self.model.encode(ground_truth, convert_to_tensor=True)

        cosine_similarity = util.pytorch_cos_sim(embedding1, embedding2)

        return cosine_similarity.item()

    def hybridSimilarity(self, prediction, ground_truth):
        
        hybrid_similarity_scores = [
            self.token_f1_score(
                prediction = prediction,
                ground_truth = ground_truth
            ),

            self.paragraph_f1_score(
                prediction = prediction,
                ground_truth = ground_truth
            ),

            self.embeddingSimilarity(
                prediction = prediction,
                ground_truth = ground_truth
            )
        ]

        weighted_scores = list(map(lambda x, y: x * y, hybrid_similarity_scores, self.weightage))
        weighted_total = sum(weighted_scores)
        expected_score = weighted_total/self.max_weight_dist

        return expected_score



