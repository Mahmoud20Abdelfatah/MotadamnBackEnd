from django.db import models

class Donor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.TextField()
    address = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    gender = models.IntegerField()
    birthdate = models.DateField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_banned = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'donor'