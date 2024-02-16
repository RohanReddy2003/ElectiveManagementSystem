from django.db import models

# Create your models here.
class DummyTable(models.Model):
    years_exp = models.FloatField()
    salary = models.FloatField()

    def __str__(self):
        return self.years_exp