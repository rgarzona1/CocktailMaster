# api_views.py
from rest_framework import generics, permissions
from .models import RecetaCreada, RecetaGuardada
from .serializers import CreatedRecipeSerializer, SavedRecipeSerializer

class MisCreacionesList(generics.ListAPIView):
    serializer_class = CreatedRecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (RecetaCreada.objects
                .filter(usuario=self.request.user)
                .order_by('-fecha_creacion'))


class RecetasGuardadasList(generics.ListAPIView):
    serializer_class = SavedRecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (RecetaGuardada.objects
                .filter(usuario=self.request.user)
                .order_by('-fecha_guardado'))
        
        
        
class RecetaListCreateAPIView(generics.ListCreateAPIView):
    queryset = RecetaCreada.objects.all()
    serializer_class = CreatedRecipeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return RecetaCreada.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)