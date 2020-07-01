from django.shortcuts import render
import requests
import json

# Create your views here.

def register(request):
    return render(request, "signup/signuppage.html")

def registerUser(request):
    email = request.GET['emailid']
    password = request.GET['pass']
    name = request.GET['name']
    print(email, password, name, "this is me")

    url = "http://127.0.0.1:8000/api/login/"

    payload = {"email":email, "password":password, "name": name}
    payload = json.dumps(payload)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    data = response.text

    return render(request, 'temp.html', {'data': data})
