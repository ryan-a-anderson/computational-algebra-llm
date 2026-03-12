R = QQ[x,y,z]
Sigma = matrix{{1,x,z}, {x,1,y}, {z,y,1}}
detSigma = det(Sigma)
A = random(ZZ^3, ZZ^3)
S = A*transpose(A)
SigmaInv = matrix{{1-y^2, -(x-y*z), x*y-z}, {-(x-y*z), 1-z^2, -(y-x*z)}, {x*y-z, -(y-x*z), 1-x^2}}
traceSSigmaInv = trace(S*SigmaInv)
I = ideal((detSigma - traceSSigmaInv)*diff(x,detSigma) + detSigma*diff(x,traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(y,detSigma) + detSigma*diff(y, traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(z, detSigma)+ detSigma*diff(z,traceSSigmaInv))
dim I
degree I
J = saturate(I,detSigma)
dim J
degree J
S = QQ[x,y,z,MonomialOrder=>Lex]
F = map(S,R,{x,y,z})
JJ = F(J)
gens gb JJ


-------GENERAL MATRIX-------
R = QQ[x,y,z,s11,s12,s13,s22,s23,s33]
Sigma = matrix{{1,x,z}, {x,1,y}, {z,y,1}}
detSigma = det(Sigma)
S=matrix{{s11,s12,s13},{s12,s22,s23},{s13,s23,s33}}
SigmaInv = matrix{{1-y^2, -(x-y*z), x*y-z}, {-(x-y*z), 1-z^2, -(y-x*z)}, {x*y-z, -(y-x*z), 1-x^2}}
traceSSigmaInv = trace(S*SigmaInv)
I = ideal((detSigma - traceSSigmaInv)*diff(x,detSigma) + detSigma*diff(x,traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(y,detSigma) + detSigma*diff(y, traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(z, detSigma)+ detSigma*diff(z,traceSSigmaInv))
dim I
degree I


-------
S=QQ[s11,s12,s13,s22,s23,s33]
F=frac S
R=F[x,y,z]
