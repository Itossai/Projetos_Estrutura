import sys
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
    return operador_1<=operador_2

def postfixo(infixo):

    pilha=Lista_encadeada()
    
    posfixa=[]

    for i in range(len(infixo)):
        variavel=infixo[i]
        if (variavel>='0' and variavel<='9'):
            posfixa.append(variavel)
        elif e_operador(variavel):
            while not pilha.eVazio() and prioridade(variavel,pilha.get_valor):
                desempilha=pilha.desempilhar()
                posfixa.append(desempilha)
            pilha.adicionar_lista(variavel)
        elif variavel=="(":
            pilha.adicionar_lista(variavel)
        elif variavel==")":
            while True:
                desempilha=pilha.desempilhar()
                if pilha.procura_valor("(") is None:
                    print("Expressao desbalanceada")
                    exit() 
                if desempilha != "(":
                   posfixa.append(desempilha)
                else:
                    break
    while not pilha.eVazio():
        posfixa.append(pilha.desempilhar())
    posfixa="".join(posfixa)
    if "(" in posfixa:
        print("A expressao esta desbalanceada em parenteses") 
        exit()
    return posfixa

