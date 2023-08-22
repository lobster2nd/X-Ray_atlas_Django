from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import ExaminationSerializer
from examinations.models import Examinations


class ExaminationsAPIList(generics.ListCreateAPIView):
    queryset = Examinations.objects.all()
    serializer_class = ExaminationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ExaminationsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Examinations.objects.all()
    serializer_class = ExaminationSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class ExaminationsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Examinations.objects.all()
    serializer_class = ExaminationSerializer
    permission_classes = (IsAdminOrReadOnly, )
