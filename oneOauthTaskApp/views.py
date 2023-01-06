from django.shortcuts import render

# Create your views here.
def home(request):
    name = "Joe"
    return render(request, 'oneOauthTaskApp/home.html', {"name":name})