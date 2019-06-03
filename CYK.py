

def ler_arquivo(path):

    s=[]
    
    with open(path, 'r') as file:
        for r in file.readlines():
            s.append(r.replace('\n', ''))

    gramatica = {}

    for r in s:
        gramatica[r[0]] = r.split('>')[1].split('|')

    return gramatica


def __gerar_lista(palavra, gramatica):
    l = []
    for letra in palavra:
        l.append(letra)

    lista =[]
    lista.append(l)
    nova_lista = []

    for caracter in lista[0]:
        for prod in gramatica:
            if caracter in gramatica[prod]:
                nova_lista.append(prod)

    if(len(nova_lista) < len(lista[0])):
        return None
    else:        
        lista.append(nova_lista)
        return lista  


def __gerar_matriz(palavra, gramatica):
    matriz = __gerar_lista(palavra, gramatica)
    if(matriz != None):
        i = len(matriz[1])
        while(i > 0):
            nova_lista = []
            for j in range(i-1):
                nova_lista.append(" ")
            if " " in nova_lista:
                matriz.append(nova_lista)
            i -= 1
        return matriz
    else:
        return None


def algoritmo_CYK(palavra, gramatica):
    matriz = __gerar_matriz(palavra, gramatica)
    if matriz != None:
        for a in range(0, (len(matriz[1])-1), 1):
            string_parcial = matriz[1][a]+matriz[1][a+1]
            for i in gramatica:
                if string_parcial in gramatica[i]:
                    if matriz[2][a] == ' ':
                        matriz[2][a] = i
                    else:
                        matriz[2][a] += i

        x = 2
        y = 1
        for i in range(3,len(matriz)-1,1):
            for j in range(len(matriz[i])-1):
                for k in range(i-1):
                    a = matriz[k+1][j]
                    b = matriz[x][y]
                    if a != ' ' and b != ' ':
                        matriz[i][j] = __combinacoes(a, b, gramatica)

                    x -= 1
                    y += 1
                x = i - 1
                y = j + 2
            x = i
            y = 1
            
        x = len(matriz) - 2
        y = 1
        vertical = 1

        while(vertical < len(matriz)-1):
            if vertical == 3:
                print(vertical)
            a = matriz[vertical][0]
            b = matriz[x][y]
            if a != ' ' and b != ' ':
                matriz[len(matriz)-1][0] = __combinacoes(a, b, gramatica)
            vertical += 1
            x -= 1
            y += 1

        if 'S' in matriz[len(matriz)-1]:
            return True
        else:
            return False
    else:
        return False


def __combinacoes(str1, str2, gramatica):
    return_ = ' '
    for i in str1:
        for j in str2:
            for k in gramatica:
                if(i+j) in gramatica[k]:
                    if return_ == ' ':
                        return_ = k
                    else:
                        return_ += k
    return return_

    


gram = ler_arquivo("gramatica.txt")

print(algoritmo_CYK("aaabbb", gram))


