from django.contrib import admin
from .models import Memorial
# Register your models here.
from eulogies.models import Eulogy

# this is added so that they appear together in the admin view
class EulogyInline(admin.TabularInline):
    model = Eulogy
    extra = 0
class adminMemorial(admin.ModelAdmin):
    inlines = [EulogyInline,]

admin.site.register(Memorial, adminMemorial)
