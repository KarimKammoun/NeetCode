heights = [2,1,5,6,2,3]
res=0
for i in range(len(heights)):
    
    k=heights[i]
    for j in range(i,len(heights)):
        if heights[j]<k:
            k=heights[j]
    a=k*(len(heights)-i)
    if a>res:
        res=a
print(res)