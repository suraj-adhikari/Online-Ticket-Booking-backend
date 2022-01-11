
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def Movielist(request):
    moviesobj = movieticket.objects.all()
    serializer = MovieSerializer(moviesobj,many=True)
    return Response(serializer.data)



@api_view(['POST'])
def post_Movie(request):
        moviesobj = movieticket.objects.all()
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def update_Movie(request,id):
    moviesobj = movieticket.objects.get(id=id)
    serializer = MovieSerializer(instance=moviesobj,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def delete_Movie(request,id):
    moviesobj = movieticket.objects.get(id=id)
    moviesobj.delete()
    return Response("movie is deleted")

