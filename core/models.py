from django.db import models

class CapitaisEstados(models.Model):

    estado = models.CharField('estado', max_length=20)
    capital = models.CharField('capital', max_length=20)
    habitantes = models.IntegerField('habitantes')

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'



    def __str__(self):
        return self.estado