from django.db import models

# Create your models here.
class Technologies(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    technology_logo = models.ImageField(upload_to='Projects/images/')

    def __str__(self):
        return self.name

class Projects(models.Model):
    title = models.CharField(max_length=100)
    descrption = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Projects/images/')
    Technologies = models.ManyToManyField(Technologies)

    def __str__(self):
        return self.title