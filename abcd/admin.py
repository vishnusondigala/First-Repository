from django.contrib import admin
from .models import User,UserProfile,Donor,Receiver

# Register your models here.


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Donor)
admin.site.register(Receiver)