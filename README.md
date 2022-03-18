# rs_django
This will be a django project, and will hold any django apps that I create.

1. create django-admin startproject projname pg 5
2. create manage.py startapp appname pg 23
3. python manage.py migrate pg 85
4. python manage.py createsuperuser pg 153
5. python manage.py runserver pg 4
5. folder layout


QueryDict
- bracket notation - keyError if missing
- getlist(keyname) - if keyname is blank then all are returned - returns empty list if missing
- GET/POST immutable
- returned as part of the request object (e.g. `request.GET.get('keyname')`)

Settings (pg 44)
- ALLOWED_HOSTS
- INSTALLED_APPS - list of apps for the site
- SECRET_KEY
- ROOT_URLCONF - which urls.py file to look at first
- TEMPLATES - templ location
- APP_DIRS - use templ folder within each app (not built by default)
