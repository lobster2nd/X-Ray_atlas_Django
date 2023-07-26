from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('head/', head, name='head'),
    path('spine/', spine, name='spine'),
    path('upper_limp', upper_limp, name='upper_limp'),
    path('lower_limp', lower_limp, name='lower_limp'),
    #path('head/<int:id>/', skullPA),
]