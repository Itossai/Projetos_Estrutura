
from types import NoneType
from Listas_Encadeadas import*
from Conversor_Posfixo import*

def faz_operacao(op,x,y):
    if op == "+":
        return x+y
    elif op == "-":
        return x-y
    elif op=="*":
        return x*y
    elif op=="/":
        return x/y
    else:
        return False

def avaliarPosfixa(expressao):
    pilha=Lista_encadeada()
    for i in range(len(expressao)):
        unidade=expressao[i]
        if unidade >="0" and unidade<="9":
            pilha.adicionar_lista(unidade)
        else:
            try:
                x=int(pilha.desempilhar())
                y=int(pilha.desempilhar())
            except  AttributeError:
                print("Operador a mais na expressao")
                exit()   
            valor=faz_operacao(unidade,x,y)

            if valor:
                pilha.adicionar_lista(valor)
            else:
                return "Operador não registrado ou Invalido"
    resultado=pilha.desempilhar()
    if pilha.eVazio():
        return resultado
    else:
        return "Expressao invalida"

