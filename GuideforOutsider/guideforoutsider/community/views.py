from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator

def lecture(request):
    lectures = Lecture.objects.all().order_by('-id')
    post_paginator = Paginator(lectures, 7)
    page = request.GET.get('page')
    lectures = post_paginator.get_page(page)
    return render(request, 'community/lecture.html', {'lectures' : lectures})

def query_lecture(request):
    if request.GET['category'] == '강의명':
        lectures = Lecture.objects.filter(lecture_name__contains=request.GET['content']).order_by('-id')
    elif request.GET['category'] == '교수명':
        lectures = Lecture.objects.filter(professor_name=request.GET['content']).order_by('-id')
    elif request.GET['category'] == '전공/교양':
        lectures = Lecture.objects.filter(completion_division=request.GET['content']).order_by('-id')
    elif request.GET['category'] == '학년':
        lectures = Lecture.objects.filter(grade=request.GET['content']).order_by('-id')
    
    searched_category = request.GET['category']
    searched_content = request.GET['content']
    return render(request, 'community/lecture.html', {'lectures':lectures, 'searched_category':searched_category, 'searched_content':searched_content})