from django.shortcuts import render
from .serializers import EstudianteSerializer
from .models import Estudiante
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

# CLASS BASED VIEWS
class EstudianteListClass(APIView):
    def get(self, request):
        estudi = Estudiante.objects.all()
        serial = EstudianteSerializer(estudi, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = EstudianteSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class EstudianteDetalleClass(APIView):
    def get_object(self, id):
        try:
            return Estudiante.objects.get(pk=id)
        except Estudiante.DoesNotExist:
            raise Http404

    def get(self, request, id):
        estudi = self.get_object(id)
        serial = EstudianteSerializer(estudi)
        return Response(serial.data)

    def put(self, request, id):
        estudi = self.get_object(id)
        serial = EstudianteSerializer(estudi, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        estudi = self.get_object(id)
        estudi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# FUNCTION BASED VIEWS
@api_view(['GET', 'POST'])
def estudiante_list(request):
    if request.method == 'GET':
        estude = Estudiante.objects.all()
        serial = EstudianteSerializer(estude, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = EstudianteSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def estudiante_detalle(request, id):
    try:
        estude = Estudiante.objects.get(pk=id)
    except Estudiante.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = EstudianteSerializer(estude)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = EstudianteSerializer(estude, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        estude.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Renderizando el template index.html en las vistas
def estudiante_list_render(request):
    return render(request, 'index.html')


def estudiante_detalle_render(request, id):
    return render(request, 'index.html')
