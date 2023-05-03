from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'Hai HOw aRe You'}
    
    return render(request,'filters.html',d)