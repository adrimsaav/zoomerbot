from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
import uuid
import boto3
import os 

def home(request):
  return render(request, 'home.html')

