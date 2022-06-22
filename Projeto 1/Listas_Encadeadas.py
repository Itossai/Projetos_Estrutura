



class Lista_encadeada:
    def __init__(self) :
        self.head=None
        self.size=0
    def __str__(self):
        return "["+str(self.head)+"]"
   
    def remove_valor(self, valor):
        assert self.head, "Impossível remover valor de lista vazia."
    # Nodo a ser removido é a cabeça da lista.
        if self.head.dadoval == valor:
            self.head = self.head.nextval
        else:
            # Encontra a posição do elemento a ser removido.
            anterior = None
            corrente = self.head
            while corrente and corrente.dadoval != valor:
                anterior = corrente
                corrente = corrente.nextval
            # O nodo corrente é o nodo a ser removido.
            if corrente:
                anterior.nextval = corrente.nextval
            else:
                # O nodo corrente é a cauda da lista.
                anterior.nextval = None
        #remove o tamanho da lista
        self.size-=1

    def adicionar_lista(self,novo_dado):
        #cria novo node
        novo_node=Node(novo_dado)
        #faz com que o novo node seja a cabeça da lista
        novo_node.nextval= self.head
        #faz com que a cabeça da lista referencie o novo node
        self.head=novo_node
        #acrescenta o indice do ultimo nó
        self.size+=1
    def adicionar_depois(self,node_anterior,novo_dado):
        assert node_anterior,"nodo_anterior precisa existir na lista"
        #cria novo node
        novo_node=Node(novo_dado)
        #faz o nextval do novo_node ser o nextval do note anterior
        novo_node.nextval=node_anterior.nextval
        #faz com que o novo_node ser o nextval do node anterior
        node_anterior.nextval=novo_node
        #adiciona o tamanho da linked list
        self.size+=1

    def procura_valor(self,valor):  
        corrente=self.head
        while corrente and corrente.dadoval!=valor:
            corrente=corrente.nextval
        return corrente 
    def get_valor(self):
        linkedlist=self.head
        return linkedlist.dadoval
    def set_valor(self,valor):
        linkedlist=self.head
        linkedlist.dadoval=valor
    def insere_no_meio(self,valor):
        #insere no meio e no final da lista
        cabeça=self.head
        if cabeça.dadoval<valor:
            self.adicionar_lista(valor)
        else:
            anterior=None
            corrente=cabeça
            while corrente and corrente.dadoval>valor:
                anterior=corrente
                corrente=corrente.nextval
            self.adicionar_depois(anterior,valor)
    def desempilhar(self):
        v=self.head.dadoval
        self.head=self.head.nextval
        self.size-=1
        return v   
    def eVazio(self):
        if self.head == None:
            return True
        else:
            return False
class Node:
    def __init__(self,dadoval,nextval=None):
        self.dadoval=dadoval
        self.nextval=nextval
        
    def __str__(self):
        return '%s -> %s' % (self.dadoval, self.nextval)
    
    
"""Utilizando uma entrada pos fixada
    (2+3)*(9+8)+(5+4)*(7+2)
    23+98+*54+72+*
    pegar os dados em ordem e colocar na lista
    se o dado informado for um simbolo matematico, executar a operação matematica nos valores e retornar resultado
    no ultimo da lista
"""    

"""lista=Lista_encadeada()  
 
for i in range (8):
    lista.adicionar_lista(i)
print(lista)

for i in range(8):
    elemento=lista.procura_valor(i)
    if elemento:
        print("Elemento {0} presente na lista".format(i))
    else:
        print("Elemento {0} não presente na lista".format(i))

for i in range(8):
    lista.remove_valor(i)
    print (lista)


lista.adicionar_lista(1)
lista.adicionar_lista(2)
lista.insere_no_meio(1.5)
print(lista)
lista.set_valor(7)
print(lista)
print(lista.get_valor())"""