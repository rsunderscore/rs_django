from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView
from .forms import ExampleForm

# Create your views here.

def index(request):
    name = request.GET.get('name') or 'world'
    #return HttpResponse(f'hello {name}')
    #name= "world!"
    return render(request, 'main.html', {"name":name})
    
def search(request):
    searchstring = request.GET.get('q') or ''
    return render(request, 'search.html', {"searchstr":searchstring})

def formview(request):

    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print(f"{name}: ({type(value)}) {value}")
    else:
        form=ExampleForm()
    return render(request, 'showform.html', {'form':form})

class MainPage(TemplateView):
    #this assumes no context is needed
    template_name = 'base.html'
    
class MyView(View):
    
    def get(self, request):
        return HttpResponse('string to render')
    
class MyFormView(FormView):
    template_name = 'showform.html'
    form_class = ExampleForm
    success_url = 'showform.html'
    
    def form_valid(self, form):
        return super().form_valid(form)