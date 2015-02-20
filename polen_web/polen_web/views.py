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
        plant_tree=u'Arce'
    )
    acer.save()

    acerGroup=AllergenInGroup(
        allergen=acer,
        group=group_3
    )
    acerGroup.save()

    aesculus = Allergen(
        pollen_type=u'Aesculus',
        plant_tree=u'Castaños de Indias'

    )
    aesculus.save()
    
    aesculusGroup=AllergenInGroup(
        allergen=aesculus,
        group=None
    )
    aesculusGroup.save()


    alnus = Allergen(
        pollen_type=u'Alnus',
        plant_tree=u'Aliso'

    )
    alnus.save()
    alnusGroup=AllergenInGroup(
        allergen=alnus,
        group=group_3
    )
    alnusGroup.save()

    artemisia = Allergen(
        pollen_type=u'Artemisia',
        plant_tree=u'Artemisia'

    )
    artemisia.save()
    artemisiaGroup=AllergenInGroup(
        allergen=artemisia,
        group=group_2
    )
    artemisiaGroup.save()

    betula = Allergen(
        pollen_type=u'Betula',
        plant_tree=u'Abedul'

    )
    betula.save()

    betulaGroup=AllergenInGroup(
        allergen=betula,
        group=group_3
    )
    betulaGroup.save()

    buxus = Allergen(
        pollen_type=u'Buxus',
        plant_tree=u'Boj'

    )
    buxus.save()
    
    buxusGroup=AllergenInGroup(
        allergen=buxus,
        group=None
    )
    buxusGroup.save()

    carex = Allergen(
        pollen_type=u'Carex',
        plant_tree=u'Cuchillera'

    )
    carex.save()
    carexGroup=AllergenInGroup(
        allergen=carex,
        group=None
    )
    carexGroup.save()

    castanea = Allergen(
        pollen_type=u'Castanea',
        plant_tree=u'Castaño'

    )
    castanea.save()
    castaneaGroup=AllergenInGroup(
        allergen=castanea,
        group=group_3
    )
    castaneaGroup.save()
    casuarina = Allergen(
        pollen_type=u'Casuarina',
        plant_tree=u''

    )
    casuarina.save()
    casuarinaGroup=AllergenInGroup(
        allergen=casuarina,
        group=group_3
    )
    casuarinaGroup.save()

    cedrus = Allergen(
        pollen_type=u'Cedrus',
        plant_tree=u'Cedro'

    )
    cedrus.save()
    cedrusGroup=AllergenInGroup(
        allergen=cedrus,
        group=None
    )
    cedrusGroup.save()

    cistaceae = Allergen(
        pollen_type=u'Cistaceae',
        plant_tree=u''

    )
    cistaceae.save()
    cistaceaeGroup=AllergenInGroup(
        allergen=cistaceae,
        group=None
    )
    cistaceaeGroup.save()

    compositae_others = Allergen(
        pollen_type=u'Compositae (otras)',
        plant_tree=u''

    )
    compositae_others.save()
    compositae_othersGroup=AllergenInGroup(
        allergen=compositae_others,
        group=None
    )
    compositae_othersGroup.save()

    corylus = Allergen(
        pollen_type=u'Corylus',
        plant_tree=u'Avellano'

    )
    corylus.save()
    corylusGroup=AllergenInGroup(
        allergen=corylus,
        group=group_3
    )
    corylusGroup.save()

    cupress_taxaceae = Allergen(
        pollen_type=u'Cupress/Taxaceae',
        plant_tree=u''

    )
    cupress_taxaceae.save()
    cupress_taxaceaeGroup=AllergenInGroup(
        allergen=cupress_taxaceae,
        group=group_4
    )
    cupress_taxaceaeGroup.save()

    cyperus = Allergen(
        pollen_type=u'Cyperus',
        plant_tree=u''

    )
    cyperus.save()
    cyperusGroup=AllergenInGroup(
        allergen=cyperus,
        group=None
    )
    cyperusGroup.save()

    chenopo_amarant = Allergen(
        pollen_type=u'Chenopo/Amarant',
        plant_tree=u'Cenizo, armuelle, bledo'

    )
    chenopo_amarant.save()
    chenopo_amarantGroup=AllergenInGroup(
        allergen=chenopo_amarant,
        group=group_2
    )
    chenopo_amarantGroup.save()
    equium = Allergen(
        pollen_type=u'Equium',
        plant_tree=u''
    )
    equium.save()
    equiumGroup=AllergenInGroup(
        allergen=equium,
        group=group_1
    )
    equiumGroup.save()
    ericaceae = Allergen(
        pollen_type=u'Ericaceae',
        plant_tree=u''

    )
    ericaceae.save()
    ericaceaeGroup=AllergenInGroup(
        allergen=ericaceae,
        group=group_2
    )
    ericaceaeGroup.save()
    eucalyptus = Allergen(
        pollen_type=u'Eucalyptus',
        plant_tree=u'Eucalipto'

    )
    eucalyptus.save()
    eucalyptusGroup=AllergenInGroup(
        allergen=eucalyptus,
        group=group_3
    )
    eucalyptusGroup.save()

    fraxinus = Allergen(
        pollen_type=u'Fraxinus',
        plant_tree=u'Fresno'

    )
    fraxinus.save()
    fraxinusGroup=AllergenInGroup(
        allergen=fraxinus,
        group=None
    )
    fraxinusGroup.save()

    gleditsia = Allergen(
        pollen_type=u'Gleditsia',
        plant_tree=u''

    )
    gleditsia.save()
    gleditsiaGroup=AllergenInGroup(
        allergen=gleditsia,
        group=None
    )
    gleditsiaGroup.save()

    juglans = Allergen(
        pollen_type=u'Juglans',
        plant_tree=u'Nogal'

    )
    juglans.save()
    juglansGroup=AllergenInGroup(
        allergen=juglans,
        group=None
    )
    juglansGroup.save()

    juncaceae = Allergen(
        pollen_type=u'Juncaceae',
        plant_tree=u'Juncácea'

    )
    juncaceae.save()
    juncaceaeGroup=AllergenInGroup(
        allergen=juncaceae,
        group=None
    )
    juncaceaGroup.save()

    labiateae = Allergen(
        pollen_type=u'Labiateae',
        plant_tree=u'Lamiácea'

    )
    labiateae.save()
    labiateaeGroup=AllergenInGroup(
        allergen=labiateae,
        group=None
    )
    labiateaeGroup.save()

    ligustrum = Allergen(
        pollen_type=u'Ligustrum',
        plant_tree=u'Aligustre'

    )
    ligustrum.save()
    ligustrumGroup=AllergenInGroup(
        allergen=ligustrum,
        group=group_3
    )
    ligustrumGroup.save()

    mercurialis = Allergen(
        pollen_type=u'Mercurialis',
        plant_tree=u''

    )
    mercurialis.save()
    mercurialisGroup=AllergenInGroup(
        allergen=mercurialis,
        group=group_1
    )
    mercurialisGroup.save()

    mimosa = Allergen(
        pollen_type=u'Mimosa',
        plant_tree=u'Mimosa'

    )
    mimosa.save()
    mimosaGroup=AllergenInGroup(
        allergen=mimosa,
        group=None
    )
    mimosaGroup.save()

    morus = Allergen(
        pollen_type=u'Morus',
        plant_tree=u'Morera'

    )
    morus.save()
    morusGroup=AllergenInGroup(
        allergen=morus,
        group=None
    )
    morusGroup.save()

    unidentified = Allergen(
        pollen_type=u'No identificados',
        plant_tree=u''

    )
    unidentified.save()
    unidentifiedGroup=AllergenInGroup(
        allergen=unidentified,
        group=None
    )
    unidentifiedGroup.save()

    olea = Allergen(
        pollen_type=u'Olea',
        plant_tree=u'Olivo'
    )
    olea.save()
    oleaGroup=AllergenInGroup(
        allergen=olea,
        group=group_4
    )
    oleaGroup.save()

    palmaceae = Allergen(
        pollen_type=u'Palmaceae',
        plant_tree=u''

    )
    palmaceae.save()
    palmaceaeGroup=AllergenInGroup(
        allergen=palmaceae,
        group=None
    )
    palmaceaeGroup.save()

    pinus = Allergen(
        pollen_type=u'Pinus',
        plant_tree=u'Pino, abeto'
    )
    pinus.save()
    pinusGroup=AllergenInGroup(
        allergen=pinus,
        group=group_4
    )
    pinusGroup.save()

    plantago = Allergen(
        pollen_type=u'Plantago',
        plant_tree=u'Llantén'
    )
    plantago.save()
    plantagoGroup=AllergenInGroup(
        allergen=plantago,
        group=group_2
    )
    plantagoGroup.save()

    platanus = Allergen(
        pollen_type=u'Platanus',
        plant_tree=u'Plátano'
        #group=group_4,
    )
    platanus.save()
    platanusGroup=AllergenInGroup(
        allergen=platanus,
        group=group_4
    )
    platanusGroup.save()

    poaceae = Allergen(
        pollen_type=u'Poaceae',
        plant_tree=u'Plantas herbáceas'

    )
    poaceae.save()
    poaceaeGroup=AllergenInGroup(
        allergen=poaceae,
        group=group_2
    )
    poaceaeGroup.save()

    populus = Allergen(
        pollen_type=u'Populus',
        plant_tree=u'Álamo'

    )
    populus.save()
    populusGroup=AllergenInGroup(
        allergen=populus,
        group=group_4
    )
    populusGroup.save()

    quercus = Allergen(
        pollen_type=u'Quercus',
        plant_tree=u'Roble, encina'

    )
    quercus.save()
    quercusGroup=AllergenInGroup(
        allergen=quercus,
        group=group_4
    )
    quercusGroup.save()

    rosacea = Allergen(
        pollen_type=u'Rosacea',
        plant_tree=u'Rosáceas'

    )
    rosacea.save()
    rosaceaGroup=AllergenInGroup(
        allergen=rosacea,
        group=None
    )
    rosaceaGroup.save()

    rumex = Allergen(
        pollen_type=u'Rumex',
        plant_tree=u''

    )
    rumex.save()
    rumexGroup=AllergenInGroup(
        allergen=rumex,
        group=group_2
    )
    rumexGroup.save()

    salix = Allergen(
        pollen_type=u'Salix',
        plant_tree=u'Sauce'

    )
    salix.save()
    salixGroup=AllergenInGroup(
        allergen=salix,
        group=None
    )
    salixGroup.save()

    sophora = Allergen(
        pollen_type=u'Sophora',
        plant_tree=u''

    )
    sophora.save()
    sophoraGroup=AllergenInGroup(
        allergen=sophora,
        group=None
    )
    sophoraGroup.save()

    taraxacum = Allergen(
        pollen_type=u'Taraxacum',
        plant_tree=u'Dientes de león'

    )
    taraxacum.save()
    taraxacumGroup=AllergenInGroup(
        allergen=taraxacum,
        group=None
    )
    taraxacumGroup.save()

    tilia = Allergen(
        pollen_type=u'Tilia',
        plant_tree=u'Tilos'

    )
    tilia.save()
    tiliaGroup=AllergenInGroup(
        allergen=tilia,
        group=None
    )
    tiliaGroup.save()

    typha = Allergen(
        pollen_type=u'Typha',
        plant_tree=u'Totoras'

    )
    typha.save()
    typhaGroup=AllergenInGroup(
        allergen=typha,
        group=None
    )
    typhaGroup.save()

    ulmus = Allergen(
        pollen_type=u'Ulmus',
        plant_tree=u'Olmos'

    )
    ulmus.save()
    ulmusGroup=AllergenInGroup(
        allergen=ulmus,
        group=group_3
    )
    ulmusGroup.save()

    umbelliferae = Allergen(
        pollen_type=u'Umbelliferae',
        plant_tree=u''

    )
    umbelliferae.save()
    umbelliferaeGroup=AllergenInGroup(
        allergen=umbelliferae,
        group=None
    )
    umbelliferaeGroup.save()

    urticaceae = Allergen(
        pollen_type=u'Urticaceae',
        plant_tree=u''

    )
    urticaceae.save()
    urticaceaeGroup=AllergenInGroup(
        allergen=urticaceae,
        group=None
    )
    urticaceaeGroup.save()
