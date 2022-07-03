import requests


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    base_url = "https://api.cryptowat.ch/markets"
    intercambio_consultado = 'btceur'
    response = requests.get(base_url)
    print('Ejemplo de obtención de un mercado.')
    print(response.json()['result'][0])
    listado_exchange = response.json()['result']
    listado_exchange_con_btceur = []
    print('-----------------------')
    print('-----------------------')
    print('-----------------------')
    print(
        'Ahora buscamos todos los exchange con la opción de transformar BTC a EUR.')
    for exchange in listado_exchange:
        if exchange['pair'] == intercambio_consultado and exchange[
            'active'] == True:
            print(exchange['exchange'], end='; ')
            listado_exchange_con_btceur.append(exchange)
    print('Un total de {}'.format(str(len(listado_exchange_con_btceur))))

    print('-----------------------')
    print('-----------------------')
    print('-----------------------')
    print('Ahora buscamos el precio más alto y el más barato.')
    print('Empezamos con un ejemplo')
    response = requests.get('{}/{}/{}/price'.format(base_url,
                                                    listado_exchange_con_btceur[
                                                        0][
                                                        'exchange'],
                                                    intercambio_consultado))
    print('Por ejemplo, en el exchange de ' + listado_exchange_con_btceur[0][
        'exchange'] +
          ' tenermos un precio de ' + str(response.json()['result']['price']))
    listado_precios = []
    for exchange in listado_exchange_con_btceur:
        response = requests.get(
            '{}/{}/{}/price'.format(base_url, exchange['exchange'],
                                    intercambio_consultado))
        aux = response.json()['result']
        aux['exchange'] = exchange['exchange']
        listado_precios.append(aux)

    listado_precios = sorted(listado_precios, key=lambda d: d['price'])

    print("El exchange que tiene el minimo valor es  {} - con: {}".format(
        listado_precios[0]['exchange'],
        str(listado_precios[0]['price'])))

    print("El exchange que tiene el minimo valor es  {} con: {}".format(
        listado_precios[-1]['exchange'],
        str(listado_precios[-1]['price'])))

    print('-----------------------')
    print('-----------------------')
    print('-----------------------')
    print('Listados de exchange')
    for i in listado_precios:
        print('{} , {}'.format(i['exchange'],
                               str(i['price'])))

    print('-----------------------')
    print('-----------------------')
    print('-----------------------')
    print('Listado de pair disponibles coinbase-pro')
    pairs_posible = []
    for exchange in listado_exchange:
        if exchange['pair'] and exchange['exchange'] == 'coinbase-pro' and \
                exchange['pair'] not in pairs_posible:
            pairs_posible.append(exchange['pair'])
    print(pairs_posible)
    print(len(pairs_posible))

    print('Listado de pair disponibles binance')
    pairs_posible = []
    for exchange in listado_exchange:
        if exchange['pair'] and exchange['exchange'] == 'binance' and exchange[
            'pair'] not in pairs_posible:
            pairs_posible.append(exchange['pair'])
    print(pairs_posible)
    print(len(pairs_posible))

    print('Listado de pair disponibles Liquid')
    pairs_posible = []
    for exchange in listado_exchange:
        if exchange['pair'] and exchange['exchange'] == 'liquid' and exchange[
            'pair'] not in pairs_posible:
            pairs_posible.append(exchange['pair'])
    print(pairs_posible)
    print(len(pairs_posible))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
