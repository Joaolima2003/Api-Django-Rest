from django.urls import path
from .views import TarefaApiView

urlpatterns = [
    path('api/tarefas/', TarefaApiView.as_view()),
    path('api/tarefas/<int:pk>/', TarefaApiView.as_view()),
]
