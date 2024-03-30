
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from utils import custom_exceptions
from django.http import JsonResponse

from rest_framework.decorators import api_view

import json
import os
from . import similarity_client


# Create your views here.
@api_view(['GET'])
def ensure(request):
    try:
        if request.method != "GET":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        response = {"success": "true", "status": "online"}
        return JsonResponse(response)
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})


@api_view(['POST'])
@csrf_exempt 
def similarity_score(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["text1", "text2"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        resp = {
            "similarity score": similarity_client.hybridSimilarity(
                prediction=req_data['text1'], 
                ground_truth=req_data['text2']
            )
        }
        return JsonResponse(resp)
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    
@api_view(['POST'])
@csrf_exempt 
def token_score(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["text1", "text2"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        resp = {
            "similarity score": similarity_client.token_f1_score(
                prediction=req_data['text1'], 
                ground_truth=req_data['text2']
            )
        }
        return JsonResponse(resp)
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    
@api_view(['POST'])
@csrf_exempt 
def paragraph_score(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["text1", "text2"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        resp = {
            "similarity score": similarity_client.paragraph_f1_score(
                prediction=req_data['text1'], 
                ground_truth=req_data['text2']
            )
        }
        return JsonResponse(resp)
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})
    
@api_view(['POST'])
@csrf_exempt 
def embedding_score(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["text1", "text2"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        resp = {
            "similarity score": similarity_client.embeddingSimilarity(
                prediction=req_data['text1'], 
                ground_truth=req_data['text2']
            )
        }
        return JsonResponse(resp)
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})