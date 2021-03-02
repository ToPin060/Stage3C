
from django.db import models
from phone_field import PhoneField

class Enfant(models.Model):

    nom = models.CharField(db_column="NOM_ENFANT", max_length=50, null=True)
    prenom = models.CharField(db_column="PRENOM_ENFANT", max_length=50, null=True)
    datenaiss = models.DateField(db_column="DATENAISS_ENFANT", null=True)
    sexe = models.CharField(db_column="SEXE_ENFANT", max_length=20, null=True)
    nbjours = models.IntegerField(db_column="NBJOURS_ENFANT", null=True)
    tableau = models.ForeignKey('Horaire',db_column="HORAIRE_ENFANT", on_delete=models.CASCADE, null=True)
    jdlsi = models.BooleanField(db_column="JDLSI_ENFANT", null=True)
    fdj = models.BooleanField(db_column="FDJ_ENFANT", null=True)
    fdjcom = models.CharField(db_column="FDJCOM_ENFANT", max_length=50, null=True)
    fh = models.BooleanField(db_column="FH_ENFANT", null=True)
    fhcom = models.CharField(db_column="FHCOM_ENFANT", max_length=50, null=True)
    mdg = models.CharField(db_column="MDG_ENFANT", max_length=200, null=True)
    rdlda = models.CharField(db_column="RDLDA_ENFANT", max_length=200, null=True)
    parent1 = models.ForeignKey('Parent',db_column="PARENT1_ENFANT", related_name="parent1", on_delete=models.CASCADE, null=True)
    parent2 = models.ForeignKey('Parent',db_column="PARENT2_ENFANT", related_name="parent2", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nom + ' ' + self.prenom
    

class Parent(models.Model):

    nom = models.CharField(db_column="NOM_PARENT", max_length=50)
    prenom = models.CharField(db_column="PRENOM_PARENT", max_length=50)
    adresse = models.CharField(db_column="ADRESSE_PARENT", max_length=200)
    mail = models.EmailField(db_column="MAIL_PARENT")
    telpor = PhoneField(db_column="TELPOR_PARENT")
    teldom = PhoneField(db_column="TELDOM_PARENT")
    profession = models.CharField(db_column="PROFESSION_PARENT", max_length=100)
    employeur = models.ForeignKey('Employeur', on_delete=models.CASCADE)
    typealoc = models.CharField(db_column="TYPEALOC_PARENT", max_length=50)
    numaloc = models.IntegerField(db_column="NUMALOC_PARENT")

    def __str__(self):
        return self.nom + ' ' + self.prenom


class Employeur(models.Model):

    nom = models.CharField(db_column="NOM_EMPLOYEUR", max_length=100)
    adresse = models.CharField(db_column="ADRESSE_EMPLOYEUR", max_length=200)

    def __str__(self):
        return self.nom

class Horaire(models.Model):

    lunarr = models.IntegerField(db_column="LUNARR_HORAIRE")
    lundeb = models.IntegerField(db_column="LUNDEB_HORAIRE")
    mararr = models.IntegerField(db_column="MARARR_HORAIRE")
    mardeb = models.IntegerField(db_column="MARDEB_HORAIRE")
    merarr = models.IntegerField(db_column="MERARR_HORAIRE")
    merdeb = models.IntegerField(db_column="MERDEB_HORAIRE")
    jeuarr = models.IntegerField(db_column="JEUARR_HORAIRE")
    jeudeb = models.IntegerField(db_column="JEUDEB_HORAIRE")
    venarr = models.IntegerField(db_column="VENARR_HORAIRE")
    vendeb = models.IntegerField(db_column="VENDEB_HORAIRE")
    samarr = models.IntegerField(db_column="SAMARR_HORAIRE")
    samdeb = models.IntegerField(db_column="SAMDEB_HORAIRE")
    dimarr = models.IntegerField(db_column="DIMARR_HORAIRE")
    dimdeb = models.IntegerField(db_column="DIMDEB_HORAIRE")

    def __str__(self):
        return "IDK ACTUALLY"