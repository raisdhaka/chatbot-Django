from django.urls import path
from .views import  ChatbotAPIView, ChatbotWelcomeAPIView, ChatbotResponseAPIView

urlpatterns = [
    path('welcome/', ChatbotWelcomeAPIView.as_view(), name='chatbot_welcome'),
    path('chat/', ChatbotAPIView.as_view(), name='chatbot_api'),
    path('response/<int:question_id>/', ChatbotResponseAPIView.as_view(), name='chatbot_response'),
]
