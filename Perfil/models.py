from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):


    foto_perfil = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True
    )

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class RecetaCreada(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recetas_creadas'
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=100)  
    ingredientes = models.TextField()
    preparacion = models.TextField()        
    imagen = models.ImageField(
        upload_to='recetas_creadas/',
        blank=True,
        null=True
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.usuario.username}"


class RecetaGuardada(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recetas_guardadas'
    )

    cocktaildb_id = models.CharField(max_length=20)
    nombre = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100, blank=True)
    tipo_bebida = models.CharField(max_length=100, blank=True)  # Alcoholic / Non Alcoholic
    instrucciones = models.TextField(blank=True)
    imagen = models.URLField(blank=True)
    fecha_guardado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} (guardada por {self.usuario.username})"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    banner = models.ImageField(upload_to='banners/', blank=True, null=True)

    def __str__(self):
        return self.full_name or self.user.username
    
