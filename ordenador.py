class ordenador:
    
    def bolha(self, lista):

        fim = len(lista)

        for i in range(fim -1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    
        return lista
    
    
    def bolha_curta(self, lista):

        fim = len(lista)

        for i in range(fim -1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if trocou == False:
                return



    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim - 1):
            #inicialmente o menor elemennto da lista é o í-ésimo
            posicao_do_minimo = i
            
            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            # coloca o menor elemento encontrado no inicio da sub-lista
            # para isso, troca de lugar os elementos nas posiçoes i e posição_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

    

