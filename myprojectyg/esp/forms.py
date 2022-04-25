# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 19:45:13 2022

@author: Rob
"""
from django import forms
from .models import Vocab


class VocabForm(forms.ModelForm):
    class Meta:
        model = Vocab
        #put POS choices in the model isntead?
        #verb, noun, adjective, adverb, pronoun, article, preposition
        POS_CHOICES = [('noun', 'noun'), ('verb', 'verb'), 
                       ('adjective', 'adjective'),
                       ('adverb', 'adverb'), ('pronoun', 'pronoun'),
                       ('article', 'article'),
                       ('preposition', 'preposition')]
        #'isdone'
        fields = ['eng', 'esp', 'pos', 'user',]#fields = '__all__' #fields to include
        #exclude = None #fields to exclude
        #pos = forms.ChoiceField(choices = POS_CHOICES)
        #https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
        widgets = {'eng':forms.TextInput(attrs={'placeholder':'word'}),
           'esp':forms.TextInput(attrs={'placeholder':'la palabra'}),
           'pos':forms.Select(choices = POS_CHOICES),
           'user':forms.TextInput(attrs={'readonly':True})#
           }
