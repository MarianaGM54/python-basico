menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

option = input(menu)

if option == '1':
    pesos = float(input('cuantos pesos colombianos tienes?: '))
    dollar_value = 5000
    dollars = str(pesos / dollar_value)
    print('Tienes $' + dollars + ' dolares')
elif option == '2':
    pesos = float(input('cuantos pesos argentinos tienes?: '))
    dollar_value = 167
    dollars = str(pesos / dollar_value)
    print('Tienes $' + dollars + ' dolares')
elif option == '3':
    pesos = float(input('cuantos pesos mexicanos tienes?: '))
    dollar_value = 19
    dollars = str(pesos / dollar_value)
    print('Tienes $' + dollars + ' dolares')
else:
    print('ingresa una opcion correcta, por favor')


