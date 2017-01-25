#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aliments import models
from django.contrib import admin
from django.db.models.deletion import Collector
from django.db.models.fields.related import ForeignKey
from django.http import HttpResponse



class NutDataInline(admin.TabularInline):
    model = models.NutData
    extra = 1


class PortionAlimentInline(admin.TabularInline):
    readonly_fields = ('id',)
    model = models.PortionAliment
    # template = "admin/tabular_pict.html" # les champ 'pict' sont traités de façon spéciale
    fields = ['poids', 'nom', 'note', 'id', 'pict']
    extra = 0


class AlimentAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('Informations de base', {'fields': ['shrt_desc', 'long_desc', 'pict', 'note', 'brand']}),
                 ('Divers', {'fields': ['maxqty', 'ctdit_no']})
                 ]
    list_display = ('shrt_desc', 'long_desc', 'ctdit_no', 'note')
    inlines = [PortionAlimentInline, NutDataInline]
    search_fields = ['shrt_desc', 'long_desc', 'ctdit_no']
    #actions = [duplicate]

admin.site.register(models.Aliment, AlimentAdmin)


class NutrimentAdmin(admin.ModelAdmin):
    list_display = ('nutr_no', 'nom', 'unit')

admin.site.register(models.Nutriment, NutrimentAdmin)



# JCB: voir http://stackoverflow.com/questions/437166/duplicating-model-instances-and-their-related-objects-in-django-algorithm-for
def duplicate(modeladmin, request, queryset):
    for obj in queryset:
        collector = Collector({})
        collector.collect([obj])
        collector.sort()
        related_models = collector.data.keys()
        data_snapshot = {}
        for key in collector.data.keys():
            data_snapshot.update({key: dict(zip([item.pk for item in collector.data[key]], [item for item in collector.data[key]]))})
        root_obj = None

        duplicate_order = reversed(related_models)
        for model in duplicate_order:
            # Find all FKs on model that point to a related_model
            fks = []
            for f in model._meta.fields:
                if isinstance(f, ForeignKey) and f.rel.to in related_models:
                    fks.append(f)
            # Replace each `sub_obj` with a duplicate
            if model not in collector.data:
                continue
            sub_objects = collector.data[model]
            for obj in sub_objects:
                for fk in fks:
                    fk_value = getattr(obj, "%s_id" % fk.name)
                    # If this FK has been duplicated then point to the duplicate
                    fk_rel_to = data_snapshot[fk.rel.to]
                    if fk_value in fk_rel_to:
                        dupe_obj = fk_rel_to[fk_value]
                        setattr(obj, fk.name, dupe_obj)
                # Duplicate the object and save it.
                obj.id = None
                obj.save()
                if root_obj is None:
                    root_obj = obj

duplicate.short_description = "Duplique les aliments selectionnes"
