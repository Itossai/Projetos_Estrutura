from ctypes import DEFAULT_MODE
from subprocess import DETACHED_PROCESS


class No:
    def __init__(self,dado):
        self.dado=dado
        self.proximo=None
        self.anterior=None

class Lista_Dupla:
    def __init__(self):
        self.inicio=None
        self.fim=None
        self.tamanho=0
    
    def vazia(self):
        if self.inicio is None:
            return True
        else:
            return False
    
    def adicionar_inicio(self,valor):
        no=No(valor)
        if self.vazia():
            self.inicio=self.fim=no
        else:
            no.proximo=self.inicio
            self.inicio.anterior=no
            no.anterior=None
            self.inicio=no
        self.tamanho+=1

    def adicionar_fim(self,valor):
        no=No(valor)
        if self.vazia():
            self.inicio=self.fim=no
        else:
            self.fim.proximo=no
            no.anterior=self.fim
            no.proximo=None
            self.fim=no
        self.tamanho+=1
    
    def inserir_indice(self,i,valor):
        metade=int(self.tamanho/2)
        if i>self.tamanho:
            raise IndexError("Posição na memória invalida")
        elif i==self.tamanho:
            self.adicionar_fim(valor)
        elif i==0:
            self.adicionar_inicio(valor)
        else:
            if i<= metade:
                no=No(valor)
                corrente=self.inicio
                cont=0
                while cont<(i-1):
                    corrente=corrente.proximo
                    cont+=1
                no.proximo=corrente.proximo
                corrente.proximo.anterior=no
                corrente.proximo=no
                no.anterior=corrente
            else:
                no=No(valor)
                corrente=self.fim
                cont=self.tamanho
                while cont>i:
                    corrente=corrente.anterior
                    cont-=1
                no.proximo=corrente.proximo
                corrente.proximo.anterior=no
                corrente.proximo=no
                no.anterior=corrente
        self.tamanho+=1

    def remover_inicio(self):
        if self.vazia():
            raise TypeError("Lista está vazia!")
        elif self.tamanho==1:
            self.inicio=None
            self.fim=None
        else:   
            self.inicio=self.inicio.proximo
            self.inicio.anterior=None
        self.tamanho-=1
    
    def remover_fim(self):
        if self.vazia():
            raise TypeError("Lista está vazia!")
        elif self.tamanho==1:
            self.remover_inicio()
        else:
            self.fim=self.fim.anterior
            self.fim.proximo=None
        self.tamanho-=1
    
    def remover_index(self,i):
        if self.vazia(self):
            raise TypeError("Lista vazia!")
        elif i==0:
            self.remover_inicio()
        elif i==self.tamanho-1:
            self.remover_fim()
        else:
            corrente=self.inicio
            cont=0
            while cont<i-1:
                corrente=corrente.proximo
                cont+=1
            auxiliar=corrente.proximo
            corrente.proximo=auxiliar.proximo
            auxiliar.proximo.anterior=corrente
            auxiliar=None
            self.tamanho-=1
    
    def remover_valor(self,valor):
        if self.tamanho==0:
            return None
        corrente=self.inicio
        cont=0
        while corrente.dado!=valor:
            corrente=corrente.proximo
            cont+=1
        self.remover_index(cont)
    
    def pop_inicio(self):
        valor=self.inicio.dado
        self.remover_inicio()
        return valor
    
    def pop_fim(self):
        valor=self.fim.dado
        self.remover_fim()
        return valor

    def visualizar(self):
        current = self.inicio
        while True:
            print(current.dado,end=" ")
            current = current.proximo
            if current == None:
                break

