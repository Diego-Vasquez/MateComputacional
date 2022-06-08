from scipy.optimize import linprog

obj= [200, 220]             #Es nuestra funcion objetivo

lhs_ineq= [[-0.7,-0.64],    #Lado izquierdo de las desigualdades
           [0.9,0.8]]

rhs_ineq= [-6.5,            #Lado derecho de las desigualdades
           8.5]

lhs_eq= [[1, 1]]            #Lado izquierdo de la igualdad

rhs_eq= [10]                #Lado derecho de la igualdad

#Resolviendo

optimo= linprog(c=obj, A_ub= lhs_ineq, b_ub= rhs_ineq,
                A_eq= lhs_eq, b_eq= rhs_eq, method= "simplex")

print(optimo)               #Imprimimos el valor optimo
