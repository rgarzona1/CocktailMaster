# api_views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import RecetaCreada, RecetaGuardada
from .serializers import CreatedRecipeSerializer, SavedRecipeSerializer

class MisCreacionesList(generics.ListAPIView):      #permite listar las creaciones del usuario
    serializer_class = CreatedRecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (RecetaCreada.objects
                .filter(usuario=self.request.user)
                .order_by('-fecha_creacion'))


class RecetasGuardadasList(generics.ListAPIView):     #permite listar las recetas guardadas
    serializer_class = SavedRecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (RecetaGuardada.objects
                .filter(usuario=self.request.user)
                .order_by('-fecha_guardado'))
        
        
        
class RecetaListCreateAPIView(generics.ListCreateAPIView):   #Permite listar  y crear recetas
    queryset = RecetaCreada.objects.all()
    serializer_class = CreatedRecipeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return RecetaCreada.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
        
        
class RecetaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):  #permite ver detalles, actualizar y eliminar
    queryset = RecetaCreada.objects.all()
    serializer_class = CreatedRecipeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return RecetaCreada.objects.filter(usuario=self.request.user)
    

