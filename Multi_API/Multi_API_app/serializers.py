from rest_framework import serializers
from .models import Schooling, Graduation


class SchoolingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schooling
        fields = '__all__'


class GrduationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graduation
        fields = '__all__'

class Get_details(serializers.Serializer):
    name = serializers.CharField()