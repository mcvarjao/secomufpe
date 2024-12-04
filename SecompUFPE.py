# CALCULADORA 

operacao = input('Escreva a opereção para a calculadora realizar: ')

if operacao == 'soma':
    elemento1 = int(input('Elemento 1: '))
    elemento2 = int(input('Elemento 2: '))

    soma = elemento1 + elemento2
    print(str(elemento1) + ' + ' + str(elemento2) + ' = ' + str(soma))

elif operacao == 'subtracao': 
    elemento1 = int(input('Elemento 1: '))
    elemento2 = int(input('Elemento 2: '))

    subtracao = elemento1 - elemento2
    print(str(elemento1) + ' - ' + str(elemento2) + ' = ' + str(subtracao))

elif operacao == 'multiplicacao': 
    elemento1 = int(input('Elemento 1: '))
    elemento2 = int(input('Elemento 2: '))

    multiplicacao = elemento1 - elemento2
    print(str(elemento1) + ' * ' + str(elemento2) + ' = ' + str(multiplicacao))

elif operacao == 'divisao': 
    elemento1 = int(input('Elemento 1: '))
    elemento2 = int(input('Elemento 2: '))

    if elemento2 == 0:
        print('Não pode dividir por zero!')
    else:
        divisao = elemento1 / elemento2
        print(str(elemento1) + ' / ' + str(elemento2) + ' = ' + str(divisao))

elif operacao == 'fatorial': 
    elemento1 = int(input('Elemento 1: '))

    fatorial = 1 
    for numero in range(1, elemento1):
        fatorial = fatorial * numero
    print(str(elemento1) + '! = ' + str(fatorial))





# LAÇOS DE REPETIÇÃO

for numero in range(10):
    print(numero)


numero = 0 
while (numero <10): 
    print(numero)
    numero = numero + 1     

soma = 0 
numero = 0 
while (numero <10): 
    soma = soma + numero
    numero = numero + 1
    print(soma)
print('Terminou tudo', soma)



# # DESCOBRINDO SE O NÚMERO É PRIMO:

primo = input('Digite um número ')
Eh_primo = True

for numero in range(1,primo): 
    if (primo % numero == 0):
        Eh_primo = False
if Eh_primo: 
    print(primo, 'é um número primo')
else: 
    print(primo, 'não é primo.')

   