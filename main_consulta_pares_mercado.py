from utils import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listado_exchange = consulta_mercados()
    print('Listado de pair disponibles coinbase-pro')
    pairs_posible = consulta_pares_intercambios('coinbase-pro',listado_exchange)
    print(pairs_posible)
    print(len(pairs_posible))
    print('Listado de pair disponibles binance')
    pairs_posible = consulta_pares_intercambios('binance',
                                                listado_exchange)
    print(pairs_posible)
    print(len(pairs_posible))
    print('Listado de pair disponibles Liquid')
    pairs_posible = consulta_pares_intercambios('liquid',
                                                listado_exchange)
    print(pairs_posible)
    print(len(pairs_posible))


