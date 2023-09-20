from django.db import models

class Item(models.Model):
    nama = models.CharField(max_length=255)
    kelas = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=255)