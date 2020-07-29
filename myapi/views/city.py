from django.http import JsonResponse
from myapi.models import City
from django.views.decorators.csrf import csrf_exempt
import json


def getAllCities(request):
    if request.method == 'GET':
        try:
            cities = City.nodes.all()
            response = []
            for city in cities:
                obj = {
                    "code": city.code,
                    "name": city.name,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)
@csrf_exempt
def cityDetails(request):
    if request.method == 'GET':
        # get one city by name
        name = request.GET.get('name', ' ')
        try:
            city = City.nodes.get(name=name)
            response = {
                "code": city.code,
                "name": city.name,
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        # create one city
        json_data = json.loads(request.body)
        name = json_data['name']
        code = json_data['code']
        try:
            city = City(name=name, code=code)
            city.save()
            response = {
                "code": city.code,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'PUT':
        # update one city
        json_data = json.loads(request.body)
        name = json_data['name']
        code = json_data['code']
        try:
            city = City.nodes.get(code=code)
            city.name = name
            city.save()
            response = {
                "code": city.code,
                "name": city.name,
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

    if request.method == 'DELETE':
        # delete one city
        json_data = json.loads(request.body)
        code = json_data['code']
        try:
            city = City.nodes.get(code=code)
            city.delete()
            response = {"success": "City deleted"}
            return JsonResponse(response)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)
