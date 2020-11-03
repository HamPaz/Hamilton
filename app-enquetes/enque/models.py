import datetime
from django.db import models
from django.utils import timezone

class Pergs(models.Model):
    txt_perg = models.CharField(max_length=200)
    dat_publ = models.DateTimeField('Publicado em')
    def __str__(self):
        return self.txt_perg
    def publicado_recente(self):
        agora = timezone.now()
        return agora - datetime.timedelta(days=1) <= self.dat_publ <= agora
    publicado_recente.admin_order_field = 'dat_publ'
    publicado_recente.boolean = True
    publicado_recente.short_description = 'Publicado recentemente?'

class Escol(models.Model):
    pergunta = models.ForeignKey(Pergs, on_delete=models.CASCADE)
    txt_escol = models.CharField(max_length=200)
    int_votos = models.IntegerField(default=0)
    def __str__(self):
        return self.txt_escol


#	    return self.dat_publ >= timezone.now() - datetime.timedelta(days=1)
