
def tamanho_da_lista():
    print(' Tamanho da lista ')
    print(' ---------------- ')
    t = int(input(' Tamanho: '))
    return t

def criar_lista(tamanho):
    print(' Criar  uma lista ')
    print(' ---------------- ')
    lista = []
    i =0
    while i < tamanho:
        n = int(input('numero: '))
        lista.append(n)
        i+=1
    return lista

def imprimir(lista):
    print(' imprimir a lista ')
    print(' ---------------- ')
    for i in lista:
        print(f'Elemento: {i}')

def imprimir_pares(lista):
    print('*- IMPRIMIR ELEMENTOS PARES DA LISTA -*')
    for i in lista:
        if i%2 == 0:
            print(f'Elemento: {i}')

def separar_pares(lista):
    print('*- Separar os ELEMENTOS PARES da LISTA -*')
    lista_pares = []
    for i in lista:
        if i%2 == 0:
            lista_pares.append(i)
            return lista_pares
        
def obter_numero():
    print(' *- OBTER NUMERO -*')
    n = int(input('Numero:'))
    return n

def verificar_ocorrencias(n,lista):
    print('*- VERIFICAR OCORRENCIAS -*')
    cont=0
    for i in lista:
        if i == n:
            cont+=1
        return cont


def principal():
    print(' Prinipal ')
    print(' ---------------- ')
    tamanho = tamanho_da_lista()
    lista = criar_lista(tamanho)
    imprimir(lista)
    print('===================')
    imprimir_pares(lista)
    lista_pares = separar_pares(lista)
    imprimir(lista_pares)
    print('====================')
    n = obter_numero()
    qtde = verificar_ocorrencias(n, lista)
    print(f'Ocorrencias:{qtde}')

principal()