from django.urls import path

from . import views 

urlpatterns = [
    path('register/', views.register, name='regoster'),
    path('login/', views.login, name='login'),
]