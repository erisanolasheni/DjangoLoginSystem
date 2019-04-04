from django.urls import path
from .views import home, user_login, register, logout_user

urlpatterns = [
    path('', home, name='home'),
    path('login', user_login, name='login'),
    path('register', register, name='register'),
    path('logout', logout_user, name='logout')
]