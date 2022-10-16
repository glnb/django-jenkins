from django.contrib import admin

# Register your models here.
from .models import BlogPost
from .models import Ingredient

admin.site.register(BlogPost)
admin.site.register(Ingredient)