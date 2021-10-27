from django.urls import path
from .view import Daily_Informations_CreateApi

urlpatterns = [
    path('create/',Daily_Informations_CreateApi.as_view()),
]