from django.urls import path
from . import views

urlpatterns =[
    path('',views.inicio,name='inicio'),
    path('historia/',views.historia,name='historia'),
    path('enemigos/',views.enemigos,name='enemigos'),
    path('curiosidades/',views.curiosidades,name='curiosidades'),
    path('aliados/',views.aliados,name='aliados'),

]