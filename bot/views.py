from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome To Sylphh Clothings Chatbot</h1>")


# Create your views here.
def register(request):
    return HttpResponse("<h1>Sefunmi mumu gan</h1>")

