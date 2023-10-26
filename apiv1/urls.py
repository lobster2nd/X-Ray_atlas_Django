from django.urls import path, include

from .views import ExaminationsAPIList, ExaminationsAPIUpdate, \
    ExaminationsAPIDestroy

urlpatterns = [
    path('examinations/', ExaminationsAPIList.as_view()),
    path('examinations/<int:pk>/', ExaminationsAPIUpdate.as_view()),
    path('examinationdelete/<int:pk>/', ExaminationsAPIDestroy.as_view()),
    # path('api/v1/drf-auth/', include('rest_framework.urls')),   # session-based authentication
    # path('api/v1/auth/', include('djoser.urls')),                   # token-based authentication
    # re_path(r'^auth/', include('djoser.urls.authtoken')),           # token-based authentication
    ]