from django.contrib import admin
from core.models import User, List, Task

# Register your models here.

class ListAdmin(admin.ModelAdmin):
    model = List
    list_display = (
        "title",
        "user",
        "date",
        "completed",
    )

class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = (
        "name",
        "time_allocated",
        "list",
        "category",
        "completed",
    )

admin.site.register(List, ListAdmin)
admin.site.register(Task, TaskAdmin)
