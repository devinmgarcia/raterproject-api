from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    designer = models.CharField(max_length=50)
    year_released = models.DateField()
    num_of_players = models.IntegerField()
    play_time = models.FloatField()
    recommended_age = models.IntegerField()
