from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import ImageUpload
from ImageUpload.settings import MEDIA_URL, BASE_DIR
# Create your views here.

#html upload id = Fileup



def main(request):
    return render(request, 'image/upform1.html')
def main2(request):
    return render(request, 'image/index.html')

def upload(request):
    if request.method == 'POST':
        #file = request.FILES['uploadBtn']
        file = request.FILES.get('uploadBtn', False)
        file_name = file.name
        img = ImageUpload(image=request.FILES.get('uploadBtn'))
        img.save()
    return render(request, 'image/uploaded.html', {'file_name': file_name})

def upload2(request):
    if request.method == 'POST':
        file = request.FILES['file1']
        file_name = file.name
        img = ImageUpload(image=request.FILES.get('file1'))
        img.save()
    return render(request, 'image/uploaded.html')



