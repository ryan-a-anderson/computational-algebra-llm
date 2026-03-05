restart
r=2; n=4; d=3;
par = toList(a_(1,1,(1,1))..a_(n-1,r,(d,d))) -- first index is for the clique, second index is for the secant copy, last two are i1 i2
var = toList(p_(1,1,1,1)..p_(toSequence(apply(toList({0..n-1}_0), i->d)))) -- need to change to n-tuples, not just 4

inds=toList((1,1,1,1)..toSequence(apply(toList({0..n-1}_0), i->d)));
S = QQ[par]
M=apply(toList({0..d^n-1}_0), i->0);

for k from 1 to r do
{Mx={}; for j in inds do (prod=1; for i from 1 to n-1 do 
(prod=prod*a_(i,k,(j#(i-1), j#i));); Mx=append(Mx,prod););
M=M+Mx;};

nums={}; nums=apply(length(generators(S)), i -> random(1,100));
toNums=map(QQ,S,nums);
A=toNums(jacobian(ideal(M)));

rank A


R=QQ[var]
f=map(S,R,M); 
I=ker f; 
