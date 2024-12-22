from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def informatics_detail(request):
    return render(request, 'details/informatics_detail.html')

def medicine_detail(request):
    return render(request, 'details/medicine_detail.html')

def economics_detail(request):
    return render(request, 'details/economics_detail.html')