from ast import Try
from datetime import date, datetime
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Products,Categories,Countries, Users,Ventas
from .serializers import CategoriesSerializer, ProductsSerializer,CountriesSerializer,VentasSerializer,UserSerializer,CantidadProductos


class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JSONResponse,self).__init__(content,**kwargs)
@csrf_exempt
def products_list(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductsSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data,status=201)
        return JSONResponse(serializer.error,status=400)
@csrf_exempt
def product_detail(request,pk):
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductsSerializer(product)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductsSerializer(product,data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)


@csrf_exempt
def categories_list(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriesSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data,status=201)
        return JSONResponse(serializer.errors,status=400)
@csrf_exempt
def categories_detail(request,pk):
    try:
        categories = Categories.objects.get(pk=pk)
    except Categories.DoesNotExist:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = CategoriesSerializer(categories)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategoriesSerializer(categories,data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        categories.delete()
        return HttpResponse(status=204)


@csrf_exempt
def country_list(request):
    if request.method == 'GET':
        countries = Countries.objects.all()
        serializer = CountriesSerializer(countries,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CountriesSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data,status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def country_detail(request,pk):
    try:
        country = Countries.objects.get(pk=pk)
    except Countries.DoesNotExist:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = CountriesSerializer(country)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CountriesSerializer(country,data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        country.delete()
        return HttpResponse(status=204)

@csrf_exempt
def venta_list(request):
    if request.method == 'GET':
        ventas = Ventas.objects.all()
        serializer = VentasSerializer(ventas,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VentasSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data,status=201)
        return JSONResponse(serializer.errors,status=400)
@csrf_exempt
def venta_detail(request,pk):
    try:
        venta = Ventas.objects.get(pk=pk)
    except Ventas.DoesNotExist:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer = VentasSerializer(venta)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VentasSerializer(venta,data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        venta.delete()
        return HttpResponse(status=204)

@csrf_exempt

def users_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UserSerializer(users,many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data,status = 201)
        return JSONResponse(serializer.errors,status = 400)
@csrf_exempt

def users_detail(request,pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return HttpResponse(status = 400)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)


@csrf_exempt
def products_cantidad(request):
    if request.method == 'GET':
        suma = 0
        products = Ventas.objects.all().filter(fecha = date.today())
        ventas = Ventas.objects.all().filter(fecha = date.today()).count()
        prod = Products.objects.all()
        numero = []
        nombres = []
        for product in products:
            suma += product.total
        for pr in prod:
            nombres.append(pr.nombre)
            numero.append(Ventas.objects.filter(producto = pr.nombre).count())
        context ={
            "suma":suma,
            "cantidad":ventas,
            "numero":numero,
            "nombres":nombres
        }
        return JSONResponse(context)
@csrf_exempt
def ventas_dia(request):
    if request.method == 'GET':
        ventasDia = Ventas.objects.all().filter(fecha = date.today())
        serializer = VentasSerializer(ventasDia,many=True)
        return JSONResponse(serializer.data)
