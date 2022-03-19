from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=64, help_text='name of person')
    email = models.EmailField(help_text = 'email address of creator')
    
    def __str__(self):
        return self.name
        
        
class Task(models.Model):
    """a particular to-do item"""
    name = models.CharField(max_length=50, help_text='a short name for the task')
    name = models.CharField(max_length=255, help_text='description of task')
    weblink = models.URLField(help_text = 'a web site link')
    creation_date = models.DateField(verbose_name='date created')
    creator = models.ForeignKey(Person, on_delete=models.CASCADE) #what to do if referenced object is deleted
    #other actions: PROTECT, SET_NULL, SET_DEFAUALT
