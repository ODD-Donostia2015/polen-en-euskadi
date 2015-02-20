from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'polen_web.views.home', name='home'),

    url(r'^allergens/(?P<allergen_slug>\S+)/$', 'polen.views.allergen_stats', name='allergen_stats'),
    url(r'^allergens/$', 'polen.views.allergen_index', name='allergen_index'),
)
