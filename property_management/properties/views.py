from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Property

def index(request):
    context = RequestContext(request)
    return render(request, 'properties/index.html', context)
    
def properties(request):
    #context = RequestContext(request)
    property_list = Property.objects.all()
    context = {'property_list': property_list }
    return render(request, 'properties/properties.html', context)
    
#def properties(request):
#	property_list = Property.objects.all()
#	context = RequestContext(request)
	#context = {'property_list': property_list}
#    return render(request, 'properties/properties.html', context)
    
    
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)
    