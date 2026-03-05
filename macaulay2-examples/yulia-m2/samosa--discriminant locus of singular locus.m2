loadPackage "Resultants";
R = QQ[x,y,z,b1,b2,b3]
M = matrix {
    {4*x,b3-2*x-2*y-2*z,b2-2*x-2*y-2*z},
    {b3-2*x-2*y-2*z,4*y,b1-2*x-2*y-2*z},
    {b2-2*x-2*y-2*z,b1-2*x-2*y-2*z,4*z}};
sing=minors(2,M) -- singular locus ideal
eliminate(sing,{x,y,z})

S =(frac QQ[b1,b2,b3])[x,y,z] -- this ring will allow us to get jacobian wrt to x,y,z only

m=map(S,R,{x,y,z,b1,b2,b3}); R = QQ[x,y,z,b1,b2,b3]; --map from ring R to ring S 
minv=map(R,S,{x,y,z,b1,b2,b3}) -- map from ring S back to ring R

m(sing) 
Jac=jacobian(m(sing)) -- need Jacobian wrt to x,y,z
J=minors(3,Jac) -- this is discriminant locus of singular locus
singsing=m(sing)+J -- 72 gens
JJ=minv(singsing) -- move this ideal back to R to eliminate variables
eliminate(JJ,{x,y,z}) -- get D!



-- Let's compute H^*
R = QQ[x,y,z,w,b1,b2,b3]
M = matrix {
    {4*x,b3-2*x-2*y-2*z,b2-2*x-2*y-2*z},
    {b3-2*x-2*y-2*z,4*y,b1-2*x-2*y-2*z},
    {b2-2*x-2*y-2*z,b1-2*x-2*y-2*z,4*z}};
f=det M
homf=homogenize(f,w,toList(4:1)|toList(3:0))


newR=QQ[x,y,z,w,b1,b2,b3, a,b,c,d]
n=map(newR,R,{x,y,z,w,b1,b2,b3})
g=n(homf)

I=ideal(a*diff(x,g)+b*diff(y,g)+c*diff(z,g)+d*diff(w,g),g)
eliminate(I,{x,y,z}) -- I don't think we should eliminate w! but then we get the empty ideal?

