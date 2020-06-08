from django.db import models
from beneficiary.models import Beneficiary

class Cases(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField()
    needed_amount = models.IntegerField()
    approved = models.IntegerField()
     #subcat = models.ForeignKey('Subcategory', on_delete=models.CASCADE)
    ben = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'case'
        verbose_name_plural = 'cases'
        managed = True
        db_table = 'cases'
