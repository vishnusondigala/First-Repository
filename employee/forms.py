from django import forms
from .models import Employee,Course,Batch,Attendance

#employee form
#modelForm -->it will create form using model fileds
#-------------------------------11 fab--implementation-----------------------------------------------------------↡↡↡↡
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' #[name,age,salary,joiningDate,post]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__' 

#-------------------------------11 fab--Task-----------------------------------------------------------↡↡↡↡


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'



class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'




