from django.urls import path
from . import views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
#from rest_framework.authtoken import views as authviews


farmdata_1F_list = views.FarmViewSet_1F.as_view({"get":"list","post":"create"})
farmdata_1F_ctl = views.FarmViewCtl_1F.as_view({"get": "retrieve", "patch":"partial_update","delete":"destroy"})
farmdata_2F_list = views.FarmViewSet_2F.as_view({"get":"list","post":"create"})
farmdata_2F_ctl = views.FarmViewCtl_2F.as_view({"get": "retrieve", "patch":"partial_update","delete":"destroy"})
farmautomaticsys_list = views.FarmViewAuto.as_view({"get": "list","post":"create","delete":"destroy" })
farmautomaticsys_ctl = views.FarmViewAuto.as_view({"get": "retrieve", "patch":"partial_update","delete":"destroy"})


urlpatterns = [
  #  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   # url(r'^', include(router.urls)),
   # path('api-token-auth/', authviews.obtain_auth_token),
    url('^smartfarm_1F/$', farmdata_1F_list, name="farmdata-list"),
    url("^smartfarm_1F/(?P<pk>[0-9]+)/$", farmdata_1F_ctl, name="farmdata-ctl"),
    url('^smartfarm_2F/$', farmdata_2F_list, name="farmdata-list"),
    url("^smartfarm_2F/(?P<pk>[0-9]+)/$", farmdata_2F_ctl, name="farmdata-ctl"),
    url("^smartfarm_auto/$", farmautomaticsys_list, name="Automation"),
    url("^smartfarm_auto/(?P<pk>[0-9]+)/$", farmautomaticsys_ctl, name="Automation"),
#    url(r'^$', views.SmartFarm_restful_main.as_view(), name='smartfarm'),
#    url(r'^smartfarm/$', views.SmartFarm_restful_main.as_view(), name='smartfarm_list'),   
#    url(r'^smartfarm/<int:pk>/', views.SmartFarm_restful_detail.as_view(), name='startfarm_datail'),
#    url(r'^smartfarm/<int:pk>/update$', views.SmartFarm_restful_update.as_view(), name='smartfarm_update'),
#    url(r'^smartfarm/<int:pk>/delete$', views.SmartFarm_restful_delete.as_view(), name='smartfarm_delete'),

]

