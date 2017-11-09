from django.db import models


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    photo = models.FileField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    room_no = models.CharField(max_length=20, default='DEFAULT VALUE')



