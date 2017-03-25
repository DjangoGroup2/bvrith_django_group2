from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ViewForm
from  facultyapp.models import Comment


def first(request):
    if request.method == "POST":
        form = ViewForm(request.POST)
        if form.is_valid():
            Comment = form.save(commit = False)
            Comment.save()            
            return redirect('success')
        
    else:
        form = ViewForm()
    return render(request, "first.html", {'form': form})
   


def display(request):
    all_facultyapp = Comment.objects.all()
    return render(request, 'facultyapp/display.html', {'all_facultyapp': all_facultyapp, })

def search(request):
    all_facultyapp = Comment.objects.all()
    return render(request, 'facultyapp/search.html', {'all_facultyapp': all_facultyapp, })

def success(request):
    return HttpResponse('Success! Notifications Updated.')
