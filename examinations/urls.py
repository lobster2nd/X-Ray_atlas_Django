from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('exam/<int:exam_id>/', show_exam, name='exam'),
    path('category/<int:cat_id>/', show_category, name='category')
]