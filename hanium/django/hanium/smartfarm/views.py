from django.shortcuts import render
from .models import Data_values_1F,Data_values_2F, Ctl_values_1F,Ctl_values_2F, AutomaticSys
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import viewsets
from .serializers import FarmCtlSerializer_1F, FarmSerializer_1F, FarmCtlSerializer_2F, FarmSerializer_2F,FarmAutoSerializer
from rest_framework.response import Response

#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import SessionAuthentication
import json

# Create your views here.

#class AllPost(APIView):

#	authentication_classes = (TokenAuthentication, SessionAuthentication)
#	permission_classes = (IsAuthenticated,)

#	def get(self, request):
#		allpost = Post.objects.order_by('id')
#		serializer = postSerializer(allpost, many=True)
#		return Response(serializer.data)


class FarmViewSet_1F(viewsets.ModelViewSet):
	#queryset = Data_values.objects.all()
	serializer_class = FarmSerializer_1F
	#authentication_classes = (TokenAuthentication, SessionAuthentication)
	#permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Data_values_1F.objects.all().order_by("-created_at")

	def perform_create(self, serializer):
		serializer.save()

class FarmViewCtl_1F(viewsets.ModelViewSet):
	#queryset = Ctl_values.objects.all()
	serializer_class = FarmCtlSerializer_1F
	#authentication_classes = (TokenAuthentication, SessionAuthentication)
	#permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Ctl_values_1F.objects.all()


	def perform_create(self, serializer):
		serializer.save()

class FarmViewSet_2F(viewsets.ModelViewSet):
        #queryset = Data_values.objects.all()
        #authentication_classes = (TokenAuthentication, SessionAuthentication)
        #permission_classes = (IsAuthenticated,)
        serializer_class = FarmSerializer_2F

        def get_queryset(self):
                return Data_values_2F.objects.all().order_by("-created_at")

        def perform_create(self, serializer):
                serializer.save()

class FarmViewCtl_2F(viewsets.ModelViewSet):
        #queryset = Ctl_values.objects.all()
        serializer_class = FarmCtlSerializer_2F
        #authentication_classes = (TokenAuthentication, SessionAuthentication)
        #permission_classes = (IsAuthenticated,)

        def get_queryset(self):
                return Ctl_values_2F.objects.all()

        def perform_create(self, serializer):
                serializer.save()

class FarmViewAuto(viewsets.ModelViewSet):
        #queryset = Ctl_values.objects.all()
        serializer_class = FarmAutoSerializer
        #authentication_classes = (TokenAuthentication, SessionAuthentication)
        #permission_classes = (IsAuthenticated,)

        def get_queryset(self):
                return AutomaticSys.objects.all()

        def perform_create(self, serializer):
                serializer.save()


#class SmartFarm_restful_update(UpdateAPIView):
#        queryset = Data_values.objects.all()
#        serializer_class = FarmSerializer

#class SmartFarm_restful_delete(DestroyAPIView):
#        queryset = Data_values.objects.all()
#        serializer_class = FarmSerializer

