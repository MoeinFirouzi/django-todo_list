from django.shortcuts import render

def home(request):
    #code
    return render(request, 'home.html',{})

def about(request):
    return render(request, 'about.html', {})
    
