# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.contrib.auth.models import User
from polen.models import *


####################################################################################################
###     home()
####################################################################################################

def home(request):

    _create_superuser()

    return_dict = {
        'sensor_stations': Sensor.objects.all(),
    }

    return render(request, 'polen_web/index.html', return_dict)


###     _create_superuser()
####################################################################################################

def _create_superuser():

    if User.objects.all().count() == 0:
        User.objects.create_superuser(
                username=u"admin",
                password=u"admin",
                email=u"superuser@admin.org",
            )


####################################################################################################
###     load_initial_data()
####################################################################################################

def load_initial_data(request):

    Sensor.objects.all().delete()
    Allergen.objects.all().delete()
    Group.objects.all().delete()
    Measurement.objects.all().delete()

    ###     sensors
    ###########################################################################

    gasteiz_sensor = Sensor(
        name=u'Vitoria-Gasteiz',
        address=u'C/Olagibel, 38',
        latitude=42.8461506,
        longitude=-2.6660749,
        height=535,
        height_from_street_level=18,
    )
    gasteiz_sensor.save()

    donostia_sensor = Sensor(
        name=u'Donostia - San Sebastián',
        address=u'Avda. Navarra, 14',
        latitude=43.325278,
        longitude=-1.970556,
        height=11,
        height_from_street_level=18,
    )
    donostia_sensor.save()

    bilbo_sensor = Sensor(
        name=u'Bilbao',
        address=u'C/ Mª Díaz de Haro, 58',
        latitude=43.260000,
        longitude=-2.944444,
        height=15,
        height_from_street_level=15,
    )
    bilbo_sensor.save()

    ###     groups
    ###########################################################################

    group_1 = Group(
        name=u'Grupo I',
        low_level_upper_limit=15,
        medium_level_upper_limit=30,
    )
    group_1.save()

    group_2 = Group(
        name=u'Grupo II',
        low_level_upper_limit=25,
        medium_level_upper_limit=50,
    )
    group_2.save()

    group_3 = Group(
        name=u'Grupo III',
        low_level_upper_limit=30,
        medium_level_upper_limit=50,
    )
    group_3.save()

    group_4 = Group(
        name=u'Grupo IV',
        low_level_upper_limit=50,
        medium_level_upper_limit=200,
    )
    group_4.save()

    ###     allergens
    ###########################################################################

    acer = Allergen(
        pollen_type=u'Acer',
        plant_tree=u'',
        group=None,
    )
    acer.save()

    aesculus = Allergen(
        pollen_type=u'Aesculus',
        plant_tree=u'',
        group=None,
    )
    aesculus.save()

    alnus = Allergen(
        pollen_type=u'Alnus',
        plant_tree=u'',
        group=None,
    )
    alnus.save()

    artemisia = Allergen(
        pollen_type=u'Artemisia',
        plant_tree=u'',
        group=None,
    )
    artemisia.save()

    betula = Allergen(
        pollen_type=u'Betula',
        plant_tree=u'',
        group=None,
    )
    betula.save()

    buxus = Allergen(
        pollen_type=u'Buxus',
        plant_tree=u'',
        group=None,
    )
    buxus.save()

    carex = Allergen(
        pollen_type=u'Carex',
        plant_tree=u'',
        group=None,
    )
    carex.save()

    castanea = Allergen(
        pollen_type=u'Castanea',
        plant_tree=u'',
        group=None,
    )
    castanea.save()

    casuarina = Allergen(
        pollen_type=u'Casuarina',
        plant_tree=u'',
        group=None,
    )
    casuarina.save()

    cedrus = Allergen(
        pollen_type=u'Cedrus',
        plant_tree=u'',
        group=None,
    )
    cedrus.save()

    cistaceae = Allergen(
        pollen_type=u'Cistaceae',
        plant_tree=u'',
        group=None,
    )
    cistaceae.save()

    compositae_others = Allergen(
        pollen_type=u'Compositae (otras)',
        plant_tree=u'',
        group=None,
    )
    compositae_others.save()

    corylus = Allergen(
        pollen_type=u'Corylus',
        plant_tree=u'',
        group=None,
    )
    corylus.save()

    cupress_taxaceae = Allergen(
        pollen_type=u'Cupress/Taxaceae',
        plant_tree=u'',
        group=None,
    )
    cupress_taxaceae.save()

    cyperus = Allergen(
        pollen_type=u'Cyperus',
        plant_tree=u'',
        group=None,
    )
    cyperus.save()

    chenopo_amarant = Allergen(
        pollen_type=u'Chenopo/Amarant',
        plant_tree=u'',
        group=None,
    )
    chenopo_amarant.save()

    equium = Allergen(
        pollen_type=u'Equium',
        plant_tree=u'',
        group=None,
    )
    equium.save()

    ericaceae = Allergen(
        pollen_type=u'Ericaceae',
        plant_tree=u'',
        group=None,
    )
    ericaceae.save()

    eucalyptus = Allergen(
        pollen_type=u'Eucalyptus',
        plant_tree=u'',
        group=None,
    )
    eucalyptus.save()

    fraxinus = Allergen(
        pollen_type=u'Fraxinus',
        plant_tree=u'',
        group=None,
    )
    fraxinus.save()

    gleditsia = Allergen(
        pollen_type=u'Gleditsia',
        plant_tree=u'',
        group=None,
    )
    gleditsia.save()

    juglans = Allergen(
        pollen_type=u'Juglans',
        plant_tree=u'',
        group=None,
    )
    juglans.save()

    juncaceae = Allergen(
        pollen_type=u'Juncaceae',
        plant_tree=u'',
        group=None,
    )
    juncaceae.save()

    labiateae = Allergen(
        pollen_type=u'Labiateae',
        plant_tree=u'',
        group=None,
    )
    labiateae.save()

    ligustrum = Allergen(
        pollen_type=u'Ligustrum',
        plant_tree=u'',
        group=None,
    )
    ligustrum.save()

    mercurialis = Allergen(
        pollen_type=u'Mercurialis',
        plant_tree=u'',
        group=None,
    )
    mercurialis.save()

    mimosa = Allergen(
        pollen_type=u'Mimosa',
        plant_tree=u'',
        group=None,
    )
    mimosa.save()

    morus = Allergen(
        pollen_type=u'Morus',
        plant_tree=u'',
        group=None,
    )
    morus.save()

    unidentified = Allergen(
        pollen_type=u'No identificados',
        plant_tree=u'',
        group=None,
    )
    unidentified.save()

    olea = Allergen(
        pollen_type=u'Olea',
        plant_tree=u'',
        group=None,
    )
    olea.save()

    palmaceae = Allergen(
        pollen_type=u'Palmaceae',
        plant_tree=u'',
        group=None,
    )
    palmaceae.save()

    pinus = Allergen(
        pollen_type=u'Pinus',
        plant_tree=u'',
        group=None,
    )
    pinus.save()

    plantago = Allergen(
        pollen_type=u'Plantago',
        plant_tree=u'',
        group=None,
    )
    plantago.save()

    platanus = Allergen(
        pollen_type=u'Platanus',
        plant_tree=u'',
        group=None,
    )
    platanus.save()

    poaceae = Allergen(
        pollen_type=u'Poaceae',
        plant_tree=u'',
        group=None,
    )
    poaceae.save()

    populus = Allergen(
        pollen_type=u'Populus',
        plant_tree=u'',
        group=None,
    )
    populus.save()

    quercus = Allergen(
        pollen_type=u'Quercus',
        plant_tree=u'',
        group=None,
    )
    quercus.save()

    rosacea = Allergen(
        pollen_type=u'Rosacea',
        plant_tree=u'',
        group=None,
    )
    rosacea.save()

    rumex = Allergen(
        pollen_type=u'Rumex',
        plant_tree=u'',
        group=None,
    )
    rumex.save()

    salix = Allergen(
        pollen_type=u'Salix',
        plant_tree=u'',
        group=None,
    )
    salix.save()

    sophora = Allergen(
        pollen_type=u'Sophora',
        plant_tree=u'',
        group=None,
    )
    sophora.save()

    taraxacum = Allergen(
        pollen_type=u'Taraxacum',
        plant_tree=u'',
        group=None,
    )
    taraxacum.save()

    tilia = Allergen(
        pollen_type=u'Tilia',
        plant_tree=u'',
        group=None,
    )
    tilia.save()

    typha = Allergen(
        pollen_type=u'Typha',
        plant_tree=u'',
        group=None,
    )
    typha.save()

    ulmus = Allergen(
        pollen_type=u'Ulmus',
        plant_tree=u'',
        group=None,
    )
    ulmus.save()

    umbelliferae = Allergen(
        pollen_type=u'Umbelliferae',
        plant_tree=u'',
        group=None,
    )
    umbelliferae.save()

    urticaceae = Allergen(
        pollen_type=u'Urticaceae',
        plant_tree=u'',
        group=None,
    )
    urticaceae.save()
