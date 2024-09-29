from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import PrescriptionUploadSerializer

class PrescriptionUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PrescriptionUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        prescription = serializer.save()
        return Response({
            'image_url': prescription.image_url
        }, status=status.HTTP_201_CREATED)