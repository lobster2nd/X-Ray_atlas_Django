from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('exam/<slug:exam_slug>/', show_exam, name='exam'),
    path('category/<slug:cat_slug>/', show_category, name='category')
]