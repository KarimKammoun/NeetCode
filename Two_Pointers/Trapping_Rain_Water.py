height=[8,5,1,1,7,3,2,1,5,8,3]

a=0
b=0
s1=0
s=0
p=-1
maxe=max(height)
if len(height)>2:
    while height[a]!=maxe:
        p=p+1
        b=b+1
        if height[b]>=height[a]:
            a=b
            s=s+s1
            s1=0
        s1=s1+(height[a]-height[b])
    a=len(height)-1
    b=len(height)-1
    s1=0
    for i in range(len(height)-1,p+1,-1):
        b=b-1
        if height[b]>=height[a]:
            a=b
            s=s+s1
            s1=0
        s1=s1+(height[a]-height[b])
    print(s)
else:
    print(0)



