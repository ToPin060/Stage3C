
"""
    PINTO Tristan
    L3 Informatique : INU Champollion - Albi
    ________________________________________
    FICHIER         : Serveur/Observatoire/views.py
    UTILITE         : Vues de l'application "Observatoire"
    COMMENTAIRES    :   + connexion -> portail de connexion
                        + ...
"""

# IMPORTS
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail

from .forms import PreInscription

# PORTAIL DE CONNEXION
def connexion(request):
    
    # TRAITEMENT DE L'AUTHENTIFICATION
    if (request.method == "POST") :

        # UTILISATEUR RENTRER
        iden = request.POST.get("identifiant", False)
        mdp = request.POST.get("mot_de_passe", False)
        utilisateur = authenticate(username=iden, password=mdp)

        # UTILISATEUR EXISTANT ?
        if (utilisateur is not None and utilisateur.is_active) :

            login(request, utilisateur)
            return redirect('connexion')
        
        else :

            return render(request, "connexion/index.html")

    if (request.user.is_authenticated) :
        return accueil(request)
    else :
        return render(request, "connexion/index.html")

def accueil(request):

    if (request.method == "POST") :
        form = PreInscription(request.POST)

        if form.is_valid() :
            values = form.save(commit=False)
            values.save()
            return redirect('accueil')

    else :
        form = PreInscription()
        return render(request, "generals/accueil__.html", {'form':form})

