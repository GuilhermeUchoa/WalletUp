from rest_framework import serializers
from . models import PortfolioModels, AtivosModels
from django.contrib.auth import get_user_model

class AtivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtivosModels
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioModels
        fields = '__all__'

