from django.db import models

class Case(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField()
    needed_amount = models.IntegerField()
    approved = models.IntegerField()
    subcat = models.ForeignKey('Subcategory', models.DO_NOTHING)
    ben = models.ForeignKey(Beneficiary, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'cases'
