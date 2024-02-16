from django.db import models

# Create your models here.
class DummyTable(models.Model):
    years_exp = models.FloatField()
    salary = models.FloatField()

    def __str__(self):
        return self.years_exp

class StudentInfo(models.Model):
    s_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    jntu_no = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    email = models.EmailField()
    curr_sem = models.IntegerField()

    def __str__(self):
        return self
    

class ElectivesInfo(models.Model):
    course_code = models.CharField(max_length=20)
    elective_name = models.CharField(max_length=100)
    offering_department = models.CharField(max_length=50)
    offering_strength = models.IntegerField()
    not_allowed_students = models.ManyToManyField(StudentInfo, blank=True)

    def __str__(self):
        return self
    
class ResultsElectiveWise(models.Model):
    id= models.UUIDField(primary_key=True)
    elective_name = models.ForeignKey('ElectivesInfo', on_delete=models.CASCADE)
    stu_name = models.ForeignKey('StudentInfo', on_delete=models.CASCADE)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self

class ResultsDeptWise(models.Model):
    id= models.UUIDField(primary_key=True)
    department = models.CharField(max_length=50)
    stu_name = models.ForeignKey('StudentInfo', on_delete=models.CASCADE)
    elective_name = models.ForeignKey('ElectivesInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self
    
class RegistrationTime(models.Model):
    # id= models.UUIDField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self
