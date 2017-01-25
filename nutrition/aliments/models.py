#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class Aliment(models.Model):
    shrt_desc = models.CharField('nom court', max_length=100)
    long_desc = models.CharField('nom long', max_length=200, blank=True, default='')
    ctdit_no = models.CharField(max_length=10, blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True, default='')
    maxqty = models.DecimalField('qte max pour 2000kcal/j', max_digits=5, decimal_places=1)
    pict = models.CharField(max_length=300, blank=True, null=True)
    brand = models.NullBooleanField(blank=True, null=True)
    israw = models.NullBooleanField(blank=True, null=True)
    packpict = models.CharField(max_length=300, blank=True, null=True)
    keywords = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["shrt_desc"]
        verbose_name = u"Aliment et produit du commerce"
    
    def __unicode__(self):
        return self.shrt_desc


class PortionAliment(models.Model):
    aliment = models.ForeignKey(Aliment) # Aliment 1:n PortionAliment
    poids = models.CharField(max_length=30)
    nom = models.CharField(max_length=100)
    note = models.CharField(max_length=100, blank=True, null=True, default='')
    pict = models.CharField(max_length=300, blank=True, null=True)
    
    class Meta:
        ordering = ["aliment"]
        
    def __unicode__(self):
        return self.aliment.shrt_desc + ' / ' + self.nom


class Nutriment(models.Model):
    nutr_no = models.CharField(max_length=10, primary_key=True)
    ifda_no = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)
    tagname = models.CharField(max_length=10)
    nom = models.CharField(max_length=100)
    
    class Meta:
        ordering = ["nutr_no"]
          
    def __unicode__(self):
        return self.nom


class NutData(models.Model):
    aliment = models.ForeignKey(Aliment) # Aliment 1:n NutData
    nutriment = models.ForeignKey(Nutriment) # Nutriment 1:n NutData
    val = models.CharField(max_length=30)
    source = models.CharField(max_length=100)
    note = models.CharField(max_length=100, blank=True, null=True, default='')
    
    class Meta:
        # guarantees unicity of nutriment for a given aliment
        unique_together = ("aliment", "nutriment")
        ordering = ["nutriment"]
        
    def __unicode__(self):
        return self.aliment.shrt_desc + '/' + self.nutriment.nom

