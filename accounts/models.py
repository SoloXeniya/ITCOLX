from django.db import models
from django.contrib.auth.models import User


#class Users(models.Model):
    # """
    # username = models.Charfield()
    # email = models.EmailField()
    # password = models.CharField()
    # password1 = models.CharField()
    
    # first_name = models.CharField()
    # last_name = models.CharField()
    
    # data_joined = models.DateTimeField()
    # created_at = models.DateTimeField()
    
    # is_staff = models.BooleanField()
    
    # is_active = models.BooleanField()
    # is_superuser = models.BooleanField()
    
    # """

class Profile(models.Model):
    image = models.ImageField(upload_to='profile_pics/', blank=True, null = True, verbose_name = "Изображения")
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = "Пользователь")
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Учетная запись'
        verbose_name_plural = 'Учетные записи'
    
    


# Profile
#    id image         user_id
#    1  img.png        1

# User
#    id username и т.д
#    1   marselle 
   
   
# {{ profile.image.url }}
# {{ profile.user.username }}