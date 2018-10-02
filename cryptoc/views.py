import requests
import datetime
from django.shortcuts import render
API_ENDPOINT = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
GIT_ENDPOINT = "https://api.github.com/users/bishalkhatri074"

# Create your views here.

def curriencies(request):
    response_data = requests.get(API_ENDPOINT)
    ctx = {
        "data": response_data.json()
    }

    return render(request, template_name="crypto/curriencies.html", context=ctx)

def github(request):
    response_data = requests.get(GIT_ENDPOINT)
    gtx = {
        "gith": response_data.json()
    }

    return render(request, template_name="crypto/git.html", context=gtx)

def index(request):
    data = {
        "todays_date" : str(datetime.datetime.now()),
    }

    return render(request, template_name= 'crypto/crypto_index.html', context=data)

def about(request):
    data = {
        "about_us" : "About Page"
    }

    return render(request, template_name='crypto/about.html', context=data)

def contact(request):
    data = {
        "contact_us" : "this is a contact page"
    }

    return render(request, template_name='crypto/contact.html', context=data)