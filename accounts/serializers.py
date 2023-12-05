from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
     
       
class ProfileSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
       
    class Meta:
        model = Profile
        fields = '__all__'  
        
