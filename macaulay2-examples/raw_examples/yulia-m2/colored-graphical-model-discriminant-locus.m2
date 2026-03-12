loadPackage "Resultants";
R = QQ[x,y,z,u,v,b1,b2,b3,b4,b5]
M = matrix {
    {y, b3/2, z, b4/2-v},
    {b3/2, b1-y, v, u},
    {z, v, b2-x, b5/2},
    {b4/2-v, u, b5/2, x}};
sing=minors(3,M) --singular locus is 2-dimensional!

S =(frac QQ[b1,b2,b3,b4,b5])[x,y,z,u,v] -- this ring will allow us to get jacobian wrt to x,y,z,u,v only
m=map(S,R,{x,y,z,u,v,b1,b2,b3,b4,b5}); R = QQ[x,y,z,u,v,b1,b2,b3,b4,b5]; --map from ring R to ring S 
minv=map(R,S,{x,y,z,u,v,b1,b2,b3,b4,b5}) -- map from ring S back to ring R
 
m(sing)
Jac=jacobian(m(sing)) -- need Jacobian wrt to x,y,z,u,v
J=minors(3,Jac); -- codimension of sing is 3

singsing=m(sing)+J;
JJ=minv(singsing);

EI=eliminate(JJ,{x,y,z,u,v})
D=EI_0
factor(D)  -- precisely alg boundary of the cone of sufficient statistics (up to a power of the factor), look at (33) in Sturmfels-Uhler

