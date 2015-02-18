from django.db import models


####################################################################################################
###     Group
####################################################################################################

class Group(models.Model):

    name = models.CharField(
        max_length=50,
    )

    low_level_bottom_limit = models.PositiveSmallIntegerField(
        default=0,
    )

    medium_level_bottom_limit = models.PositiveSmallIntegerField(
        default=0,
    )

    high_level_bottom_limit = models.PositiveSmallIntegerField(
        default=0,
    )


####################################################################################################
###     Allergen
####################################################################################################

class Allergen(models.Model):

    pollen_type = models.CharField(
        max_length=50,
    )

    plant_tree = models.CharField(
        max_length=250,
    )

    group = models.ForeignKey('Group')


####################################################################################################
###     Measurement
####################################################################################################

class Measurement(models.Model):

    date = models.DateField()

    allergen = models.ForeignKey('Allergen')

    value = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
    )


####################################################################################################
###     AllergenInGroup
####################################################################################################

class AllergenInGroup(models.Model):

    allergen = models.ForeignKey('Allergen')

    group = models.ForeignKey('Group')

    class Meta:
        unique_together = ('allergen', 'group')
        verbose_name_plural = 'Allergens in group'


####################################################################################################
###     Sensor
####################################################################################################

class Sensor(models.Model):

    name = models.CharField(
        max_length=50,
    )

    address = models.CharField(
        max_length=150,
    )

    latitude = models.FloatField(
        default=0,
        blank=True,
        null=True,
    )

    longitude = models.FloatField(
        default=0,
        blank=True,
        null=True,
    )

    height = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
    )

    height_from_street_level = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
    )
