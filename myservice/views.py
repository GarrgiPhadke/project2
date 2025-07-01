from django.shortcuts import render

def myservice(request):
    return render(request, 'myservice.html')
def interior(request):
    return render(request, 'interior.html')
def architectural(request):
    return render(request, 'architectural.html')
def visu(request):
    return render(request, 'visu.html')
def project(request):
    return render(request, 'project.html')
def product(request):
    return render(request, 'product.html')
# Create your views here.
