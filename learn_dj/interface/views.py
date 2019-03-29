from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def get(request):
    data = {}
    name = request.GET.get('name')
    age = request.GET.get('age')
    data['firstname'] = name
    data['age-age'] = age
    print(data)
    return JsonResponse(data)
