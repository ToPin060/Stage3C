
"""
    PINTO Tristan
    L3 Informatique : INU Champollion - Albi
    ________________________________________
    FICHIER         : Serveur/Observatoire/urls.py
    UTILITE         : Définir les routes de l'application "Observatoire"
    COMMENTAIRES    :   + Route de base -> connexion
                        + ...
"""

# IMPORTS
from django.urls import path
from . import views

# ROUTES
urlpatterns = [
    path("", views.connexion, name="connexion"),
]
