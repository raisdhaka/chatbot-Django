from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_chatbot_data

class ChatbotWelcomeAPIView(APIView):
    def get(self, request):
        data = get_chatbot_data('responses.json')  # Or None for database
        return Response(
            {
                "welcome_message": data["welcome_message"],
                "questions": [{"id": q["id"], "short_text": q["short_text"]} for q in data["questions"]],
            },
            status=status.HTTP_200_OK,
        )

class ChatbotResponseAPIView(APIView):
    def get(self, request, question_id):
        data = get_chatbot_data('responses.json')  # Or None for database
        question = next((q for q in data["questions"] if q["id"] == question_id), None)
        if question:
            return Response({"response": question["response"]}, status=status.HTTP_200_OK)
        return Response({"error": "Question not found."}, status=status.HTTP_404_NOT_FOUND)