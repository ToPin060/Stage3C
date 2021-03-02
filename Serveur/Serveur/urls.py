
"""
    PINTO Tristan
    L3 Informatique : INU Champollion - Albi
    ________________________________________
    FICHIER         : Serveur/urls.py
    UTILITE         : Définir les routes du serveur
    COMMENTAIRES    :   + Actuellement il route sur un application "Observatoire" mais il permet de faire le liens entre plusieurs applications.
                        + L'application "Observatoire" est l'application principale pour le moment.
"""

# IMPORTS
from django.contrib import admin
from django.urls    import path, include

# ROUTES
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Observatoire.urls")),
]
