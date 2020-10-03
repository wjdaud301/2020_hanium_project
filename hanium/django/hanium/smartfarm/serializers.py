from .models import Data_values_1F, Data_values_2F, Ctl_values_1F, Ctl_values_2F, AutomaticSys
from rest_framework import serializers
from rest_framework.response import Response


class FarmSerializer_1F(serializers.ModelSerializer):
    class Meta:
        model = Data_values_1F
        fields = ('name', 'tem_data', 'hum_data', 'light_data', 'sm_data','co2','created_at')


class FarmCtlSerializer_1F(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ctl_values_1F
        fields = ('id','fan_ctl','light_ctl','water_ctl','slide', 'heat_ctl')


class FarmSerializer_2F(serializers.ModelSerializer):
    class Meta:
        model = Data_values_2F
        fields = ('name', 'tem_data', 'hum_data', 'light_data', 'sm_data','co2','created_at')


class FarmCtlSerializer_2F(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ctl_values_2F
        fields = ('id','fan_ctl','light_ctl','water_ctl', 'slide', 'heat_ctl')


class FarmAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutomaticSys
        fields = ('at','led_time','pump_time','mintmp','maxtmp','minhum','maxhum','light_avg', 'sm_avg')
