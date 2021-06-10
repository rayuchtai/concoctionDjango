from django.db import models

# Create your models here.
class World(models.Model):
    name = models.CharField(max_length=50)
    creation = models.CharField(max_length=300)
    notes = models.TextField()
