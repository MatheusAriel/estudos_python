from django.shortcuts import render, get_object_or_404, Http404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


# Create your views here.

def index(request):
    # messages.add_message(request, messages.ERROR, 'ocorreu um erro')

    contatos = Contato.objects.all().order_by('-nome').filter(
        mostrar=True,
        # nome__contains='Bryan'
    )
    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos,
        'titulo': 'Agenda'
    })


def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id, mostrar=True)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato,
        'titulo': f'Ver contato - {contato.nome}'
    })


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        # raise Http404()
        messages.add_message(request, messages.ERROR, 'Busca não pode ficar vazio')
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')

    # contatos = Contato.objects.all().order_by('-nome').filter(
    #     Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
    #     mostrar=True,
    # )

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    # print(contatos.query)
    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    messages.add_message(request, messages.SUCCESS, 'Busca realizada com sucesso')

    return render(request, 'contatos/busca.html', {
        'contatos': contatos,
        'titulo': 'Agenda'
    })
