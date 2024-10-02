import cloudinary.uploader
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import PrescriptionUploadSerializer
from .models import Prescription
from ocr_processing.extract_text import extract_text_from_image

class PrescriptionUploadView(APIView):
    def post(self, request, *args, **kwargs):
        prescription_image = PrescriptionUploadSerializer(data=request.data)
        prescription_image.is_valid(raise_exception=True)

        #Get the image from the validated data
        image = prescription_image.validated_data['prescription_image']

        #Upload the image to cloudinary
        upload_data = cloudinary.uploader.upload(image)
        image_url = upload_data.get('url')

        # Extract text using OCR
        extracted_text = extract_text_from_image(image_url)

        #Create a new prescription instance to save image_path
        prescription = Prescription(image_url=image_url)

        # Save the Prescription instance with the updated image_url
        prescription.save()
        return Response({
            'image_url': prescription.image_url,
            'extracted_text': extracted_text,
        }, status=status.HTTP_201_CREATED)