from rest_framework.decorators import api_view
from rest_framework.response import Response
from .llm import ask_llm
from .retrieval import find_best_doc
# Create your views here.

@api_view(['POST'])
def ask(request):
    question = request.data.get ('question')
    context = find_best_doc(question)
    return Response (ask_llm(question, context))


