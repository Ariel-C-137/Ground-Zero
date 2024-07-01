from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Artista, Pintura, Escultura, Orfebreria, Tejido, Genero

admin.site.register(Genero)
# Registra los otros modelos también si aún no lo has hecho
admin.site.register(Artista)
admin.site.register(Pintura)
admin.site.register(Escultura)
admin.site.register(Orfebreria)
admin.site.register(Tejido)