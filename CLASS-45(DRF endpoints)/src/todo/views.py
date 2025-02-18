from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import TodoSerializers

@api_view(['GET', 'POST'])
def todos(request):
    print(request)

    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializers(todos, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        print("User Data: ", request.data)

        serializer = TodoSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"Success": "Todo created Successfully"},
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)