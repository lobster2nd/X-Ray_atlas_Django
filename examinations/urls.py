from django.urls import path, include

from .views import *

urlpatterns = [
    path('', ExaminationsHome.as_view(), name='home'),
    path('atlas/', atlas, name='atlas'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('exam/<slug:exam_slug>/', ShowExam.as_view(), name='exam'),
    path('category/<slug:cat_slug>/', ExaminationsCategory.as_view(), name='category'),
    path('social/', include('social_django.urls', namespace='social_auth')),
]
