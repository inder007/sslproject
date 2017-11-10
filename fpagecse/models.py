from django.db import models


class Faculty(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    faculty_name = models.CharField(max_length=300)
    department = models.CharField(max_length=300)
    designation = models.CharField(max_length=250)
    phone = models.BigIntegerField()
    email = models.EmailField()
    room_no = models.CharField(max_length=20)

    def __str__(self):
        return self.faculty_name


# class LoginUser(models.Model):
#     user = models.ForeignKey(Faculty, on_delete=models.CASCADE)
#
#
#     def __str__(self):
#         return self.username
