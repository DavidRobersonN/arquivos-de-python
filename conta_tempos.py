import random
import ordenador
import time

class contatempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]#inteiros entre 0 e 999
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara (self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = self.lista_quase_ordenada(n)
        

        o = ordenador.ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("bolha demorou ", antes - depois)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("seleção direta demorou ", antes - depois)

        
        antes = time.time()
        o.bolha_curta(lista3)
        depois = time.time()
        print("bolha curta demorou ", antes - depois)
