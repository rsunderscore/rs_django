from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from .models import Vocab
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import VocabForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def vocabCreateView(request):
    #context = {}
    #return render(request, 'vocabform.html', context)
    user=request.user.id

    if request.method == 'POST':
        form = VocabForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print(f"{name}: ({type(value)}) {value}")
    else:
        form = VocabForm(initial={'user':user})
        #form = form()
    return render(request, 'vocabform.html', {'form':form})


class VocabCreateView(LoginRequiredMixin, CreateView):
    #use requst.user in this view to pre-set the user value?
    model = Vocab
    fields = ['eng', 'esp','pos','user']
    template_name = 'vocabform.html'
    success_url = 'success/'


class IndexView(TemplateView):
    template_name = 'index.html'
    
class SuccessView(TemplateView):
    template_name = 'success.html'
    
def vocabListView(request):
    vocablist = Vocab.objects.all()
    return render(request, 'vocablist.html', {'vocab': vocablist})