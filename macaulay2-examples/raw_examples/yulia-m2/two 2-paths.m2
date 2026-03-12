R=QQ[x,y,z,w,s11,s12,s22,s33,s34,s44]
M=matrix{{s11,s12,x,y},{s12,s22,z,w},{x,z,s33,s34},{y,w,s34,s44}}
--f=s12^2*s34^2 - s11*s22*s34^2 - s12^2*s33*s44 + s11*s22*s33*s44 - s11*s33*w^2 - 2*s12*s34*w*x - s22*s44*x^2 + w^2*x^2 + 2*s12*s33*w*y + 2*s22*s34*x*y - s22*s33*y^2 + 2*s11*s34*w*z + 2*s12*s44*x*z - 2*s12*s34*y*z - 2*w*x*y*z - s11*s44*z^2 + y^2*z^2
--sing = ideal(f, diff(x,f), diff(y,f), diff(z,f), diff(w,f))
sing=minors(3,M)
dim sing
S =(frac QQ[s11,s12,s22,s33,s34,s44])[x,y,z,w]
m=map(S,R,{x,y,z,w,s11,s12,s22,s33,s34,s44}); R = QQ[x,y,z,w,s11,s12,s22,s33,s34,s44]; 
minv=map(R,S,{x,y,z,w,s11,s12,s22,s33,s34,s44})
m(sing) 
Jac=jacobian(m(sing));
J=minors(3,Jac);
singsing=m(sing)+J;
JJ=minv(singsing);
D=eliminate(JJ,{x,y,z,w})
mingens D

----
ss=minors(2,M)
eliminate(ss,{x,y,z,w})
----

decompose D --the irreducible components of this variety are precisely the two 2x2 minors
 
K=ideal((s14^2-s11*s44)*(s13^2-s11*s33)*(s12^2-s11*s22))
decompose(K)
