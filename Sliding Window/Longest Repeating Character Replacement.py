s = "AAABABB"
k = 1

maxs = 0
p = 0
q = 0
n = len(s)
freq = {}

while q < n:
    freq[s[q]] = freq.get(s[q], 0) + 1
    max_freq = max(freq.values())  
    if (q - p + 1) - max_freq > k:
        freq[s[p]] -= 1
        p += 1 
    
    maxs = max(maxs, q - p + 1)
    q += 1

print(maxs)
