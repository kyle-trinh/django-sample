from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
class PingView(APIView):
    def get(self, request):
        divide = 1 / 0 
        return Response({"message": "pong"})

def hello(request):
    return JsonResponse({"message": "hello"})

class PostView(APIView):
    def post(self, request):
        return Response({"post": "request"})
