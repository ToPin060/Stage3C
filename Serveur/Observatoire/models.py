
from django.db import models

class Enfant(models.Model):

    nom = models.CharField(db_column="NOM_ENFANT", max_length=50)
    prenom = models.CharField(db_column="PRENOM_ENFANT", max_length=50)

    def __str__(self):
        return self.nom + ' ' + self.prenom
    
