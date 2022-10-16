from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Ingredient(models.Model):
    nom = models.CharField(max_length=50)

class BlogPost(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField(Ingredient)
    titre = models.CharField(max_length=100)
    slug = models.SlugField()
    publication = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    contenu = models.TextField()

    def publish(self):
        self.publication = timezone.now()
        self.save()
