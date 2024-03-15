from django.contrib import admin
from django.contrib.auth.models import User
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User
    # display name on admin page
    fields = ["name"]