from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class FacultyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class AdminProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
