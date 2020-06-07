from django.db import models

class Charity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    phone = models.TextField()
    address = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    description = models.TextField()
    password = models.CharField(max_length=255)
    is_banned = models.IntegerField()
    created_at = models.DateTimeField()
    city = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'charity'

