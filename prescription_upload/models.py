from django.db import models

# Create your models here.
class Prescription(models.Model):
    prescription_image = models.ImageField(upload_to='prescriptions/')
    image_url = models.URLField(blank=True)
