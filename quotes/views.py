# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Quotes
from .forms import PostForm
import requests
from django.http import JsonResponse
import pandas as pd
from datetime import datetime, timedelta

# Função principal renderiza template
def quote_list(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            data_inicio = form.cleaned_data['dia_inicio']
            data_fim = form.cleaned_data['dia_fim']
            moeda = form.cleaned_data['moeda']
            print(data_inicio, data_fim, moeda)

            base_api_url = 'https://api.vatcomply.com/rates?base=USD'

            # Dados da API com os dias uteis selecionados
            resultados = chamada_urls_com_intervalo(base_api_url, data_inicio.strftime('%Y-%m-%d'), data_fim.strftime('%Y-%m-%d'))
        else:
            return redirect('quote_list')

    else:
        ultimos_5_dias_uteis = obter_data_5_dias_uteis_atras()

        # Parametros para chamar a série de dados na API
        base_api_url = 'https://api.vatcomply.com/rates?base=USD'
        # Obter o primeiro dia
        data_inicio = ultimos_5_dias_uteis[0].strftime('%Y-%m-%d')
        # Obter o último dia
        data_fim = ultimos_5_dias_uteis[-1].strftime('%Y-%m-%d')

        # Dados da API com os dias uteis selecionados
        resultados = chamada_urls_com_intervalo(base_api_url, data_inicio, data_fim)

        # Instanciando Form de seleção de dias e moedas
        form = PostForm()

        moeda = 'BRL'

    return render(request, 'quotes_list.html', {
        'form': form,
        'resultados': resultados,
        'moeda': moeda
    })

# Função para chamar serie de dados da API indicada
def chamada_urls_com_intervalo(base_url, data_inicial, data_final):
    resultados = []

    # Converte as datas de string para objetos datetime
    data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')
    data_final = datetime.strptime(data_final, '%Y-%m-%d')

    # Gera as datas no intervalo desejado
    datas_no_intervalo = [data_inicial + timedelta(days=n) for n in range((data_final - data_inicial).days + 1)]

    # Cria URLs com base nas datas geradas
    for data in datas_no_intervalo:
        url = f"{base_url}&date={data.strftime('%Y-%m-%d')}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Verifica se houve erros na resposta

            # Adiciona os dados da resposta à lista de resultados (apenas dias úteis)
            if response.json() not in resultados:
                resultados.append(response.json())

        except requests.exceptions.RequestException as e:
            # Lidar com erros de solicitação
            resultados.append({'error': str(e)})

    return resultados

# Função para obter 5 dias uteis para trás a partir da data atual
def obter_data_5_dias_uteis_atras():
    # Obter a data atual
    data_atual = datetime.now()

    # Subtrair 9 dias da data atual para obter os últimos 10 dias
    data_inicial = data_atual - timedelta(days=9)

    # Criar um objeto DataFrame com uma única coluna de datas começando da data atual
    df = pd.DataFrame({'data': pd.date_range(start=data_inicial, end=data_atual)})

    # Adicionar uma coluna indicando se cada data é um dia útil
    df['dia_util'] = df['data'].apply(lambda x: x.weekday() < 5)

    # Filtrar para obter os últimos 5 dias úteis
    ultimos_5_dias_uteis = df[df['dia_util']].tail(5)['data']

    return ultimos_5_dias_uteis.tolist()