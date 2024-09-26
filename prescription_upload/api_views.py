from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import PrescriptionUploadSerializer

class PrescriptionUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PrescriptionUploadSerializer(data=request.data)
        if serializer.is_valid():
            prescription = serializer.save()
            return Response({
                'image_url': prescription.image_url
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)