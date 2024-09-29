from django.shortcuts import render
from .forms import PrescriptionUploadForm

def PrescriptionUploadView(request):
    if request.method == "POST":
        form = PrescriptionUploadForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = PrescriptionUploadForm()
        return render()
