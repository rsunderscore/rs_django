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

views - should prepare any data necessary for the template and pass it in the context
- each view defined as a function (called from ursl.py) that takes request as input
- function returns 
	- HttpResponse (from django.http import HttpResponse) - to return a raw string
	- render (from django.shortcuts import render) - to render a template
		- params: request, templatename, context_dict
		- context_dict specifies what names are available to the html
- class based views (CBV) - less readable but easier to write (pg 131, 553)
	- built-in 
		- View - base class for all CBVs
		- TemplateView - render template based on parameters from url
		- RedirectView - redirect user to a resource based on the request
		- DetailView - view mapped to django model and used to render the data obtained using specified template
	- other useful primitives in django.views.generic.edit
		- CreateView
		- FormView - form_valid method, as_p to render field values inside p tags
		- UpdateView - 
		- DeleteView (pg 563)

static files
- look this up

styles
- bootstrap

admin - CRUD operations 
	- usually sufficient for smaller apps
	- need to register models for them to appear in the interface - update the admin.py file
		- import the model classes
		- admin.site.register(modelname) for each model
	- subclass AdminSite and AdminConfig to integrate app adminstration with users/groups admin
		- auto-discovery integration with native is done by (combination of book and django docs)
			- create an admin.py in root folder (root of the project - not the app subdir)
				- define a child class of admin.AdminSite
				- can customize title_header, site_header, and index_title
			- create an apps.py in root folder with a class instance
				- create a sublcass of `django.contrib.admin.apps` AdminConfig class with default_site set to 'admin.NewAdminName' (from your admin.py file)
			- modify installed apps in config to point  to the new apps file and the config class - e.g. 'apps.myCustomAdminConfig', 
		- "When you put 'django.contrib.admin' in your INSTALLED_APPS setting, Django automatically looks for an admin module in each application and imports it." - https://docs.djangoproject.com/en/4.0/ref/contrib/admin/
			- AdminConfig calls autodiscover when imported (which gets admin.py files in app subdirs)
			- overriding default admin site = https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#overriding-default-admin-site
	- subclass ModelAdmin (appname/admin.py) to customize model list and detail views
		- create a subclass of ModelAdmin for each model type in appname/admin.py
		- when registering the model add a second param for the new subclass e.g. `admin.site.register(Book, BookAdmin)`
		- list_display - default listing is based on the __str__ function defined in the model (pg 198)
			- set `list_display = ` - any of these work:
				- `('field1','field2')`#a tuple of fields from the model taht you want
				- function that takes the model instance as arg 
				- Method from ModelAdmin subclass that takes model as arg
				- method of the model class (if it accepts model obj as arg i.e. self)
			- computed fields cannot be sorted in the admin interface (e.g. reformatted)
			- cannot include a Many-to-many field
			- list_filter
				- enabling a drop-down for the provided fields that limits displayed records -  controlled with list_filter attribute of a ModelAdmin subclass
			- date_hierarchy - filters rows by date with links above the table display
			- search_fields - enables the search box to look for text in the specified fields
				- use two underscores to search on a foreign_key field (e.g. 'publisher__name')
				- default is contains - append '__exact' to fields that should be matched exactly (e.g. isbn__exact)
				- can also use '__startswith' appended to field name
		- customizing detail views
			- hide fields 
				- will be hidden if model field is defined with auto (e.g. auto_now_add for a date field)
				- `exclude = ('field1', 'field2'...)` in the subclass of modelAdmin
				- `fields = ('list', 'of', 'fields', ...)` can be used to include only specified fields if it is easier than excluding
				- `fieldsets = ` iter of group names followed by a dict with {'fields':('field1' ,'field2') to produce an interface with fields grouped and ordered
forms
- look this up
- csrf token - cross-site request forgery
	- look this up
- request.method passed in context dict as 'method': request.method
	- data passed with request.GET or request.POST QueryDict

templates
- html files with special tags for vars {{ }} and logic {% %}
- inheritance
- ideally each app will have its own child templates folder 
- shared templates in the root folder
- custom template tags
	 - live inside the templatetags subdir for each app

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
- field options - https://docs.djangoproject.com/en/4.0/ref/models/fields/
	- `null = True` - allow the DB to accept blanks/null
	- `blank = True` - allow the field to accept a blank value
	- `default = value` - the value to use if nothing is specified
	- `auto_now_add = True` - set the field to now when the object is first created - field will be hidden by default in admin interface (detail)
	- help_text = 'words' - set the hint text that displays under the field in admin interface
	- max_length = # - set how may characters are allowed
- model methods
	- __str__() - change how the str method works - used by default by admin interface to choose how to display records
	- can also include a method that tells admin interface how to display records
	
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

SECRET_KEY pg 675
- 3rd party lib django Configurations has a values.SecretValue module
- store in ENV variable and retrieve with os.environ.get('keyname', default)
- 50 character random string
- get a new secret key by using get_random_secret_key from django.core.management.utils
	- get_random_string - specify a length as first param - 
	- uses python standard lib secrets module - cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets
- why are there so many web based apps to generate this key?
