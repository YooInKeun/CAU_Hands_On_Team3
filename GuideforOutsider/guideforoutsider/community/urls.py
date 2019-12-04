from django.urls import path

from . import views


app_name = 'community'
urlpatterns = [
    path('lecture/', views.lecture, name='lecture'),
    path('lecture/query/', views.query_lecture, name='query_lecture'),
    path('lecture/detail/<int:pk>/', views.lecture_detail, name='lecture_detail'),
    path('board/create/<int:pk>/', views.create_board, name='create_board'),
    path('board/create/complete/<int:pk>/', views.complete_create_board, name='complete_create_board'),
]