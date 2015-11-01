from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Game(models.Model):
    "A game"
    name = models.CharField(max_length=200)

    description = models.TextField()
    start_time = models.DateTimeField()
    postcode = models.CharField(max_length=10)

    game_master = models.ForeignKey(User, related_name="games_running")
    players = models.ManyToManyField(User, related_name="games_playing_in")

    def __unicode__(self):
        return "{name} (GM: {gm1} {gm2})".format(
            name=self.name,
            gm1=self.game_master.first_name,
            gm2=self.game_master.last_name
        )
