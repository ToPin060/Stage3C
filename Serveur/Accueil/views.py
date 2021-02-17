
from django.shortcuts import render
from django.http import HttpResponse

def index(resquest):

    return render(resquest, "Accueil/index.html")
