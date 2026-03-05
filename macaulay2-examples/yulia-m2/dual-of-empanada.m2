loadPackage "Resultants";
--b1=665, b2=463, b3=407 will give an empanada!
R = QQ[x,y,z,w]
M = matrix {
    {4*x,407-2*x-2*y-2*z,463-2*x-2*y-2*z},
    {407-2*x-2*y-2*z,4*y,665-2*x-2*y-2*z},
    {463-2*x-2*y-2*z,665-2*x-2*y-2*z,4*z}};
f=det(M)
homf=homogenize(f,w)
dualVar=dualVariety(ideal(homf))
S=QQ[x,y,z]; m=map(S,R,{x,y,z,0})
fdual=m((sub(dualVar, {w=>1}))_0)
sing=ideal(fdual,diff(x,fdual),diff(y,fdual),diff(z,fdual))
dim sing -- one-dimensional singular locus on algebraic boundary?? wrong
--singularLocus(sing)
