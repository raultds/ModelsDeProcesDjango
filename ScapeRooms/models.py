from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from datetime import date, datetime
from django import *


# Create your models here.

class ScapeRoom(models.Model):
    name = models.TextField(blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    city = models.TextField(default="")
    telf = models.TextField(blank=True, null=True)
    mail = models.TextField(blank=True, null=True)
    zipCode = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('ScapeRoom:scapeRoom_detail', kwargs={'pk': self.pk})


class CustomUser(User):
    birthday = models.DateField(default=datetime.date(datetime.today()))

    def __unicode__(self):
        return u"%s" % self.get_full_name()

    def get_absolute_url(self):
        return reverse('User:User detail', kwargs={'pk': self.pk})


class Opinion(models.Model):
    scapeRoomID = models.ForeignKey(ScapeRoom, default=1, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, default=2, on_delete=models.SET_DEFAULT)  # recordar de fer el usuari 2
    opinion = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.id

    def get_absolute_url(self):
        return reverse('Opinion:Opinion detail', kwargs={'pk': self.pk})


class Reservation(models.Model):
    date = models.DateField(default=date.today())
    scapeRoomID = models.ForeignKey(ScapeRoom, default=1, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, default=2, on_delete=models.SET_DEFAULT)  # recordar de fer el usuari 2

    def __unicode__(self):
        return u"%s" % self.id

    def get_absolute_url(self):
        return reverse('Reservation:Reservation detail', kwargs={'pk': self.pk})
