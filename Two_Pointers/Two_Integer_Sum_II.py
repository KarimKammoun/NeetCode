numbers=[-2,2,3,4,5,6,7]
target=0

a=0
b=len(numbers)-1
for i in range(len(numbers)):
    d=numbers[a]+numbers[b]
    if d>target:
        b=b-1
    elif d<target:
        a=a+1
    else:
        break
print([a+1,b+1])
    