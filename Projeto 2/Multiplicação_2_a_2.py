from LIsta_duplamente_encadeada import*

def separa_str_dois_a_dois(string):
    lista=[]
    c=0
    if len(string)%2==1:
        lista.append(string[0])
        c+=1
    lista+=[string[i:i+2] for i in range(c,len(string),2)]
    return lista

def coloca_str_na_lista(lista_str):
    lista_dupla=Lista_Dupla()
    for i in lista_str:
        lista_dupla.adicionar_fim(i)
    return lista_dupla

def multiplica_dois_a_dois(numero1,numero2):
    str_numero_1=separa_str_dois_a_dois(numero1)
    str_numero_2=separa_str_dois_a_dois(numero2)
    lista_dupla1=coloca_str_na_lista(str_numero_1)
    lista_dupla2=coloca_str_na_lista(str_numero_2)
    lista_dupla_resultado=Lista_Dupla()
    calda1=lista_dupla1.fim
    calda2=lista_dupla2.fim
    calda_resultado1=None
    calda_resultado2=None
    buffer=0;resultado=0;num1=0;num2=0;
    numero_resultado=""
    
    while calda1!=None:
        calda2=lista_dupla2.fim
        n1=int(calda1.dado)
        calda_resultado2=calda_resultado1
        while calda2!=None:
            n2=int(calda2.dado)
            resultado=n1*n2
            if calda_resultado2 is not None:
                resultado+=int(calda_resultado2.dado)
                buffer=resultado//100
                resultado-=buffer*100
                if resultado//10==0:
                    resultado="0"+str(resultado)
                calda_resultado2.dado=str(resultado)
                if calda_resultado2.anterior is None:
                    if calda2.anterior is not None:
                        lista_dupla_resultado.adicionar_inicio(str(buffer))
                    else:
                        if buffer!=0:
                            lista_dupla_resultado.adicionar_inicio(str(buffer))
                else:
                    calda_resultado2.anterior.dado = str(buffer+int(calda_resultado2.anterior.dado))
            elif lista_dupla_resultado.inicio is not None:
                resultado+=int(lista_dupla_resultado.inicio.dado)
                buffer=resultado//100
                resultado-=buffer*100
                if resultado//10==0:
                    resultado="0"+str(resultado)
                lista_dupla_resultado.inicio.dado=(str(resultado))
                if calda2.anterior is not None:
                    lista_dupla_resultado.adicionar_inicio(str(buffer))
                elif buffer!=0:
                    lista_dupla_resultado.adicionar_inicio(str(buffer))
            else:
                buffer=resultado//100
                resultado-=buffer*100
                if resultado//10==0:
                    resultado="0"+str(resultado)
                lista_dupla_resultado.adicionar_inicio(str(resultado))
                lista_dupla_resultado.adicionar_inicio(str(buffer))
            if calda_resultado2 is not None:
                calda_resultado2=calda_resultado2.anterior
            calda2=calda2.anterior
        calda_resultado1=lista_dupla_resultado.fim.anterior if calda_resultado1 is None else calda_resultado1.anterior
        calda1=calda1.anterior         
    while not lista_dupla_resultado.vazia():
        numero_resultado+=lista_dupla_resultado.pop_inicio()
    return numero_resultado





    


