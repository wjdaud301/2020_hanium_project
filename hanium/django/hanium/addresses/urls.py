from django.urls import path
from . import views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
#from rest_framework.authtoken import views as authviews
#from django.contrib.auth import views as auth_views



urlpatterns = [
    #path('login/', login_list),
    url(r'signup/$', views.signup, name='signup'),
    url(r'^app_login/$', views.app_login, name='app_login'),
    path('logout/',views.logout, name='logout'),
    path('addlist/', views.address_list),
    path('add/<int:pk>/', views.address),

]
