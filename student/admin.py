from django.contrib import admin
from .models import student,product,StudentProfile,Category,Service,Teacher,TeacherProfile,Hospital,Doctor

# Register your models here.

admin.site.register(student)
admin.site.register(product)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Teacher)
admin.site.register(TeacherProfile)
admin.site.register(Hospital)
admin.site.register(Doctor)