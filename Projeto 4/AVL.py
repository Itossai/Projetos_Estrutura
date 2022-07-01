class No_Arvore:
    def __init__(self,chave=None,parente=None,esquerda=None,direita=None):
        self.chave=chave
        self.esquerda=esquerda
        self.direita=direita
        self.altura=1
    
    def __repr__(self) -> str:
        return "%s -> " % (self.chave)

class Arvore_Balanceada:
    def altura(self,no_arvore):
        if no_arvore is None:
            return 0
        else:
            return no_arvore.altura

    def balanco(self,no_arvore):
        if no_arvore is None:
            return 0 
        else:
            return self.altura(no_arvore.esquerda)-self.altura(no_arvore.direita)

    def rotacao_esquerda(self,no_arvore):
        no_esquerdo=no_arvore.direita
        ramo=no_esquerdo.esquerda
        no_esquerdo.esquerda=no_arvore
        no_arvore.direita=ramo
        no_arvore.altura=1+max(self.altura(no_arvore.esquerda),self.altura(no_arvore.direita))
        no_esquerdo.altura=1+max(self.altura(no_esquerdo.esquerda),self.altura(no_esquerdo.direita))
        return no_esquerdo
    
    def rotacao_direita(self,no_arvore):
        no_direito=no_arvore.esquerda
        ramo=no_direito.direita
        no_direito.direita=no_arvore
        no_arvore.esquerda=ramo
        no_arvore.altura=1+max(self.altura(no_arvore.esquerda),self.altura(no_arvore.direita))
        no_direito.altura=1+max(self.altura(no_arvore.esquerda),self.altura(no_arvore.direita))
        return no_direito

    def inserir(self,valor,no):
        if no is None:
            return  No_Arvore(valor)
        elif valor<=no.chave:
            no.esquerda=self.inserir(valor,no.esquerda)
        elif valor>no.chave:
            no.direita=self.inserir(valor,no.direita)
        no.altura=1+max(self.altura(no.esquerda),self.altura(no.direita))
        balanco=self.balanco(no)
        if balanco > 1 and (no.esquerda.chave > valor):
            return self.rotacao_direita(no)
        if balanco < -1 and (valor > no.direita.chave):
            return self.rotacao_esquerda(no)
        if balanco > 1 and (valor>no.esquerda.chave):
            no.esquerda=self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)
        if balanco<-1 and (valor<no.direita.chave):
            no.direita=self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)
        return no   

    def pre_ordem(self,no):
        if no is None:
            return
        print(no.chave,end=" ")
        self.pre_ordem(no.esquerda)
        self.pre_ordem(no.direita)

    def pos_ordem(self,no):
        if no is None:
            return
        self.pos_ordem(no.esquerda)
        self.pos_ordem(no.direita)
        print(no.chave,end=" ")

arvore=Arvore_Balanceada()
raiz=None
for i in range(20):
    raiz=arvore.inserir(i,raiz)
print("Pré ordem")
arvore.pre_ordem(raiz)