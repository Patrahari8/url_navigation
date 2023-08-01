from django.shortcuts import render

# Create your views here.
def death_note(request):
    return render(request,'death_note.html')