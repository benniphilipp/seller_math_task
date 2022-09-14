from django.db import models


class CsvSeller(models.Model):
    zip = models.CharField(max_length=30, blank=True, null=True)
    summe = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.summe)

