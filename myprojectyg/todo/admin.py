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


from esp.models import Vocab

class VocabAdmin(admin.ModelAdmin):
    list_display = ('eng', 'esp', 'pos', 'sub_date', 'user')
    list_filter = ('user', )
    date_hierarchy = ('sub_date')
    search_fields = ('eng', 'esp', 'user')
    
admin.site.register(Vocab, VocabAdmin)