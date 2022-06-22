from Listas_Encadeadas import *

def e_operador(o):
    if o in "+-*/":
        return True
    else:
        return False
def prioridade(op_1, op_2):
    if op_1== "+" or op_1=="-":
        operador_1=1
    elif op_1== "*" or op_1=="/":
        operador_1=2
    else:
        operador_1=3
    if op_2=="+" or op_2=="-":
        operador_2=1
    elif op_2=="*" or op_2=="/":
        operador_2=2
    else:
        operador_2=0
    return operador_1>=operador_2

def postfixo(infixo):
    posfixa=[]
    pilha_operação=Lista_encadeada()
    pilha_parenteses=Lista_encadeada()
    for i in range(len(infixo)):
        variavel=infixo[i]
        if (variavel>='0' and variavel<='9'):
            posfixa.append(variavel)
        elif e_operador(variavel):
            while not pilha_operação.eVazio() and prioridade(variavel,pilha_operação.get_valor()):
                desempilha=pilha_operação.desempilhar()
                posfixa.append(desempilha)
            pilha_operação.adicionar_lista(variavel)
        elif variavel=="(":
            pilha_parenteses.adicionar_lista(variavel)
        elif variavel==")" :
            while True:
                desempilha1=pilha_parenteses.desempilhar()
                desempilha2=pilha_operação.desempilhar()
                posfixa.append(desempilha2)
                if pilha_parenteses.eVazio():
                    break
    if not pilha_parenteses.eVazio():
        print("Parenteses desbalanceado")
        exit()
    while not pilha_operação.eVazio():
        posfixa.append(pilha_operação.desempilhar())
    posfixa=("").join(posfixa)
    return posfixa
infixo=input("digite uma expressao: ")
posfixo=postfixo(infixo)
print(posfixo)
        
