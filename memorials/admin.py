from django.contrib import admin
from .models import Memorial
from eulogies.models import Eulogy

# Register your models here.


# This makes it so that they appear together in the admin page

class EulogyInline(admin.TabularInline):
    model = Eulogy
    extra = 0
class adminMemorial(admin.ModelAdmin):
    inline = [EulogyInline,]

admin.site.register(Memorial, adminMemorial)
