from django.shortcuts import render, redirect
from .models import Course

def index(request):
    return render(request, 'course_bot/index.html')

def process(request):
    return redirect('/')
