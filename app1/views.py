from django.shortcuts import render

# Create your views here.
def degree(request):
    return render(request,'degree.html')



def mca(request):
    return render(request,'mca.html')