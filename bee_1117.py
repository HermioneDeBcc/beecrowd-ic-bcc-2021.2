notasInseridas=0
somatorioNotas=0

while (notasInseridas<2):
    nota=float(input())

    if(nota>10 or nota<0):
        print("nota invalida")
        continue;
    
    somatorioNotas+=nota
    notasInseridas+=1
print("media = {}".format(somatorioNotas/2))