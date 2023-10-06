x, y = input().split()
linhas = int(x)
colunas = int(y)
lista = []
lista_p = []
flag = False
for cont in range(linhas):
    cam = list(input())
    print(cam)
    for e in range(len(cam)):
        if cam[e] == "o":
            comeco = (cont, e)  
    lista.append(cam)
    
print(comeco)
lista_p.append(comeco)


'''       
if comeco[1] - 1 > 1 and lista[comeco[0]][comeco[1] - 1] == "H":
    comeco = (comeco[0], comeco[1] - 1)
elif comeco[1] - 1 > 1 and lista[comeco[0]][comeco[1] + 1] == "H":
    comeco = (comeco[0], comeco[1] + 1) 
    
elif  and lista[comeco[0] - 1][comeco[1]] == "H":
    comeco = (comeco[0] - 1, comeco[1]) 
elif  and lista[comeco[0] + 1][comeco[1]] == "H":
    comeco = (comeco[0] + 1, comeco[1])
'''
