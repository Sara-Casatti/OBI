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

while not flag:
    if comeco[1] + 1 < colunas and lista[comeco[0]][comeco[1] + 1] == "H" and (comeco[0], comeco[1] + 1) not in lista_p:
        comeco = (comeco[0], comeco[1] + 1)
        print("1", comeco)
        lista_p.append(comeco)
    elif comeco[1] - 1 >= 0 and lista[comeco[0]][comeco[1] - 1] == "H" and (comeco[0], comeco[1] - 1) not in lista_p:
        comeco = (comeco[0], comeco[1] - 1)
        print("2", comeco)
        lista_p.append(comeco)
    elif comeco[0] + 1 < linhas and lista[comeco[0] + 1][comeco[1]] == "H" and (comeco[0] + 1, comeco[1]) not in lista_p:
        comeco = (comeco[0] + 1, comeco[1])
        print("3", comeco)
        lista_p.append(comeco)
    elif comeco[0] - 1 >= 0 and lista[comeco[0] - 1][comeco[1]] == "H" and (comeco[0] - 1, comeco[1]) not in lista_p:
        comeco = (comeco[0] - 1, comeco[1])
        print("4", comeco)
        lista_p.append(comeco)
    else:
        flag = True

print(comeco[0] + 1, comeco[1]+1)

