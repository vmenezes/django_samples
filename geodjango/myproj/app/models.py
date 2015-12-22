from django.contrib.gis.db import models


class Park(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    country = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    address = models.TextField()
    location = models.PointField()

    def __str__(self):
        return "{}, {}, {} - {} - {}, Coords: {}".format(
            self.name,
            self.address,
            self.city,
            self.state,
            self.country,
            self.location.coords
        )
