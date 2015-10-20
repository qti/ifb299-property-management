from django.contrib import admin
from properties.models import Property
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User, Group


# Note to self, read the docs before trying to overengineer something simple ;_;
class PropertyAdmin(admin.ModelAdmin):
    # Set form fields to read-only depending on the user
    def get_form(self, request, obj=None, **kwargs):
        if request.user.groups.filter(name='owners').exists():
            self.readonly_fields = ('owner', 'manager', 'contract_information',)
        elif request.user.groups.filter(name='managers').exists():
            self.readonly_fields = ('manager',)

        return super(PropertyAdmin, self).get_form(request, obj, **kwargs)

    # Filter queryset to properties we own
    def get_queryset(self, request):
        qs = super(PropertyAdmin, self).get_queryset(request)

        # If admin, show all properties
        if request.user.is_superuser:
            return qs
        elif request.user.groups.filter(name='owners').exists():
            return qs.filter(owner=request.user)
        elif request.user.groups.filter(name='managers').exists():
            return qs.filter(manager=request.user)



# Register your models here.
admin.site.register(Property, PropertyAdmin)
