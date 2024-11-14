from django.db import models

# Create your models here.

# link photo to person (makes it easier to use AI to associate it with a person)
class Person (models.Model):
    person_id = models.BigAutoField(primary_key= True)
    fistname = models.CharField(max_length= 255)
    lastname = models.CharField(max_length= 255)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return f'{self.fistname} {self.lastname}'   
    
class Tags (models.Model):
    id = models.BigAutoField(primary_key= True)
    label = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.label    

class Images (models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length= 1000)
    image_file = models.ImageField(upload_to='PhotoGallery/images/')
    tags = models.ManyToManyField(Tags)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_public = models.BooleanField(default=True)
    upload_date = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100, blank=True)
    associate_person = models.ForeignKey(Person, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = "Images"

    def __str__(self):
        return f'{self.title} - {self.associate_person.__str__()}'