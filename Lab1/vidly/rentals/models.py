from django.db import models
from django.contrib import admin
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    star = models.CharField(max_length=255)
    release_year = models.IntegerField()
    price = models.FloatField()
    in_stock = models.IntegerField()    
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    in_4k = models.BooleanField()
    director = models.ForeignKey(Director, on_delete = models.CASCADE)
    image_url = models.TextField()

    def __str__(self):
        return self.title + " : " + str(self.release_year) 


class Game(models.Model):
    title = models.CharField(max_length=255)
    system = models.CharField(max_length=255)
    price = models.FloatField()
    in_stock = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE)
    image_url = models.TextField()
    
    def __str__(self):
        return self.title + " : " + str(self.publisher)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display = ('id', 'release_year', 'title', 'genre')

class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display = ('id', 'system', 'title', 'genre')
    