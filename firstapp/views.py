from django.shortcuts import render
from django.http import HttpResponse

from firstapp.models import Person

# Create your views here.
def myView(request):
    return HttpResponse('Hello World!')

def oneView(request):
    name = '박하영'
    return render(request, 'firstapp/one.html',{'name': name} )

def twoView(request):
	return render(request, 'firstapp/two.html')

def threeView(request):
	return render(request, 'firstapp/three.html')

def personView(request):
	people = Person.objects.all()
	return render(request, 'firstapp/person.html', {'people': people})