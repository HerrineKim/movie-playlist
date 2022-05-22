# accounts/admin.py
# admin site에 Custom User 모델 등록

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)