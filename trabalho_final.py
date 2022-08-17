from ast import walk
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def palav(frases):
    palavras = []
    for n in frases:
        o = separa_palavras(n)
        for y in o:
            palavras.append(y)
    return palavras
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
# primeiro passo: subtrair os elementos de uma lista com os da outra lista, na mesma ordem
    i = 0
    x = 0
    subtracao_das_listas = []
    while i < len(as_b):    # I sera a lista referente a um texto, ouseja quando x percorrer os resultados de um texto, passara para outro
        x = 0
        while x < len(as_a):        # X ira percorrer os resultados dentro da lista de um unico texto, quando acabar x, aumentar um I, que ira mudar para outro texto
            subtracao_das_listas[i][x] = as_a[x] - as_b[x]  
            x = x + 1
        i = i + 1
    abs(subtracao_das_listas)
#proximo passo: somar os resultados de cada lista i (subtracao_das_listas)
    i = 0 
    lista_soma_dos_resultados = []

    while i < len(subtracao_das_listas):
        for v in subtracao_das_listas[i]:
            lista_soma_dos_resultados[i] = lista_soma_dos_resultados[i] + v
        i = i + 1
# Proximo passo dividir cada lista por 6, guardar o valor separadamente como elemento em uma lista
    resultado_final = []
    i = 0
    while i < len(resultado_final):
        for x in lista_soma_dos_resultados:
            resultado_final[i] = x / 6
        i - i + 0

    return resultado_final

def frases_s(x):
    frases = []
    for j in x:
        m = separa_frases(j)
        for q in m:
            frases.append(q)
    return frases
def letras_s(palavras):
    letras = []
    for x in palavras:
        for p in x:
            for e in p:
                for t in e:                                   # Este trecho ira transformar as palavras em listas, mas as palavras ja estaram divididas em letras, cada letra sera um elemento da list
                    letras.append(t)
    return letras

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.''' 

    # essa funçao ira separa as frases letras etc de cada texto, mas ainda precisa ir para a funçao define valores para definer a media das frases, media das palavras etc..
# o primeiro passo sera separar as sentenças de um texto por vez 
    frases = []
    
    sentencas = []
    
    i = 0
    palavras = []
    
    
    
    
    x = separa_sentencas(texto)
    sentencas = x[:]

# feito isso, obteremos, uma vez de cada, uma lista, que contem separadamente, as sentenças do texto atual:
    x = frases_s(x)
    frases = x[:]
            
    
#feito isso, (M) esta criando uma lista das frases contida na sentença

    
    
       
    palavras = palav(frases)                # este codigo esta separando as palavras das frases, em uma lista
                
    letras = letras_s(palavras)
    
    n = len(letras)
    
            
    palavras_unicas = n_palavras_unicas(palavras)
    palavras_diferentes = n_palavras_diferentes(palavras)
    


    lista_valores = [sentencas, frases, palavras, letras, palavras_unicas, palavras_diferentes]
    # posiçao 0 = sentenças //  posição 1 = frases // posição 2 = palavras // posição 3 = letras // posição 4 palavras unicas // posição 5 palavras diferentes

    
    caracteres = len(lista_valores[3])
    print("total de letras", caracteres)
    num_palavras_diferentes = lista_valores[5]
    total_palavras = len(lista_valores[2])
    print("total de palavras", total_palavras)
    palavras_unicas = lista_valores[4]
    num_sentencas = len(lista_valores[0])
    numero_frases = len(lista_valores[1])
# posiçao 0 = sentenças //  posição 1 = frases // posição 2 = palavras // posição 3 = letras // posição 4 palavras unicas // posição 5 palavras diferentes


#Primeiro passo: tamanho medio da palavra ("media simples do numero de caracteres por palavras..   soma do tamanho das palavras divido pelo total de palavras")
        # dividir a quantidade dos caracteres pelo total das palavras
    
    

    tamanho_medio_palavra = caracteres / total_palavras

#Segundo passo: relação Type Token (numero de palavras diferentes dividos pelo total de palavras)
    
    type_token = num_palavras_diferentes / total_palavras

# Terceiro passo: hapax legomana, numero de palavras ultilizadas uma vez, dividio pelo total de palavras
    
    hapax_legomana = palavras_unicas / total_palavras

#Terceiro passo: tamanho medio da setença (media simples do numero de caracteres por setenças)
    
    media_sentencas = caracteres / num_sentencas
    print("sentencas", num_sentencas)
    print("caracteres", caracteres)
    print("sentencas media ", media_sentencas)

#quarto passo: complexidade de sentença (media do numero de frases por senteça)
    
    complexidade_sentenca = numero_frases / num_sentencas

#quinto passo: media de frase
    tamanho_medio_frase = caracteres / numero_frases

    
    lista_valores_calcular = []
# 0 = tamanho_medio_palavra, 1 = type_token, 2 = hapax_legomana, 3 = media_sentencas, 4 = complexidade_sentenca, 5 = tamanho_medio_frase
    lista_valores_calcular = [tamanho_medio_palavra, type_token, hapax_legomana, media_sentencas, complexidade_sentenca, tamanho_medio_frase]

#a lista+valores_calcular   esta indo para a variavel texto, que ira ser calculada 

    
# valores calculados, (lista)        
# 0 = tamanho_medio_palavra, 1 = type_token, 2 = hapax_legomana, 3 = media_sentencas, 4 = complexidade_sentenca, 5 = tamanho_medio_frase
    print(lista_valores_calcular)
    return lista_valores_calcular

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    i = 0
    a = []
    b = []
    while i < len(textos):   
        a = calcula_assinatura(textos)
        b = compara_assinatura(ass_cp, a)
        b.index(min(b))

    return b


def menu():
    c = []
    b = []
    a = []
    
# primeiro passo: ler a assinatura a ser comparada
    a = le_assinatura() # le a assinatura do infectado por coh piah

    b = le_textos()    # b e a lista dos textos a serem comparados

    i = 0
    while i < len(b):
        y = (b[i])
        c = calcula_assinatura(y)   # criando a assinatura dos textos 
    
    d = avalia_textos(c, a)
    print(d)
    menu()

menu()    
