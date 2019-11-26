from django.urls import path

from . import views


app_name = 'community'
urlpatterns = [
    path('lecture/', views.lecture, name='lecture'),
    path('lecture/query/', views.query_lecture, name='query_lecture'),
]