from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def codeplayground(request):
    return HttpResponse("<h1>under development</h1>")
    