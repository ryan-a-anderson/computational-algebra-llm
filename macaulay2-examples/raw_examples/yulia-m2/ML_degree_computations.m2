--ML estimation using minors: determinental variety
restart
n = 3
R = QQ[p_(0,0)..p_(n-1,n-1)]
nVars = #(flatten entries vars R)

M=matrix(for i to n-1 list(for j to n-1 list p_(i,j))) -- 3x3 matrix
I=ideal(det M,sum(gens R)-1) -- our ideal

--construct the augmented Jacobian
firstRow = matrix{for i to nVars-1 list random(1,100)}
-- multiply each column by the corresponding variable
D = matrix for i to nVars-1 list for j to nVars-1 list if i==j then (vars R)_(0,i) else 0;
lastRows = (transpose Jac)*D
augmentedJacobian = firstRow||lastRows

--find the critical locus
Jac = jacobian(I)
c = codim I
C = minors(c,Jac)

--compute the likelihood ideal
J=minors(numgens I + 1,augmentedJacobian)+I
K=saturate(J,C*ideal(product(gens R))*ideal(sum(gens R)))
dim K
degree K


-------------------------------------------

--ML estimation using Lagrangians: determinental variety
restart
n=2
R=QQ[p_(0,0)..p_(n-1,n-1),l_1,l_2]
M=matrix(for i to n-1 list(for j to n-1 list p_(i,j))) -- 3x3 matrix
D=det M -- determinant of M
L=matrix{flatten(for i to n-1 list(for j to n-1 list p_(i,j))), 
    flatten(for i to n-1 list(for j to n-1 list p_(i,j)*det(matrix(for k from 1 to n-1 list(for l from 1 to n-1 list p_((i+k)%n,(j+l)%n)))))),apply(n*n, i-> random 65521)} -- matrix with the first row equal to variables, the second row equal to partial derivatives of the determinant and the third row equal to random numbers
Lker=matrix{{l_1,l_2,1}}
sys=Lker*L
I=ideal(join((flatten entries sys),{D,sum(flatten(for i to n-1 list(for j to n-1 list p_(i,j))))-1}))
dim I
degree I

