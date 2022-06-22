from Arvore import*

def inserir_ordenado(array,inicio,fim,raiz):
    if fim==inicio:
        raiz.inserir(array[inicio])
        return
    if inicio>fim:
        raiz.inserir(array[inicio])
        return
    metade=(inicio+fim)//2
    raiz.inserir(array[metade])
    inicio_2=metade+1
    fim_2=metade-1
    inserir_ordenado(array,inicio,fim_2,raiz)
    inserir_ordenado(array,inicio_2,fim,raiz)

raiz=BuscaArvoreBinaria()
array=[]
for i in range(15):
    array.append(i)
fim=len(array)-1
inicio=0
inserir_ordenado(array,inicio,fim,raiz)
raiz.pre_ordem()