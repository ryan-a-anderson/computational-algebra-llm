loadPackage "NumericalAlgebraicGeometry"; loadPackage "EigenSolver"; 
R = QQ[x,y,z]
Sigma = matrix{{1,x,z}, {x,1,y}, {z,y,1}}
detSigma = det(Sigma)
A = random(ZZ^3, ZZ^3)
S = A*transpose(A)
--S=matrix{{1211/4560, -217/3420, 1/30},{-217/3420, 827/2565, 1/9},{1/30, 1/9, 1}}
SigmaInv = matrix{{1-y^2, -(x-y*z), x*y-z}, {-(x-y*z), 1-z^2, -(y-x*z)}, {x*y-z, -(y-x*z), 1-x^2}}
traceSSigmaInv = trace(S*SigmaInv)
I = ideal((detSigma - traceSSigmaInv)*diff(x,detSigma) + detSigma*diff(x,traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(y,detSigma) + detSigma*diff(y, traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(z, detSigma)+ detSigma*diff(z,traceSSigmaInv))
dim I
degree I
J = saturate(I,detSigma)
dim J
degree J
zeroDimSolve J



solveSystem J_*
toString J_*

T = QQ[x,y,z,MonomialOrder=>Lex]
F = map(T,R,{x,y,z})
JJ = F(J)
gens gb JJ
solveSystem JJ_*


for i from 0 to 5 do print sub(J_i,{x=>63.1901,y=>0.447025,z=>0.882024})
 
 
 
 
---
loadPackage "NumericalAlgebraicGeometry"
R = QQ[x,y,z]
Sigma = matrix{{1,x,z}, {x,1,y}, {z,y,1}}
detSigma = det(Sigma)
--A = random(ZZ^3, ZZ^3)
--S = A*transpose(A)
S=matrix{{813/304, 103/76, 1/2},{103/76, 85/57, 1/3},{1/2, 1/3, 1/3}}
SigmaInv = matrix{{1-y^2, -(x-y*z), x*y-z}, {-(x-y*z), 1-z^2, -(y-x*z)}, {x*y-z, -(y-x*z), 1-x^2}}
traceSSigmaInv = trace(S*SigmaInv)
I = ideal((detSigma - traceSSigmaInv)*diff(x,detSigma) + detSigma*diff(x,traceSSigmaInv),
     (detSigma - traceSSigmaInv)*diff(y,detSigma) + detSigma*diff(y, traceSSigmaInv), 
     (detSigma - traceSSigmaInv)*diff(z, detSigma)+ detSigma*diff(z,traceSSigmaInv))
dim I
degree I
J = saturate(I,detSigma)
dim J
degree J
solveSystem J_*
zeroDimSolve J_*
toString J_*
 

-------
--for thesis:
loadPackage "EigenSolver";
R = QQ[x,y,z]
Sigma = matrix{{1,x,z}, {x,1,y}, {z,y,1}}
detSigma = det(Sigma)
A = random(ZZ^3, ZZ^3)
S = A*transpose(A)
M = matrix{{1-y^2, -(x-y*z), x*y-z}, {-(x-y*z), 1-z^2, -(y-x*z)}, {x*y-z, -(y-x*z), 1-x^2}}
trSM = trace(S*M);
I = ideal((detSigma-trSM)*diff(x,detSigma)+detSigma*diff(x,trSM), 
          (detSigma-trSM)*diff(y,detSigma)+detSigma*diff(y,trSM),
          (detSigma-trSM)*diff(z,detSigma)+detSigma*diff(z,trSM));
dim I
degree I
L = saturate(I,detSigma)
dim L
degree L
zeroDimSolve L







