from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato


# Create your views here.

def login(request):
    view = render(request, 'accounts/login.html', {'titulo': 'login'})

    if request.method != 'POST':
        # messages.info(request, 'nada postado')
        return view

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    if not usuario or not senha:
        messages.error(request, 'Preencha todos os campos')
        return view

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usário não encontrado')
        return view
    else:
        auth.login(request, user)
        messages.success(request, 'Logado com sucesso')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')


def cadastro(request):
    # messages.success(request, 'TESTE')
    # print(request.POST)

    view = render(request, 'accounts/cadastro.html', {'titulo': 'cadastro login'})

    if request.method != 'POST':
        # messages.info(request, 'nada postado')
        return view

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Preencha todos os campos')
        return view

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return view

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter ao menos 6 caracteres')
        return view

    if len(usuario) < 6:
        messages.error(request, 'Usuário precisa ter ao menos 6 caracteres')
        return view

    if senha != senha2:
        messages.error(request, 'Senhas não conferem')
        return view

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já cadastrado')
        return view

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já cadastrado')
        return view

    messages.success(request, 'Usuário cadastrado com sucesso ! Faça o login')

    user = User.objects.create_user(username=usuario, password=senha, email=email, first_name=nome, last_name=sobrenome)
    user.save()

    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    form = FormContato()
    view = render(request, 'accounts/dashboard.html', {'titulo': 'dashboard', 'form': form})

    if request.method != 'POST':
        # messages.info(request, 'nada postado')
        return view

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        form = FormContato(request.POST)
        messages.error(request, 'Erro no formulário')
        return render(request, 'accounts/dashboard.html', {'titulo': 'dashboard', 'form': form})

    descricao = request.POST.get('descricao')
    if len(descricao) < 5:
        form = FormContato(request.POST)
        messages.error(request, 'Erro na descricao')
        return render(request, 'accounts/dashboard.html', {'titulo': 'dashboard', 'form': form})

    form.save()
    messages.success(request, f'{request.POST.get("nome")} Salvo com sucesso')
    return redirect('dashboard')
