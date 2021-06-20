from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def syllabus(request):
    return render(request,'syllabus.html')

def contact(request):
    return render(request,'contact.html')

def resources(request):
    return render(request,'resources.html')

def extras(request):
    return render(request,'extras.html')

def notes(request):
    return render(request,'notes.html')


def Qpapers(request):
    return render(request,'Qpapers.html')


def books(request):
    return render(request,'books.html')

def login(request):
    return render(request,'login.html')

def pdfNotes(request):
    return render(request,'pdfNotes.html')

def resources(request):
    return render(request,'resources.html')

def studilinks(request):
    return render(request,'studilinks.html')

def writtenNotes(request):
    return render(request,'writtenNotes.html')

