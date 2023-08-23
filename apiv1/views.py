from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import ExaminationSerializer
from examinations.models import Examinations


class ExaminationsAPIListPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ExaminationsAPIList(generics.ListCreateAPIView):
    queryset = Examinations.objects.all()
    serializer_class = ExaminationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = ExaminationsAPIListPagination


class ExaminationsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Examinations.objects.all()
    serializer_class = ExaminationSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    authentication_classes = (TokenAuthentication, )


class ExaminationsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Examinations.objects.all()
    serializer_class = ExaminationSerializer
    permission_classes = (IsAdminOrReadOnly, )
