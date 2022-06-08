import sympy as sy
from sympy import Symbol, Rational, binomial, expand_func
#Ingresamos los puntos y obtenemos el n
P = sy.Matrix([[-2, 4],
               [1, 3],
               [2, -1]])

n = P.shape[1] - 1
t = sy.Symbol('t')

#Definimos lo que sería la fórmula del polinomio interpolador de lagrange como una función
def polinomioInterpolador(n, i):
    temp=1
    for k in range(n+1):
        if k != i:
            temp = temp*(t-k)/(i-k)
    return sy.simplify(temp)
#Formamos los polinomios interpoladores en un arreglo
polinomios = sy.Matrix([polinomioInterpolador(n, i) for i in range(n+1)])
polinomios
#De aca podemos obtener lo que sería los coeficientes para la representación matricial
sy.expand(polinomios)
#Finalmente obtenemos el polinomio interpolador
Lx = P[:,0].T @ polinomios
Ly = P[:,1].T @ polinomios
L = sy.Matrix([Bx, By])
L
# Forma matricial
# [P0, P1, P2] [[1, -3/2, 1/2],   [1,         
#               [0    2    -1],    t,    
#               [0   -1/2  1/2]]   t^2]
# Igualmente declaramos los puntos 
P = sy.Matrix([[-2, 4],
               [1, 3],
               [2, -1]]).T
#Definimos lo que corresponde a nuestro polinomio interpolador
t = sy.Symbol('t')
BernsteinPolynomial = lambda i, n: binomial(n, i)*((1-t)**(n-i))*(t**i)
#Calculamos los polinomios
n = P.shape[1] - 1
interp = sy.Matrix([BernsteinPolynomial(i,n) for i in range(n+1)])
interp
#De aca podemos obtener lo que sería los coeficientes para la representación matricial
sy.expand(interp)
#Aca expresamos lo que sería el polinomio de Bezier de la forma usual parametrica
Bx = P[0,:] @ interp
By = P[1,:] @ interp
B = sy.Matrix([Bx, By])
B
# Forma matricial
# [P0, P1, P2] [[1,  -2,    1],   [1,         
#               [0    2    -2],    t,    
#               [0    0     1]]   t^2]