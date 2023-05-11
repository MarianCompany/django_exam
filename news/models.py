from django.db import models
from branch.models import Branch
from simple_history.models import HistoricalRecords


class News(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    date = models.DateField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='news', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'
