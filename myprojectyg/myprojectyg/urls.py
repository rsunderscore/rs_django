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
    path('accounts/', include(('django.contrib.auth.urls','auth'), namespace='accounts')),
    path('admin/', admin.site.urls),
    path('accounts/profile/', todo.views.profile),
    path('', todo.views.index), 
    path('search/', todo.views.search),
    path('alltasks.html', todo.views.allTasksView),
    path('taskdetail/<int:id>/', todo.views.taskdetail),
    path('showform.html', todo.views.formview),
    path('taskform.html', todo.views.taskView),
    path('showform2.html', todo.views.MyFormView),
    path('logouttest.html', todo.views.logoutTest),
    path('CBVtest', todo.views.MyView.as_view(), name='index_view'),
]

# authurls = [<URLPattern 'login/' [name='login']>, 
#             <URLPattern 'logout/' [name='logout']>, 
#             <URLPattern 'password_change/' [name='password_change']>, 
#             <URLPattern 'password_change/done/' [name='password_change_done']>, 
#             <URLPattern 'password_reset/' [name='password_reset']>, 
#             <URLPattern 'password_reset/done/' [name='password_reset_done']>, 
#             <URLPattern 'reset/<uidb64>/<token>/' [name='password_reset_confirm']>,
#             <URLPattern 'reset/done/' [name='password_reset_complete']>]

# import django
# for url in django.contrib.auth.urls.urlpatterns:
#     urlparts = url.name, url.lookup_str
#     patt = url.pattern
#     patparts = patt.describe(), patt.name, patt.regex
#     print(urlparts, patparts)
    
pathtoauthfiles = r'C:\Users\Rob.DESKTOP-HBG5EOT\.conda\envs\django\Lib\site-packages\django\contrib\auth'
