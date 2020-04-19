from django.contrib import admin
from .models import Seguimiento, Tipo_seguimiento, Avances
# Register your models here.

admin.site.register(Seguimiento)
admin.site.register(Tipo_seguimiento)
admin.site.register(Avances)