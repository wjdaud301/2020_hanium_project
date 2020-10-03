from django.shortcuts import render , redirect
from .forms import UserForm, LoginForm
from .models import Addresses
from .serializers import AddressesSerializer 
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.views import View
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
import logging
# Create your views here. 

 
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def address_list(request):
    if request.method == 'GET':
        query_set = Addresses.objects.all()
        serializer = AddressesSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def address(request, pk):

    obj = Addresses.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = AddressesSerializer(obj)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def app_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        id = request.POST.get('username','')
        pw = request.POST.get('password1','')
        result = authenticate(username=id, password=pw)

        if result is not None:
            logging.error("login success!")
            login(request, result)
            return JsonResponse({'code':'0000', 'msg':'login success'},status=200)
        else:
            logging.error("failed")
            return JsonResponse({'code':'1001', 'msg':'faild'},status=200)

    else :
        form = LoginForm()
        return render(request, 'addresses/login.html',{'form': form})


@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if  request.POST['password1'] == request.POST['password2'] :
            user = User.objects.create_user(username = request.POST["username"], password = request.POST["password1"])
            login(request,user)
            return JsonResponse({'code':'0000', 'msg':'signup success'},status=200)
            #return redirect('/addresses/app_login')
        else:
            return JsonResponse({'code':'1001', 'msg':'signup failed'},status=200)


    else:
        form = UserForm()
        return render(request, 'addresses/adduser.html',{'form': form})

@csrf_exempt
def logout(request):
    auth.logout(request)
    #return render(request, "addresses/login.html")
    return JsonResponse({'code':'0000', 'msg':'logout'},status=200)

@csrf_exempt
def login_page(request):
    return render(request, "addresses/login.html")

