from django.db import models

#-------------------------------11 fab--implementation-----------------------------------------------------------↡↡↡↡

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"
        
    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.IntegerField()

    class Meta:
        db_table = "course"

    def __str__(self):
        return self.name
    
#-------------------------------11 fab--Task-----------------------------------------------------------↡↡↡↡

class Batch(models.Model):
    batch_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    timing = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = "batch"

    def __str__(self):
        return self.batch_name
    

class Attendance(models.Model):
    student_name = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "attendance"

    def __str__(self):
        return self.student_name

