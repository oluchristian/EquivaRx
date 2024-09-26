from django import forms


class PrescriptionUploadForm(forms.Form):
    prescription_image = forms.ImageField(label="Upload Prescription Image")