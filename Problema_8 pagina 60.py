n=int(input('Dati numarul de elemente din mulțimea A n='))
A=set()
print('Introduceti ',n,' elemente pentru mulțimea creată')
for i in range(0, n):
    x=int(input('elementul A[' +str(i)+']='))
    A.add(x)
print('Mulțimea obtinută',A)

z=int(input('Dati numarul de elemente din mulțimea B n='))
B=set()
print('Introduceti ',n,' elemente pentru mulțimea creată')
for i in range(0, n):
    y=int(input('elementul B[' +str(i)+']='))
    B.add(y)
print('Mulțimea obtinută',B)

print('Intersecția mulțimilor: ', A.intersection(B))
print('Reuniunea mulțimilor: ', A.union(B))
print('Diferența mulțimilor: ', A.difference(B))





