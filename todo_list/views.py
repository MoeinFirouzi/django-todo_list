from django import forms
from django.shortcuts import redirect, render
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

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

def delete(request,item_id):
    item = List.objects.get(pk=item_id)
    item.delete()
    messages.success(request,"Item has been deleted")
    return redirect('home')

def uncross(request,item_id):
    item = List.objects.get(pk=item_id)
    item.completed = False
    item.save()
    return redirect('home')

def cross_off(request,item_id):
    item = List.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return redirect('home')    

def edit(request,item_id):
    """
    from home by GET method and from edit page by POST method
    """
    if request.method == "POST":
        edited_item = List.objects.get(pk=item_id)
        """
        note:
        A model form instance attached to a model object will 
        contain an instance attribute that gives its methods 
        access to that specific model instance.
        https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#overriding-the-clean-method
        """
        form = ListForm(request.POST, instance=edited_item)
        if form.is_valid():
            form.save()
            messages.success(request,f"Item has been changed to \"{str(edited_item)}\"")
            return redirect('home')
    else: 
        item = List.objects.get(pk=item_id)
        context = {"item": item}
        return render(request, 'edit.html', context)