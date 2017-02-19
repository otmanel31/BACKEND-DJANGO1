from django.db import models

from django.contrib.auth.models import User


from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
#         #print(token.key)

class Portionaliment(models.Model):
    aliment_id = models.ForeignKey('Aliment')
    poids = models.CharField(max_length=30)
    nom = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    pict = models.CharField(max_length=300)
    
    def __str__(self):
        return self.nom

    class Meta:
        db_table = 'portionaliment'

class Nutriment(models.Model):
    nutr_no = models.CharField(primary_key=True, max_length=10)
    ifda_no = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)
    tagname = models.CharField(max_length=10)
    nom = models.CharField(max_length=10)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = 'nutriment'

class Nutdata(models.Model):
    aliment_id = models.ForeignKey('Aliment')
    nutriment_id = models.ForeignKey('Nutriment',max_length = 10)
    val = models.CharField(max_length = 30)
    source = models.CharField(max_length = 100)
    note = models.CharField(max_length = 100)

        
    def __str__(self):
        return self.val

    class Meta:
        db_table = 'nutdata'

class Aliment(models.Model):
    shrt_desc = models.CharField(max_length = 100)
    long_desc = models.CharField(max_length = 200)
    ctdit_no = models.CharField(max_length = 10, blank = True) 
    note = models.CharField(max_length = 100, blank = True)
    maxqty = models.DecimalField(max_digits=10, decimal_places= 2)
    pict = models.CharField(max_length = 300)
    brand = models.NullBooleanField()
    israw = models.NullBooleanField()
    packpict = models.CharField(max_length = 300)
    keywords = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.shrt_desc
    class Meta:
        db_table = 'aliment'
        ordering = ['shrt_desc']

