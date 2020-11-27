from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

"""
APUNTES

Para cada uno de los modelos que se ha definido en el fichero models.py Django creará una tabla en la base
de datos. A través de estos modelos, Django ofrece una API que permite realizar acciones sobre objetos de la 
base de datos de manera sencilla.
"""

##########################
###### MODELO POST #######
##########################

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField( max_length = 250 )
    slug = models.SlugField( max_length = 250, unique_for_date='publish' )
    author = models.ForeignKey( User, on_delete=models.CASCADE, related_name='blog_posts' )
    body = models.TextField()
    publish = models.DateTimeField( default = timezone.now )
    created = models.DateTimeField( auto_now_add=True )
    status = models.CharField( max_length = 10, choices = STATUS_CHOICES, default='draft')
    objects = models.Manager() #El gestor por defecto
    published = PublishedManager() #El nuevo gestor

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title