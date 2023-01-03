from django.shortcuts import render , HttpResponseRedirect
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse , Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Matkul
from .serializers import ItemSerializer

@csrf_exempt
def ItemsView(request):
    if request.method == 'GET':
        items = Matkul.objects.all()
        serializer = ItemSerializer(items, many = True)
        return JsonResponse(serializer.data , safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)


@csrf_exempt
def ItemView(request, nm):
    try:
        item  = Matkul.objects.get(id = nm)
    except Matkul.DoesNotExist:
        raise Http404('Not Found')

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(item, data=data)

        if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "DELETE":
        item.delete()
        return HttpResponse(status = 204)
# Create your views here.
