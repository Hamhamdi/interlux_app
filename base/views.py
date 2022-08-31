import email
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from base.form import RegistrationForm, AccountAuthenticationForm, ResCa, Rl1Form, Rl2Form, ResInf, ResFin

# from base.form import RoleForm
from .models import RL1, RL2, Base, RchA, RespoFin, RespoINf
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
            email = request.POST['email']
            role = request.POST['role']
            password = request.POST['password']
            user = authenticate(email=email,role =role, password=password)
            if user:

                login(request, user)

            # try:
                # user = Base.objects.get(email=email , role=role)
                user_role = user.role
                print(user.username)

                if user_role == "chargee affaire":
                    return redirect('respo_ca', user.id)
                elif user_role == "responsable informatique":
                    return redirect('respo_info', user.id)
                elif user_role == "responsable financier":
                    return redirect('respo_fin', user.id)
                elif user_role == "responsable logistique1":
                    return redirect('respo_log1', user.id)
                elif user_role == "responsable logistique2":
                    return redirect('respo_log2', user.id)
                
               
            # except:

            #     form = AccountAuthenticationForm()
                 
            #     context['login_form'] = form
            #     return render(request, 'base/login.html', context)

    else:
       form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'base/login.html', context)



# def login_view(request):

# 	context = {}

# 	user = request.user
# 	if user.is_authenticated: 
# 		return redirect("home")

# 	if request.POST:
# 		form = AccountAuthenticationForm(request.POST)
# 		if form.is_valid():
# 			email = request.POST['email']
# 			password = request.POST['password']
# 			user = authenticate(email=email, password=password)

# 			if user:
# 				login(request, user)
# 				return redirect("home")

# 	else:
# 		form = AccountAuthenticationForm()

# 	context['login_form'] = form

# 	# print(form)
# 	return render(request, "account/login.html", context)
















































def registerPage(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            role = form.cleaned_data.get('role')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(
            email=email, role=role, password=raw_password)
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

def rl1Page(request, pk):
    try:
        user = RL1.objects.get(id=pk)
    except:
         return HttpResponse('pas de user')


    user_log1 = RL1.objects.all()
    context = {'user' : user, 'user_log1':user_log1}

    if request.POST:
        form = Rl1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['rl1_form'] = form
    else:  # GET request
        form = Rl1Form()
        context['rl1_form'] = form
    return render(request, 'base/respo_log1.html', context)

def rl2Page(request, pk):
    user = RL2.objects.get(id=pk)

    context = {'user' : user}

    if request.POST:
        form = Rl2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['rl2_form'] = form
    else:  # GET request
        form = Rl2Form()
        context['rl2_form'] = form
    return render(request, 'base/respo_log2.html', context)


def rinfoPage(request, pk):
    user = RespoINf.objects.get(id=pk)
    context = {'user' : user}

    if request.POST:
        form = ResInf(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['rinf_form'] = form
    else:  # GET request
        form = ResInf()
        context['rinf_form'] = form
    return render(request, 'base/respo_info.html', context)


def rfinPage(request, pk):
    user = RespoFin.objects.get(id=pk)
    context = {'user' : user}    

    if request.POST:
        form = ResFin(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['rfin_form'] = form
    else:  # GET request
        form = ResFin()
        context['rfin_form'] = form
    return render(request, 'base/respo_fin.html', context)

def RCa(request, pk):
    user = RchA.objects.get(id=pk)
    user_ca = RchA.objects.all()

    context = {'user' : user, 'user_ca':user_ca}

    if request.POST:
        form = ResCa(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['rca_form'] = form
    else:  # GET request
        form = ResCa()

    context['rca_form'] = form
    return render(request, 'base/respo_ca.html', context)

# def rCaPage(request, pk):
#     user = RchA.objects.get(id=pk)
#     context = {'user' : user}

#     return render(request, 'base/respo_ca.html', context)


