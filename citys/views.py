import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from citys.models import CitysModel


def add_city(request):
    with open('city.json', 'r', encoding='utf-8') as f:
        city_dict = json.load(f)
        for i in city_dict['Data']['CityList']:
            for r in i['CityList']:
                CitysModel.objects.create(
                    name = r['AreaName'],
                    is_popular = True,
                    start_str = r['FirstLetter']
                )
    return HttpResponse('导入成功')
