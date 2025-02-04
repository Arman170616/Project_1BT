from rest_framework import serializers
from .models import HomePageContent

class HomePageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageContent
        fields = ['title_en', 'title_fr', 'description_en', 'description_fr']