
from Listas_Encadeadas import Lista_encadeada


class No_Arvore:
    def __init__(self,chave=None,esquerda=None,direita=None):
        self.chave=chave
        self.esquerda=esquerda
        self.direita=direita

    def __repr__(self) -> str:
        return " %s " % (self.chave)

class Arvore_Binaria:
    def __init__(self,data=None,no=None):
        if no:
            self.raiz=no
        elif data:
            no=No_Arvore(data)
            self.raiz=no
        else:
            self.raiz=None 

    def em_ordem(self,no=None):
        if no is None:
            no=self.raiz
        if no.esquerda:
            self.em_ordem(no.esquerda)
        print(no,end=" ")
        if no.direita:
            self.em_ordem(no.direita)

    def pos_ordem(self,no=None):
        if no is None:
            no=self.raiz
        if no.esquerda:
            self.pos_ordem(no.esquerda)
        if no.direita:
            self.pos_ordem(no.direita)
        print(no,end=" ")

    def pre_ordem(self,no=None):
        if no is None:
            no=self.raiz
        print(no,end=" ")
        if no.esquerda:
            self.pos_ordem(no.esquerda)
        if no.direita:
            self.pos_ordem(no.direita)
    
    def altura(self,no=None):
        if no is None:
            no=self.raiz
        altura_esquerda=0
        altura_direita=0
        if no.esquerda:
            altura_esquerda=self.altura(no.esquerda)
        if no.direita:
            altura_direita=self.altura(no.direita)
        if altura_direita>altura_esquerda:
            return altura_direita+1
        return altura_esquerda+1

    def nivel_ordenado(self,no=None):
        if no is None:
            no=self.raiz
        fila=Lista_encadeada()
        fila.adicionar_lista(no)

        while not fila.eVazio():
            no=fila.desempilhar()
            if no.esquerda:
                fila.adicionar_lista(no.esquerda)
            if no.direita:
                fila.adicionar_lista(no.direita)
            print(no,end=" ")

class BuscaArvoreBinaria(Arvore_Binaria):
    
    def inserir(self,valor):
        parente=None
        raiz=self.raiz
        while raiz:
            parente=raiz
            if valor<raiz.chave:
                raiz=raiz.esquerda
            else:
                raiz=raiz.direita
        if parente is None:
            self.raiz=No_Arvore(valor)
        elif valor<parente.chave:
            parente.esquerda=No_Arvore(valor)
        else:
            parente.direita=No_Arvore(valor)


    def procurar(self,valor):
        return self._procurar(valor,self.raiz)
    
    def _procurar(self,valor,no):
        if no is None:
            return no
        if no.chave==valor:
            return Arvore_Binaria(no)
        if valor<no.chave:
            return self._procurar(valor,no.esquerda)
        return self._procurar(valor,no.direita)
    
    def minimo(self, no=None):
        if no==None:
            no=self.raiz
        while no.esquerda:
            no=no.esquerda
        return no.chave
    
    def maximo(self,no=None):
        if no==None:
            no=self.raiz
        while no.direita:
            no=no.direita
        return no.chave
    def remover(self,valor,no):
        if no is None:
            no=self.raiz
        if valor<no.chave:
            no.esquerda=self.remover(valor,no.esquerda)
        elif valor>no.chave:
            no.direita=self.remover(valor,no.direita)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            else:
                subistituto=self.minimo(no.direita)
                no.chave=subistituto
                no.direita=self.remover(subistituto,no.direita)
        return no


#lista_raiz=BuscaArvoreBinaria()
#array=[15,25,10,2,5,50,46,90,64,24,32,97,85,58,4,9,99]
#for i in range(len(array)):
 #   lista_raiz.inserir(array[i])
#lista_raiz.em_ordem(None)
#print("\n",lista_raiz.minimo(None))
#print(lista_raiz.maximo(None))






