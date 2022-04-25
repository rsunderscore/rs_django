# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:43:13 2022

@author: Rob
"""
from django.urls import path,include
from .views import IndexView, VocabCreateView, SuccessView, vocabListView

from . import views

urlpatterns = [
    path('',IndexView.as_view()),
    path('success/', SuccessView.as_view()),
    path('new_word.html', VocabCreateView.as_view()),
    path('new_word2.html', views.vocabCreateView),
    path('vocab/', vocabListView)
    ]