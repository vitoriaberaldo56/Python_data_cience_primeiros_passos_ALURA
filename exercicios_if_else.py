#Exercicio 01
n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))

if n1 > n2:
    print(f'O primeiro número é maior: {n1}')
elif n2 > n1:
    print(f'O segundo número é maior: {n2}')
else: # Caso os números sejam iguais
    print('Os dois números são iguais.')


#Exercicio 02
#letra = str(input('Digite uma letra: ')).lower()
#vogais = 'aeiou'
#if letra in vogais:
 #   print('A letra é uma vogal')
#else:
 #   print('A letra é uma consoante')


#Exercicio 03
letra = input('Digite uma letra: ').lower()
vogais = 'aeiou'

if letra in vogais:
    print('A letra é uma vogal.')
else:
    print('A letra é uma consoante.')


#Exercicio 04
a1=int(input('Digite o preço médio do primeiro ano: '))
a2=int(input('Digite o preço médio do segundo ano: '))
a3=int(input('Digite o preço médio do terceiro ano: '))

if a1>a2 and a1>a3:
   print(f'O valor mais alto foi {a1}, no primeiro ano.')
elif a2>a1 and a2>a3:
    print(f'O valor mais alto foi {a2}, no segundo ano.')
else:
    print(f'O valor mais alto foi {a3}, no terceiro ano.')


#Exercicio 05
p1 = float(input('Digite o primeiro valor: '))
p2 = float(input('Digite o segundo valor: '))
p3 = float(input('Digite o terceiro valor: '))

if p1<p2 and p1<p3:
   print(f'O primeiro produto é mais barato, e custa R${p1}')
elif p2<p1 and p2<p3:
   print(f'O segundo produto é mais barato, e custa R${p2}')
else:
    print(f'O terceiro produto é mais barato, e custa R${p3}')


#Exercicio 06
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
lista = [n1,n2,n3]
lista.sort(reverse=True)

print(lista)


#Exercicio 07
t = str(input('Em qual turno você estuda? '))

if t == 'manha':
    print("Bom dia!")
elif t == 'tarde':
    print('Boa tarde!')
elif t == 'noite':
    print('Boa noite!')
else:
    print('Valor Inválido')

#Exercicio 08
n = int(input('Digite um número: '))

if n % 2 == 0:
    print(f'O número {n} é par')
else:
    print(f'o número {n} é ímpar')


#Exercicio 09
n = float(input('Digite um número: '))

if n//1 == n:
    print('Número inteiro')
else:
    print('Número decimal')

