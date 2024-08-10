"""heights =[1,8,6,2,5,4,8,3,7]

liste=[]
for i in range(len(heights)):
    liste.append([heights[i],i])

print(liste)
liste.sort()
print(liste)

s=0

a=0
b=1
for i in range(len (heights)-1):
    print(a,b)
    if (min(liste[a][0],liste[b][0]))*abs(liste[a][1]-liste[b][1])>s:
        s=(min(liste[a][0],liste[b][0]))*abs(liste[a][1]-liste[b][1])
    a=a+1
    b=b+1
    if (liste[a][0]==liste[a-1][0]) and (liste[i][0]==liste[a][0]) :
        a=a-1
    else:
        a=i
print(s)"""



heights =[1,8,6,2,5,4,8,3,7]
s=0

a=0
while a<len(heights)-1:
    for i in range(a+1,len(heights)):
        if min(heights[a],heights[i])*(i-a)>s:
            s=min(heights[a],heights[i])*(i-a)
    a=a+1
print(s)

























