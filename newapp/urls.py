from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('national', views.national, name="national"),
    path('business', views.business, name="business"),
    path('sports', views.sports, name="sports"),
    path('world', views.world, name="world"),
    path('politics', views.politics, name="politics"),
    path('technology', views.technology, name="technology"),
    path('startup', views.startup, name="startup"),
    path('entertainment', views.entertainment, name="entertainment"),
    path('miscellaneous', views.miscellaneous, name="miscellaneous"),
    path('hatke', views.hatke, name="hatke"),
    path('science', views.science, name="science"),
    path('automobile',views.automobile,name="automobile")
]