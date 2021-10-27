from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from ..models import Daily_Informations

class Daily_Informations_Serializer (serializers.ModelSerializer) :
    class Meta :
        model = Daily_Informations
        fields = '__all__'