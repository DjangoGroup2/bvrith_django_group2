from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import TPO_Venue
from .models import Student

def index(request):
    latest_venue_list = TPO_Venue.objects.order_by('tpo_venue')[:5]
    template = loader.get_template('students/index.html')
    context = {
        'latest_venue_list': latest_venue_list,
    }
    return HttpResponse(template.render(context, request))


#def detail(request, venue_id):
#    try:
#        venue = TPO_Venue.objects.get(pk=venue_id)
#    except Question.DoesNotExist:
#        raise Http404("Venue does not exist")
#    return render(request, 'students/detail.html', {'venue': venue})

def detail(request, venue_id):
    venue = get_object_or_404(TPO_Venue, pk=venue_id)
    return render(request, 'students/detail.html', {'venue': venue})

def search(request):
    return render(request, 'students/search.html', {})

#.filter(student_percentage__range=(start_pctg, end_pctg))
def searchResults(request):
    try:

        start_pctg = '0'
        end_pctg = '100'
        backlogs = '0'
        if( 'start_pctg' in request.GET) and request.GET['start_pctg'].strip():  
          start_pctg = request.GET['start_pctg']
        if( 'end_pctg' in request.GET) and request.GET['end_pctg'].strip():  
          end_pctg = request.GET['end_pctg']
        if( 'backlogs' in request.GET) and request.GET['backlogs'].strip():  
          backlogs = request.GET['backlogs']
       	students = Student.objects.filter(student_percentage__range=(start_pctg, end_pctg)).filter(student_backlogs__in=(backlogs))
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'students/search.html', {'students': students})

