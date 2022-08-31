from pyexpat import model
from django import forms
from tkinter import Widget
from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




# Create your models here.

user_roles = (
    ('responsable informatique','Responsable Informatique'),
    ('chargee affaire','Chargee Affaire'),
    ('responsable logistique1','Responsable Logistique 1'),
    ('responsable financier','Responsable Financier'),
    ('responsable logistique2','Responsable Logistique 2'),
    )
# class Roles(models.Model):
#     role = models.CharField(max_length=100, null = True)
#     def __str__(self):
#        return self.role


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, role, password=None):
        if not email:
            raise ValueError("users must have an email address")
        if not username:
            raise ValueError("users must have a username")
        if not role:
            raise ValueError("users must have a role")

        user = self.model(
            email= self.normalize_email(email),
            username = username,
            role = role,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email, username, role, password=None):

        user = self.create_user(
               email,
               username = username,
               password = password,
               role = role,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class Base(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique= True)
    # role =  models.ForeignKey(Roles, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=100, choices= user_roles, null=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']

    objects = MyAccountManager()


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True







class RchA(models.Model):
    n_Dossier = models.IntegerField()
    fournisseur = models.CharField(max_length=200)
    role = models.TextField(default="chargee affaire")
    nom = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    date_VCL = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
       return self.nom


STATUT_IMP = (
    ('en_negociation','En Negociation'),
    ('confirmee_fourn', 'Confirmee Fourn'),
    ('ex_c_payement','Ex_C_Payement'),
    ('en_preparation','En Preparation'),
    ('prelevee','Prelevee'),
    ('arrivee_maroc','Arrivee Maroc'),
    ('en_dedouanement','En Dedouanement'),
    ('liquide','Liquide'),
    ('en_entrepot','En Entrepot'),
    ('livree','Livree'),
    ('cloturee','Cloturee'),

)




class RL1(models.Model):
    n_Dossier = models.ForeignKey(RchA, on_delete=models.CASCADE)
    statut_Imp = models.CharField(max_length=20, choices=STATUT_IMP, default='en_negociation')
    role = models.TextField(default="responsable logistique1")
    date_TCS = models.DateTimeField() #date Transmission Commande Service 
    code_Four_Sage = models.IntegerField()
    ref_Bon_Cmd_Sage= models.CharField(max_length=200)
    cat_Cmd = models.CharField(max_length=200)
    date_CCF = models.DateTimeField() #date confirmation de la commande fournisseur
    n_FP= models.IntegerField()
    date_FP = models.DateTimeField()
    pays_Origine= models.CharField(max_length=200)
    incoterm = models.CharField(max_length=200)
    pays_Prt =models.CharField(max_length=200)
    montant_Dev = models.IntegerField()
    devise=models.CharField(max_length=200)
    mode_Pay = models.CharField(max_length=200)
    delai_Liv = models.CharField(max_length=200)
    Exec_Co_Pay = models.CharField(max_length=200)
    date_PPF = models.DateField() #date prevue pickup fournisseur
    date_PAM = models.DateTimeField() #date prevue arivee au maroc
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
       return self.role

class RespoINf(models.Model):
    n_Dossier = models.ForeignKey(RchA, on_delete=models.CASCADE)
    date_cacrs = models.DateTimeField()
    role = models.TextField(default="responsable informatique")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
       return self.role

class RespoFin(models.Model):
    n_Dossier = models.ForeignKey(RchA, on_delete=models.CASCADE)
    role = models.TextField(default="responsable financier")
    date_capf = models.DateTimeField()
    date_capp = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
       return self.role


class RL2(models.Model):
    n_Dossier = models.ForeignKey(RchA, on_delete=models.CASCADE)
    role = models.TextField(default="responsable logistique2")
    date_pickup = models.DateTimeField()
    freightforward = models.CharField(max_length=100)
    mode_trans =  models.CharField(max_length=100)
    date_AM =  models.CharField(max_length=100)
    transitaire =  models.CharField(max_length=100)
    Mt_ded_dh =  models.CharField(max_length=100)
    date_ld =  models.DateTimeField()
    date_lc =  models.DateTimeField()
    litige =  models.CharField(max_length=100)
    class_litige =  models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
       return self.role









