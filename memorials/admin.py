from django.contrib import admin
from .models import Memorial, Eulogy
# Register your models here.

# this is added so that they appear together in the admin view
class EulogyInline(admin.TabularInline):
    model = Eulogy
    extra = 0
class adminMemorial(admin.ModelAdmin):
    inlines = [EulogyInline,]

admin.site.register(Memorial, adminMemorial)
admin.site.register(Eulogy)
