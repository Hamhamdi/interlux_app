from asyncore import write
from datetime import date, datetime
import email
from email.mime import base
from typing import OrderedDict
from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from itertools import chain
from operator import attrgetter
from django.db.models import Q

import xlwt
from django.http import HttpResponse
import csv


from base.context_processor import get_notified
from base.form import AdminForm, RegistrationForm, AccountAuthenticationForm, ResCa, ResFin, ResInf, Rl1Form, Rl2Form

# from base.form import RoleForm
from .models import  Base, GeneralDTable
from django.contrib.auth.forms import UserCreationForm


# Create your views here.




def loginPage(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:

                login(request, user)
                return redirect('general_db')

    else:
       form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            role = form.cleaned_data.get('role')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, role=role, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:  # GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'base/register.html', context)

def home(request):
    return render(request, 'base/home.html')




def addRCa(request):
    
    form = ResCa()
    extra_context = {}

    if request.method == 'POST':
        form = ResCa(request.POST)

        if form.is_valid():
            resca =form.save(commit=False)       
            resca.date_validation_e1 = datetime.now()
            if 'btn_submit' in request.POST:
                 resca.etape+=1
            resca.save()
           


            
            

            return redirect('general_db')
        
    context={'form': form}
    return render(request, 'base/respo_ca_add.html', context)
    
@login_required(login_url='/login')
def updateRCa (request, pk):

    rca = GeneralDTable.objects.get(id=pk)
    form = ResCa(instance=rca)
   

    if request.method == 'POST':
        form = ResCa(request.POST, instance=rca) 
        if form.is_valid():
            resca =form.save(commit=False)  
            resca.date_validation_e1 = datetime.now()
            if 'btn_submit' in request.POST:
                 resca.etape+=1
            resca.save()
            return redirect('general_db')
    context={'form': form}
    return render(request, 'base/respo_ca_add.html', context)


@login_required(login_url='/login')
def updatelog1 (request, pk):
    log1 = GeneralDTable.objects.get(id=pk)
    form = Rl1Form(instance=log1)

    if request.POST:
        form = Rl1Form(request.POST, instance=log1)
        if form.is_valid():
            
            reslog1 =form.save(commit=False)     
            log1.statut_Imp =  reslog1.statut_Imp
            log1.date_TCS =  reslog1.date_TCS
            log1.code_Four_Sage =  reslog1.code_Four_Sage
            log1.ref_Bon_Cmd_Sage =  reslog1.ref_Bon_Cmd_Sage
            log1.cat_Cmd =  reslog1.cat_Cmd
            log1.date_CCF =  reslog1.date_CCF
            log1.n_FP =  reslog1.n_FP
            log1.date_FP =  reslog1.date_FP
            log1.pays_Origine =  reslog1.pays_Origine
            log1.incoterm =  reslog1.incoterm
            log1.pays_Prt =  reslog1.pays_Prt
            log1.montant_Dev =  reslog1.montant_Dev
            log1.devise =  reslog1.devise
            log1.mode_Pay =  reslog1.mode_Pay
            log1.delai_Liv =  reslog1.delai_Liv
            log1.Exec_Co_Pay =  reslog1.Exec_Co_Pay
            log1.date_PPF =  reslog1.date_PPF
            log1.date_PAM =  reslog1.date_PAM
            log1.date_validation_e2 = datetime.now()
            log1.delai_e2 = (log1.date_validation_e2.day - log1.date_validation_e1.day) + 1
            if 'btn_submit' in request.POST:
                log1.etape+=1
            log1.save()
            return redirect('general_db')


    context={'form': form, 'log1':log1}
    return render(request, 'base/respo_log1_add.html', context)           
def addlog1(request, pk):

    form = Rl1Form()
    log1 = GeneralDTable.objects.get(id=pk)
   

    if request.POST:
        form = Rl1Form(request.POST)
        if form.is_valid():
            
            reslog1 =form.save(commit=False)     
            log1.statut_Imp =  reslog1.statut_Imp
            log1.date_TCS =  reslog1.date_TCS
            log1.code_Four_Sage =  reslog1.code_Four_Sage
            log1.ref_Bon_Cmd_Sage =  reslog1.ref_Bon_Cmd_Sage
            log1.cat_Cmd =  reslog1.cat_Cmd
            log1.date_CCF =  reslog1.date_CCF
            log1.n_FP =  reslog1.n_FP
            log1.date_FP =  reslog1.date_FP
            log1.pays_Origine =  reslog1.pays_Origine
            log1.incoterm =  reslog1.incoterm
            log1.pays_Prt =  reslog1.pays_Prt
            log1.montant_Dev =  reslog1.montant_Dev
            log1.devise =  reslog1.devise
            log1.mode_Pay =  reslog1.mode_Pay
            log1.delai_Liv =  reslog1.delai_Liv
            log1.Exec_Co_Pay =  reslog1.Exec_Co_Pay
            log1.date_PPF =  reslog1.date_PPF
            log1.date_PAM =  reslog1.date_PAM
            log1.date_validation_e2 = datetime.now()
            log1.delai_e2 = (log1.date_validation_e2.day - log1.date_validation_e1.day) + 1
            if 'btn_submit' in request.POST:
                log1.etape+=1
            log1.save()
            
             


            return redirect('general_db')


    context={'form': form, 'log1':log1}
    return render(request, 'base/respo_log1_add.html', context)

@login_required(login_url='/login')
def updatelog2(request, pk):
    log2 = GeneralDTable.objects.get(id=pk)
    form = Rl2Form(instance=log2)
    if request.POST:

        form = Rl2Form(request.POST, instance=log2)
        if form.is_valid():
            reslog2 =form.save(commit=False)     
            
            log2.date_pickup =  reslog2.date_pickup
            log2.freightforward =  reslog2.freightforward
            log2.mode_trans =  reslog2.mode_trans
            log2.date_AM =  reslog2.date_AM
            log2.transitaire =  reslog2.transitaire
            log2.Mt_ded_dh =  reslog2.Mt_ded_dh
            log2.date_ld =  reslog2.date_ld
            log2.date_lc =  reslog2.date_lc
            log2.litige =  reslog2.litige
            log2.class_litige =  reslog2.class_litige           
            log2.date_validation_e3 = datetime.now()
            log2.delai_e3 = (log2.date_validation_e3.day - log2.date_validation_e2.day)+1
            if 'btn_submit' in request.POST:
                log2.etape+=1
            log2.save()
            
            

            return redirect('general_db')

    context={'form': form}
    return render(request, 'base/respo_log2_add.html', context)
def addlog2(request, pk):
    
    form = Rl2Form()
    log2 = GeneralDTable.objects.get(id=pk)
    

    if request.POST:
        form = Rl2Form(request.POST)
        if form.is_valid():
            reslog2 =form.save(commit=False)     
            
            log2.date_pickup =  reslog2.date_pickup
            log2.freightforward =  reslog2.freightforward
            log2.mode_trans =  reslog2.mode_trans
            log2.date_AM =  reslog2.date_AM
            log2.transitaire =  reslog2.transitaire
            log2.Mt_ded_dh =  reslog2.Mt_ded_dh
            log2.date_ld =  reslog2.date_ld
            log2.date_lc =  reslog2.date_lc
            log2.litige =  reslog2.litige
            log2.class_litige =  reslog2.class_litige           
            log2.date_validation_e3 = datetime.now()
            log2.delai_e3 = (log2.date_validation_e3.day - log2.date_validation_e2.day) + 1
            if 'btn_submit' in request.POST:
                log2.etape+=1
            log2.save()
            
            

            return redirect('general_db')

    context={'form': form}
    return render(request, 'base/respo_log2_add.html', context)

@login_required(login_url='/login')
def updatefin(request, pk):
    

    fin = GeneralDTable.objects.get(id=pk)
    form = ResFin(instance=fin)

   

    if request.POST:
        form = ResFin(request.POST, instance=fin)
        if form.is_valid():
            resfin =form.save(commit=False)     
            
            fin.date_capf =  resfin.date_capf
            fin.date_capp =  resfin.date_capp
            fin.date_validation_e4 = datetime.now()
            fin.delai_e4 = (fin.date_validation_e4.day - fin.date_validation_e3.day) + 1
            if 'btn_submit' in request.POST:
                fin.etape+=1
            fin.save()
            
            return redirect('general_db')

    context={'form': form}
    return render(request, 'base/respo_fin_add.html', context)
def addfin(request, pk):
    

    form = ResFin()
    fin = GeneralDTable.objects.get(id=pk)

   

    if request.POST:
        form = ResFin(request.POST)
        if form.is_valid():
            resfin =form.save(commit=False)     
            
            fin.date_capf =  resfin.date_capf
            fin.date_capp =  resfin.date_capp
            fin.date_validation_e4 = datetime.now()
            fin.delai_e4 = (fin.date_validation_e4.day - fin.date_validation_e3.day) + 1
            if 'btn_submit' in request.POST:
                fin.etape+=1
            fin.save()
            
            return redirect('general_db')

    context={'form': form}
    return render(request, 'base/respo_fin_add.html', context)

@login_required(login_url='/login')
def updateinfo(request, pk):    
    inf = GeneralDTable.objects.get(id=pk)
    Infform = ResInf(instance = inf )
    
   
   

    if request.POST:
        Infform = ResInf(request.POST, instance=inf)
        if Infform.is_valid():
            resinf = Infform.save(commit=False)     
            
            inf.date_cacrs =  resinf.date_cacrs
          
            inf.date_validation_e5 = datetime.now()
            inf.delai_e5 = (inf.date_validation_e5.day - inf.date_validation_e4.day) + 1
            if 'btn_submit' in request.POST:
                inf.etape+=1
            inf.save()


            
            
        

            return redirect('general_db')

    context={'Infform': Infform }
    return render(request, 'base/respo_info_add.html', context)
def addinfo(request, pk):
    
    Infform = ResInf()
    inf = GeneralDTable.objects.get(id=pk)
    
   
   

    if request.POST:
        Infform = ResInf(request.POST)
        if Infform.is_valid():
            resinf = Infform.save(commit=False)     
            
            inf.date_cacrs =  resinf.date_cacrs
          
            inf.date_validation_e5 = datetime.now()
            inf.delai_e5 = (inf.date_validation_e5.day - inf.date_validation_e4.day) + 1
            if 'btn_submit' in request.POST:
                inf.etape+=1
            inf.save()


            
            
        

            return redirect('general_db')

    context={'Infform': Infform }
    return render(request, 'base/respo_info_add.html', context)

def add_admin_table(request):
    return render(request, 'base/createEtape.html')
          
def export_general_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="general.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Genral Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['N Dossier','Fournisseur','Pays','Nom','Client',
    'Date du validation des conditions Logistiques','Date Validation E1', 
    'Statut Importation','Date transmission de la commande au service logistique','Code Fournisseur Sage','Reference bon de commande Sage','Catégorie commande','Date Confirmation de commande Fournisseur','Numero FP','Date FP',
    'Pays D\'origine','Incoterm','Pays Prelevement','Montant Devises','Devise','Mode Payement','Delai de livraison',
    'Execution condition payment','Date Prevu Pickup Fournisseur','Date Prevu Arrivee au maroc','Date Validation E2','Date PickUp','FreightForward','Mode Transport','Date Arrivee Maroc','Transiter',
    'Montant dedouanement dh','Date livraison Depot','Date livraison client','Litige','Classe Litige','Date Validation E3',
    'Date clôture Administrative du Payement Fournisseur','Date clôture administrative du Payement des Partenaires','Date Validation E4','Date Clôture Administrative du Cout de Revient Sage','Date Validation E5' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = GeneralDTable.objects.all().values_list('n_Dossier','fournisseur','pays','nom','client','date_VCL','date_validation_e1', 
     'statut_Imp','date_TCS','code_Four_Sage','ref_Bon_Cmd_Sage','cat_Cmd','date_CCF','n_FP','date_FP','pays_Origine','incoterm','pays_Prt','montant_Dev','devise','mode_Pay',
     'delai_Liv','Exec_Co_Pay','date_PPF','date_PAM','date_validation_e2','date_pickup','freightforward','mode_trans',
     'date_AM','transitaire','Mt_ded_dh','date_ld','date_lc','litige','class_litige','date_validation_e3','date_capf','date_capp','date_validation_e4', 
     'date_cacrs','date_validation_e5')
    print(rows)
    rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime) else x for x in row] for row in rows ]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

def export_dossier_xls(request, pk):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Dossier.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Dossier Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['N Dossier','Fournisseur','Pays','Nom','Client',
    'Date du validation des conditions Logistiques','Date Validation E1', 
    'Statut Importation','Date transmission de la commande au service logistique','Code Fournisseur Sage','Reference bon de commande Sage','Catégorie commande','Date Confirmation de commande Fournisseur','Numero FP','Date FP',
    'Pays D\'origine','Incoterm','Pays Prelevement','Montant Devises','Devise','Mode Payement','Delai de livraison',
    'Execution condition payment','Date Prevu Pickup Fournisseur','Date Prevu Arrivee au maroc','Date Validation E2','Date PickUp','FreightForward','Mode Transport','Date Arrivee Maroc','Transiter',
    'Montant dedouanement dh','Date livraison Depot','Date livraison client','Litige','Classe Litige','Date Validation E3',
    'Date clôture Administrative du Payement Fournisseur','Date clôture administrative du Payement des Partenaires','Date Validation E4','Date Clôture Administrative du Cout de Revient Sage','Date Validation E5' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    dossier = GeneralDTable.objects.values_list('n_Dossier','fournisseur','pays','nom','client','date_VCL','date_validation_e1', 
     'statut_Imp','date_TCS','code_Four_Sage','ref_Bon_Cmd_Sage','cat_Cmd','date_CCF','n_FP','date_FP','pays_Origine','incoterm','pays_Prt','montant_Dev','devise','mode_Pay',
     'delai_Liv','Exec_Co_Pay','date_PPF','date_PAM','date_validation_e2','date_pickup','freightforward','mode_trans',
     'date_AM','transitaire','Mt_ded_dh','date_ld','date_lc','litige','class_litige','date_validation_e3','date_capf','date_capp','date_validation_e4', 
     'date_cacrs','date_validation_e5').get(id=pk)   
  
    row_num += 1
    for col_num in range(len(dossier)):
       

        ws.write(row_num, col_num, str(dossier[col_num]), font_style)

   
    wb.save(response)




    return response

@login_required(login_url='/login')
def General_db(request):
    general_datable_1 = GeneralDTable.objects.filter(etape = request.user.etape).values()
    general_datable_2 = GeneralDTable.objects.exclude(etape = request.user.etape).values().order_by('etape')

 
    general_datable  = []

    for x in general_datable_1:
        general_datable.append(x)
    for x in general_datable_2:
        general_datable.append(x)
    
    context = {'general_datable' : general_datable , 'nombre': len(general_datable), 'general_datable_1':general_datable_1 } 
    return render(request, 'base/general.html', context)