restart
needsPackage "MultigradedImplicitization"
r=2; n=5; d=2;
pars = toList(a_(1,1,(1,1))..a_(n-1,r,(d,d))) -- first index is for the clique, second index is for the secant copy, last two are i1 i2
 -- need to change to n-tuples, not just 4


inds=toList((toSequence(apply(toList({0..n-1}_0), i->1)))..toSequence(apply(toList({0..n-1}_0), i->d)));
probabilities= toList(p_(1,1,1,1,1)..p_(2,2,2,2,2))

R=QQ[probabilities]
S=QQ[pars]

M=apply(toList({0..d^n-1}_0), i->0);

for k from 1 to r do
{Mx={}; for j in inds do (prod=1; for i from 1 to n-1 do
(prod=prod*a_(i,k,(j#(i-1), j#i));); Mx=append(Mx,prod););
M=M+Mx;};


phi = map(S,R,M);

G = componentsOfKernel(6,phi);
G = flatten values G;


