from django.db import models
from .rating import Rating

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    designer = models.CharField(max_length=50)
    year_released = models.DateField()
    num_of_players = models.IntegerField()
    play_time = models.FloatField()
    recommended_age = models.IntegerField()
    categories = models.ManyToManyField("Category", through="GameCategory", related_name="Category")

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = Rating.objects.filter(game=self)

        # Sum all of the ratings for the game
        total_rating = 0
        for rating in ratings:
            total_rating += rating.rating
        
        if len(ratings):
            return total_rating / len(ratings)

        

        # Calculate the averge and return it.
        # If you don't know how to calculate averge, Google it.
