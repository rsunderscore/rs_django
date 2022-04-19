from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from .models import Vocab
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class VocabCreateView(CreateView):
    model = Vocab
    fields = ['eng', 'esp','pos','user']
    template_name = 'vocabform.html'
    success_url = 'simple.html'


class IndexView(TemplateView):
    template_name = 'index.html'
    
class SuccessView(TemplateView):
    template_name = 'success.html'
    
def vocabListView(request):
    vocablist = Vocab.objects.all()
    return render(request, 'vocablist.html', {'vocab': vocablist})