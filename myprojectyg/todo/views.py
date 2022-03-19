from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    name = request.GET.get('name') or 'world'
    #return HttpResponse(f'hello {name}')
    #name= "world!"
    return render(request, 'base.html', {"name":name})
    
def search(request):
    searchstring = request.GET.get('q') or ''
    return render(request, 'search.html', {"searchstr":searchstring})