from django.db import models
from simple_history.models import HistoricalRecords


class Branch(models.Model):
    name = models.CharField(max_length=64)
    geo = models.CharField(max_length=128)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Branches'

    def __str__(self):
        return f'{self.name}'
