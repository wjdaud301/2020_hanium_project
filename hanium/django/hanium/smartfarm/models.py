from django.db import models

# Create your models here.

class Data_values_1F(models.Model):
    name = models.CharField(max_length=20)
    tem_data = models.FloatField()
    hum_data = models.FloatField()
    light_data = models.FloatField()
    sm_data = models.FloatField()
    co2 = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Data_values_2F(models.Model):
    name = models.CharField(max_length=20)
    tem_data = models.FloatField()
    hum_data = models.FloatField()
    light_data = models.FloatField()
    sm_data = models.FloatField()
    co2 = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Ctl_values_1F(models.Model):
    name = models.CharField(max_length=20)
    fan_ctl = models.BooleanField()
    water_ctl = models.BooleanField()
    light_ctl = models.BooleanField()
    heat_ctl = models.BooleanField()
    slide = models.BooleanField()


class Ctl_values_2F(models.Model):
    name = models.CharField(max_length=20)
    fan_ctl = models.BooleanField()
    water_ctl = models.BooleanField()
    light_ctl = models.BooleanField()
    heat_ctl = models.BooleanField()
    slide = models.BooleanField()


class AutomaticSys(models.Model):
    name = models.CharField(max_length=20)
    at = models.BooleanField()
    mintmp = models.IntegerField()
    maxtmp = models.IntegerField()
    minhum = models.IntegerField()
    maxhum = models.IntegerField()
    led_std = models.IntegerField()
    pump_std = models.IntegerField()
    led_time = models.IntegerField()
    pump_time = models.IntegerField()
    light_avg = models.IntegerField()
    sm_avg = models.IntegerField()


class Data_standard(models.Model):
    minled = models.IntegerField()
    maxled = models.IntegerField()
    minpump = models.IntegerField()
    maxpump = models.IntegerField()



def __str__(self):
    return self.name
