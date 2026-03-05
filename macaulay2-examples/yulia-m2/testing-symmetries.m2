restart
t = 5
d = 6
l = 8
u = 2
v = 2
j = 2

conj = d*(2*t - 2 - j) + (t-1)*(u+v)+ j*(l-u-v) - (j^2 + 2*(t-1-j)^2 + 2*(j)*(t-1-j))


param = (m, n1, n2, n3) -> toList flatten (flatten entries (m_{0..t-2} * n1), flatten entries (m_{t-j-1..t-2} * n2), flatten entries (m_{t-j-1..2*t-2-j-1} * n3))


R = QQ[m_1..m_(d*(2*t-2-j)), a_1..a_((t-1)*u), b_1..b_(j*(l-u-v)), c_1..c_((t-1)*v)]
length gens R

M  = genericMatrix(R, m_1, d, (2*t-2-j))
N1 = genericMatrix(R, a_1, (t-1), u)
N2 = genericMatrix(R, b_1, j, (l-u-v))
N3 = genericMatrix(R, c_1, t-1, v)




par = param(M, N1, N2, N3)
jac = jacobian(ideal(par))
subz = apply(gens(R), g -> g => random(1,50));
j = sub(jac, subz);
rank j



---------------------------------
---------------------------------
---------------------------------
A2 = random(R^(t-2), R^(t-2));
A2inv = inverse(A2)

Z = transpose matrix{{0,0,0,0}}
B = random(R^(t-1), R^1) ++ 0 | Z | Z
C = Z | Z | 0 ++ random(R^(t-1), R^1)

A = 0 ++ A2 ++ 0
D = A + B + C





D1 = D_{0..t-2}^{0..t-2}
D1inv = inverse D1

D3 = D_{1..t-1}^{1..t-1}
D3inv = inverse D3



L1 = param(M, N1, N2, N3)
L2 = param(M*D, D1inv*N1, A2inv*N2, D3inv*N3)


L1 == L2



