from django.contrib import admin
from mrs.models import Person, Movie, Role
# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    
    list_display =('name','ranking')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    
    list_display =('title','ranking', 'year','director', 'actors_list')
    
    def actors_list(self, movie):
        return ', '.join([str(t) for t in movie.actors.all()])

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    
    list_display =('role',)