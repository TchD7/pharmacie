from django.db import models
from phone_field import PhoneField
# Create your models here.
class Commune(models.Model):
    listes_des_communes = (('ADETIKOPE','ADETIKOPE'),('LEGBASSITO','LEGBASSITO'),
                           ('BAGUIDA','BAGUIDA'),('BE_EST','BE_EST'),('BE_CENTRE','BE_CENTRE'),
                           ('BE_OUEST','BE_OUEST'),('AFLAO_SAGBADO','AFLAO_SAGBADO'),
                           ('AFLAO_GAKLI','AFLAO_GAKLI'),('VAKPOSSITO','VAKPOSSITO'),
                           ('AGOENYIVE','AGOENYIVE'),('ZANGUERA','ZANGUERA'),('TOGBLE','TOGBLE'),('AMOUTIVE','AMOUTIVE') )
    nom_commune = models.CharField(choices=listes_des_communes,max_length=200)

    def __str__(self):
        return self.nom_commune


class Pharms(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    localisation = models.URLField(max_length=150)
    commune = models.ForeignKey(Commune,max_length=200,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
        #return  self.commune
class Pharms_de_garde(models.Model):
    pharm = models.OneToOneField(Pharms, on_delete=models.CASCADE,)
    is_garde = models.BooleanField(default=True)
    def __str__(self):
        return self.pharm.name