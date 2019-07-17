from django.urls import path
from apps.user.views import home, login, register

urlpatterns = [
    path('', home),
    path('login', login),
    path('register', register),
]