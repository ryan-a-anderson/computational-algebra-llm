loadPackage "NumericalAlgebraicGeometry";
R = QQ[x,y,z,b1,b2,b3];
K1=matrix{{1,0,0},{0,1,1},{0,1,1}};
K2=matrix{{1,0,1},{0,1,0},{1,0,1}};
K3=matrix{{1,1,0},{1,1,0},{0,0,1}};
M = matrix {
    {2*x,b3/2-x-y-z,b2/2-x-y-z},
    {b3/2-x-y-z,2*y,b1/2-x-y-z},
    {b2/2-x-y-z,b1/2-x-y-z,2*z}};
I = minors(2,M);
f = first first entries gens eliminate({y,z},I);
toString factor(discriminant(f,x))

disc=b1^6-6*b1^5*b2+19*b1^4*b2^2-28*b1^3*b2^3+19*b1^2*b2^4-6*b1*b2^5+b2^6-6*b1^5*b3+14*b1^4*b2*b3-24*b1^3*b2^2*b3-24*b1^2*b2^3*b3+14*b1*b2^4*b3-6*b2^5*b3+19*b1^4*b3^2-24*b1^3*b2*b3^2+106*b1^2*b2^2*b3^2-24*b1*b2^3*b3^2+19*b2^4*b3^2-28*b1^3*b3^3-24*b1^2*b2*b3^3-24*b1*b2^2*b3^3-28*b2^3*b3^3+19*b1^2*b3^4+14*b1*b2*b3^4+19*b2^2*b3^4-6*b1*b3^5-6*b2*b3^5+b3^6;

---
R' = QQ[x,y,z]
F=map(R',R,{x,y,z,0,0,0})




for i from 1 to 10 do
{A=random(ZZ^3,ZZ^3);
S=A*transpose(A);
M'=sub(M,{b1=>trace(S*K1),b2=>trace(S*K2),b3=>trace(S*K3)});
g=det(M');
--J=ideal(F(g),diff(x,F(g)),diff(y,F(g)),diff(z,F(g)))
J=minors(2,F(M'));
print degree J;
print solveSystem(J_*);
print toString (trace(S*K1)/trace(S*K3), trace(S*K2)/trace(S*K3));}


---computing singular stratification, etc.
R = QQ[l1,l2,l3]
K=matrix{{l1+l2+l3,l3,l2},{l3,l1+l2+l3,l1},{l2,l1,l1+l2+l3}}
I=ideal(det(K))
isPrime I
codim I
J=minors(2,K)

