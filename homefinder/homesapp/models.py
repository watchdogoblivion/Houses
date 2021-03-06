from django.db import models

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length = 200)
    location_type = models.CharField(max_length = 200)

    def pr():
        logger.warning("Your log message is here")


    def __str__(self):
        return self.location_name

class Property(models.Model):
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    property_name = models.CharField(max_length = 200)
    area = models.CharField(max_length = 200)
    age = models.CharField(max_length = 200)
    price = models.CharField(max_length = 200)
    floors = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    beds = models.CharField(max_length = 200)
    baths = models.CharField(max_length = 200)
    typ = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    image_url = models.CharField(max_length = 400)
    maps_url = models.CharField(max_length = 400)
    seller_name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)

    def __str__(self):
        return self.property_name