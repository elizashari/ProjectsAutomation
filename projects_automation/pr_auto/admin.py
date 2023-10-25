from django.contrib import admin


from .models import Student, Level, Project

admin.site.register(Level)
admin.site.register(Student)
admin.site.register(Project)
