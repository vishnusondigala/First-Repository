from django.db import models

# project definition mujab data dictionary mujab all modeles design karo and class banavo.

#-----------------------------------------------------------------------------------------------

class User(models.Model):

    roles = (
        ('Admin', 'Admin'),
        ('Donor', 'Donor'),
        ('Receiver', 'Receiver'),
        ('Volunteer', 'Volunteer'),
        ('Logistics', 'Logistics'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=roles)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.name


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    class Meta:
        db_table = "user_profile"

    def __str__(self):
        return self.user.name

#------------------------------------------------------------------------------------------------------------

