from django.contrib import admin
from .models import Genre, Movie, Game, Director, Publisher, GenreAdmin, MovieAdmin, GameAdmin
# Register your models here.

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Publisher)
admin.site.register(Director)


