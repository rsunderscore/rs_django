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
    path('delete_word/<int:pk>', views.VocabDeleteView.as_view()),
    path('update_word/<int:pk>', views.VocabUpdateView.as_view()),
    #path('vocab_confirm_delete.html', ),
    path('vocab/', vocabListView)
    ]