from django.shortcuts import get_object_or_404, render

from .models import Property

# Create your views here.
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/properties.html',
        { 'properties': properties })

def property_detail(request):
    individual_property = get_object_or_404(Property, pk=pk)
    return render(request, 'properties/property.html', 
        { 'individual_property': individual_property })

