# Text-Semantics
Text Semantics aims to quantify the similarity dynamics of texts exploring semantic similarity, token based n gram similarity, paragraph similarity as well as hybrid similairty which can be used across other pipelines and NLP usecases. 

It mainly performs three kinds of similarities:
    1. Overall Semantic Similarity (Hybrid) ---> Weightage of all 
    2. Token based similarity ---> Similarity between each token
    3. Paragraph based similarity ----> Similarity between paragraphs
    4. Embedding based similarity ---> Embedding semantic similarity

## Endpoints

BASE URL: `http://127.0.0.1:8000/text-similarity`

- **Ensure Endpoint**

  - URL: `/ensure`
  - Description: Endpoint for ensuring that the API is running properly.
  - Method: GET

- **Overall Similarity Score Endpoint**

  - URL: `/similarity-score/overall`
  - Description: Endpoint for calculating the overall similarity score between two text paragraphs using a hybrid approach combining token-based F1 score, paragraph-based F1 score, and embedding similarity.
  - Method: POST
  - Request Body:
    ```json
    {
      "text1": "First text paragraph...",
      "text2": "Second text paragraph..."
    }
    ```
  - Response Body:
    ```json
    {
      "similarity score": 0.88
    }
    ```

- **Token Similarity Score Endpoint**

  - URL: `/similarity-score/token`
  - Description: Endpoint for calculating the token-based similarity score between two text paragraphs using F1 score.
  - Method: POST
  - Request Body: Same as Overall Similarity Score Endpoint
  - Response Body: Same as Overall Similarity Score Endpoint

- **Paragraph Similarity Score Endpoint**

  - URL: `/similarity-score/paragraph`
  - Description: Endpoint for calculating the paragraph-based similarity score between two text paragraphs using F1 score.
  - Method: POST
  - Request Body: Same as Overall Similarity Score Endpoint
  - Response Body: Same as Overall Similarity Score Endpoint

- **Embedding Similarity Score Endpoint**

  - URL: `/similarity-score/embedding`
  - Description: Endpoint for calculating the embedding-based similarity score between two text paragraphs using cosine similarity.
  - Method: POST
  - Request Body: Same as Overall Similarity Score Endpoint
  - Response Body: Same as Overall Similarity Score Endpoint

## Getting Started

To run the API locally, follow these steps:

1. Clone this repository
2. Install Python and Django.
3. Copy the repository files to the instance.
4. Install dependencies using pip install -r requirements.txt.
5. Run the Django server using python manage.py runserver.

Ensure that the appropriate firewall rules and network configurations are set up to allow incoming traffic on the specified port.

Github: https://github.com/cosmiiccat/Text-Semantics




