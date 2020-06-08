from django.db import models
import datetime
class Charity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=("Charity Name"))
    email = models.CharField(unique=True, max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    logo  = models.ImageField(upload_to='charity/')
    description = models.TextField()
    password = models.CharField(max_length=255)
    is_banned = models.IntegerField()
    created_at = models.DateTimeField(blank=True, default=datetime.datetime.now)
    city = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'charity'
        verbose_name_plural = 'charities'
        managed = True
        db_table = 'charity'
