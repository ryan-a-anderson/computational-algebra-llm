R=QQ[s11,s12,s13,s22,s23,s33]
I=ideal(s13,s12*s23-s22*s13)
dim I
codim I

--------Matrices of the first kind--------
R=QQ[t1,t2,t3,t4]
Sigma = matrix{{t1,0,0}, {0,t2,t3}, {0,t3,t4}}
detSigma = det(Sigma)
A = random(ZZ^3, ZZ^3)
S = A*transpose(A)
SigmaInv = matrix{{-t3^2 + t2*t4,0,0},{0,t1*t4,-t1*t3},{0,-t1*t3,t1*t2}}
traceSSigmaInv = trace(S*SigmaInv)
I = ideal((detSigma - traceSSigmaInv)*diff(t1,detSigma) + detSigma*diff(t1,traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(t2,detSigma) + detSigma*diff(t2, traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(t3, detSigma)+ detSigma*diff(t3,traceSSigmaInv),(detSigma - traceSSigmaInv)*diff(t4, detSigma)+ detSigma*diff(t4,traceSSigmaInv))
dim I
degree I
J = saturate(I,detSigma)
dim J
degree J
T = QQ[t1,t2,t3,t4,MonomialOrder=>Lex]
F = map(T,R,{t1,t2,t3,t4})
JJ = F(J)
gens gb JJ

--------Matrices of the second  kind--------
R=QQ[s1,s2,s3,s4]
Sigma = matrix{{s1,s2,0}, {s2,s3,0}, {0,0,s4}}
detSigma = det(Sigma)
SigmaInv = matrix{{s3*s4,-s2*s4,0},{-s2*s4,s1*s4,0},{0,0,-s2^2 + s1*s3}}
traceSSigmaInv = trace(S*SigmaInv)
I = ideal((detSigma - traceSSigmaInv)*diff(s1,detSigma) + detSigma*diff(s1,traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(s2,detSigma) + detSigma*diff(s2, traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(s3, detSigma)+ detSigma*diff(s3,traceSSigmaInv),(detSigma - traceSSigmaInv)*diff(s4, detSigma)+ detSigma*diff(s4,traceSSigmaInv))
dim I
degree I
J = saturate(I,detSigma)
dim J
degree J
T = QQ[s1,s2,s3,s4,MonomialOrder=>Lex]
F = map(T,R,{s1,s2,s3,s4})
JJ = F(J)
gens gb JJ


--------General case--------
F=frac QQ[s11,s12,s13,s22,s23,s33]
R=F[s1,s2,s3,s4]
Sigma = Sigma = matrix{{s1,s2,0}, {s2,s3,0}, {0,0,s4}}
detSigma = det(Sigma)
S=matrix{{s11,s12,s13},{s12,s22,s23},{s13,s23,s33}}
SigmaInv = matrix{{s3*s4,-s2*s4,0},{-s2*s4,s1*s4,0},{0,0,-s2^2 + s1*s3}}
traceSSigmaInv = trace(S*SigmaInv)
I = ideal((detSigma - traceSSigmaInv)*diff(s1,detSigma) + detSigma*diff(s1,traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(s2,detSigma) + detSigma*diff(s2, traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(s3, detSigma)+ detSigma*diff(s3,traceSSigmaInv),(detSigma - traceSSigmaInv)*diff(s4, detSigma)+ detSigma*diff(s4,traceSSigmaInv))
dim I
degree I
J = saturate(I,detSigma)
dim J
degree J
