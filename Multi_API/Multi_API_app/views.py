import os
from Multi_API_app import serializers, models
from Multi_API_app.serializers import SchoolingSerializer, GrduationSerializer
from Multi_API_app.models import Schooling, Graduation
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.views import APIView


class Postdetails(CreateAPIView):
    serializer_class = serializers.SchoolingSerializer

    def post(self, request):
        try:
            serializer_class = serializers.SchoolingSerializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data)
        except Exception as e:
            return Response(e)


class Postdetails1(CreateAPIView):
    serializer_class = serializers.GrduationSerializer

    def post(self, request):
        try:
            serializer_class = serializers.GrduationSerializer(data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data)
        except Exception as e:
            return Response(e)


class Get_all_details_in_one_API(GenericAPIView):
    serializer_class = serializers.Get_details
    queryset = models.Schooling, models.Graduation

    def post(self, request):
        try:
            query_set_schooling = models.Schooling.objects.filter(name=request.data['name'])
            query_set_graduation = models.Graduation.objects.filter(name=request.data['name'])

            serializer_class_schooling = serializers.SchoolingSerializer(query_set_schooling, many=True)
            serializer_class_graduation = serializers.GrduationSerializer(query_set_graduation, many=True)

            return Response({
                'schooling': serializer_class_schooling.data,
                'graduation': serializer_class_graduation.data
            })
        except Exception as e:
            return Response({'error': str(e)}, status=500)


def get_details_by_name(models_class, serializer_class, name):
    query = models_class.objects.filter(name=name)
    serializer = serializer_class(query, many=True)
    return serializer.data


class GetSchooling(GenericAPIView):
    serializer_class = serializers.Get_details
    queryset = models.Schooling

    def post(self, request):
        response_data = get_details_by_name(models.Schooling, serializers.SchoolingSerializer, request.data['name'])
        return Response({'schooling': response_data})


class GetGraduation(GenericAPIView):
    serializer_class = serializers.Get_details
    queryset = models.Graduation

    def post(self, request):
        response_data = get_details_by_name(models.Graduation, serializers.GrduationSerializer, request.data['name'])
        return Response({'graduation': response_data})
