"""myprojectyg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import todo.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('django.contrib.auth.urls','auth'),namespace='accounts')),
    path('', todo.views.index), 
    path('search/', todo.views.search),
    path('alltasks.html', todo.views.allTasksView),
    path('taskdetail/<int:id>/', todo.views.taskdetail),
    path('showform.html', todo.views.formview),
    path('taskform.html', todo.views.taskView),
    path('showform2.html', todo.views.MyFormView),
    path('CBVtest', todo.views.MyView.as_view(), name='index_view'),
]
