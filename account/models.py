from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    follows = models.ManyToManyField("self", symmetrical=False, related_name='followers', blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def follow(self, user):
        self.follows.add(user)

    def unfollow(self, user):
        self.follows.remove(user)

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва курсу")
    description = models.TextField(verbose_name="Опис курсу")
    start_date = models.DateField(verbose_name="Дата початку")
    end_date = models.DateField(verbose_name="Дата закінчення")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"
        ordering = ['start_date']


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Учень")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="Дата запису")

    def __str__(self):
        return f"{self.student.username} записаний на {self.course.name}"

    class Meta:
        verbose_name = "Запис на курс"
        verbose_name_plural = "Записи на курси"
        unique_together = ['student', 'course']  
