from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Property

def index(request):
    context = RequestContext(request)
    return render(request, 'properties/index.html', context)

#def index(request):
#	template = loader.get_template('properties/index.html')
#    context = RequestContext(request, {
#        
#    })
#    return render(template.render(context))
    

def properties(request):
    context = RequestContext(request)
    return render(request, 'properties/properties.html', context)
    
#def properties(request):
#    template = loader.get_template('properties/properties.html')
#    return HttpResponse(template.render())
