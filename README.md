# rs_django
This will be a django project, and will hold any django apps that I create.

Reference [book code] (https://github.com/PacktPublishing/Web-Development-with-Django/)

1. create django-admin startproject projname pg 5
2. create manage.py startapp appname pg 23
3. add app to INSTALLED_APPS in settings.py pg 47
3. python manage.py migrate pg 85
4. python manage.py createsuperuser pg 153
5. python manage.py runserver pg 4
	- python manage.py shell pg 105 - invoke a shell in app context
5. starting folder layout

todo
1. get user to populate automatically in the form
	1. do this by manually creating a text or hidden input in the template
	1. set with javascript after page load?
1. something else.

<pre>
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
</pre>

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
- class based views (CBV) - less readable but easier to write (pg 131, 553) - used to handle multiple request types
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

### SECRET_KEY pg 675
- 3rd party lib django Configurations has a values.SecretValue module
- store in ENV variable and retrieve with os.environ.get('keyname', default)
- 50 character random string
- get a new secret key by using get_random_secret_key from django.core.management.utils
	- get_random_string - specify a length as first param - 
	- uses python standard lib secrets module - cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets
- why are there so many web based apps to generate this key?

## static files
- django not intended to serve static - standard web server would do that - just a stopgap for dev purposes
	- also facilitates locating files - change a value in settings.py to remap files - value to be changed varies based on the finder
	- retrieving that static file ties up the python process - so performance rapidly degrades in multi-user setup
- management commands
	- findstatic - takes filename as input and shows what paths were searched
	- collectstic - bundles static assets for upload to a server directory
- static template tag - used to convert a filename to a URL or path that can be used in a template
- finder - utility that translate url location to asset location on disk
	- AppDirectoriesFinder - searches app subdirectories (static folder) for assets
	- FileSystemFinder - searches specified folder locations (e.g. for assets shared across multiple apps)

### styles
- bootstrap (p 146) - https://getbootstrap.com/docs/4.4/getting-started/introduction/
	- https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
- specifc styles provided via classes (e.g. btn-primary)
- other styles served as static files


## MEDIA - uploads, files/images
- SETTINGS
- store on disk directly
- store on disk with path in a model
1. settings.py 
	- add a new option to options key of templates setting of  `django.template.context_processors.media`
	- after STATIC_URL setting add two new settings
		1. `MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`
		1. `MEDIA_URL = '/media/' #note trailing slash included so not needed when used`
	- urls.py 
		- import settings `from django.conf`
		- import static from `django.conf.urls.static`
		- add a conditional if settings.DEBUG section after urlpatterns
			- append to urlpatterns (+=) `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT`
			- 

## models
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
- to rename a field - https://thewebdev.info/2022/04/01/how-to-rename-a-model-and-relationship-fields-with-python-django-migrations/
	- manually create a migration file with migrations.RenameModel or RenameField
	- run make migrations to run the file? (not migrate?) - https://docs.djangoproject.com/en/4.0/topics/migrations/

### integration with existing DB
- configure connection then run python manage.py inspectdb > models.py (generates python classes that align with existing tables) adjust if needed
	- generated classes have attribute `manged = False` which means that migrate won't touch them
	- https://docs.djangoproject.com/en/4.0/ref/django-admin/ 
	- can append a space separated list of tables to look examine
	- flag to include-views


## admin - CRUD operations 
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


## Authentication/Authorization
 - re-using the admin auth templates - not working as described  :rage1:
	- login works because it's not in the admin path for registration - but the others default to using the admin template rather than the app template - not sure why
		- corrected an issue with urls.py syntax when import auth.urls to tha accounts namespace (paren mismatch)
	1. add to urls.py urlpatterns `path('accounts', include(('django.contrib.auth.urls','auth'),namespace='accounts')),`
		1. routes: login, logout, password_change, password_change/done, password_reset, password_reset/done, rest/<uidb64>/<token>, reset/done, 
	1. copy common views from django admin package to templates/registration
		1. everything in <envloc>\lib\site-packages\django\contrib\admin\templates\registration
			1. full list(8 html files): password_reset_email, password_change_form, password_change_done, password_reset_form, password_reset_done, password_reset_confirm, password_reset_complete, logged_out
		1. login.html from <envloc>\lib\site-packages\django\contrib\admin\templates\admin
		1. envloc can be determined by running `import sys` and then `sys.path`
	1. to verify routing and templates are functioning, go to:  127.0.0.1:8000/accounts/login 
	1. modify the copied templates to go with your site - e.g. 
		1. extend base.html rather than admin/base_site.html
		1. copy conent_title and reset_link block text into content block
		1. remove unused blocks
		1. replace reverse urls with namespaced equivalents (e.g. 'login' becomes 'accounts:login')
			1. in some cases the url is set in a variable that is later reference
		1. login.html 
			1. ok to remove all blocks except content
	1. add a profile view and template (login redirects to it by default)
- use this instead? https://docs.djangoproject.com/en/4.0/topics/auth/default/
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication - this WORKS :tada:
	- `path('accounts/', include('django.contrib.auth.urls'))`
	- they suggestion putting registration stuff in a tempaltes subfolder off of project directory and then adding that directory to DIRS in TEMPLATES in settings.py e.g. `os.path.join(BASE_DIR, 'templates')`
- access is controlled via the views
	- decorators from from django.contrib.auth.decorators import 
		- login_required - redirect user to login then come back here 
			- login_url param - where to redirect after login (default is page redirected from)
			- redirect_field_argument param - what the redirect param will be within url (default: next=)
		- permission_required - limit access to a user with specific permission level e.g. @permission_required('view_group')
		- user_passes_test - uses a function that takes user as input to pull information about the user and test it - returns False or Truthy (e.g. non-zero) - used for more flexible control of auth
		- method_decorator - needed if you have a class based view
	- can also manually invoke `redirect_to_login` function for even more control
	- check in templates for request.user == AnonymousUser (means they didn't login) or user.is_authenticated


## forms
- look this up
- csrf token - cross-site request forgery
	- look this up
- request.method passed in context dict as 'method': request.method
	- data passed with request.GET or request.POST QueryDict
- custom validation - solution to choose varies by use case
	- override clean method in form class - use `self.add_error('field', 'msg')`
	- add a per-field clean method (e.g. `clean_username(self)` and raise django.core.exceptions.ValidationError for issues; **must** return value)
	- add custom validation function that takes value as param and raises ValidationError for issues (no return) 
- attrs - a form field attribute that takes a dict of additional settings
	-"placeholder" - added with placeholder attribute to the form field
-initial values - added with initial attribute to the form field
	- can also be set with initial attribute to Form - dict of field names and values
- ModelForms - used to auto create forms from models `class modelnameForm(forms.ModelForm): class Meta: model=modelname fields=('tuple','of','fieldnames')`
	- fields can be '__all__' to use all fields
	- include a subclass Meta with attributes to specify the model to use and the fields to include (or exclude)
		- best to avoid exclude so that special fields are not accidentally exposed
- use crispy forms package to integrate with CSS and bootstrap (prettier forms)

## templates
- html files with special tags for vars {{ }} and logic {% %}
- inheritance
- ideally each app will have its own child templates folder 
- shared templates in the root folder
- custom template tags
	 - live inside the templatetags subdir for each app


	
## sessions
- cookie based, file based, or db based - SESSION_ENGINE in settings.py
- there are laws about sites notifying about cookies now - make sure to notify
- request.session

- pickle vs JSON for storage  - configured via SESSION_SERIALIZER
- parts: key, data, expire_date
- storing: `request.session['keyname'] = value` (or pass a dict to request.session)
- retrieve: `var = requset.session.get('keyname', []) #common to use [] as default`
- `{% empty %}` tag for template handles condition when var is empty in a loop

## custom tags and filters
1. create a folder called 'templatetags' #default name auto-searched by django
1. create custom_filter.py or custom_tags.py
1. `from django import template`
1. `register = template.Library()`
- filters
	- function that accepts a var (can also have more args, but first param is always the var from the tag) - shoudl return a string
	- decroate function with `@register.filter`
		- can pass context by adding `takes_context=True` to the decorator
	- args are specified after a colon when used e.g. `{{ some_value | filter:'arg' }}`
	- stringfilter - special case that ensures that the input is a string (converts if not) 
		- from django.template.defaultfilters import stringfilter
		- used as decorator on the filter
	- *note* params passed to filter must be immediately after the colon (space will throw an error that 'not enough parameters were provided')
- tags - two types of tags implementations - create in a template_tags directory
	- simple - render in same template
		- decorate a function with @register.simple_tag
		- params are space separated after tha nem when used in the template e.g. `{% mytag 'arg1' var %}`
	-inclusion -  calls an additional template that renders with the provided information and replaces the tag
		- e.g. use-case: adding custom widgets to a page
		- `@inclusion_tag('templatename.html')` decorator
			- template specified should exist in the templates dir
		- function should return a dict that is used as the context for the sepcified template
- in template need to {% load pyfilename %} - can load multiple modules in series (separate with spaces)
	
## REST (API using JSON)
- separate api views into their own file (api_views.py)
1. `pip install djangorestframework`
2. add rest_framework to isntalled_apps (settings.py)
3. import `rest_framework.decorators` api_view and Response
4. decorate a view with api_view and use Resopnse to return a dict and it will be converted to a JSON
5. update urls with a path for the view
	- when viewed in the browser the result is formatted
- can use serializers to convert between output types e.g. rest_framework.serializers
	- create custom serializers in serializers.py - similar fields to forms e.g. CharField, DateField, EmailField
	- run serializer on an object and then pass result.data to Response to get JSON
	- serializers has a ModelSerializer than can bet extended
		- specify the model and fields in a Meta subclass
- Viewsets/Routers (sub-component of django rest framework)
	- combines list and details views
	- extend viewsets.ModelViewset  ans set serializer_class and queryset (the model name)
	- `router.register(r'name', xxxViewSet)`
	- `urlpatterns = router.urls` - detail view becomes name/<id> and list view is just /name/
	- in views.py import DefaultRouter from rest_framework.routers and then add a `path('api/', include(router.urls), 'api')`


## Browser Debug toolbar (i.e. DjDt)
provides large amounts of information about page parameters, state, db, load times, etc...
1. conda -c conda-forge install django-debug-toolbar
1. settings.py 
	- add `debug_toolbar` to INSTALLED_APPS
	- add `debug_toolbar.middleware.DebugToolbarMiddleware` to MIDDLEWARE (first or as early in the list as possible)
	- add `127.0.0.1` to INTERNAL IPS
	- verify that STATICFILES_DIRS is defined (e.g. `[os.path.join(BASE_DIR, 'static' )]` and that the directory exists (<projdir>/static)
1. urls.py - add `path('__debug__/', include(debug_toolbar.urls))` add to the end of the list in DEBUG section

## including charts
	- bokeh - embed html
	- plotly - embed html
	- matplotlib - write to StringIO as svg then pass the output to the template to render in tag `{{ chart | safe }}`
		
### Misc
- x-frames-options - used to prevent clickjacking, most browsers / sites use x-frames-options deny so that each page cannot be embedded in a frame
	- other options: sameorigin = allow if the site is the same, exempt = allow everywhere
- django messaging framework - https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
- book says class based views are better but almost all documentation is for function based views and hard to find solutions that work for CBVs as well
	- e.g. rendering the result on the same page
	
	
# integration with Apache
- links
	- pypi page: https://pypi.org/project/mod-wsgi/
	- more docs here: https://modwsgi.readthedocs.io/en/master/index.html
		-  broken link (fow windows) that points roughly to this github repos https://github.com/GrahamDumpleton/mod_wsgi

- https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/modwsgi/
    - If you are running Windows, it is recommended you use the Apache distribution from Apache Lounge (www.apachelounge.com). 

# apache and mod_wsgi install
- [quick install guide](https://modwsgi.readthedocs.io/en/master/user-guides/quick-installation-guide.html) that describes how to compile
- I also needed to `apt install apache-dev` in order to get the apxs library needed to compile mod_wsgi
- add LoadModule to apache configuration
	- some apache2 installs break out modules and configurations until a sub-folder structure - so the load file and conf file would go in modules avail folder and then enable with a2enmod and a2enconf commands described in httpd.conf
- restart apache - e.g. service apache2 restart or apachectl restart or ...
- additional configuration:
	- WSGIScriptAlias /myapp /usr/local/www/wsgi-scripts/myapp.wsgi
	- Directory /usr/local/www/wsgi-scripts
	- AddHandler wsgi-script .wsgi
	- possible 'delegate to daemon' config
	
[libpython error](https://github.com/GrahamDumpleton/mod_wsgi/issues/338)
 GrahamDumpleton commented on Jan 14, 2020
	
The message is saying it can't find libpython3.7m.so.1.0 not the mod_wsgi.so file. See:
    https://modwsgi.readthedocs.io/en/develop/user-guides/installation-issues.html#unable-to-find-python-shared-library
	
In short, you are trying to use a Python installation in a non standard location, so you need to tell the build where it is. You can also fudge things by adding:
	
LoadFile /some/path/libpython3.7m.so.1.0
	
before the LoadModule line, where /some/path is replaced with the directory where Python library was installed.
	
You may also need to set WSGIPythonHome directory to be what sys.prefix is set to for Python since not in standard location.
