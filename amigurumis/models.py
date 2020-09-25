from django.db import models

# Create your models here.

class Cliente(models.Model):
    name = models.CharField('Nombre', max_length=30)

    def __str__(self):
        return self.name

class Color(models.Model):
    color = models.CharField('Colores', max_length=20)

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colorcitos'
        ordering = ['color']

    def __str__(self):
        return self.color

class Pedido(models.Model):
    name_cte = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    name = models.CharField('Personaje', max_length=30)
    tamano = models.IntegerField('Tamaño')
    colores = models.ManyToManyField(Color)
    cel = models.CharField('Celular', max_length=13)
    mail = models.CharField('Mail', max_length=50, blank = True, null = True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['name']
    
    def __str__(self):
        return str(self.name_cte) + ' pidió ' + self.name
