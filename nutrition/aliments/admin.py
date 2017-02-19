from django.contrib import admin
from .models import Portionaliment, Aliment, Nutriment, Nutdata

# Register your models here.
admin.site.register(Portionaliment)
admin.site.register(Nutriment)
admin.site.register(Nutdata)

class PortionAlimentInline(admin.TabularInline):
    model = Portionaliment

class NutdataInline(admin.TabularInline):
    model = Nutdata

class AlimentAdmin(admin.ModelAdmin):
    list_display = ('shrt_desc','long_desc')
    fieldsets = (
            ('Information de base',{ 'fields':('shrt_desc', 'long_desc' )}),
            
    )
    inlines = [
        PortionAlimentInline,
        NutdataInline,
    ]


    

admin.site.register(Aliment, AlimentAdmin)
