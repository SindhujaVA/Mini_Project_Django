from django.urls import  path
from . import views


urlpatterns=[
    path('form/', views.login),
    path('auth/',views.UserAuth.as_view()),
    path('register/',views.register),
    path('profile/',views.profile),
    ]