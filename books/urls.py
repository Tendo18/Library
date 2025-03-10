from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryAPIView.as_view()),
    path('', BookAPIView.as_view()),
]