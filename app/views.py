from django.shortcuts import render

# Create your views here.
def naruto(request):
    return render(request,'naruto.html')
def sasuke(request):
    return render(request,'sasuke.html')
