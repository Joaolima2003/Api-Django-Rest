from .models import Tarefa
from rest_framework import serializers  


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'descricao', 'data_criacao', 'data_conclusao', 'concluida']