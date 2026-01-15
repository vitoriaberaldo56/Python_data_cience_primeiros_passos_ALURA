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


# numeros = []
# numerosPares = []
#
# for i in range(20):
#     num =random.randint(1,30)
#     numeros.append(num)
#
# print(f'Lista gerada {numeros}')
#
# for item in numeros:
#     if item % 2 == 0:
#         numerosPares.append(item)
# print(f'Lista somente com os números pares {numerosPares}')

# listaNumeros = []
#
# n = int(input('Digite um número: '))
#
# while n != 0:
#     listaNumeros.append(n)
#     n = int(input('Digite um número: '))
#
#
# media = sum(listaNumeros) / len(listaNumeros)
#
# print('Tentativa correta! Segue abaixo:')
# print(f'Lista gerada: {listaNumeros}')
# print(f'Média dos números digitados: {media}')


# notas = [5.2,6.3,7.8,10,9,9.5,3.4,6,7,6.7,2,3,5,5.2]
# qtdInicial = len(notas)
#
# print(notas)
# for item in notas:
#     if item < 6:
#         notas.remove(item)
#
# qtdFinal = len(notas)
#
# print(f'Após remover as notas, a lista ficou como: {notas}')
# print(f'{qtdInicial - qtdFinal} notas foram removidas')

# from collections import Counter
#
# numeros = [1,2,2,3,3,3]
# contagem = Counter(numeros)
#
# print(contagem)

#
# listaCompras = []
#
# def menu():
#     print('=== MENU DE OPÇÕES ===\n'
#           '1 - Inserir Produto\n'
#           '2 - Excluir Produto\n'
#           '3 - Mostrar lista\n')
#
# def opcoes():
#     op = int(input('Digite a opção selecionada: '))
#
#     if op == 1: #inserir produtos
#         item = str(input('Digite o nome do Item que quer inserir: '))
#         listaCompras.append(item)
#
#     elif op == 2: #inserir produtos
#         item = str(input('Digite o item a ser removido'))
#         if item in listaCompras: #verifica se o produto existe na lista
#             listaCompras.remove(item)
#         else:
#             print('Item não encontrado.')
#     else:
#         print('Mostrando a lista de compras:')
#         print(listaCompras)
#
# menu()
# opcoes()
#
# def saudacao():
#     print('olá mundo')
#
# saudacao()
#
# aluno = {'nome':'joao',
#          'nota1': 7.5,
#          'nota2': 8.3,
#          'nota3': 9.5}
#
# media = aluno['nota1'] + aluno['nota2'] + aluno['nota3'] / 3
# print(f'Média das notas: {media:.2f}')

#
# alunos = {'aluno1': 'Otavio', 'media1': 7.8,
#           'aluno2': 'Julia', 'media2': 8.5,
#           'aluno3': 'Pedro', 'media3': 3.7,
#           'aluno4': 'Flavio', 'media4': 4.8,
#           'aluno5': 'Gustavo', 'media5': 5.7,
#           'aluno6': 'Mariana', 'media6': 9.0,
#           'aluno7': 'Carla', 'media7': 8.7
#           }
#
# notas = [] #lista que vai armazenar somente as notas medias
#
# for Nota in alunos.values(): #laco for que insere as notas na lista
#     if Nota >=6:
#         print(Nota)


palavra = str(input('Digite uma palavra'))

