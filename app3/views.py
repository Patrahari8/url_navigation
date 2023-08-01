from django.shortcuts import render

# Create your views here.
def goku(request):
    d={'n':['the','name', 'is','one','and','only','none','other','than','goku']}
    return render(request,'goku.html',context=d)