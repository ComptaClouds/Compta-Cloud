from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    name = models.CharField(blank=True, max_length=255)
    denominations = models.CharField(max_length=45, blank=True, null=True)
    sieges = models.CharField(max_length=45, blank=True, null=True)
    objets = models.CharField(max_length=45, blank=True, null=True)
    capitals = models.FloatField(blank=True, null=True)
    durees = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.email


class Compte(models.Model):
    compteid = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=45, blank=True, null=True)
    classe = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compte'


class Contrat(models.Model):
    users_userid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'contrat'


class Credits(models.Model):
    creditsid = models.AutoField(primary_key=True)
    operation_operationid = models.IntegerField()
    compte_compteid = models.IntegerField()
    operation_typejournal_typejournalid = models.IntegerField()
    operation_piece_pieceid = models.IntegerField()
    operation_piece_typepiece_typepieceid = models.IntegerField()
    operation_travailleur_users_userid = models.IntegerField()
    operation_travailleur_travailleuridsaisie = models.IntegerField()
    operation_travailleur_travailleuridimpute = models.IntegerField()
    montant = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credits'
        unique_together = (('creditsid', 'operation_operationid', 'compte_compteid', 'operation_typejournal_typejournalid', 'operation_piece_pieceid', 'operation_piece_typepiece_typepieceid', 'operation_travailleur_users_userid', 'operation_travailleur_travailleuridsaisie', 'operation_travailleur_travailleuridimpute'),)


class Debits(models.Model):
    debitsid = models.AutoField(primary_key=True)
    operation_operationid = models.IntegerField()
    compte_compteid = models.IntegerField()
    operation_typejournal_typejournalid = models.IntegerField()
    operation_piece_pieceid = models.IntegerField()
    operation_piece_typepiece_typepieceid = models.IntegerField()
    operation_travailleur_users_userid = models.IntegerField()
    operation_travailleur_travailleuridsaisie = models.IntegerField()
    operation_travailleur_travailleuridimpute = models.IntegerField()
    montant = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'debits'
        unique_together = (('debitsid', 'operation_operationid', 'compte_compteid', 'operation_typejournal_typejournalid', 'operation_piece_pieceid', 'operation_piece_typepiece_typepieceid', 'operation_travailleur_users_userid', 'operation_travailleur_travailleuridsaisie', 'operation_travailleur_travailleuridimpute'),)


class Dfe(models.Model):
    users_userid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dfe'



class Dsv(models.Model):
    users_userid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dsv'


class Operation(models.Model):
    operationid = models.AutoField(primary_key=True)
    typejournal_typejournalid = models.IntegerField()
    piece_pieceid = models.IntegerField()
    piece_typepiece_typepieceid = models.IntegerField()
    travailleur_users_userid = models.IntegerField()
    travailleur_travailleuridsaisie = models.IntegerField()
    travailleur_travailleuridimpute = models.IntegerField()
    libelle = models.CharField(max_length=45, blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)
    dateoperation = models.DateField(blank=True, null=True)
    datesaisie = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operation'
        unique_together = (('operationid', 'typejournal_typejournalid', 'piece_pieceid', 'piece_typepiece_typepieceid', 'travailleur_users_userid', 'travailleur_travailleuridsaisie', 'travailleur_travailleuridimpute'),)


class Piece(models.Model):
    pieceid = models.AutoField(primary_key=True)
    typepiece_typepieceid = models.IntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    lien = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'piece'
        unique_together = (('pieceid', 'typepiece_typepieceid'),)


class Statut(models.Model):
    users_userid = models.IntegerField(primary_key=True)
    denomination = models.CharField(max_length=45)
    siege = models.CharField(max_length=45, blank=True, null=True)
    objet = models.CharField(max_length=45, blank=True, null=True)
    capital = models.FloatField(blank=True, null=True)
    duree = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statut'


class Travailleur(models.Model):
    travailleurid = models.AutoField(primary_key=True)
    users_userid = models.IntegerField()
    nom = models.CharField(max_length=20, blank=True, null=True)
    prenom = models.CharField(max_length=20, blank=True, null=True)
    fonction = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travailleur'
        unique_together = (('travailleurid', 'users_userid'),)


class Typejournal(models.Model):
    typejournalid = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typejournal'


class Typepiece(models.Model):
    typepieceid = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typepiece'


class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    denomination = models.CharField(max_length=45, blank=True, null=True)
    siege = models.CharField(max_length=45, blank=True, null=True)
    objet = models.CharField(max_length=45, blank=True, null=True)
    capital = models.FloatField(blank=True, null=True)
    duree = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'