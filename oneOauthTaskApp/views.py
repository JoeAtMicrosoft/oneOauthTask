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

    return render(request, 'oneOauthTaskApp/oauth.html')

def oauth_token(request):
    # api-endpoint
    url = """https://app.vssps.visualstudio.com/oauth2/token"""


    # defining a params dict for the parameters to be sent to the API
    headers = { 
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "1322"
            }
    
    app_secret = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIs"

    callback_url = "https://ado-oauth.azurewebsites.net"

    body = {
            f"client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer&client_assertion={app_secret}&grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion={code}&redirect_uri={callback_url}"
    }
    print(body)
    # sending post request and saving response as response object
    r = requests.post(url = url, headers=headers, json=body)
    
    # extracting data in json format
    data = r.json()
    
    return render(request, 'oneOauthTaskApp/oauth_token.html', {"data": data})

    

