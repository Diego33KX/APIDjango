from unicodedata import name
from django.urls import re_path as url
from . import views
from django.urls import path
urlpatterns = [
    url(r'^productos/$',views.products_list),
    url(r'^productos/(?P<pk>[0-9]+)/$',views.product_detail),
    url(r'^categorias/$', views.categories_list),
    url(r'^categorias/(?P<pk>[0-9]+)/$',views.categories_detail),
    url(r'^paises/$',views.country_list),
    url(r'^paises/(?P<pk>[0-9]+)/$',views.country_detail),
    url(r'^ventas/$',views.venta_list),
    url(r'^ventas/(?P<pk>[0-9]+)/$',views.venta_detail),
    url(r'^usuarios/$',views.users_list),
    url(r'^usuarios/(?P<pk>[0-9]+)/$',views.users_detail),
    url(r'^cantidadproductos/',views.products_cantidad),
    url(r'^ventasdia/$',views.ventas_dia),
]
