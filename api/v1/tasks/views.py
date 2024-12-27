from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from django.shortcuts import render
from euphoria.models import Task
from .serializers import TaskSerializer
from datetime import timedelta



@api_view(['GET'])


def api(request):
    api = Task.objects.all()
    serializers = TaskSerializer(api , many=True)
    return Response (serializers.data)
    # return Response (TaskSerializer({'message': 'Success'}).data)


# View to list and create tasks
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

SIMPLE_JWT = {
    'ACCES_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME':timedelta(days =7),
}

@api_view(['POST'])


def create_api(request):
    serializers = TaskSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data , status=status.HTTP_201_CREATED)
    return Response(serializers.errors , status=status.HTTP_400_BAD_REQUEST)
    print(requestdata)


@api_view([ 'GET','PUT', 'DELETE' ])

def detail_api(request , pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers= TaskSerializer(task)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers =TaskSerializer(task , data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' :
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


