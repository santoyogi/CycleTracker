from django.db import models


# Create your models here.
class Cycle(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField(max_length=2000)