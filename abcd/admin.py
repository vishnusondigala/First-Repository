from django.contrib import admin
from .models import User,UserProfile,Donor,Receiver,Volunteer,Logistics,Donations,PickupRequest,ReceiverRequest,TaskAssignment,Delivery,Inventory,Feedback,Reports

# Register your models here.


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Donor)
admin.site.register(Receiver)
admin.site.register(Volunteer)
admin.site.register(Logistics)
admin.site.register(Donations)
admin.site.register(PickupRequest)
admin.site.register(ReceiverRequest)
admin.site.register(TaskAssignment)
admin.site.register(Delivery)
admin.site.register(Inventory)
admin.site.register(Feedback)
admin.site.register(Reports)
