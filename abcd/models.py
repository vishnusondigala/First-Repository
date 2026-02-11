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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=150)
    receiver_type = models.CharField(max_length=20, choices=RECEIVER_TYPE)
    registration_no = models.CharField(max_length=100)

    class Meta:
        db_table = "receivers"

    def __str__(self):
        return self.organization_name
    
#------------------------------------------------------------------------------------------

class Volunteer(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)
    assigned_area = models.CharField(max_length=100)

    class Meta:
        db_table = "volunteers"

    def __str__(self):
        return self.user.name
    
#-------------------------------------------------------------------------------------------

class Logistics(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=50)
    service_area = models.CharField(max_length=100)

    class Meta:
        db_table = "logistics"

    def __str__(self):
        return self.user.name

#-------------------------------------------------------------------------------------------

class Donations(models.Model):

    CONDITION_CHOICES = (
        ("New", "New"),
        ("Good", "Good"),
        ("Usable", "Usable"),
    )

    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Collected", "Collected"),
        ("Delivered", "Delivered"),
    )

    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    cloth_type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    pickup_required = models.BooleanField(default=False)
    donation_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    class Meta:
        db_table = "donations"

    def __str__(self):
        return f"{self.cloth_type} - {self.donor.user.name}"

#-------------------------------------------------------------------------------------------

class PickupRequest(models.Model):

    PICKUP_STATUS = (
        ("Scheduled", "Scheduled"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    )
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE,null=True)
    donation = models.OneToOneField(Donations,on_delete=models.CASCADE)
    pickup_address = models.TextField()
    pickup_date = models.DateField()
    pickup_status = models.CharField(
        max_length=20,
        choices=PICKUP_STATUS,
        default="Scheduled"
    )

    class Meta:
        db_table = "pickup_requests"

    def __str__(self):
        return f"Pickup for Donation {self.donation.id}"

#-----------------------------------------------------------------------------------


class ReceiverRequest(models.Model):

    REQUEST_STATUS = (
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Fulfilled", "Fulfilled"),
    )

    receiver = models.ForeignKey(
        Receiver,                 # Receiver table (NGO / Shelter / Orphanage)
        on_delete=models.CASCADE
    )
    cloth_type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    request_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=REQUEST_STATUS,
        default="Approved"
    )

    class Meta:
        db_table = "receiver_requests"

    def __str__(self):
        return f"Request by {self.receiver.id}"
    
#----------------------------------------------------------------------------

class TaskAssignment(models.Model):

    taskTypes = (
        ("Collection", "Collection"),
        ("Sorting", "Sorting"),
        ("Delivery", "Delivery"),
    )

    taskStatus = (
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    )

    volunteer = models.ForeignKey(Volunteer,on_delete=models.CASCADE)
    donation = models.ForeignKey(Donations,on_delete=models.CASCADE)
    taskType = models.CharField(max_length=20,choices=taskTypes)
    taskStatus = models.CharField(max_length=20,choices=taskStatus,default="Pending")

    class Meta:
        db_table = "task_assignment"

    def __str__(self):
        return self.taskType
    
#----------------------------------------------------------------------------------------------

class Delivery(models.Model):

    deliveryStatus = (
        ("Pending", "Pending"),
        ("Delivered", "Delivered"),
    )

    donation = models.ForeignKey(Donations,on_delete=models.CASCADE)
    logistics = models.ForeignKey(Logistics,on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver,on_delete=models.CASCADE)
    deliveryDate = models.DateField()
    deliveryStatus = models.CharField(max_length=20,choices=deliveryStatus,default="Pending")

    class Meta:
        db_table = "delivery"

    def __str__(self):
        return str(self.id)
    
#---------------------------------------------------------------------------------------------------------

class Inventory(models.Model):
    clothType = models.CharField(max_length=100)
    availableQuantity = models.IntegerField()
    lastUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "inventory"

    def __str__(self):
        return self.clothType
    
#--------------------------------------------------------------------------------------------------------------
 
class Feedback(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    message = models.TextField()
    feedbackDate = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "feedback"

    def __str__(self):
        return str(self.user.id)
    
#-----------------------------------------------------------------------------------------------------------------    

class Reports(models.Model):

    reportTypes = (
        ("Donation", "Donation"),
        ("Receiver", "Receiver"),
        ("Volunteer", "Volunteer"),
    )

    generatedBy = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    reportType = models.CharField(
        max_length=100,
        choices=reportTypes
    )
    generatedDate = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "reports"

    def __str__(self):
        return self.reportType


    






