from django.urls import path

from . import views


app_name = 'community'
urlpatterns = [
    path('lecture/', views.lecture, name='lecture'),
    path('lecture/query/', views.query_lecture, name='query_lecture'),
    path('lecture/detail/<int:pk>/', views.lecture_detail, name='lecture_detail'),

    path('board/create/<int:pk>/', views.create_board, name='create_board'),
    path('board/create/complete/<int:pk>/', views.complete_create_board, name='complete_create_board'),
    path('board/update/<int:pk>/', views.update_board, name='update_board'),
    path('board/update/complete/<int:pk>/', views.complete_update_board, name='complete_update_board'),
    path('board/delete/<int:pk>/', views.delete_board, name='delete_board'),
    
    path('board/reply/create/<int:pk>/', views.create_reply, name='create_reply'),
    path('board/reply/update/<int:pk>/', views.update_reply, name='update_reply'),
    path('board/reply/update/complete/<int:pk>/', views.complete_update_reply, name='complete_update_reply'),
    path('board/reply/delete/<int:pk>/', views.delete_reply, name='delete_reply'),

    path('message/create/<int:pk>/', views.create_message, name='create_message'),
]