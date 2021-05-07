from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage

def button(request):
    return render(request,'home.html')

def external(request):
    image=request.FILES['image']
    print("image is",image)
    
    fs=FileSystemStorage()
    filename=fs.save(image.name,image)
    fileurl=fs.open(filename)
    templateurl=fs.url(filename)

    print("file raw url",filename)
    print("file full url",fileurl)
    print("template url",templateurl)

    image = run([sys.executable,'F://webtest files//Webtest//imagecode.py',str(fileurl),str(filename)],shell=False,stdout=PIPE)
    print(image.stdout)
    return render(request,'home.html',{'raw_url':templateurl,'edit_url':image.stdout.decode('utf-8')}) # add .decode('utf-8') only in Windows 10