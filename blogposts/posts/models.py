from django.db import models
from datetime import datetime

# Create your models here.
class PoliticsBlogs(models.Model):
    image=models.ImageField(upload_to='imgs')
    title=models.CharField(max_length=100)
    body=models.TextField()
    date_posted=models.DateTimeField(default = datetime.now,blank=True)
    time_it_takes_to_read=models.CharField(max_length=20)
    

    def __str__(self):
        return self.title




class BusinessBlogs(models.Model):
    image=models.ImageField(upload_to='imgs')
    title=models.CharField(max_length=100)
    body=models.TextField()
    date_posted=models.DateTimeField(default = datetime.now,blank=True)
    time_it_takes_to_read=models.CharField(max_length=20)
    

    def __str__(self):
        return self.title




class EducationBlogs(models.Model):
    image=models.ImageField(upload_to='imgs')
    title=models.CharField(max_length=100)
    body=models.TextField()
    date_posted=models.DateTimeField(default = datetime.now,blank=True)
    time_it_takes_to_read=models.CharField(max_length=20)
    

    def __str__(self):
        return self.title





class EntertainmentBlogs(models.Model):
    image=models.ImageField(upload_to='imgs')
    title=models.CharField(max_length=100)
    body=models.TextField()
    date_posted=models.DateTimeField(default = datetime.now,blank=True)
    time_it_takes_to_read=models.CharField(max_length=20)
    

    def __str__(self):
        return self.title




class HealthBlogs(models.Model):
    image=models.ImageField(upload_to='imgs')
    title=models.CharField(max_length=100)
    body=models.TextField()
    date_posted=models.DateTimeField(default = datetime.now,blank=True)
    time_it_takes_to_read=models.CharField(max_length=20)
    

    def __str__(self):
        return self.title 




class LifestyleBlogs(models.Model):
    image=models.ImageField(upload_to='imgs')
    title=models.CharField(max_length=100)
    body=models.TextField()
    date_posted=models.DateTimeField(default = datetime.now,blank=True)
    time_it_takes_to_read=models.CharField(max_length=20)
    

    def __str__(self):
        return self.title





class TravelBlogs(models.Model):
    image=models.ImageField(upload_to='imgs')
    title=models.CharField(max_length=100)
    body=models.TextField()
    date_posted=models.DateTimeField(default = datetime.now,blank=True)
    time_it_takes_to_read=models.CharField(max_length=20)
    

    def __str__(self):
        return self.title
    