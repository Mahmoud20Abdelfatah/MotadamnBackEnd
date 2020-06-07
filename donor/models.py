from django.db import models

class Donor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=("اسم المتبرع"))
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    gender = models.IntegerField()
    birthdate = models.DateField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_banned = models.IntegerField()
    created_at = models.DateTimeField()
    def __str__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'donor'