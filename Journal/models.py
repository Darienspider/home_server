from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Locations(models.Model):
    id = models.BigAutoField(primary_key= True)
    label = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.label    

class Tags (models.Model):
    id = models.BigAutoField(primary_key= True)
    label = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.label    

class Journal (models.Model):
    id = models.BigAutoField(primary_key= True)
    title = models.TextField(max_length= 200)
    content  = models.TextField(max_length=1024)
    entry_date = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tags)
    location = models.ManyToManyField(Locations)



    def __str__(self):
        return f'{self.title}'