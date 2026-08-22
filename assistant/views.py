from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .llm import ask_llm
# Create your views here.

@api_view(['POST'])
def ask(request):
    question = request.data.get ('question')
    return Response (ask_llm(question))


