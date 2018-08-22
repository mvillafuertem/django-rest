from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('name',)
