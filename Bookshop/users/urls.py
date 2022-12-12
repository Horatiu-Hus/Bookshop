from django.urls import path, include
from django.contrib.auth.views import LoginView
from users.views import profile_view, register_view

app_name = 'users'

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('login/', LoginView.as_view(template_name='users/login.html')),
    path('register/', register_view, name='register'),
    path('', include('django.contrib.auth.urls')),
]
