from dataclasses import field
from rest_framework import serializers
from .models import Categories, Countries, Products, Users,Ventas
from django.contrib.auth.hashers import make_password, check_password
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id','nombre','categoria','pais','precio','stock','marca','talla','genero','img_delante','img_atras','img_atras','cantidad','descripcion','pub_date')

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id','nombre','pub_date','img')

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ('id','nombre','pub_date','img')

class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = ('id','producto','precio','cantidad','subtotal','igv','total','fecha','cliente')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','username','email','password')
class CantidadProductos(serializers.ModelSerializer):
    class Meta:
        fields = ('cantidad')

