from django.contrib import admin
from .models import DummyTable,StudentInfo,ElectivesInfo,ResultsElectiveWise,ResultsDeptWise,RegistrationTime

# Register your models here.
admin.site.register(DummyTable)
admin.site.register(StudentInfo)
admin.site.register(ElectivesInfo)
admin.site.register(ResultsElectiveWise)
admin.site.register(ResultsDeptWise)
admin.site.register(RegistrationTime)
