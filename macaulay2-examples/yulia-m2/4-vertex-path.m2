R=QQ[t1,t2,t3,t4,t5,t6,t7]
SigmaPrime=matrix{{t1*t4, t2*t3, t2*t4, 0},{t2*t3, t3*t4, t4^2, 0},{t2*t4, t4^2, t4*t5, t4*t6},{0, 0, t4*t6, t4*t7}}
detSigmaPrime = det(SigmaPrime)
A = random(ZZ^4, ZZ^4)
S = A*transpose(A)
denom=t4
T = frac R
F = map(T,R,{t1,t2,t3,t4,t5,t6,t7})
fracSigmaPrime=F(SigmaPrime)
fracDetSigmaPrime=F(detSigmaPrime)
fracSigmaInv=inverse(fracSigmaPrime)*fracDetSigmaPrime

R=QQ[t1,t2,t3,t4,t5,t6,t7]
U=map(R,T,{t1,t2,t3,t4,t5,t6,t7})
SigmaInv=U(fracSigmaInv)
traceSSigmaInv = trace(S*SigmaInv)
detSigmaPrime=U(detSigmaPrime)
I = ideal((detSigmaPrime - traceSSigmaInv)*diff(t1,detSigmaPrime) + detSigmaPrime*diff(t1,traceSSigmaInv), (detSigmaPrime - traceSSigmaInv)*diff(t2,detSigmaPrime) + detSigmaPrime*diff(t2, traceSSigmaInv), (detSigmaPrime - traceSSigmaInv)*diff(t3, detSigmaPrime)+ detSigmaPrime*diff(t3,traceSSigmaInv),(detSigmaPrime - traceSSigmaInv)*diff(t4, detSigmaPrime)+ detSigmaPrime*diff(t4,traceSSigmaInv),(detSigmaPrime - traceSSigmaInv)*diff(t5, detSigmaPrime)+ detSigmaPrime*diff(t5,traceSSigmaInv),(detSigmaPrime - traceSSigmaInv)*diff(t6, detSigmaPrime)+ detSigmaPrime*diff(t6,traceSSigmaInv),(detSigmaPrime - traceSSigmaInv)*diff(t7, detSigmaPrime)+ detSigmaPrime*diff(t7,traceSSigmaInv))
dim I
degree I
J=saturate(I, detSigmaPrime*U(denom))
dim J
degree J
loadPackage "NumericalAlgebraicGeometry"
solveSystem J_*


-----------------------------------------
F=frac QQ[s11,s12,s13,s14,s22,s23,s24,s33,s34,s44]
R=F[t1,t2,t3,t4,t5,t6,t7]
SigmaPrime=matrix{{t1*t4, t2*t3, t2*t4, 0},{t2*t3, t3*t4, t4^2, 0},{t2*t4, t4^2, t4*t5, t4*t6},{0, 0, t4*t6, t4*t7}}
detSigmaPrime = det(SigmaPrime)
S= matrix{{s11,s12,s13,s14},{s12,s22,s23,s24},{s13,s23,s33,s34},{s14,s24,s34,s44}}
denom=t4
T = frac (QQ[t1,t2,t3,t4,t5,t6,t7])
G = map(T,R,{t1,t2,t3,t4,t5,t6,t7})
fracSigmaPrime=G(SigmaPrime)
fracDetSigmaPrime=G(detSigmaPrime)
fracSigmaInv=inverse(fracSigmaPrime)*fracDetSigmaPrime


R=F[t1,t2,t3,t4,t5,t6,t7]
U=map(R,T,{t1,t2,t3,t4,t5,t6,t7})
SigmaInv=U(fracSigmaInv)
traceSSigmaInv = trace(S*SigmaInv)
detSigmaPrime=U(G(detSigmaPrime))
I = ideal((detSigmaPrime - traceSSigmaInv)*diff(t1,detSigmaPrime) + detSigmaPrime*diff(t1,traceSSigmaInv), (detSigmaPrime - traceSSigmaInv)*diff(t2,detSigmaPrime) + detSigmaPrime*diff(t2, traceSSigmaInv), (detSigmaPrime - traceSSigmaInv)*diff(t3, detSigmaPrime)+ detSigmaPrime*diff(t3,traceSSigmaInv),(detSigmaPrime - traceSSigmaInv)*diff(t4, detSigmaPrime)+ detSigmaPrime*diff(t4,traceSSigmaInv),(detSigmaPrime - traceSSigmaInv)*diff(t5, detSigmaPrime)+ detSigmaPrime*diff(t5,traceSSigmaInv),(detSigmaPrime - traceSSigmaInv)*diff(t6, detSigmaPrime)+ detSigmaPrime*diff(t6,traceSSigmaInv),(detSigmaPrime - traceSSigmaInv)*diff(t7, detSigmaPrime)+ detSigmaPrime*diff(t7,traceSSigmaInv))
dim I
degree I
J=saturate(I, detSigmaPrime*t4)
dim J
degree J
loadPackage "NumericalAlgebraicGeometry"
solveSystem J_*


-------------------------------
Z=F[t1,t2,t3,t4,t5,t6,t7, MonomialOrder=>Lex]
L=map(Z,R,{t1,t2,t3,t4,t5,t6,t7})
JJ=L(J)
degree JJ
dim JJ
