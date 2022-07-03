from utils import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    intercambio_consultado = 'btceur'
    print(
        'Ahora buscamos todos los exchange con la opción de transformar BTC a EUR.')
    listado_precios = \
        consulta_mejor_par_intercambio(intercambio_consultado)
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



