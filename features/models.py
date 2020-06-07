from django.db import models

class Features(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'features'
        verbose_name_plural = 'features' 
        managed = True
        db_table = 'features'