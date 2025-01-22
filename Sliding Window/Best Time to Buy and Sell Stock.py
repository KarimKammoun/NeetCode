prices = [10,1,5,6,7,1]
res=0
n=len(prices)
p=0
q=1
while q<n :
    if prices[q]-prices[p]>res:
        res=prices[q]-prices[p]
    if prices[q]<prices[p]:
        p=q
    q=q+1
print (res)
