from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator

def lecture(request):
    lectures = Lecture.objects.all().order_by('-id')
    post_paginator = Paginator(lectures, 7)
    page = request.GET.get('page')
    lectures = post_paginator.get_page(page)
    return render(request, 'community/lecture.html', {'lectures' : lectures})