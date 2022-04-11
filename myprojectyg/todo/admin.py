from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    list_filter = ('name',)
    search_fields = ('name', 'email',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_date', 'assignee', 'isdone')
    list_filter = ('isdone', 'assignee')
    date_hierarchy = 'creation_date'
    search_fields = ('name', 'details')

from todo.models import Person, Task
# Register your models here.
admin.site.register(Person, PersonAdmin)
admin.site.register(Task, TaskAdmin)