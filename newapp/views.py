from json import JSONDecodeError

import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    try:
        records = {}
        url = requests.get("")
        response = url.json()
        records['all'] = response
        return render(request, 'index.html',records)
    except JSONDecodeError as e:
        return render(request, 'index.html', e)
    # except TypeError as e:
    #     return render(request, 'index.html', e)

def national(request):
    try:
        records = {}
        url = requests.get("")
        response = url.json()
        records['national'] = response
        return render(request, 'national.html',records)
    except JSONDecodeError as e:
        return render(request, 'national.html',e)
    # except TypeError as e:
    #     return render(request, 'national.html',e)

def business(request):
    try:
        records = {}
        url = requests.get("")
        response = url.json()
        records['business'] = response
        return render(request, 'business.html',records)
    except JSONDecodeError as e:
        return render(request, 'business.html',e)
    # except TypeError as e:
    #     return render(request, 'business.html',e)

def sports(request):
    try:
        records = {}
        url = ""
        response = requests.get(url=url)
        inshorts_data= response.json()
        records['sports'] = inshorts_data
        return render(request, 'sports.html',records)
    except JSONDecodeError as e:
        return render(request, 'sports.html',e)
    # except TypeError as e:
    #     return render(request, 'sports.html',e)

def world(request):
    try:
        records = {}
        url = requests.get("")
        response = url.json()
        records['world'] = response
        return render(request, 'world.html',records)
    except JSONDecodeError as e:
        return render(request, 'world.html',e)
    # except TypeError as e:
    #     return render(request, 'world.html',e)

def politics(request):
    try:
        records = {}
        url = requests.get("")
        response = url.json()
        records['politics'] = response
        return render(request, 'politics.html',records)
    except JSONDecodeError as e:
        return render(request, 'politics.html',e)
    # except TypeError as e:
    #     return render(request, 'politics.html',e)

def technology(request):
    try:
        records = {}
        url = requests.get("")
        response = url.json()
        records['technology'] = response
        return render(request, 'technology.html',records)
    except JSONDecodeError as e:
        return render(request, 'technology.html',e)
    # except TypeError as e:
    #     return render(request, 'technology.html',e)

def startup(request):
    try:
        records = {}
        url = requests.get("")
        response = url.json()
        records['startup'] = response
        return render(request, 'startup.html',records)
    except JSONDecodeError as e:
        return render(request, 'startup.html',e)
    # except TypeError as e:
    #     return render(request, 'startup.html',e)

def entertainment(request):
    try:
        records = {}
        url = requests.get("")
        response = url.json()
        records['entertainment'] = response
        return render(request, 'entertainment.html',records)
    except JSONDecodeError as e:
        return render(request, 'entertainment.html',e)
    # except TypeError as e:
    #     return render(request, 'entertainment.html',e)

def miscellaneous(request):
    try:
        records = {}
        url = requests.get("")
        response = url.json()
        records['miscellaneous'] = response
        return render(request, 'miscellaneous.html',records)
    except JSONDecodeError as e:
        return render(request, 'miscellaneous.html',e)
    # except TypeError as e:
    #     return render(request, 'miscellaneous.html',e)

def hatke(request):
    try:
        records = {}
        url = requests.get("")
        response = url.json()
        records['hatke'] = response
        return render(request, 'hatke.html',records)
    except JSONDecodeError as e:
        return render(request, 'hatke.html',e)
    # except TypeError as e:
    #     return render(request, 'hatke.html',e)

def science(request):
    try:
        records = {}
        url = requests.get("")
        response = url.json()
        records['science'] = response
        return render(request, 'science.html',records)
    except JSONDecodeError as e:
        return render(request, 'science.html',e)
    # except TypeError as e:
    #     return render(request, 'science.html',e)

def automobile(request):
    try:
        records = {}
        url = requests.get("")
        response = url.json()
        records['automobile'] = response
        return render(request, 'automobile.html',records)
    except JSONDecodeError as e:
        return render(request, 'automobile.html',e)
    # except TypeError as e:
    #     return render(request, 'automobile.html',e)
