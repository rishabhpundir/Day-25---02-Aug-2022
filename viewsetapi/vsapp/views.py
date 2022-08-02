from urllib import response
from django.shortcuts import render
from vsapp.serializers import UserSerializer
from vsapp.models import User
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# to get indivitual user details
# def user_details(request, user_id):
#     user = User.objects.get(id=user_id)
#     serializer = UserSerializer(user)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')

# # to get all users details in one go
# def all_user_details(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser.parse(stream=stream)
        serializer = UserSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Data Created'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
