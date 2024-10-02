from rest_framework import serializers
from .models import Prescription


class PrescriptionUploadSerializer(serializers.ModelSerializer):
    #This field will not be saved to the model
    prescription_image = serializers.ImageField(write_only=True)
    class Meta:
        model = Prescription
        fields = ['prescription_image']
