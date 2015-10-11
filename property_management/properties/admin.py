from django.contrib import admin
from properties.models import Property
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User
import guardian.shortcuts
from guardian.shortcuts import get_perms
from guardian.admin import GuardedModelAdmin

from functools import partial


# TODO: Figure out a way to hide the object permissions button
class PropertyAdmin(GuardedModelAdmin):
    def has_change_permission(self, request, obj=None):
        ct = ContentType.objects.get_for_model(self.model)
        can_view = False
        if request.user.is_superuser:
            can_view = True
        else:
            if request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)):
                can_view = True
            elif request.user.has_perm('%s.change_%s' % (ct.app_label, ct.model)):
                can_view = True

        return can_view

    def get_readonly_fields(self, request, obj=None):
        ct = ContentType.objects.get_for_model(self.model)

        if request.user.has_perm('%s.change_%s' % (ct.app_label, ct.model), obj):
            return self.readonly_fields
        elif not request.user.is_superuser and request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)):
            return [user.name for user in self.model._meta.fields]

    # Workaround for guardian queryset bug
    @property
    def queryset(self):
        return partial(self.get_queryset)

# Register your models here.
admin.site.register(Property, PropertyAdmin)
