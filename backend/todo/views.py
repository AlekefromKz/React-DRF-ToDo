from rest_framework import viewsets

from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
