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

def pplu(A,lbi):
    troca = []
    n = len(A[0])

    for k in range(0,n):
        troca.append(k)
    for k in range(0,n):
        max = abs(A[k][k -k+lbi])
        kMax = k
        for i in range(k+1,n):
            if (abs(A[i][k -i+lbi])) > max:
                max = abs(A[i][k -i+lbi])
                kMax = i
        if k != kMax:
            iAux = troca[kMax]
            troca[kMax] = troca[k]
            troca[k] = iAux
            for j in range(0,n):
                aux = A[kMax][j -kMax+lbi]
                A[kMax][j -kMax+lbi] = A[k][j -k+lbi]
                A[k][j -k+lbi] = aux
        for i in range(k+1,n):
            A[i][k -i+lbi] = A[i][k -i+lbi]/A[k][k -k+lbi]
            for j in range(k+1,n):
                print(i)
                print(j)
                print(k)
                A[i][j -i+lbi] = A[i][j -i+lbi] - A[i][k -i+lbi]*A[k][j -k+lbi]

    x = []
    # Substituicao Lc = Pb
    for i in range(0,n):
        x.append(b[troca[i]])
        for j in range(0,i):
            x[i] = x[i] - A[i][j -i+lbi]*x[j]

    # Retro-substituicao Ux = c
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            x[i] = x[i] - A[i][j -i+lbi]*x[j]
        x[i] = x[i]/A[i][i -i+lbi]

    return x

def band_format(A_orig,lbi,lbs):
    qLines = A_orig.shape[0]
    qColumns = lbi + 1 + lbs + lbi
    A = [[0 for x in range(qColumns)] for y in range(qLines)]

    for i in range(0,A_orig.shape[0]):
        for j in range(0,A_orig.shape[1]):
            k = j - i + lbi
            if (k >= 0) and (k < qColumns - lbi):
                A[i][k] = A_orig[i][j]

    return A

A_orig = np.loadtxt("matrix.txt")
b = np.loadtxt("b_array.txt")

lbi = 1
lbs = 2

#Original Entries
print_matrix(A_orig)
print("\n")
print_array(b)
print("\n")

print("Formato de Banda:")
A = band_format(A_orig,lbi,lbs)
print_matrix(A)
print("\n")

print("Resultado:")
print(pplu(A,lbi))
