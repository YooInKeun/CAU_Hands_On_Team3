from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator

def lecture(request):
    lectures = Lecture.objects.all()
    return render(request, 'community/lecture.html', {'lectures' : lectures})