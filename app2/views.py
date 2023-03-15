from django.shortcuts import render

# Create your views here.
def ssc(request):
    return render(request,'ssc.html')


def inter(request):
    return render(request,'inter.html')
