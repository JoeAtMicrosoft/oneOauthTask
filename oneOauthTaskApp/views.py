from django.shortcuts import render
import requests

    # https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?view=azure-devops
    # Step 1 is REGISTERING THE APP. This is done manually on the referenced portal
    # Step 2 of the MS docs: AUTHORIZING THE APP. Here, the user is authorizing the app to do certain things.
def home(request):
    url = """https://app.vssps.visualstudio.com/oauth2/authorize?client_id=4849160F-C8F2-43C2-AB32-3EE2F7D6DD54&response_type=Assertion&state=User1&scope=vso.taskgroups_write&redirect_uri=https://ado-oauth.azurewebsites.net/oauth""" 
    print(url)
    return render(request, 'oneOauthTaskApp/home.html', {"url":url})

    # Handles callback from above.
def oauth(request):
    code = request.GET.get('code', '')
    state = request.GET.get('state', '')

    # Save the authorization token.
    file = open("oneOauthTaskApp/auth codes/authorization_code.txt", "w")
    file.write(code)
    return render(request, 'oneOauthTaskApp/oauth.html', {"code":code})

    # Step 3 of the MS docs: GET ACCESS AND REFRESH TOKENS FOR THE USER. This establishes the app and server with the 3p auth server.
def oauth_token(request):

    url = """https://app.vssps.visualstudio.com/oauth2/token"""

    # Retrieve the authorization token
    file = open("oneOauthTaskApp/auth codes/authorization_code.txt", "r")
    code = file.read()
    
    #from the authorization portal used in step 1
    app_secret = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIs"
    callback_url = "https://ado-oauth.azurewebsites.net"

    body = {
            f"client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer&client_assertion={app_secret}&grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion={code}&redirect_uri={callback_url}"
    }

    r = requests.post(url = url, json=body)
    
    data = r.json()
    
    return render(request, 'oneOauthTaskApp/oauth_token.html', {"data": data})

    

