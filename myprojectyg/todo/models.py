from django.db import models
from django.conf import settings

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=64, help_text='name of person')
    email = models.EmailField(help_text = 'email address of creator')
    
    def __str__(self):
        return self.name
        
        
class Task(models.Model):
    """a particular to-do item"""
    isdone = models.BooleanField(default=False)
    name = models.CharField(max_length=50, help_text='a short name for the task')
    details = models.TextField(max_length=255, help_text='description of task')#large text field #max_length not enforced in DB
    weblink = models.URLField(help_text = 'a web site link', blank=True, null=True)#blank allows you to pass it a null value, but null tells the database to accept null values
    creation_date = models.DateField(verbose_name='date created', auto_now_add=True)#set form field to widget HiddenInput
    due_date = models.DateField(verbose_name = 'target completion date', blank=True, null=True)
    #user = models.TextField(hidden) #or should this be Foreignkey to the Users table?
    #swap creator for assignee
    creator= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assignee = models.ForeignKey(Person, on_delete=models.CASCADE) #what to do if referenced object is deleted
    #other actions: PROTECT, SET_NULL, SET_DEFAUALT


#    User
    # AUTH_USER_MODEL
    # get_user_model()