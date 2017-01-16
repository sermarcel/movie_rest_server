from django.db import models


RANKING= (
    (0,''),
    (1,'*'),
    (2,'**'),
    (3,'***'),
    (4,'****'),
    (5,'*****')
)



class Person(models.Model):
    
    name = models.CharField(max_length=32)
    ranking=models.IntegerField(choices=RANKING, null=True)
    birth_date=models.DateField()

    def __str__(self):
        return self.name

class Movie(models.Model):

    title = models.CharField(max_length=64)
    descritpion=models.TextField()
    director=models.ForeignKey(Person, related_name='movie_director')
    year=models.IntegerField()
    actors=models.ManyToManyField(Person, through='Role',blank=True, related_name='movie_actors')
    ranking=models.IntegerField(choices=RANKING, null=True)
    
    def __str__(self):
        return self.title

class Role(models.Model):

    role=models.CharField(max_length=64, primary_key=True)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE, related_name="Movie_movie")
    person=models.ForeignKey(Person,on_delete=models.CASCADE, related_name="Movie_person")

    