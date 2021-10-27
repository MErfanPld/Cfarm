from django.db.models.query import QuerySet
from rest_framework import generics, serializers
from rest_framework.response import Response
from .serializers import Daily_Informations_Serializer 
from ..models import Daily_Informations

class Daily_Informations_CreateApi (generics.CreateAPIView) :
    QuerySet = Daily_Informations.objects.all()
    serializer_class = Daily_Informations_Serializer