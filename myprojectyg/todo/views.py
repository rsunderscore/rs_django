from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView
from django.core import serializers
from .forms import ExampleForm, TaskForm
from .models import Task

# Create your views here.

def index(request):
    name = request.GET.get('name') or 'world'
    #return HttpResponse(f'hello {name}')
    #name= "world!"
    return render(request, 'main.html', {"name":name})
    
def search(request):
    searchstring = request.GET.get('q') or ''
    return render(request, 'search.html', {"searchstr":searchstring})

def allTasksView(request):
    fields = Task._meta.get_fields()
    #tasklist = serializers.serialize("python",Task.objects.all()) #this makes it a list of dicts
    tasklist = Task.objects.all()
    return render(request, 'alltasks.html', {'fields':fields, 'tasks':tasklist})


def taskdetail(request, id):
    task = Task.objects.get(id=id)
    #return HttpResponse(f'hello {id} <br> {task}')
    return render(request, 'taskdetail.html', {'id':id, 'task':task})
    
def formview(request):

    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print(f"{name}: ({type(value)}) {value}")
    else:
        form=ExampleForm()
    return render(request, 'showform.html', {'form':form})

def taskListView(request):
    pass

def taskView(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print(f"{name}: ({type(value)}) {value}")
    else:
        form=TaskForm()
    return render(request, 'taskform.html', {'form':form})

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
    
        
