from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ViewForm
from  student.models import StudentContactDetails


def base(request):
    if request.method == "POST":
        form = ViewForm(request.POST) 
        if form.is_valid():
            StudentContactDetails = form.save(commit = False)
            StudentContactDetails.save()            
            return redirect('result')
        
    else:
        form = ViewForm()
    return render(request, "base.html", {'form': form})


def result(request):
    return HttpResponse('result')
