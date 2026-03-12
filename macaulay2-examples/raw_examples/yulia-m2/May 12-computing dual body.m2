loadPackage "Resultants"; loadPackage "NumericalAlgebraicGeometry";
--first we find the polynomial defining the algebraic boundary of the dual body, call it g
R = QQ[x,y,t]
f = (x^2 - 1)*y^2 - x^2 - 1/126*(109*x - 111)*y + 37/42*x + 5941/63504
fhom = homogenize(f,t)
fdualhom = dualVariety(ideal(fhom))
fdual = sub(fdualhom, {t=>1})
g=fdual_0

--now we compute the ideal of the singular locus
I=ideal(diff(x,g),diff(y,g),g)
dim I

--this ideal currently lives in the ring R, but we need for it to live
S = QQ[x,y]
m=map(S,R,{x,y,0})
J=m(I); dim J
solveSystem(J_*)
