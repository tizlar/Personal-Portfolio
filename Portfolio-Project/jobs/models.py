from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100, default=None)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
