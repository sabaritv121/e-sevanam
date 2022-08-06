from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_govt = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class Department(models.Model):
    name= models.CharField(max_length=200)
    place= models.CharField(max_length=200)
    contact_number= models.CharField(max_length=100)
    email= models.EmailField()

    def __str__(self):
        return self.name



class Government(models.Model):
    user= models.OneToOneField(Login,on_delete=models.CASCADE,related_name='govt')
    name= models.CharField(max_length=100)
    contact_number=models.CharField(max_length=100)
    email =models.EmailField()
    address= models.TextField(max_length=200)
    department= models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Complaints(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    complaint = models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True, blank=True)


class User(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE,related_name='user')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class AppointmentSchedule(models.Model):
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(AppointmentSchedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)


class Uploads(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200, blank = True)
    document = models.FileField(upload_to='documents/')
    email = models.EmailField()
    contact_no = models.CharField(max_length=100)

