from django.http import HttpResponse, HttpResponseRedirect
from resume_builder.forms import StudentForm
from django.shortcuts import redirect,render
from resume_builder.models import personalInfo

def index(request):
	return HttpResponse("welcome")
def resume(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			personalInfo = form.save(commit = False)
			personalInfo.save()
			return redirect('success')
	else:
		form = StudentForm()
	return render(request, 'resume_builder/resume.html', {'form': form})

def success(request):
	return HttpResponse("success Hurray!!")
	