# numeros = []
#
# for i in range(5):
#     n = int(input('Digite um número: '))
#     numeros.append(n)
# print(numeros)

# numeros = []
#
# for i in range(5):
#     n = int(input('Digite um número: '))
#     numeros.append(n)
#
# print(f'O maior número digitado foi {max(numeros)}')
# print(f'O menor número digitado foi {min(numeros)}')
# print(f'A soma entre os números digitados foi {sum(numeros)}')


# nomes = ['marcio','pedro','juliana','otavio','fernanda','talita','fabiana','rogerio','marcos','beatriz']
#
# pesquisa = str(input('Digite um nome a ser procurado: '))
#
# if pesquisa in nomes:
#     print(f'O nome {pesquisa} foi encontrado!')
# else:
#     print('Nome não encontrado. Tente novamente!')


# n = [5, 9, 1, 3, 4, 5, 8, 3, 9, 7, 3, 5, 1, 3, 8,8,3,9,1,3,8,1,3,8,7,2,3,9,7,1,2,6,98,7,6,1,3,5,4,8]
#
#
# valor = int(input('Qual valor deseja conferir? '))
# print(f'O valor {valor} apareceu {n.count(valor)} vezes')



import random
# numbers = []
#
# for i in range(10):
#     number =random.randint(1,1000)
#     numbers.append(number)
#
# #print dos numeros em ordem crescente
# numbers.sort()
# print(numbers)
#
# #print dos numeros em ordem decrescente
# numbers.sort(reverse = True)
# print(numbers)


numeros = []
numerosPares = []

for i in range(20):
    num =random.randint(1,30)
    numeros.append(num)

print(f'Lista gerada {numeros}')

for item in numeros:
    if item % 2 == 0:
        numerosPares.append(item)
print(f'Lista somente com os números pares {numerosPares}')

