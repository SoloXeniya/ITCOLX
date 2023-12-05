from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter


from .models import Category, Ads
from.serializers import CategorySerializers, AdsSerializers

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [permissions.AllowAny]
    
    
class AdsViewSet(viewsets.ModelViewSet):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializers
    permission_classes = [permissions.AllowAny]