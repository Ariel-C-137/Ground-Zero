from django.db import models

# Create your models here.

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    biografia = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)
  
class Pintura(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey('Artista', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='pinturas/')
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Escultura(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey('Artista', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='esculturas/')
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Orfebreria(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey('Artista', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='orfebreria/')
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Tejido(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey('Artista', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tejidos/')
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo