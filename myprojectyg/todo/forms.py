# -*- coding: utf-8 -*-
"""forms.py
Created on Fri Mar 25 19:34:09 2022

@author: Rob
"""
from django import forms
from todo.models import Task

class ExampleForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=10)
    password = forms.CharField(min_length=8, widget= forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        #if condition then self.add_error("field", "msg"))#use None as first var for non-field error
        
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        #'isdone'
        fields = ['isdone', 'name', 'details', 'due_date', 'weblink', 'assignee', 'creator']#fields = '__all__' #fields to include
        #exclude = None #fields to exclude
        widgets = {'name':forms.TextInput(attrs={'placeholder':'task name'}),
                   'due_date':forms.DateInput(attrs={'type':'date'}),
                   'creator':forms.TextInput(attrs={'readonly':True}),
                   }
        
#disable editing of form fields with wdget.atrrs['readonly'] = True
# set value of disabled field by setting initial 