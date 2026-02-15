from django.db import models

# Create your models here.

class Servicee(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField(help_text="Duration in days")

    class Meta:
        db_table = "Servicee"   
    def __str__(self):
        return self.name
