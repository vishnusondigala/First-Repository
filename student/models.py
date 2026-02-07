from django.db import models

# Create your models here.
class product(models.Model):
    productname=models.CharField(max_length=100)
    productprice=models.IntegerField()
    productdescription=models.TextField()
    productstock=models.PositiveIntegerField()
    productcolor=models.CharField(max_length=20,null=True)
    productstatus=models.BooleanField(default=True)

    class meta:
        db_table = "product"

#----------------------------------------------------------------------

class student(models.Model):
    studentname=models.CharField(max_length=100)
    studentage=models.IntegerField()
    studentcity=models.CharField(max_length=100)
    studentemail=models.EmailField(null=True)

    class meta:
        db_table = "student"
    def __str__(self):
        return self.studentname   


class StudentProfile(models.Model):
    hobbies =(("reading","reading"),("travel","travel"),("music","music"))
    #studentPrilfe id --> pk create auto...
    studentId = models.OneToOneField(student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()
    
    class Meta:
        db_table = "studentprofil"

    def __str__(self):
        return self.studentId.studentname    


#-------------------------------------------------------------------------------------------      
    

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"    

    def __str__(self):
        return self.categoryName    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName  

#--------------------------------------------------------------------------------------------------------          


#6-feb task-->create one to one relation (unique key) and 2 table one to menny(foraign key)        
#week end task--> create new app-->app name test-->models.py-->data dictonary all design/class

#---------------------------------------------------------------------------------------------------------

class Teacher(models.Model):
    teachername = models.CharField(max_length=100)
    teacherage = models.IntegerField()
    teacheremail = models.EmailField(null=True)

    class Meta:
        db_table = "teacher"

    def __str__(self):
        return self.teachername
    
 
class TeacherProfile(models.Model):

    subjects = (("maths", "maths"),("science", "science"),("english", "english"))

    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    teacherSubject = models.CharField(max_length=100, choices=subjects)
    teacherPhone = models.CharField(max_length=10)
    teacherAddress = models.CharField(max_length=100)
    teacherGender = models.CharField(max_length=10)
    teacherDOB = models.DateField()

    class Meta:
        db_table = "teacherprofile"

    def __str__(self):
        return self.teacher.teachername   
    
#----------------------------------------------------------------------------------------    

class Hospital(models.Model):
    hospitalName = models.CharField(max_length=100)
    hospitalAddress = models.CharField(max_length=200)
    hospitalstatus = models.BooleanField(default=True)

    class Meta:
        db_table = "hospital"

    def __str__(self):
        return self.hospitalName
    
class Doctor(models.Model):

    specialization = (("cardio", "cardio"),("ortho", "ortho"),("neuro", "neuro"))

    doctorName = models.CharField(max_length=100)
    doctorPhone = models.CharField(max_length=10)
    doctorSpecialization = models.CharField(max_length=50,choices=specialization)
    hospitalId = models.ForeignKey(Hospital,on_delete=models.CASCADE)

    class Meta:
        db_table = "doctor"

    def __str__(self):
        return self.doctorName

