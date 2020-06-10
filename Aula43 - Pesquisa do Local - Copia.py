#Aula 30 - Requisições HTTP em Python
#HMAP - 22/03/2020
#Aula 36 - Obtendo Clima Atual
#HMAP - 18/04/2020
#Módulo da requisição
import requests
#Dicionário da requisição
import json
#Módulo para imprimir o dicionário
import pprint
#
from datetime import date

import urllib.parse

accuweatherAPIKey = '3I2Ai2Zf5bJ9uT1Skx3WM0sAKwvpLLxl'
mapboxToken = "pk.eyJ1IjoiaGVucmlxdWVtYXRoZXVzIiwiYSI6ImNrOTc4dTd1YzA4YmYzZG5vanAyZ2k5bTgifQ.CAuXnH7xGiqKgbANaPGFuA"
dias_semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

def pegarCoordenadas():
    r = requests.get('http://www.geoplugin.net/json.gp')
    #Verificação de localização, baseado na numeração de erro 200
    if (r.status_code != 200):
        print('Não foi possível obter a localização.')
        return None
    else:
        try:
            #print(r.text) - dados da requisição http
            localizacao = json.loads(r.text)
            coordenadas = {}
            coordenadas['lat'] = localizacao['geoplugin_latitude']
            coordenadas['long'] = localizacao['geoplugin_longitude']
            return coordenadas
        except:
            return None
    
def pegarCodigoLocal(lat,long):
    LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + accuweatherAPIKey + "&q=" + lat + "%2C" + long + "&language=pt-br"
    
    r = requests.get(LocationAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter a localização.')
        return None
    else:
        try:
            locationResponse = json.loads(r.text)
            infoLocal = {}
            infoLocal['nomeLocal'] = locationResponse['LocalizedName'] + "," + locationResponse['AdministrativeArea']['LocalizedName'] + "." + locationResponse['Country']['LocalizedName']
            infoLocal['codigoLocal'] = locationResponse['Key']
            return infoLocal
        except:
            return None

def pegarTempoAgora(codigoLocal, nomeLocal):
    CurrentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" + codigoLocal + "?apikey=" + accuweatherAPIKey + "&language=pt-br"

    r = requests.get(CurrentConditionsAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter o clima atual.')
        return None
    else:
        try:
            CurrentConditionsResponse = json.loads(r.text)
            infoClima = {}
            infoClima['textoClima'] = CurrentConditionsResponse[0]['WeatherText']
            infoClima['temperatura'] = CurrentConditionsResponse[0]['Temperature']['Metric']['Value']
            infoClima['nomeLocal'] = nomeLocal
            return infoClima
        except:
            return None

def pegarPrevisao5Dias(codigoLocal):
    DailyAPIUrl = " http://dataservice.accuweather.com/forecasts/v1/daily/5day/" + codigoLocal + "?apikey=" + accuweatherAPIKey + "&language=pt-br&metric=true"

    r = requests.get(DailyAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter o clima atual.')
        return None
    else:
        try:
            DailyResponse = json.loads(r.text)
            infoClima5Dias = []
            for dia in DailyResponse['DailyForecasts']:
                climaDia = {}
                climaDia['max']=dia['Temperature']['Maximum']['Value']
                climaDia['min']=dia['Temperature']['Minimum']['Value']
                climaDia['clima']=dia['Day']['IconPhrase']
                diaSemana = int(date.fromtimestamp(dia['EpochDate']).strftime("%w"))
                climaDia['dia']=dias_semana[diaSemana]
                infoClima5Dias.append(climaDia)
            return infoClima5Dias
        except:
            return None

##Início do código

def mostrarPrevisao(lat, long):
    try:
        local = pegarCodigoLocal(lat, long)
        climaAtual = pegarTempoAgora(local['codigoLocal'], local['nomeLocal'])
        print('\nClima atual em: ' + climaAtual['nomeLocal'])
        print(climaAtual['textoClima'])
        print('Temperatura: ' + str(climaAtual['temperatura']) + "\xb0" + "C")
    except:
        print('Erro ao obter o clima atual.')

    opcao = input('\nDeseja ver a previsão para os próximos dias? (s ou n)').lower()

    if opcao == "s":
        print('\nClima para hoje e para os próximos dias: \n')
        try:
            previsao5Dias = pegarPrevisao5Dias(local['codigoLocal'])
            for dia in previsao5Dias:
                print(dia['dia'])
                print('Mínima: ' + str(dia['min']) + "\xb0" + "C")
                print('Máxima: ' + str(dia['max']) + "\xb0" + "C")
                print('Clima: ' + dia['clima'])
                print('----------------------------------------')
        except:
            print('Erro ao obter a previsão para os próximos dias.')

def pesquisarLocal(local):
    _local = urllib.parse.quote(local)
    mapboxGeocodeUrl = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + _local +".json?access_token=" + mapboxToken

    r = requests.get(mapboxGeocodeUrl)
    if (r.status_code != 200):
        print('Não foi possível obter o clima atual.')
        return None
    else:
        try:
            MapboxResponse = json.loads(r.text)
            coordenadas = {}
            coordenadas['long'] = str(MapboxResponse['features'][0]['geometry']['coordinates'][0])
            coordenadas['lat'] = str(MapboxResponse['features'][0]['geometry']['coordinates'][1])
            return coordenadas
        except:
            print('Erro na pesquisa de local.')
try:
    coordenadas = pegarCoordenadas()
    mostrarPrevisao(coordenadas['lat'],coordenadas['long'])

    continuar = "s"

    while continuar == "s":
        continuar = input("\nDeseja consultar a previsão de outro local? (s ou n)").lower()
        if continuar != "s":
            break
        local = input('Digite a cidade e o Estado: ')
        try:
            coordenadas = pesquisarLocal(local)
            mostrarPrevisao(coordenadas['lat'], coordenadas['long'])
        except:
            print('Não foi possível obter a previsão para este local.')
except:
    print('Erro ao processar a solicitação. Entre em contato com o suporte')