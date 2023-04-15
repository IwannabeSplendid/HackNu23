from django.shortcuts import render
from .models import User, Courier, Employee, Client, Order, Address, Company, Department
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
import requests

# Home page view extends the index.html template
# track, login buttons 
def home(request):
    # return to another page with order info
    if request.method == "POST":
        iin = request.POST['iin']
        order_number = request.POST['order_number']
        
        token = get_token()
        url = 'http://hakaton-fl.gov4c.kz/api/persons/' + iin
        client_info = requests.get(url, headers={'authorization': 'Bearer ' + token})

        
        return client_info
    
    return render(request, 'home.html')

def get_token():
    url = 'http://hakaton-idp.gov4c.kz/auth/realms/con-web/protocol/openid-connect/token'
    myobj = {'username': 'test-operator', 'password' : 'DjrsmA9RMXRl', 'client_id' : 'cw-queue-service', 'grant_type' : 'password'}

    token = requests.post(url, json = myobj)
    
    return token.text


def login_view(request):

    #when submitted (button clicked)
    if request.method == "POST":

        #authenticate user
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        
        #redirect to their pages
        if user is not None: 
            login(request, user)

            return HttpResponseRedirect(reverse('personal'))
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid credentials'
            })
            
# def index(request):
#     return render(request, 'index.html')

# def index(request):
#     return render(request, 'index.html')

# def index(request):
#     return render(request, 'index.html')

# def index(request):
#     return render(request, 'index.html')