from django.contrib import admin
from .models import Journal, Tags, Locations
# Register your models here.
admin.site.register(Journal)
admin.site.register(Tags)
admin.site.register(Locations)