from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):

    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Item has been added to the list")

    all_items = List.objects.all()
    context = {"items" : all_items}        
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {})