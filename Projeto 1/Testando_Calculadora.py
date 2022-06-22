from Listas_Encadeadas import*
from Conversor_Posfixo import*
from Verificador import*

expressao_infixa=input("digite uma expressao numerica: ")

expressao_posfixa=postfixo(expressao_infixa)

print("\n Expressão infixa : {0} \n expressão pósfixada {1}".format(expressao_infixa,expressao_posfixa))

resultado=avaliarPosfixa(expressao_posfixa)

print("Resultado: {0}\n".format(resultado))
