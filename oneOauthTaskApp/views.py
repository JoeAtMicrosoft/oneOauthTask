from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    url = """https://app.vssps.visualstudio.com/oauth2/authorize?client_id=4849160F-C8F2-43C2-AB32-3EE2F7D6DD54&response_type=Assertion&state=User1&scope=vso.taskgroups_write&redirect_uri=https://ado-oauth.azurewebsites.net/oauth""" 
    print(url)
    return render(request, 'oneOauthTaskApp/home.html', {"url":url})

def oauth(request):
    code = request.GET.get('code', '')
    state = request.GET.get('state', '')
    print(code)
    print(state)
    return render(request, 'oneOauthTaskApp/oauth.html')

