from django.utils import timezone
from aliments.models import *
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import  User
from rest_framework.authtoken.models import Token
from django.conf import  settings
from django.db.models.signals import post_save
from django.dispatch import receiver

#Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    print('paassage in create auth user models')
    print(instance)
    print(instance.id)
    # for user in User.objects.all():
    #     Token.objects.get_or_create(user=user)
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def update_bmi( instance, update_fields, created=False, **kwargs):

    print('instance in update bmi',instance)
    query = Nutriuser.objects.get(username=instance)
    print(query.id)
    newbmi = ((query.weight) / (query.height * query.height)) * 10000
    Nutriuser.objects.filter(username=instance).update(bmi=newbmi)


class Nutriuser(AbstractUser):
    height = models.IntegerField(null=True) #(int, cm)
    weight = models.FloatField(null=True) #(float, kg)
    birthdate = models.DateField(null=True) #(date)
    gender = models.CharField(null=True, max_length=1) #(char, 'M' ou 'F')
    rda = models.FloatField(default=2200) #(float)
    bmi = models.FloatField(null=True, blank=True) #(float)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

class Repas(models.Model):
    user = models.ForeignKey(Nutriuser) #user 1:n JourRepas
    date = models.DateField(default=timezone.now())
    no_repas = models.IntegerField() # 0: peti dej., 1:coll.10h, 2:dejeuner etc

class ElementRepas(models.Model):
    repas = models.ForeignKey(Repas)
    portion = models.ForeignKey(Portionaliment)
    nbPortion = models.CharField(max_length=30, blank=True, null=True, default='')
    aliment = models.ForeignKey(Aliment)
    poids = models.CharField(max_length=30, blank=True, null=True, default='')
