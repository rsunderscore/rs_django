# -*- coding: utf-8 -*-
"""forms.py
Created on Fri Mar 25 19:34:09 2022

@author: Rob
"""
from django import forms

class ExampleForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=10)
    password = forms.CharField(min_length=8, widget= forms.PasswordInput)
