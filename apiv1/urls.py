from django.urls import path, include, re_path

from .views import ExaminationsAPIList, ExaminationsAPIUpdate, \
    ExaminationsAPIDestroy

urlpatterns = [
    path('examinations/', ExaminationsAPIList.as_view()),
    path('examinations/<int:pk>/', ExaminationsAPIUpdate.as_view()),
    path('examinationdelete/<int:pk>/', ExaminationsAPIDestroy.as_view()),
    path('drf-auth/', include('rest_framework.urls')),   # session-based authentication
    path('auth/', include('djoser.urls')),                   # token-based authentication
    #re_path(r'^auth/', include('djoser.urls.authtoken')),           # token-based authentication
    ]
