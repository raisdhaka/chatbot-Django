from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .nltk_chatbot import get_response
import nltk
from django.http import HttpResponse

class ChatbotAPIView(APIView):
    def post(self, request):
        user_input = request.data.get('message')
        if not user_input:
            return Response({"error": "Message field is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        bot_response = get_response(user_input)
        return Response({"response": bot_response}, status=status.HTTP_200_OK)

def InitialView(request):
    nltk.download('punkt')
    nltk.download('stopwords')
    return HttpResponse("nltk packages downloaded successfully",  status=status.HTTP_200_OK, content_type='text/plain')
