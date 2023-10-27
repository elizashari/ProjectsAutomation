from django.contrib import admin


from .models import Student, Level, Project, Call_time, PM, Group, Project_week

admin.site.register(Level)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Call_time)
admin.site.register(PM)
admin.site.register(Group)
admin.site.register(Project_week)