

def ler_arquivo(arquivo_texto):
    s=[]
    
    with open(arquivo_texto, 'r') as file:
        for r in file.readlines():
            s.append(r.replace('\n', ''))

    gramatica = {}

    for r in s:
        gramatica[r[0]] = r.split('>')[1].split('|')

    return gramatica


def gerar_matriz(palavra, gramatica):
    matriz = []
    linha = []
    celula = []
    for char in palavra:
        for item in gramatica:
            if char in gramatica[item]:
                celula.append(item)
        linha.append(celula)
        celula = []
    
    if(len(linha) == len(palavra)):
        matriz.append(linha)

        tamanho_total = len(linha)
        tamanho_linha = tamanho_total-1

        for i in range(tamanho_total-1):
            linha = []
            for j in range(tamanho_linha):
                linha.append([])
            tamanho_linha -= 1
            matriz.append(linha)

        #gerando a segunda linha da matriz

        for i in range(len(matriz[1])):
            for j in matriz[0][i]:
                for k in matriz[0][i+1]:
                    for y in gramatica:
                        if j+k in gramatica[y]:
                            matriz[1][i].append(y)
                        

        return matriz
    else:
        return None             


def Cyk(palavra, gramatica):
    matriz = gerar_matriz(palavra, gramatica)
    if matriz != None:
       
        x_vertical = 1
        y_vertical = 0
        x_diagonal = 0
        y_diagonal = 2
        x = 2
        y = 0
        vertical = matriz[x_vertical][y_vertical]
        diagonal = matriz[x_diagonal][y_diagonal]
        chegou_topo = False

        while(not(chegou_topo)):

            for v in vertical:
                for d in diagonal:
                    for g in gramatica:
                        concat = v+d
                        if concat in gramatica[g]:
                            matriz[x][y].append(g)  


            if x_vertical == 0:
                if x == len(matriz)-1:
                    chegou_topo = True
                    break
                if y+1 < len(matriz[x]):
                    y += 1
                    x_vertical = x-1
                    y_vertical = y
                    x_diagonal = 0
                    y_diagonal = y_vertical + x
                else:
                    x += 1
                    y = 0
                    x_vertical = x-1
                    y_vertical = 0
                    x_diagonal = 0
                    y_diagonal = x
            else:
                x_vertical -= 1
                x_diagonal += 1
                y_diagonal -= 1
            
            vertical = matriz[x_vertical][y_vertical]
            diagonal = matriz[x_diagonal][y_diagonal]

        if 'S' in matriz[len(matriz)-1][0]:
            for m in matriz:
                print(m)
            return True
        else:
            print("else interno")
            for m in matriz:
                print(m)
            return False
    else:
        for m in matriz:
            print(m)
        return False



gram = ler_arquivo("gramatica.txt")

#print(productions)
print(gram)

resultado = Cyk('aaabbb', gram)
print(resultado)
