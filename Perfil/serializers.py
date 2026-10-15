# serializers.py
from rest_framework import serializers
from .models import RecetaGuardada, RecetaCreada

class CreatedRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaCreada
        fields = [
            'id',
            'nombre',
            'descripcion',
            'tipo',
            'ingredientes',
            'preparacion',
            'imagen',
            'fecha_creacion'
        ]


class SavedRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaGuardada
        fields = '__all__'
        read_only_fields = ['usuario', 'fecha_guardado']
   



