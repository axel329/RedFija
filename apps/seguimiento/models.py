from django.db import models

# Create your models here.

class Tipo_seguimiento(models.Model):

    tipo =models.CharField(max_length=50,verbose_name="Tipo")
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name='tipo'
        verbose_name_plural = 'tipos'
        ordering = ['tipo']

    def __str__(self):
        return self.tipo


class Seguimiento(models.Model):

    numero_seguimiento=models.CharField(max_length=30, null=True, blank=True)
    cedula=models.CharField(max_length=20, null=True, blank=True)
    nombre=models.CharField(max_length=50, null=True, blank=True, verbose_name="Cliente")
    telefono=models.CharField(max_length=10, null=True, blank=True)
    direccion=models.CharField(max_length=50, null=True,blank=True, verbose_name="Dirección")
    departamento=models.CharField(max_length=30, null=True, )
    ciudad=models.CharField(max_length=50, verbose_name="Ciudad", null=True)
    descripcion=models.TextField(verbose_name="Descripción")
    fecha_apertura=models.DateField()
    estado_siebel=models.CharField(max_length=10, null=False, blank=True)
    grupo=models.CharField(max_length=10, null=True, blank=True)
    asunto_correo=models.CharField(max_length=30, null=False, blank=True)
    empresa=models.CharField(max_length=30, null=False, blank=True)
    nombre_obra=models.CharField(max_length=30, null=False, blank=True)
    consorcio=models.CharField(max_length=30, null=False, blank=True)
    arpu=models.CharField( max_length=30, null=False, blank=True)
    tipo_seguimiento = models.ManyToManyField(Tipo_seguimiento, verbose_name="Tipo")

    class Meta:
        verbose_name='Seguimiento'
        verbose_name_plural = 'Seguimientos'
       
        ordering = ['numero_seguimiento']

    def __str__(self):
        return self.numero_seguimiento

class Avances(models.Model):

    fecha_avance=models.DateField()
    desc_avance=models.CharField(max_length=1000)
    seguimiento = models.ManyToManyField(Seguimiento, verbose_name="Avance", blank=True)

    class Meta:
        verbose_name='Avance'
        verbose_name_plural = 'Avances'
        ordering = ['fecha_avance']

    def __str__(self):
        return str(self.fecha_avance)
