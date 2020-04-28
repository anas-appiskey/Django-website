from django.contrib import admin
from .models import Question

# Register your models here.

#this will register the question function 
admin.site.register(Question)