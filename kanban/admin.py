from django.contrib import admin

from .models import Category, Project, Status, Task, Team

# Register your models here.
admin.site.register(Status)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Team)
admin.site.register(Task)
