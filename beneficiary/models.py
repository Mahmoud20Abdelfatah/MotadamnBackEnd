from django.db import models

class Beneficiary(models.Model):
    id = models.BigAutoField(primary_key=True)
    national_id = models.BigIntegerField(unique=True)
    gender = models.IntegerField()
    martial_status = models.CharField(max_length=8)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    birthdate = models.DateField()
    photo = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    charity = models.ForeignKey('Charity', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'beneficiary'