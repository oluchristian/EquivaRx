from django.db import models

# Create your models here.
class Prescription(models.Model):
    image_url = models.URLField(blank=True)
