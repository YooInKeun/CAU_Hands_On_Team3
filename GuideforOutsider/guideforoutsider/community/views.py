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

def lecture_detail(request, pk):
    lecture_pk = pk
    lecture_name = Lecture.objects.get(pk=lecture_pk).lecture_name
    
    studies = Board.objects.filter(board_category__board_category="스터디", lecture=pk)
    teamplays = Board.objects.filter(board_category__board_category="팀플", lecture=pk)
    reviews = Board.objects.filter(board_category__board_category="강의 후기", lecture=pk)
    return render(request, 'community/lecture_detail.html', {'lecture_name':lecture_name, 'lecture_pk':lecture_pk, 'studies':studies, 'teamplays':teamplays, 'reviews':reviews})

def create_board(request, pk):
    lecture_pk = pk
    selected_lecture= Lecture.objects.filter(pk=pk)[0]
    return render(request, 'community/create_board.html', {'lecture_pk':lecture_pk, 'selected_lecture':selected_lecture})

def complete_create_board(request, pk):
    lecture_pk = pk
    lecture_name = Lecture.objects.get(pk=lecture_pk).lecture_name

    board = Board()
    board.user = request.user
    board.board_category = Board_Category.objects.get(board_category=request.POST['category'])
    board.lecture = Lecture.objects.get(pk=lecture_pk)
    board.title = request.POST['title']
    board.content = request.POST['content']
    board.save()

    studies = Board.objects.filter(board_category__board_category="스터디", lecture=pk)
    teamplays = Board.objects.filter(board_category__board_category="팀플", lecture=pk)
    reviews = Board.objects.filter(board_category__board_category="강의 후기", lecture=pk)
    return render(request, 'community/lecture_detail.html', {'lecture_name':lecture_name, 'lecture_pk':lecture_pk, 'studies':studies, 'teamplays':teamplays, 'reviews':reviews})

def update_board(request, pk):
    board_pk = pk
    selected_board= Board.objects.filter(pk=board_pk)[0]
    return render(request, 'community/update_board.html', {'board_pk':board_pk, 'selected_board':selected_board})

def complete_update_board(request, pk):
    lecture_pk = pk
    selected_lecture= Lecture.objects.filter(pk=pk)[0]
    return render(request, 'community/create_board.html', {'lecture_pk':lecture_pk, 'selected_lecture':selected_lecture})

def delete_board(request, pk):
    lecture_pk = pk
    selected_lecture= Lecture.objects.filter(pk=pk)[0]
    return render(request, 'community/create_board.html', {'lecture_pk':lecture_pk, 'selected_lecture':selected_lecture})