# rs_django
This will be a django project, and will hold any django apps that I create.

1. create django-admin startproject projname pg 5
2. create manage.py startapp appname pg 23
3. add app to INSTALLED_APPS in settings.py pg 47
3. python manage.py migrate pg 85
4. python manage.py createsuperuser pg 153
5. python manage.py runserver pg 4
	- python manage.py shell pg 105 - invoke a shell in app context
5. folder layout
projname
/projname
	| __init__.py
	| asgi.py
	| settinsg.py
	| urls.py
	| wsgi.py
/appname
	/templates
		|html files go here
	/migrations
		|migration files
	| __init__
	| admin.py
	| apps.py
	| models.py
	| tests.py
	| views.py
| db.sqlite3
| manage.py


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

urls
- set routing relative from the base url
- make sure that appname.views is imported

views
- each view defined as a function (called from ursl.py) that takes request as input
- function returns 
	- HttpResponse (from django.http import HttpResponse) - to return a raw string
	- render (from django.shortcuts import render) - to render a template
		- params: request, templatename, context_dict
		- context_dict specifies what names are available to the html

templates
- html files with special tags for vars {{ }} and logic {% %}

models
- tables are defined as classes that extend models.Model
- after changing
	1. python manage.py makemigrations appname
		- creates a new migration script file in migrations subfolder
	1. python manage.py showmigrations
	1. python manage.py sqlmigrate appname 
		- autoincremented primary key id is automatically added
		- may be followed by an optional designation (i.e. which migration to apply?)
- relationships
	- new field defined with type of models.ForeignKey with first param as the classname for the other table
	- dependency actions (e.g. on_delete) - what to do if the row referenced by the foreign_key is deleted
		- models.CASCADE - delete rows referencing that foreign_key from this table too
		- models.PROTECT - prevent deletion unless all referenced objects deleted
		- models.SET_NULL - set null
		- models.SET_DEFAULT - revert the field to the default value
	- many-many
		- new field with type models.ManytoManyField with first param as the classname for the other table
			- through param - intermediary to store relationshiop details (table must be manually defined and have ForeignKey relationships with both tables)
	- one-one
		- use models.OneToOneField with first param as the classname for the other table
- choices
	- can define a nested class that has attributes representing possible form selection values for a field
	- can be referenced by the model field as the choices parameter
	- convention: each choice name is all caps and gets a tuple of strings as a value (e.g. `AUTHOR = 'AUTHOR','Author'`
		- presumably the first item in the tuple is the form field Value and the other is the label
- model methods
	- __str__() - change how the str method works
- create new instances form shell by importing the table class from models and then creating a new one with params as field names and values
	- insert via objname.save() method
- if the row is in scope (obj instance, a field may be modified with dot notation `person.name = 'new name'` and then class `person.save()`
- create a dependent ForeignKey by importing that class also and using get to retrieve the relevant row
	- then pass that object to the new instance for the dependent table
	- `person = Person.objects.get(name='some name')`
	- then `newrow = Task(..., creator=person, ...)`
	- for many-many you search up the items in each table and then store as references in the intermediary table
		- can use add method and through defaults
	- create method can create a new object and establish  relationship in one step (e.g. `book.contributors.create(first_names='Packtp', last_names=
'Editor Example', email='PacktEditor2@example.com',
through_defaults={'role': 'EDITOR'})` pg 111
