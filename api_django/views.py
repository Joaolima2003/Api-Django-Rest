from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TarefaSerializer
from .models import Tarefa
from rest_framework import status

class TarefaApiView(APIView):
    def get(self, request, pk=None): 
        if pk:
            try:
                tarefa = Tarefa.objects.get(pk=pk)
            except Tarefa.DoesNotExist:
                return Response(status=404)
            serializer = TarefaSerializer(tarefa)
        else:
            try:
                tarefas = Tarefa.objects.all()
                serializer = TarefaSerializer(tarefas, many=True)
            except Tarefa.DoesNotExist:
                return Response(status=404)
        return Response(serializer.data)
        
    
    def post(self, request):
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        try:
            tarefa = Tarefa.objects.get(pk=pk)
        except Tarefa.DoesNotExist:
            return Response(status=404)
        
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            tarefa = Tarefa.objects.get(pk=pk)
        
        except Tarefa.DoesNotExist:
            return Response(status=404)
        
        tarefa.delete()
        return Response(status=204)
    
class TarefaApiUnique(APIView):
    def get(self, request, pk): 
        try:
            tarefa = Tarefa.objects.get(pk=pk)
        except Tarefa.DoesNotExist:
            return Response(status=404)
        
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)