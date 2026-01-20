from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register'),
    path('login/', views.login_view, name='login'),
    path('courses/', views.courses_list, name='courses_list'),
    path('courses/enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
]
