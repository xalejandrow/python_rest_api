from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """ API view de Prueba """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Retornar Lusta de características del APIView """
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logica de nuastra aplicación',
            'Esta mapeado manualmente a los URLs',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self, request):
        """ Crea un mensaje con nuestro Nombre"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Maneja actualizar un objeto """
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """ Maneja actualización parcial de un objecto """
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """ Borra un objeto  """
        return Response({'method':'DELETE'})