import requests

_base_url = "https://api.cryptowat.ch/markets"

'''
Esta función devuelve una lista de diccionarios con la información de cada 
exchange y par disponible en la API de CryptoWatch.
Parámetros:
    None    
Retorno:
    listado_exchange: lista de exchange disponible en la API de CryptoWatch.
'''
def consulta_mercados():
    response = requests.get(_base_url)
    listado_exchange = response.json()['result']
    return listado_exchange

'''
Esta función devuelve una lista con los pares de intercambio que posee un exchange.
Parámetros:
    exchange_consultado: exchange del que se quiere conocer los pares de intercambio.
    listado_exchange: lista de exchange disponible en la API de CryptoWatch.    
Retorno:
    listado_exchange: lista de exchange disponible en la API de CryptoWatch.  
'''
def consulta_pares_intercambios( exchange_consultado, listado_exchange= None):
    pairs_posible = []
    if not listado_exchange:
        listado_exchange = consulta_mercados()
    for exchange in listado_exchange:
        if exchange['pair'] and exchange['exchange'] == exchange_consultado and \
                exchange['pair'] not in pairs_posible:
            pairs_posible.append(exchange['pair'])
    return pairs_posible

'''
Esta función devuelve una lista con los exchanges que poseen un par de intercambio y su valor. 
parámetros:
    intercambio: par de intercambio que se quiere conocer los exchanges y su valor.
    listado_exchange: lista de exchange disponible en la API de CryptoWatch.
Retorno:
    listado_precios: lista de precios/exchanges de un par de intercambio.
'''
def consulta_mejor_par_intercambio( intercambio, listado_exchange= None):
    listado_exchange_con_btceur = []
    if not listado_exchange:
        listado_exchange = consulta_mercados()
    for exchange in listado_exchange:
        if exchange['pair'] == intercambio and exchange[
            'active'] == True:
            print(exchange['exchange'], end='; ')
            listado_exchange_con_btceur.append(exchange)

    listado_precios = []
    for exchange in listado_exchange_con_btceur:
        response = requests.get(
            '{}/{}/{}/price'.format(_base_url, exchange['exchange'],
                                    intercambio))
        aux = response.json()['result']
        aux['exchange'] = exchange['exchange']
        listado_precios.append(aux)
    return listado_precios