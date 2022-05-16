from app.models import Todo
from app.serializers import TodoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

#views quando acessamos url's, ela são "chamadas". Evia dados e recebe dados. Primeiro método para acessar view será GET. Depois disso, precisamos registrar uma url que chame essa função quando for acessada.
@api_view(['GET'])
def todo_list(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)



