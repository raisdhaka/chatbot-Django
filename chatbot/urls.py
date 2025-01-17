from django.urls import path
from .views import  ChatbotWelcomeAPIView, ChatbotResponseAPIView

urlpatterns = [
    path('welcome/', ChatbotWelcomeAPIView.as_view(), name='chatbot_welcome'),
    path('response/<int:question_id>/', ChatbotResponseAPIView.as_view(), name='chatbot_response'),
]
