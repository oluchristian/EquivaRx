from rest_framework import serializers
from .models import Prescription
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary import CloudinaryImage


class PrescriptionUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['prescription_image']

    def create(self, validated_data):
        """Create and returns a new PrescriptionUpload instance
            given the validated data
        """
        prescription = Prescription(**validated_data)
        prescription.save()
        prescription.image_url = prescription.prescription_image.url
        prescription.save(update_fields=['image_url'])
        return prescription
        