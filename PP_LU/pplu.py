import numpy as np



def print_matrix(m):
    l = ""
    for line in m:
        for element in line:
            l = l+str(element)+"  "
        print(l)
        l = ""

def print_array(a):
    l = ""
    for element in a:
        l = l+str(element)+"  "
    print(l)


A = np.loadtxt("matrix.txt")
b = np.loadtxt("b_array.txt")

print_matrix(A)
print("\n")
print_array(b)
print("\n")

troca = []
n = A[0].size

for k in range(0,n):
    troca.append(k)
for k in range(0,n):
    max = abs(A[k][k])
    kMax = k
    for i in range(k+1,n):
        if (abs(A[i][k])) > max:
            max = abs(A[i][k])
            kMax = i
    if k != kMax:
        iAux = troca[kMax]
        troca[kMax] = troca[k]
        troca[k] = iAux
        for j in range(0,n):
            aux = A[kMax][j]
            A[kMax][j] = A[k][j]
            A[k][j] = aux
    for i in range(k+1,n):
        A[i][k] = A[i][k]/A[k][k]
        for j in range(k+1,n):
            A[i][j] = A[i][j] - A[i][k]*A[k][j]

x = []
# Substituicao Lc = Pb
for i in range(0,n):
    x.append(b[troca[i]])
    for j in range(0,i):
        x[i] = x[i] - A[i][j]*x[j]

# Retro-substituicao Ux = c
for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        x[i] = x[i] - A[i][j]*x[j]
    x[i] = x[i]/A[i][i]

print_array(x)
