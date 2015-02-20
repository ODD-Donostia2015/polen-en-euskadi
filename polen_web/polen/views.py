# -*- coding: utf-8 -*-

from django.shortcuts import render

from polen.models import *


####################################################################################################
###     allergen_index()
####################################################################################################

def allergen_index(request):

    return_dict = {
        'allergens': Allergen.objects.all(),
    }

    return render(request, 'polen/allergens.html', return_dict)


####################################################################################################
###     allergen_stats(allergen_slug)
####################################################################################################

def allergen_stats(request, allergen_slug):

    allergen = Allergen.objects.get(slug=allergen_slug)

    measurements = Measurement.objects.filter(
        allergen=allergen,
    )

    colors = []

    allergen_in_group = AllergenInGroup.objects.filter(allergen=allergen)[0]

    if allergen_in_group:
        medium_value = allergen_in_group.group.low_level_upper_limit
        high_value = allergen_in_group.group.medium_level_upper_limit

    else:
        medium_value = 0
        high_value = 0

    for m in measurements:
        if m.value > high_value:
            m.color = 'red'
        elif m.value > medium_value:
            m.color = 'orange'
        else:
            m.color = 'green'

    return_dict = {
        'measurements': measurements,
        'medium_value': medium_value,
        'high_value': high_value,
        'colors': colors,
    }

    return render(request, 'polen/allergen_stats.html', return_dict)
