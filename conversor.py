def converter(type_pesos, dollar_value):
    pesos = float(input('cuantos pesos ' + type_pesos + ' tienes?: '))
    dollars = str(pesos / dollar_value)
    print('Tienes $' + dollars + ' dolares')



menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

option = int(input(menu))

if option == 1:
    converter('colombianos', 5000)
elif option == 2:
    converter('argentinos', 167)
elif option == 3:
    converter('mexicanos', 19)
else:
    print('ingresa una opcion correcta, por favor')


