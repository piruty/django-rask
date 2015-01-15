from django.contrib import admin
from task.models import List, Task

class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('id', 'title', )
admin.site.register(List, ListAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'finished', )
    list_display_links = ('id', 'title', )
admin.site.register(Task, TaskAdmin)
