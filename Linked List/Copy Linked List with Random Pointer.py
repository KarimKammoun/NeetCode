

head = [[3,None],[7,3],[4,0],[5,1]]

liste=[]


i=head

pos=0
while(i!=None):
    inter=[]
    inter.append(i.val)
    j=i
    indice=pos
    while(j!=i.random):
        j=j.suivant
        indice+=1
    inter.append(indice)
    liste.append(inter)
    pos+=1
print(liste)