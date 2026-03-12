R=QQ[g13,g14,g22,g23,g24,g33,g34,g44]
SigmaPrime = matrix{{(g13*g14*g23^2 - g13^2*g23*g24 - g13*g14*g22*g33 + g13^2*g22*g34)*(g24*g33 - g23*g34), (g14*g23^2 - g13*g23*g24 - g14*g22*g33 + g13*g22*g34)*(g23*g24*g33 - g23^2*g34), -(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)*g13, -(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)*g14},{(g14*g23^2 - g13*g23*g24 - g14*g22*g33 + g13*g22*g34)*(g23*g24*g33 - g23^2*g34), -(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)*g22, -(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)*g23, -(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)*g24},{-(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)*g13, -(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)*g23, -(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)*g33, -(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)*g34},{(-(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)*g14, -(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)*g24, -(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)*g34, -(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)*g44)}}
detSigmaPrime = det(SigmaPrime)
A = random(ZZ^4, ZZ^4)
S = A*transpose(A)
denom=-(g23*g24*g33 - g23^2*g34)*(g24*g33 - g23*g34)
T = frac R
F = map(T,R,{g13,g14,g22,g23,g24,g33,g34,g44})
fracSigmaPrime=F(SigmaPrime)
fracDetSigmaPrime=F(detSigmaPrime)
fracSigmaInv=inverse(fracSigmaPrime)*fracDetSigmaPrime*denom

R=QQ[g13,g14,g22,g23,g24,g33,g34,g44]
U=map(R,T,{g13,g14,g22,g23,g24,g33,g34,g44})
SigmaInv=U(fracSigmaInv)
traceSSigmaInv = trace(S*SigmaInv)
detSigmaPrime=U(detSigmaPrime)
I = ideal((detSigmaPrime - traceSSigmaInv)*diff(g13,detSigmaPrime) + detSigmaPrime*diff(g13,traceSSigmaInv), (detSigmaPrime - traceSSigmaInv)*diff(g14,detSigmaPrime) + detSigmaPrime*diff(g14, traceSSigmaInv), (detSigmaPrime - traceSSigmaInv)*diff(g22, detSigmaPrime)+ detSigmaPrime*diff(g22,traceSSigmaInv),(detSigmaPrime - traceSSigmaInv)*diff(g23, detSigmaPrime)+ detSigmaPrime*diff(g23,traceSSigmaInv),(detSigmaPrime - traceSSigmaInv)*diff(g24, detSigmaPrime)+ detSigmaPrime*diff(g24,traceSSigmaInv),(detSigmaPrime - traceSSigmaInv)*diff(g33, detSigmaPrime)+ detSigmaPrime*diff(g33,traceSSigmaInv),(detSigmaPrime - traceSSigmaInv)*diff(g34, detSigmaPrime)+ detSigmaPrime*diff(g34,traceSSigmaInv),(detSigmaPrime - traceSSigmaInv)*diff(g44, detSigmaPrime)+ detSigmaPrime*diff(g44,traceSSigmaInv))
(detSigmaPrime - traceSSigmaInv)*diff(g13,detSigmaPrime)
dim I
degree I
