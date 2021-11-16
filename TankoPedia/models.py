from django.db import models
from django.db.models.base import Model

# Create your models here.
class tanks(models.Model):
    nom=models.CharField(max_length=50)
    pays=models.CharField(max_length=50)
    cat=models.CharField(max_length=50)
    desc=models.TextField()
    tank_id=models.IntegerField()

    def __str__(self):
        return self.nom