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

    return_dict = {
        'measurements': measurements,
        'medium_value': 25,
        'high_value': 50,
    }

    return render(request, 'polen/allergen_stats.html', return_dict)
