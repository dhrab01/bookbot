from django.contrib import admin
from .models import profile

# Register your models here.
@admin.register(profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']
