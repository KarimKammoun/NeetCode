temperatures = [30,38,30,36,35,40,28]

res=[]
dic={}
for i in range(len(temperatures)):
    if (temperatures[i] in dic)==False:
        dic[temperatures[i]]=i
    
    if i>0:
        for j in range(temperatures[i]):
            if j in dic:
                res.append(i-dic[i])


print(dic)
print(res)