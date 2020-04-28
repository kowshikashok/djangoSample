from django.http import HttpResponse

# Create your views here.

def services(request):
    # http://127.0.0.1:8000/test/?person=kowshik&place=coimbatore
	return HttpResponse("Hello, Team! This is " +request.GET.get('person', None)+ " from "+request.GET.get('place', None))