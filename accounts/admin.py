from django.contrib import admin
from .models import Profile
from django.utils.safestring import mark_safe


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user__username', 'user__is_active', 'user__is_staff', 'user__date_joined']
    search_fields = ['user__username']
    
    def photo(self, obj):
        if obj.image:
            return mark_safe(f"<img src = '{obj.photo.url}' width= '100' height='100'/>") 
        else:
            return "Нет фото"
    

