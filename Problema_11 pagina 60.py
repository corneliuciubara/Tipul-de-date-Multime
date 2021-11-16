s = ['A','B','C','D']
p = [[]]
f = [[],s]

for i in range(len(s)):
    for j in range(i+1,len(s)):
        p[-1].append([i,j])

for i in range(len(s)-3):
    p.append([])
    for m in p[-2]:
        p[-1].append(m+[m[-1]+1])

for i in p:
    for j in i:
        n = []
        for m in j:
            if m < len(s):
                n.append(s[m])
        if n not in f:
            f.append(n)

for i in s:
    if [i] not in f:
        f.append([i])

print('Submultimele mulțimii: ',f)

