from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .forms import NameForm, HashForm, UploadFileForm
from .models import Alumnos, Diplomas
import hashlib
from connect_web3 import consulta_diploma

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the data_base index for query hash.")
    return render(request, "data_base/index.html")

def search_user(request):
    form = NameForm(request.POST)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = request.POST.get('your_name')
            alumno = Alumnos.objects.filter(first_name__gte=name).values()
            print(alumno)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, "data_base/index.html",{"formu":form}) 
    
    return render(request, "data_base/search_user.html",{"formu":form}) 

def search_diplom_by_hash(request):
    form = HashForm(request.POST)
    if request.method == 'POST':
        form = HashForm(request.POST)

        if form.is_valid():
            hash_num = request.POST.get(('hash_number'))
            qry = Diplomas.objects.filter(diplom_hash__gte= hash_num).values()[0]
            img =open(qry['document'], 'rb')
            return FileResponse(img)

    return render(request, "data_base/search_hash.html",{"formu":form}) 


def hash_file(request):
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            file1 = request.FILES['file']
            
            print(request.FILES['file'])
            file_hash = hashlib.sha256() 
            BLOCK_SIZE = 65537
            
            fb = file1.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
            while len(fb) > 0: # While there is still data being read from the file
                file_hash.update(fb) # Update the hash
                fb = file1.read(BLOCK_SIZE) # Read the next block from the file
            return HttpResponse(f'success your hash is: {file_hash.hexdigest()}')


    return render(request, "data_base/create_hash.html",{"formu":form}) 

def view_hash_blockchain(request):
    form = HashForm(request.POST)
    if request.method == 'POST':
        form = HashForm(request.POST)
        if form.is_valid():
            hash_num = request.POST.get(('hash_number'))
            diplom_name = consulta_diploma(hash_num)
            if diplom_name =='':
                return HttpResponse("no existe el hash en la blockchain, trate nuevamente")
            else:
                return HttpResponse(f'success el diploma pertenece a: {diplom_name}')

    return render(request, "data_base/search_hash_block.html",{"formu":form}) 