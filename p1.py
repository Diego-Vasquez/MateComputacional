import sympy as sy
#el primer eje es 
v1 = sy.Matrix((2, 0, -2))
v2 = sy.Matrix((-3, 1, 1))
#calculamos las normas
norm1 = sy.sqrt((v1.T @ v1)[0])
norm2 = sy.sqrt((v2.T @ v2)[0])
#normalizamos los vectores
u1 = v1/norm1
u2 = v2/norm2
#Procedemos a definir los cuaterniones, teniendo en cuenta que usaremos un theta = pi/6 porque hara una rotacion de 2 theta
q1 = sy.Quaternion(sy.cos(sy.pi/6), sy.sin(sy.pi/6)*u1[0], sy.sin(sy.pi/6)*u1[1], sy.sin(sy.pi/6)*u1[2])
q2 = sy.Quaternion(sy.cos(sy.pi/6), sy.sin(sy.pi/6)*u2[0], sy.sin(sy.pi/6)*u2[1], sy.sin(sy.pi/6)*u2[2])

#Tenemos el cuaternion de la primera rotacion
q1
#Tenemos el cuaternion de la segunda rotacion
q2
#Ahora, queremos que primero se realice la primera rotación y luego la segunda rotación
#es decir, obtenemos primero T1 (v) = q1 v q1^-1
#y luego hacer la rotación T2 (u) = q2 u q2^-1

#Entonces tendriamos la composicion T2 (T1(v)) = T2 o T1 (v)= q2 (q1 v q1^-1) q2^-1 = (q2 q1) v (q1^-1 q2^-1) = (q2 q1) v (q2 q1)^-1
#Entonces el cuaternion resultante de la composición es
q2*q1