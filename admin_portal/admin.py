from django.contrib import admin
from .models import StudentInfo,ElectivesInfo,ResultsElectiveWise,RegistrationTime,Department,Elective

# Register your models here.
# admin.site.register(DummyTable)
admin.site.register(StudentInfo)
admin.site.register(ElectivesInfo)
admin.site.register(ResultsElectiveWise)
admin.site.register(RegistrationTime)
admin.site.register(Department)
admin.site.register(Elective)
