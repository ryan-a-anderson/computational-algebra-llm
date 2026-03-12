--same state spaces
restart
r=2; n=5; d=2;
par = toList(a_(1,1,(1,1))..a_(n-1,r,(d,d))) -- first index is for the clique, second index is for the secant copy, last two are i1 i2
var = toList(p_(toSequence(apply(toList({0..n-1}_0), i->1)))..p_(toSequence(apply(toList({0..n-1}_0), i->d)))) -- need to change to n-tuples, not just 4

inds=toList((toSequence(apply(toList({0..n-1}_0), i->1)))..toSequence(apply(toList({0..n-1}_0), i->d)));
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

--Kaie's code: different state spaces (3-path only)
restart
r = 2
d1 = 4
d2 = 5
d3 = 4
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)))
probabilities = toList(x_(1,1,1)..x_(d1,d2,d3))
allVars = join(probabilities,pars)
R = QQ[allVars]

I = ideal flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list x_(i,j,k) -  sum for l from 1 to r list a_(l,i,j)*b_(l,j,k);
startIx = d1*d2*d3
endIx = d1*d2*d3 + r*(d1*d2+d2*d3)-1
endIx-startIx
K = eliminate (I,flatten entries (vars R)_{startIx..endIx})
codim K
degree K


--check dimension -- fails for a 3-path!
restart
r = 1
d1 = 2
d2 = 2
d3 = 4
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)))
probabilities = toList(x_(1,1,1)..x_(d1,d2,d3))
S=QQ[pars]
M = flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list  sum for l from 1 to r list a_(l,i,j)*b_(l,j,k);
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A
r*d2*(d1+d3-r) 
min(r*d2*(d1+d3-r),d1*d2*d3)

h=vector({-1,-1,1,1,1,-1,1,-1,-1,1,1,-1})
w=entries(transpose(A)*h)
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)))
r=sort unique(join(toSequence(r)))
h,A_l,A_r

rank A_l
rank A_r





--Terracini
restart
r = 2
d1 = 2
d2 = 3
d3 = 2
d4 = 2
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)), toList (c_(1,1,1)..c_(r,d3,d4)))
probabilities = toList(x_(1,1,1,1)..x_(d1,d2,d3,d4))
S=QQ[pars]
M = flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list  sum for l from 1 to r list a_(l,i,j)*b_(l,j,k)*c_(l,k,m);
nums={}; nums=apply(length(generators(S)), i -> random(1,100));
--nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A

h=vector({-1,1,-1,1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,1})
h=vector({1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,1})
--r*d2*(d1+d3-r) 
--min(r*d2*(d1+d3-r),d1*d2*d3)


--needsPackage "Polyhedra"
--P = convexHull A
--dim P
--faces(1,P)


for i from 1 to 1000 do
(
v=vector(toList apply(splice(1..16), i->sub(random(-1,1),QQ)));
w=entries(transpose(A)*v);
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)));
r=sort unique(join(toSequence(r)));
if rank A_l==11 and rank A_r==11 then print(v, A_l, A_r);
)

h=vector({-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1}) --very special


w=entries(transpose(A)*h)
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)))
r=sort unique(join(toSequence(r)))
h,A_l,A_r

rank A_l
rank A_r


convexHull(A_l)


P1=convexHull(A_l)
P2=convexHull(A_r)
facets(P1)
facets(P2)

dim intersection(P1,P2)



----------------------
--for a 5 path, when we append one more edge
restart
r = 1
d1 = 2
d2 = 3
d3 = 2
d4 = 2
d5 = 2
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)), toList (c_(1,1,1)..c_(r,d3,d4)), toList (d_(1,1,1)..d_(r,d4,d5)))
probabilities = toList(x_(1,1,1,1,1)..x_(d1,d2,d3,d4,d5))
S=QQ[pars]
M = flatten flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list for n from 1 to d5 list sum for l from 1 to r list a_(l,i,j)*b_(l,j,k)*c_(l,k,m)*d_(l,m,n);
--nums={}; nums=apply(length(generators(S)), i -> random(1,100));
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A


h=vector({-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,0,0,0,0})
w=entries(transpose(A)*h)
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)))
r=sort unique(join(toSequence(r)))
h,A_l,A_r

rank A_l
rank A_r
rank A

-----
restart
r = 1
d1 = 4
d2 = 2
d3 = 2
d4 = 2
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)), toList (c_(1,1,1)..c_(r,d3,d4)))
probabilities = toList(x_(1,1,1,1)..x_(d1,d2,d3,d4))
S=QQ[pars]
M = flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list  sum for l from 1 to r list a_(l,i,j)*b_(l,j,k)*c_(l,k,m);
--nums={}; nums=apply(length(generators(S)), i -> random(1,100));
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A

h=vector({1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1}) 
--h=vector({-1,-1,1,1,1,-1, 1,-1,1,-1,1,1,1,-1,-1, -1,1,-1,1,1,-1}) 




w=entries(transpose(A)*h)
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)))
r=sort unique(join(toSequence(r)))
h,A_l,A_r

rank A_l
rank A_r


-----
--gluing an edge in the middle
--for a 5 path, when we append one more edge
restart
r = 1
d1 = 2
d2 = 3
d3 = 2
d4 = 2
d5 = 2
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)), toList (c_(1,1,1)..c_(r,d3,d4)), toList (d_(1,1,1)..d_(r,d3,d5)))
probabilities = toList(x_(1,1,1,1,1)..x_(d1,d2,d3,d4,d5))
S=QQ[pars]
M = flatten flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list for n from 1 to d5 list sum for l from 1 to r list a_(l,i,j)*b_(l,j,k)*c_(l,k,m)*d_(l,m,n);
--nums={}; nums=apply(length(generators(S)), i -> random(1,100));
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A


h=vector({-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,0,0,0,0})
w=entries(transpose(A)*h)
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)))
r=sort unique(join(toSequence(r)))
h,A_l,A_r

rank A_l
rank A_r

rank A


------for a 6 path, when we append one more edge
restart
r = 1
d1 = 2
d2 = 3
d3 = 2
d4 = 2
d5 = 3
d6 = 3
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)), toList (c_(1,1,1)..c_(r,d3,d4)), toList (d_(1,1,1)..d_(r,d4,d5)), toList (e_(1,1,1)..e_(r,d5,d6)))
probabilities = toList(x_(1,1,1,1,1)..x_(d1,d2,d3,d4,d5))
S=QQ[pars]
M = flatten flatten flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list for n from 1 to d5 list for o from 1 to d6 list sum for l from 1 to r list a_(l,i,j)*b_(l,j,k)*c_(l,k,m)*d_(l,m,n)*e_(l,n,o);
--nums={}; nums=apply(length(generators(S)), i -> random(1,100));
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A


h=vector({-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0})
w=entries(transpose(A)*h)
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)))
r=sort unique(join(toSequence(r)))
h,A_l,A_r

rank A_l
rank A_r
rank A


----
--weird structure with a fork
restart
r = 1
d1 = 2
d2 = 3
d3 = 2
d4 = 2
d5 = 3
d6 = 3
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)), toList (c_(1,1,1)..c_(r,d3,d4)), toList (d_(1,1,1)..d_(r,d4,d5)), toList (e_(1,1,1)..e_(r,d5,d6)))
probabilities = toList(x_(1,1,1,1,1)..x_(d1,d2,d3,d4,d5))
S=QQ[pars]
M = flatten flatten flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list for n from 1 to d5 list for o from 1 to d6 list sum for l from 1 to r list a_(l,i,j)*b_(l,j,k)*c_(l,k,m)*d_(l,k,n)*e_(l,n,o);
--nums={}; nums=apply(length(generators(S)), i -> random(1,100));
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A


h=vector({-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0})
w=entries(transpose(A)*h)
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)))
r=sort unique(join(toSequence(r)))
h,A_l,A_r

rank A_l
rank A_r
rank A


----
--cycle
restart
r = 1
d1 = 4
d2 = 2
d3 = 2
d4 = 2
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)), toList (c_(1,1,1)..c_(r,d3,d4)),  toList (d_(1,1,1)..d_(r,d1,d4)))
probabilities = toList(x_(1,1,1,1)..x_(d1,d2,d3,d4))
S=QQ[pars]
M = flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list  sum for l from 1 to r list a_(l,i,j)*b_(l,j,k)*c_(l,k,m)*d_(l,i,m);
--nums={}; nums=apply(length(generators(S)), i -> random(1,100));
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A

h=vector({-1,1,-1,1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,0,0,0,0,0,0,0,0})  
h=vector({-1,1,-1,1,1,-1,1,-1, 1,-1,-1,1, 1,-1,1,-1, 1,-1,-1,1,-1,1,-1,1}) 
w=entries(transpose(A)*h)
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)))
r=sort unique(join(toSequence(r)))
h,A_l,A_r

rank A_l
rank A_r

 v=vector({1,-2,-2,1,-2,1,1,-3,-1,1,1,-1,-3,1,1,1,1,-3,1,-3,-1,1,1,1})

--test all hyperplanes with the same number of 1 and -1 in each chunk
for i from 1 to 50000 do
(
v=vector(toList apply(splice(1..24), i->sub({-2,-1,1,2}_(random(0,3)),QQ)));
--v=vector(toList apply(splice(1..24), i->sub(random(-2,2),QQ)));
w=entries(transpose(A)*v);
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)));
r=sort unique(join(toSequence(r)));
if rank A_l==15 and rank A_r==15 then print(v, A_l, A_r);
)


s1=subsets(8,4)
s2=subsets(4,2)
for el1 in s1 do
(for el2 in s2 do
    (for el3 in s2 do
	for el4 in s1 do
       	 (
	     c1=toList(apply(splice(0..7), i->(if member (i,el1) then 1 else -1)));
	     c2=toList(apply(splice(0..3), i->(if member (i,el2) then 1 else -1)));
	     c3=toList(apply(splice(0..3), i->(if member (i,el3) then 1 else -1)));
	     c4=toList(apply(splice(0..7), i->(if member (i,el4) then 1 else -1)));
	     v=vector(c1|c2|c3|c4);
	     w=entries(transpose(A)*v);
	     l={}; r={};
	     for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
	     l=sort unique(join(toSequence(l)));
	     r=sort unique(join(toSequence(r)));
	     if rank A_l==15 and rank A_r==15 then print(v, A_l, A_r);
	 ););print el1;)

----
--cycle the other way -- BAD
restart
r = 1
d1 = 2
d2 = 4
d3 = 2
d4 = 2
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)), toList (c_(1,1,1)..c_(r,d3,d4)),  toList (d_(1,1,1)..d_(r,d1,d4)))
probabilities = toList(x_(1,1,1,1)..x_(d1,d2,d3,d4))
S=QQ[pars]
M = flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list  sum for l from 1 to r list a_(l,i,j)*b_(l,j,k)*c_(l,k,m)*d_(l,i,m);
--nums={}; nums=apply(length(generators(S)), i -> random(1,100));
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A

h=vector({1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,1})  
w=entries(transpose(A)*h)
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)))
r=sort unique(join(toSequence(r)))
h,A_l,A_r

rank A_l
rank A_r




----
--5-cycle
restart
r = 1
d1 = 2
d2 = 4
d3 = 2
d4 = 2
d5 = 3
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)), toList (c_(1,1,1)..c_(r,d3,d4)),  toList (d_(1,1,1)..d_(r,d4,d5)), toList (e_(1,1,1)..e_(r,d4,d5)))
probabilities = toList(x_(1,1,1,1,1)..x_(d1,d2,d3,d4,d5))
S=QQ[pars]
M = flatten flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list for n from 1 to d5 list sum for l from 1 to r list a_(l,i,j)*b_(l,j,k)*c_(l,k,m)*d_(l,m,n)*e_(l,i,n);
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A


h=vector({1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,1,0,0,0,0,0,0,0,0,0,0,0,0})
w=entries(transpose(A)*h)
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)))
r=sort unique(join(toSequence(r)))
h,A_l,A_r

rank A_l
rank A_r
rank A


----
--4-cycle
restart
r = 1
d1 = 4
d2 = 3
d3 = 2
d4 = 2
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)), toList (c_(1,1,1)..c_(r,d3,d4)),  toList (d_(1,1,1)..d_(r,d1,d4)))
probabilities = toList(x_(1,1,1,1)..x_(d1,d2,d3,d4))
S=QQ[pars]
M = flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list  sum for l from 1 to r list a_(l,i,j)*b_(l,j,k)*c_(l,k,m)*d_(l,i,m);
--nums={}; nums=apply(length(generators(S)), i -> random(1,100));
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A

h=vector({-2,1,2,-1,-1,-2,1,1, 2,-2,-1,1, 2,-1,-2,2, 2,-2,1,1,-1,1,-1,-2}) -- for the 4-2-2-2 case

--copying first and second values, respectively
h=vector({-2,1,-2,2,-1,2,-1,-2,-1,1,1,1, 2,-2,-1,1,2,-2, 2,-1,-2,2, 2,-2,1,1,-1,1,-1,-2})  -- for the 4-3-2-2 case
h=vector({-2,1,1,2,-1,-1,-1,-2,-2,1,1,1, 2,-2,-1,1,-1,1, 2,-1,-2,2, 2,-2,1,1,-1,1,-1,-2}) --  for the 4-3-2-2 case

w=entries(transpose(A)*h)
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)))
r=sort unique(join(toSequence(r)))

rank A_l
rank A_r
rank A



----
restart
r = 1
d1 = 4
d2 = 3
d3 = 2
d4 = 2
d5 = 3
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)), toList (c_(1,1,1)..c_(r,d3,d4)),  toList (d_(1,1,1)..d_(r,d1,d4)), toList (e_(1,1,1)..e_(r,d2,d5)), toList (f_(1,1,1)..f_(r,d4,d5)))
probabilities = toList(x_(1,1,1,1,1)..x_(d1,d2,d3,d4,d5))
S=QQ[pars]
M = flatten flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list for n from 1 to d5 list  sum for l from 1 to r list a_(l,i,j)*b_(l,j,k)*c_(l,k,m)*d_(l,i,m)*e_(l,j,n)*f_(l,m,n);
--nums={}; nums=apply(length(generators(S)), i -> random(1,100));
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A

h=vector({-2,1,2,-1,-1,-2,1,1, 2,-2,-1,1, 2,-1,-2,2, 2,-2,1,1,-1,1,-1,-2,0,0,0,0,0,0,0,0,0,0,0,0}) -- for the 4-2-2-2 case
h=vector({-2,1,-2,2,-1,2,-1,-2,-1,1,1,1, 2,-2,-1,1,2,-2, 2,-1,-2,2, 2,-2,1,1,-1,1,-1,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}) -- for the 4-3-2-2 case

w=entries(transpose(A)*h)
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)))
r=sort unique(join(toSequence(r)))

rank A_l
rank A_r
rank A


----
----
----
--getting hyperplanes for base cases

--2-3-2-3 cycle
restart
r = 1
d1 = 2
d2 = 3
d3 = 2
d4 = 3
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)), toList (c_(1,1,1)..c_(r,d3,d4)),  toList (d_(1,1,1)..d_(r,d1,d4)))
probabilities = toList(x_(1,1,1,1)..x_(d1,d2,d3,d4))
S=QQ[pars]
M = flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list  sum for l from 1 to r list a_(l,i,j)*b_(l,j,k)*c_(l,k,m)*d_(l,i,m);
--nums={}; nums=apply(length(generators(S)), i -> random(1,100));
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A


for i from 1 to 10000 do
(
v=vector(toList apply(splice(1..24), i->sub({-3,-2,-1,1,2,3}_(random(0,5)),QQ)));
--v=vector(toList apply(splice(1..24), i->sub(random(-2,2),QQ)));
w=entries(transpose(A)*v);
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)));
r=sort unique(join(toSequence(r)));
if rank A_l==15 and rank A_r==15 then print(toString(v));
)

---
---
---

--2-3-2-3 cycle
restart
r = 1
d1 = 2
d2 = 3
d3 = 2
d4 = 3
d5 = 2
d6 = 2
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d1,d4)), toList (c_(1,1,1,1)..c_(r,d2,d3,d5)),  toList (d_(1,1,1,1)..d_(r,d3,d4,d6)))
probabilities = toList(x_(1,1,1,1,1,1)..x_(d1,d2,d3,d4,d5,d6))
S=QQ[pars]
M = flatten flatten flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list  for n from 1 to d5 list  for o from 1 to d6 list sum for l from 1 to r list a_(l,i,j)*b_(l,i,m)*c_(l,j,k,n)*d_(l,k,m,o);
 
--nums={}; nums=apply(length(generators(S)), i -> random(1,100));
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A


for i from 1 to 100 do
(
--v=vector(toList apply(splice(1..36), i->sub({-3,-2,-1,1,2,3}_(random(0,5)),QQ)));
v=vector(toList apply(splice(1..36), i->sub(random(-10,10),QQ)));
w=entries(transpose(A)*v);
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)));
r=sort unique(join(toSequence(r)));
if rank A_l==27 and rank A_r==27 then print(toString(v));
)

v= vector {10, -3, 3, -10, -8, 6, -6, 5, -7, 3, 1, 1, 7, -4, 10, 6, -8, -4, -8, 10, 5, -5, 10, -6, -3, -1, 8, -3, 1, 4, -10, 7, 0, 9, -5, 2}


---
restart
r = 1
d1 = 2
d2 = 3
d3 = 2
d4 = 3
d5 = 2
d6 = 2
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d1,d4)), toList (c_(1,1,1,1)..c_(r,d2,d3,d5)),  toList (d_(1,1,1,1)..d_(r,d3,d4,d6)), toList  (e_(1,1,1,1)..e_(r,d3,d5,d6)))
probabilities = toList(x_(1,1,1,1,1,1)..x_(d1,d2,d3,d4,d5,d6))
S=QQ[pars]
M =flatten flatten flatten flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list  for n from 1 to d5 list  for o from 1 to d6 list sum for l from 1 to r list a_(l,i,j)*b_(l,i,m)*c_(l,j,k,n)*d_(l,k,m,o)*e_(l,k,n,o);
 
--nums={}; nums=apply(length(generators(S)), i -> random(1,100));
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A


for i from 1 to 100 do
(
--v=vector(toList apply(splice(1..36), i->sub({-3,-2,-1,1,2,3}_(random(0,5)),QQ)));
v=vector(toList apply(splice(1..36), i->sub(random(-10,10),QQ)));
w=entries(transpose(A)*v);
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)));
r=sort unique(join(toSequence(r)));
if rank A_l==27 and rank A_r==27 then print(toString(v));
)

v= vector {10, -3, 3, -10, -8, 6, -6, 5, -7, 3, 1, 1, 7, -4, 10, 6, -8, -4, -8, 10, 5, -5, 10, -6, -3, -1, 8, -3, 1, 4, -10, 7, 0, 9, -5, 2,0,0,0,0,0,0,0,0}
w=entries(transpose(A)*v);
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)));
r=sort unique(join(toSequence(r)));
rank A_l
rank A_r
rank A

---
---
---

restart
r = 1
d1 = 2
d2 = 3
d3 = 2
d4 = 3
d5 = 2
d6 = 2
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d1,d4)), toList (c_(1,1,1,1)..c_(r,d2,d3,d5)),  toList (d_(1,1,1,1)..d_(r,d3,d4,d6)), toList  (e_(1,1,1,1)..e_(r,d3,d5,d6)))
probabilities = toList(x_(1,1,1,1,1,1)..x_(d1,d2,d3,d4,d5,d6))
S=QQ[pars]
M =flatten flatten flatten flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list  for n from 1 to d5 list  for o from 1 to d6 list sum for l from 1 to r list a_(l,i,j)*b_(l,i,m)*c_(l,j,k,n)*d_(l,k,m,o)*e_(l,k,n,o);
 
--nums={}; nums=apply(length(generators(S)), i -> random(1,100));
nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rank A


for i from 1 to 100 do
(
--v=vector(toList apply(splice(1..36), i->sub({-3,-2,-1,1,2,3}_(random(0,5)),QQ)));
v=vector(toList apply(splice(1..36), i->sub(random(-10,10),QQ)));
w=entries(transpose(A)*v);
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)));
r=sort unique(join(toSequence(r)));
if rank A_l==27 and rank A_r==27 then print(toString(v));
)


v=vector {2, 3, -3, 2, 2, -2, -2, -1, -3, -3, -1, 1, -1, 1, 3, 2, 3, -1, 2, -2, -2, -2, 1, 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}


w=entries(transpose(A)*v);
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)));
r=sort unique(join(toSequence(r)));
rank A_l
rank A_r
rank A





--------------------------
--------------------------
--------------------------
-- general code

-- to generate a hyperplane 
restart
n = 4 -- # vertices
d_1 = 4
d_2 = 2
d_3 = 2
d_4 = 2
ds=(d_1,d_2,d_3,d_4)

cliques = ((1,2),(2,3),(3,4),(1,4))
c = length(cliques)

pz = {}; for j from 1 to c do (k=length(cliques#(j-1)); cliquez = apply(cliques, (i -> apply(i, j-> d_j))); pz=append(pz, toList (a_(j, toSequence apply(k,i->1))..a_(j,cliquez#(j-1))) ))
pars = join(toSequence pz)
inds = toList(toSequence apply(n,i->1)..ds)

S=QQ[pars]
M={}; for i in inds do (prod=1; for j from 1 to c do (prod=prod*a_(j,toSequence(i_(toList (cliques#(j-1)) / (i->i-1))));); M=append(M,prod);)

nums={}; nums=apply(length(generators(S)), i -> 1);
toNums=map(QQ,S,nums);
J=jacobian(ideal(M));
A=toNums(J);
rk=rank A

-- to FIND a hyperplane:
for i from 1 to 1000 do
(
--v=vector(toList apply(splice(1..length(pars)), i->sub({-3,-2,-1,1,2,3}_(random(0,5)),QQ)));
v=vector(toList apply(splice(1..length(pars)), i->sub(random(-10,10),QQ)));
w=entries(transpose(A)*v);
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)));
r=sort unique(join(toSequence(r)));
if rank A_l==rk and rank A_r==rk then print(toString(v));
)



-- to TEST find a hyperplane:
v=vector({-5, 9, 5, 7, 7, -10, -7, -10, 10, -5, -7, 6, -3, -1, 3, -5, -4, 2, -10, -1, 4, -10, 2, 7}) --your huperplane goes here
w=entries(transpose(A)*v);
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)));
r=sort unique(join(toSequence(r)));

rank A_l
rank A_r
rk
