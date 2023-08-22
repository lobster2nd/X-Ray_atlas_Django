from rest_framework import serializers
from examinations.models import Examinations


class ExaminationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Examinations
        fields = '__all__'
