F=frac QQ[t]
R=F[x,y,z]
Sigma = matrix{{1,x,z}, {x,1,y}, {z,y,1}}
detSigma = det(Sigma)
S=matrix{{t,0,0},{0,t,0},{0,0,t}}
SigmaInv = matrix{{1-y^2, -(x-y*z), x*y-z}, {-(x-y*z), 1-z^2, -(y-x*z)}, {x*y-z, -(y-x*z), 1-x^2}}
traceSSigmaInv = trace(S*SigmaInv)
I = ideal((detSigma - traceSSigmaInv)*diff(x,detSigma) + detSigma*diff(x,traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(y,detSigma) + detSigma*diff(y, traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(z, detSigma)+ detSigma*diff(z,traceSSigmaInv))
dim I
degree I
J = saturate(I,detSigma)
dim J
degree J
T = F[x,y,z,MonomialOrder=>Lex]
M = map(T,R,{x,y,z})
JJ = M(J)
gens gb JJ

leadTerm(JJ)

f=4*z^7+(-t^2+18*t-9)*z^5+(-2*t^3+25*t^2-24*t+6)*z^3+(8*t^3-12*t^2+6*t-1)*z
factor f
----------------FOR t=1----------------

R = QQ[x,y,z]
Sigma = matrix{{1,x,z}, {x,1,y}, {z,y,1}}
detSigma = det(Sigma)
S=matrix{{1,0,0},{0,1,0},{0,0,1}}
SigmaInv = matrix{{1-y^2, -(x-y*z), x*y-z}, {-(x-y*z), 1-z^2, -(y-x*z)}, {x*y-z, -(y-x*z), 1-x^2}}
traceSSigmaInv = trace(S*SigmaInv)
I = ideal((detSigma - traceSSigmaInv)*diff(x,detSigma) + detSigma*diff(x,traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(y,detSigma) + detSigma*diff(y, traceSSigmaInv), (detSigma - traceSSigmaInv)*diff(z, detSigma)+ detSigma*diff(z,traceSSigmaInv))
dim I
degree I
J = saturate(I,detSigma)
dim J
degree J
T = QQ[x,y,z,MonomialOrder=>Lex]
M = map(T,R,{x,y,z})
JJ = M(J)
gens gb JJ

leadTerm JJ
