from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    url = "https://api.agify.io?name=celeste"
    
    response = requests.request("GET", url)
    print(response.text)
    return render(request, 'oneOauthTaskApp/home.html', {"name":response.text})

def oauth(request):


    return render(request, 'oneOauthTaskApp/oauth.html')

