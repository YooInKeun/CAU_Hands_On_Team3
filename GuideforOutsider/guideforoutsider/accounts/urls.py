from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url

from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.ConfirmIsValidUserView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.CreateUserView.as_view(), name='signup'),
    path('signup/done/', views.RegisteredView.as_view(), name='create_user_done'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('message/', views.message, name='message'),
    path('create/message/<int:pk>', views.create_message, name='create_message'),
    path('delete/message/<int:pk>', views.delete_message, name='delete_message'),
]