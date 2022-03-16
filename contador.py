#Desenvolver um script que imprima na tela todos os números de 1 até 100, com as seguintes regras:

#Se o número for divisível por 3, deve ser impressa a string 'Ruby'
#Se o número for divisível por 5, deve ser impressa a string 'Python'
#Se o número for divisível por 3 e 5, deve ser impressa a string 'Py-Ruby'
#Nos outros casos, o número deve ser impresso como o próprio número

for c in range(1, 101):
    if c % 3 == 0:
        print(c, ' => Ruby')
        print("=" * 15)

    elif c % 5 == 0:
        print(c, ' => Python')
        print("=" * 15)

    if c % 3 == 0 == c % 5 == 0:
        print(c, ' => Py-Ruby')
        print("=" * 15)

    elif c % 3 != 0 and c % 5 != 0:
        print(c, ' => Não é divisivel por 3 e 5')
        print("=" * 15)
    
