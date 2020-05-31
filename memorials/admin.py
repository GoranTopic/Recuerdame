from django.contrib import admin
from .models import Memorial
from eulogies.models import Eulogy
from tributes.models import Tribute

# This makes it so that they appear together in the admin page
class EulogyInline(admin.TabularInline):
    model = Eulogy
    extra = 0

class TributeInline(admin.TabularInline):
    model = Tribute

class adminMemorial(admin.ModelAdmin):
    inline = [ EulogyInline, ]

admin.site.register(Memorial, adminMemorial)
