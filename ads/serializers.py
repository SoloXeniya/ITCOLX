from rest_framework import serializers

from .models import Category, Ads

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class AdsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = '__all__'
        
        