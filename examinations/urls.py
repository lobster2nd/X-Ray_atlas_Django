from django.urls import path

from .views import *

urlpatterns = [
    path('', ExaminationsHome.as_view(), name='home'),
    path('atlas/', atlas, name='atlas'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('exam/<slug:exam_slug>/', ShowExam.as_view(), name='exam'),
    path('category/<slug:cat_slug>/', ExaminationsCategory.as_view(), name='category')
]