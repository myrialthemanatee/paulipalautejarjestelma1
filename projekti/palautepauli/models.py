from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.base import Model
from django import forms
from django.forms import widgets



class TalkooPalaute(models.Model):
    kayttaja = models.ForeignKey(User, on_delete=models.CASCADE)
    t_hyvaa = models.TextField("Missä onnistuimme?", max_length=1000)
    t_huonoa = models.TextField("Missä emme onnistuneet?", max_length=1000)
    t_kehitettavaa = models.TextField("Kehitysehdotukset", max_length=1000)
    ARVOSANA= (('1', '1. Surkea'),('2', '2. Huono'),('3', '3. Ok'),('4', '4. Hyvä'),('5', '5. Kiitettävä'),)
    arvosana = models.CharField("Anna kokonaisarvosana talkoille", max_length=10, choices=ARVOSANA, default=None)
    date = models.DateTimeField('date created', auto_now_add=True)
    def __str__(self):
        return '%s %s %s %s %s' % (self.kayttaja, self.t_hyvaa, self.t_huonoa, self.t_kehitettavaa, self.arvosana)
        #return self.comment


class KokousPalaute(models.Model):
    kayttaja = models.ForeignKey(User, on_delete=models.CASCADE)
    k_hyvaa = models.TextField("Missä onnistuimme?", max_length=1000)
    k_huonoa = models.TextField("Missä emme onnistuneet?", max_length=1000)
    k_kehitettavaa = models.TextField("Kehitysehdotukset", max_length=1000)
    ARVOSANA= (('1', '1. Surkea'),('2', '2. Huono'),('3', '3. Ok'),('4', '4. Hyvä'),('5', '5. Kiitettävä'),)
    arvosana = models.CharField(max_length=10, choices=ARVOSANA, default=None)
    date = models.DateTimeField('date created', auto_now_add=True)
    def __str__(self):
        return '%s %s %s %s %s' % (self.kayttaja, self.k_hyvaa, self.k_huonoa, self.k_kehitettavaa, self.arvosana)
    #    return self.comment


class Hairioilmoitus(models.Model):
    kayttaja = models.ForeignKey(User, on_delete=models.CASCADE)
    h_huoneisto = models.TextField("Mitä huoneistoa ilmoitus koskee?", max_length=10)
    h_hairionkuvaus = models.TextField("Kuvaile häiriön tyyppi", max_length=1000)
    h_hairiontarkennus = models.TextField("Tarkenna häiriön kuvausta", max_length=1000)
    ARVOSANA= (('1', '1. Häiritsee hyvin vähän'),('2', '2. Häiritsee vähän'),('3', '3. Häiritsee jonkin verran'),('4', '4. Häiritsee paljon'),('5', '5. Häiritsee koko ajan'),)
    arvosana = models.CharField(max_length=10, choices=ARVOSANA, default=None)
    date = models.DateTimeField('date created', auto_now_add=True)
    def __str__(self):
        return '%s %s %s %s %s' % (self.kayttaja, self.h_huoneisto, self.h_hairionkuvaus, self.h_hairiontarkennus, self.arvosana)
    #    return self.comment

