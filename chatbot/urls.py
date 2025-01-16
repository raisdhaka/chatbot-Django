from django.urls import path
from .views import ChatbotAPIView, InitialView

urlpatterns = [
    path('chat/', ChatbotAPIView.as_view(), name='chatbot_api'),
    path('initial/', InitialView, name='initial_view')
]
