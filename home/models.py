# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Clientes(models.Model):

    #__Clientes_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)

    #__Clientes_FIELDS__END

    class Meta:
        verbose_name        = _("Clientes")
        verbose_name_plural = _("Clientes")


class Datos-Clientes(models.Model):

    #__Datos-Clientes_FIELDS__
    cliente_id = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    telefono = models.IntegerField(null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)

    #__Datos-Clientes_FIELDS__END

    class Meta:
        verbose_name        = _("Datos-Clientes")
        verbose_name_plural = _("Datos-Clientes")


class Prendas(models.Model):

    #__Prendas_FIELDS__
    cliente_id = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fecha_venta = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Prendas_FIELDS__END

    class Meta:
        verbose_name        = _("Prendas")
        verbose_name_plural = _("Prendas")



#__MODELS__END
