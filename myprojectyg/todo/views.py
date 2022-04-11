from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core import serializers
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.utils.decorators import method_decorator

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

@login_required
def profile(request):
    return render(request, 'profile.html')


def logoutTest(request):
    return render(request, 'registration/logged_out.html')

def taskdetail(request, id):
    #task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    
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

#Or, more succinctly, you can decorate the class instead and pass the name of the method to be decorated as the keyword argument name:
@method_decorator(login_required, name='dispatch' )
class TodoCreateView(CreateView):
    #fine unless you need a custom widget, then you might as well use ModelForm
    model = Task
    #fields = ['isdone', 'name', 'details', 'creation_date', 'weblink', 'creator']
    template_name = 'TodoForm.html'
    success_url = 'simple.html'
    form_class = TaskForm
    


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
    
class SimplePage(TemplateView):
    #this assumes no context is needed
    template_name = 'simple.html'
    
    #allows the view to be rendered in a frame by passing the x-frames-options header
    #can also be set globally with django middleware and custom setting
    #arguably function based views are shorter, esp if having to override something
    @method_decorator(xframe_options_sameorigin)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
class MyView(View):
    
    def get(self, request):
        return HttpResponse('string to render')
    
class MyFormView(FormView):
    template_name = 'showform.html'
    form_class = ExampleForm
    success_url = 'showform.html'


class FormRespView(FormView):
    template_name = 'formresp.html'
    form_class = ExampleForm
    #success_url = '/success/'
    def form_valid(self, form):
        #return super().form_valid(form)#HttpResponseRedirect(str(self.success_url))
        #messages.success()
        context = self.get_context_data()
        context['num'] = 11.4
        return render(self.request, 'formresp.html', context)

    def get_context_data(self, **kwargs):
        #mynum = kwargs.pop('number', 999)#remove to prevent pass to super?
        
        context = super().get_context_data(**kwargs)
        #context['name'] = 'newname'
        #context['num'] = mynum #kwargs.get('number', 999)
        return context
