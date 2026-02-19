from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=32)

def __repr__(self):
    return f'Color(self.name)'

class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    colors = models.ManyToManyField(to=Color)

def __str__(self):
    return self.name