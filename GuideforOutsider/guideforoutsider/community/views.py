from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator

def lecture(request):
    if request.user.is_authenticated is False:
        return redirect('accounts:login')
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
    
    study_replys = Reply.objects.filter(board__board_category__board_category="스터디", board__lecture=pk)
    teamply_replys = Reply.objects.filter(board__board_category__board_category="팀플", board__lecture=pk)
    review_replys = Reply.objects.filter(board__board_category__board_category="강의 후기", board__lecture=pk)

    studies = Board.objects.filter(board_category__board_category="스터디", lecture=pk)
    teamplays = Board.objects.filter(board_category__board_category="팀플", lecture=pk)
    reviews = Board.objects.filter(board_category__board_category="강의 후기", lecture=pk)
    return render(request, 'community/lecture_detail.html', {'study_replys':study_replys, 'teamplay_replys':teamply_replys, 'review_replys':review_replys, 'lecture_name':lecture_name, 'lecture_pk':lecture_pk, 'studies':studies, 'teamplays':teamplays, 'reviews':reviews})

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
    
    study_replys = Reply.objects.filter(board__board_category__board_category="스터디", board__lecture=pk)
    teamply_replys = Reply.objects.filter(board__board_category__board_category="팀플", board__lecture=pk)
    review_replys = Reply.objects.filter(board__board_category__board_category="강의 후기", board__lecture=pk)

    studies = Board.objects.filter(board_category__board_category="스터디", lecture=pk)
    teamplays = Board.objects.filter(board_category__board_category="팀플", lecture=pk)
    reviews = Board.objects.filter(board_category__board_category="강의 후기", lecture=pk)
    return render(request, 'community/lecture_detail.html', {'study_replys':study_replys, 'teamplay_replys':teamply_replys, 'review_replys':review_replys, 'lecture_name':lecture_name, 'lecture_pk':lecture_pk, 'studies':studies, 'teamplays':teamplays, 'reviews':reviews})

def update_board(request, pk):
    board_pk = pk
    selected_board= Board.objects.filter(pk=board_pk)[0]
    lecture_pk = selected_board.lecture.pk
    return render(request, 'community/update_board.html', {'board_pk':board_pk, 'selected_board':selected_board, 'lecture_pk':lecture_pk})

def complete_update_board(request, pk):
    board_pk = pk
    board_is_completed = False
    board= Board.objects.filter(pk=board_pk)[0]
    board.title = request.POST['title']
    board.content = request.POST['content']

    if str(request.POST['is_completed']) == '완료':
        board_is_completed = True
    elif str(request.POST['is_completed']) == '미완료':
        board_is_completed = False

    board.is_completed = board_is_completed
    board.save()

    lecture_name = board.lecture.lecture_name
    lecture_pk = board.lecture.pk

    study_replys = Reply.objects.filter(board__board_category__board_category="스터디", board__lecture=lecture_pk)
    teamply_replys = Reply.objects.filter(board__board_category__board_category="팀플", board__lecture=lecture_pk)
    review_replys = Reply.objects.filter(board__board_category__board_category="강의 후기", board__lecture=lecture_pk)

    studies = Board.objects.filter(board_category__board_category="스터디", lecture=lecture_pk)
    teamplays = Board.objects.filter(board_category__board_category="팀플", lecture=lecture_pk)
    reviews = Board.objects.filter(board_category__board_category="강의 후기", lecture=lecture_pk)
    return render(request, 'community/lecture_detail.html', {'study_replys':study_replys, 'teamplay_replys':teamply_replys, 'review_replys':review_replys, 'lecture_name':lecture_name, 'lecture_pk':lecture_pk, 'studies':studies, 'teamplays':teamplays, 'reviews':reviews})

def delete_board(request, pk):
    board_pk = pk
    board= Board.objects.get(pk=board_pk)
    lecture_name = board.lecture.lecture_name
    lecture_pk = board.lecture.pk
    board.delete()

    study_replys = Reply.objects.filter(board__board_category__board_category="스터디", board__lecture=lecture_pk)
    teamply_replys = Reply.objects.filter(board__board_category__board_category="팀플", board__lecture=lecture_pk)
    review_replys = Reply.objects.filter(board__board_category__board_category="강의 후기", board__lecture=lecture_pk)

    studies = Board.objects.filter(board_category__board_category="스터디", lecture=lecture_pk)
    teamplays = Board.objects.filter(board_category__board_category="팀플", lecture=lecture_pk)
    reviews = Board.objects.filter(board_category__board_category="강의 후기", lecture=lecture_pk)
    return render(request, 'community/lecture_detail.html', {'study_replys':study_replys, 'teamplay_replys':teamply_replys, 'review_replys':review_replys, 'lecture_name':lecture_name, 'lecture_pk':lecture_pk, 'studies':studies, 'teamplays':teamplays, 'reviews':reviews})

def create_reply(request, pk):
    reply = Reply()
    reply.user = request.user
    reply.board = Board.objects.get(pk=pk)
    reply.content = request.POST['reply']
    reply.save()

    board_pk = pk
    board= Board.objects.get(pk=board_pk)
    lecture_name = board.lecture.lecture_name
    lecture_pk = board.lecture.pk

    study_replys = Reply.objects.filter(board__board_category__board_category="스터디", board__lecture=lecture_pk)
    teamply_replys = Reply.objects.filter(board__board_category__board_category="팀플", board__lecture=lecture_pk)
    review_replys = Reply.objects.filter(board__board_category__board_category="강의 후기", board__lecture=lecture_pk)

    studies = Board.objects.filter(board_category__board_category="스터디", lecture=lecture_pk)
    teamplays = Board.objects.filter(board_category__board_category="팀플", lecture=lecture_pk)
    reviews = Board.objects.filter(board_category__board_category="강의 후기", lecture=lecture_pk)
    return render(request, 'community/lecture_detail.html', {'study_replys':study_replys, 'teamplay_replys':teamply_replys, 'review_replys':review_replys, 'lecture_name':lecture_name, 'lecture_pk':lecture_pk, 'studies':studies, 'teamplays':teamplays, 'reviews':reviews})

def update_reply(request, pk):
    reply = Reply.objects.get(pk=pk)
    reply.content = request.POST['reply']
    reply.save()
    reply = Reply.objects.get(pk=pk)
    board_pk = reply.board.pk
    board= Board.objects.get(pk=board_pk)
    lecture_name = board.lecture.lecture_name
    lecture_pk = board.lecture.pk

    study_replys = Reply.objects.filter(board__board_category__board_category="스터디", board__lecture=lecture_pk)
    teamply_replys = Reply.objects.filter(board__board_category__board_category="팀플", board__lecture=lecture_pk)
    review_replys = Reply.objects.filter(board__board_category__board_category="강의 후기", board__lecture=lecture_pk)

    studies = Board.objects.filter(board_category__board_category="스터디", lecture=lecture_pk)
    teamplays = Board.objects.filter(board_category__board_category="팀플", lecture=lecture_pk)
    reviews = Board.objects.filter(board_category__board_category="강의 후기", lecture=lecture_pk)
    return render(request, 'community/lecture_detail.html', {'study_replys':study_replys, 'teamplay_replys':teamply_replys, 'review_replys':review_replys, 'lecture_name':lecture_name, 'lecture_pk':lecture_pk, 'studies':studies, 'teamplays':teamplays, 'reviews':reviews})

def complete_update_reply(request, pk):
    board_pk = pk
    board= Board.objects.filter(pk=board_pk)[0]
    board.title = request.POST['title']
    board.content = request.POST['content']
    board.save()

    lecture_name = board.lecture.lecture_name
    lecture_pk = board.lecture.pk

    study_replys = Reply.objects.filter(board__board_category__board_category="스터디", board__lecture=lecture_pk)
    teamply_replys = Reply.objects.filter(board__board_category__board_category="팀플", board__lecture=lecture_pk)
    review_replys = Reply.objects.filter(board__board_category__board_category="강의 후기", board__lecture=lecture_pk)

    studies = Board.objects.filter(board_category__board_category="스터디", lecture=lecture_pk)
    teamplays = Board.objects.filter(board_category__board_category="팀플", lecture=lecture_pk)
    reviews = Board.objects.filter(board_category__board_category="강의 후기", lecture=lecture_pk)
    return render(request, 'community/lecture_detail.html', {'study_replys':study_replys, 'teamplay_replys':teamply_replys, 'review_replys':review_replys, 'lecture_name':lecture_name, 'lecture_pk':lecture_pk, 'studies':studies, 'teamplays':teamplays, 'reviews':reviews})

def delete_reply(request, pk):
    reply_pk = pk
    reply= Reply.objects.get(pk=reply_pk)
    lecture_name = reply.board.lecture.lecture_name
    lecture_pk = reply.board.lecture.pk
    reply.delete()

    study_replys = Reply.objects.filter(board__board_category__board_category="스터디", board__lecture=lecture_pk)
    teamply_replys = Reply.objects.filter(board__board_category__board_category="팀플", board__lecture=lecture_pk)
    review_replys = Reply.objects.filter(board__board_category__board_category="강의 후기", board__lecture=lecture_pk)

    studies = Board.objects.filter(board_category__board_category="스터디", lecture=lecture_pk)
    teamplays = Board.objects.filter(board_category__board_category="팀플", lecture=lecture_pk)
    reviews = Board.objects.filter(board_category__board_category="강의 후기", lecture=lecture_pk)
    return render(request, 'community/lecture_detail.html', {'study_replys':study_replys, 'teamplay_replys':teamply_replys, 'review_replys':review_replys, 'lecture_name':lecture_name, 'lecture_pk':lecture_pk, 'studies':studies, 'teamplays':teamplays, 'reviews':reviews})

def create_message(request, pk):
    user_pk = pk
    lecture_pk = request.POST['lecture_pk']
    lecture_name = Lecture.objects.get(pk=lecture_pk).lecture_name

    message = Message()
    message.sender = request.user
    message.receiver = User.objects.get(pk=user_pk)
    message.board = Board.objects.filter(lecture__pk=lecture_pk)[0]
    message.content = request.POST['message']
    message.save()

    study_replys = Reply.objects.filter(board__board_category__board_category="스터디", board__lecture=lecture_pk)
    teamply_replys = Reply.objects.filter(board__board_category__board_category="팀플", board__lecture=lecture_pk)
    review_replys = Reply.objects.filter(board__board_category__board_category="강의 후기", board__lecture=lecture_pk)

    studies = Board.objects.filter(board_category__board_category="스터디", lecture=lecture_pk)
    teamplays = Board.objects.filter(board_category__board_category="팀플", lecture=lecture_pk)
    reviews = Board.objects.filter(board_category__board_category="강의 후기", lecture=lecture_pk)
    return render(request, 'community/lecture_detail.html', {'study_replys':study_replys, 'teamplay_replys':teamply_replys, 'review_replys':review_replys, 'lecture_name':lecture_name, 'lecture_pk':lecture_pk, 'studies':studies, 'teamplays':teamplays, 'reviews':reviews})