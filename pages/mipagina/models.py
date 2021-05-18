from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse


# Create your models here.

#modelo del usario personalizado del proyecto final
class UsuarioPers(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)
    telefono = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    genero = models.CharField(null=True,blank=True, max_length=1)
    

#modelo de la tabla de libros de manga
class Manga(models.Model):
    text = models.TextField(default="")
    descrpicion = models.TextField(default="")
    img = models.TextField(default="")
   
    def __str__(self):
        return self.text
#modelos descripcion de los libros
class DescripLib(models.Model):
    text = models.TextField(default="")
    descrpicion = models.TextField(default="")
    img = models.TextField(default="")
    presio = models.TextField(default="")
   
    def __str__(self):
        return self.text
#modelos de los autores de libros 
class Autores(models.Model):
    Nombre = models.TextField(default="")
    Descripcion = models.TextField(default="")
    img = models.TextField(default="")
    Nacionalidad = models.TextField(default="")
    F_Muerte = models.TextField(default="")
    autor = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )
#campo que se mostrara en el admin
    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('', args=[str(self.id)])





#modelo de los libros agrgando una llave foranea para los autores
class Post(models.Model):
    text = models.TextField(default="")
    descrpicion = models.TextField(default="")
    img = models.TextField(default="")
    autores = models.ForeignKey(
        Autores,
        default="",
        on_delete= models.CASCADE,
    )
    #campo que se mostrara en el admin
    def __str__(self):
        return self.text
   
#modelo de los comentarios  agregando dos llaves foraneas para los autores y los usarios
class Comentario(models.Model):
    comentario = models.CharField(max_length=300)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        related_name='comentario'
        )
    autores = models.ForeignKey(
        Autores,
        default="",
        on_delete= models.CASCADE,
    )
        
    def __str__(self):
        return self.comentario
    
    
class CV(models.Model):
    Foto = models.TextField(default="")
    Nombre = models.TextField(default="")
    Experiencia = models.TextField(default="")
    Preparatoria = models.TextField(default="")
    Univerisdad = models.TextField(default="")
    Otros_Estudios = models.TextField(default="")
    autor = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        )
    def __str__(self):
        return self.Nombre

