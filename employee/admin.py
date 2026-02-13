from django.contrib import admin
from .models import Employee,Course,Batch,Attendance

# Register your models here.

admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Attendance)