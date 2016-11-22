from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, logout, login as authlogin
from django.http.response import HttpResponse
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required
from .models import relacao, objeto, restricao, casos


# Create your views here.

def caso(request):
    context_dict = {}
    relacaoList = relacao.objects.order_by('-nome')
    objetosList = objeto.objects.order_by('-nome')
    restricaoList = restricao.objects.order_by('-distancia')

    context_dict['relacoes'] = relacaoList
    context_dict['objetos'] = objetosList
    context_dict['restricoes'] = restricaoList

    return render(request, 'pages/caso.html', context_dict)

def comparacao(request):
    peso = [0.2, 0.1, 0.2]
    if request.POST:
        objeto1 = request.POST.get('objeto1')
        relacao = request.POST.get('relacao')
        objeto2 = request.POST.get('objeto2')
        distancia = request.POST.get('distancia')
    novoCaso = [objeto1, relacao, objeto2, distancia]
    peso = [0.2, 0.1, 0.2]
    resultado = []
    def EhIgual(x, y):
        peso = 0
        if (x == y):
            peso = 0
        else:
            peso = 1
        return peso

    def distancia(peso, caso, novoProblema):
        pesoInstancias = []
        distancia = 0.0
        for i in range(0, len(peso)):
            pesoInstancias.append(EhIgual(caso[i], novoProblema[i]))
        for i in range(0, len(peso)):
            distancia += (peso[i] * pesoInstancias[i])
        distancia = distancia
        resultado = [caso, novoProblema, distancia]
        return resultado

    casolist = casos.objects.order_by('-id')
    for caso in casolist:
        velhoCaso = [caso.objeto1, caso.relacao, caso.objeto2, caso.distancia, caso.resultado, caso.plano_acao]
        resultado += distancia(peso,velhoCaso,novoCaso)

    return render(request, 'pages/comparacao.html', {"resultado": resultado})