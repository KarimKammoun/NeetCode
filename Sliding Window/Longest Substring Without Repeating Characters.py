s = "ddffdggdfgdfgd"

p = 0  
q = 0 
pos = [0] * 256 
maxs = 0  
n = len(s)

while q < n:
    if pos[ord(s[q])] == 0:
        pos[ord(s[q])] += 1
        maxs = max(maxs, q - p + 1)
        q += 1
    else: 
        while (pos[ord(s[q])])>0:
            if (pos[ord(s[p])])>0:
                (pos[ord(s[p])])-=1
            p += 1 


print(maxs)