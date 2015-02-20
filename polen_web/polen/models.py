# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify


####################################################################################################
###     Group
####################################################################################################

class Group(models.Model):

    name = models.CharField(
        max_length=50,
    )

    slug = models.SlugField(
        max_length=50,
        blank=True,
        unique=True,
    )

    low_level_upper_limit = models.PositiveSmallIntegerField(
        default=0,
    )

    medium_level_upper_limit = models.PositiveSmallIntegerField(
        default=0,
    )

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Group, self).save(*args, **kwargs)


####################################################################################################
###     Allergen
####################################################################################################

class Allergen(models.Model):

    pollen_type = models.CharField(
        max_length=50,
    )

    slug = models.SlugField(
        max_length=50,
        blank=True,
        unique=True,
    )

    plant_tree = models.CharField(
        max_length=250,
    )

    class Meta:
        ordering = ['pollen_type']

    def __unicode__(self):
        return self.pollen_type

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pollen_type)

        super(Allergen, self).save(*args, **kwargs)


####################################################################################################
###     AllergenInGroup
####################################################################################################

class AllergenInGroup(models.Model):

    allergen = models.ForeignKey('Allergen')

    group = models.ForeignKey('Group', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Allergens in group'


####################################################################################################
###     Measurement
####################################################################################################

class Measurement(models.Model):

    date = models.DateField()

    allergen = models.ForeignKey('Allergen')

    sensor = models.ForeignKey('Sensor')

    value = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
    )

    class Meta:
        ordering = ['date', 'allergen']


####################################################################################################
###     Sensor
####################################################################################################

class Sensor(models.Model):

    name = models.CharField(
        max_length=50,
    )

    slug = models.SlugField(
        max_length=50,
        blank=True,
        unique=True,
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

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Sensor, self).save(*args, **kwargs)
