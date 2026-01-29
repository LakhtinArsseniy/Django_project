from django.shortcuts import render, redirect
from django.contrib.auth import login

from account.forms import RegistrationForm, LoginForm
from account.models import User
from django.contrib import messages
from .models import Course, Enrollment
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            return redirect('login')
    return render(request, 'account/register.html', {'form': form})


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    return render(request, 'account/login.html', {'form': form})


@login_required
def enroll_course(request, course_id):
    course = Course.objects.get(id=course_id)
    student = request.user
    if Enrollment.objects.filter(student=student, course=course).exists():
        messages.warning(request, "Ви вже записані на цей курс.")
    else:
        Enrollment.objects.create(student=student, course=course)
        messages.success(request, f"Ви успішно записані на курс: {course.name}")

    return redirect('courses_list')

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'account/courses_list.html', {'courses': courses})
