from django.db import models

class Supercategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'supercategory'
        verbose_name_plural = 'supercategories' 
        managed = True
        db_table = 'supercategory'
