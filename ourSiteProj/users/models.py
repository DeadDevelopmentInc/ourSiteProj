from django.db import models

class Student(models.Model):
    first_name = models.CharField(
        max_length = 255,
    )
    last_name = models.CharField(
        max_length = 255,
    )
    passwords = models.CharField(
        max_length = 255,
    )
    email = models.EmailField()

class Worker(models.Model):
    first_name = models.CharField(
        max_length = 255,
    )
    last_name = models.CharField(
        max_length = 255,
    )
    passwords = models.CharField(
        max_length = 255,
    )
    email = models.EmailField()
