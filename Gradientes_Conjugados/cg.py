import numpy as np

#It's assumed that A is symmetric and positive-definite
#It's assumed there is no error in the input
def conjugate_gradient(A,b,x0,TOLERANCE = 1.0e-10):
    x = x0
    r0 = b - np.dot(A, x)
    p = r0

    for i in range(len(b)):
        alpha = float(np.dot(r0.T, r0)/np.dot(np.dot(p.T, A), p))
        x = x + p*alpha
        ri = r0 - np.dot(A*alpha, p)

        print(i,np.linalg.norm(ri))

        if np.linalg.norm(ri) < TOLERANCE:
            return x
        beta = float(np.dot(ri.T, ri)/np.dot(r0.T, r0))
        p = ri + beta * p
        r0 = ri
    return x

A = np.loadtxt("matrix.txt")
b = np.loadtxt("b_array.txt")


print("\nResult:",conjugate_gradient(A,b,(0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)))
