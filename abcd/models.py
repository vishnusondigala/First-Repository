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

class Donor(models.Model):

    DONOR_TYPE = (
        ('Individual', 'Individual'),
        ('Organization', 'Organization'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    donor_type = models.CharField(max_length=20, choices=DONOR_TYPE)
    organization_name = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "donors"

    def __str__(self):
        return self.user.name
    
#----------------------------------------------------------------------------------------------------


class Receiver(models.Model):

    RECEIVER_TYPE = (
        ('NGO', 'NGO'),
        ('Shelter', 'Shelter'),
        ('Orphanage', 'Orphanage'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=150)
    receiver_type = models.CharField(max_length=20, choices=RECEIVER_TYPE)
    registration_no = models.CharField(max_length=100)

    class Meta:
        db_table = "receivers"

    def __str__(self):
        return self.organization_name

