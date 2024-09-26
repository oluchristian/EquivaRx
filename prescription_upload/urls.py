from django.urls import path
from . import views, api_views


urlpatterns = [
    path('upload/', api_views.PrescriptionUploadView.as_view(), name='upload_prescription'),
]