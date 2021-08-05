from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    image = models.ImageField()
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)