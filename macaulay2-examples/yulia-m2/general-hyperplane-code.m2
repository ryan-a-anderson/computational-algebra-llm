--------------------------
--------------------------
--------------------------
-- general code

restart
n = 6 -- # vertices
d_1 = 2
d_2 = 2
d_3 = 2
d_4 = 2
d_5 = 2
d_6 = 2
ds=(d_1,d_2,d_3,d_4,d_5,d_6)

cliques = ((1,2,6),(2,3),(3,4),(4,5,6))
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

--------------------------
--------------------------
--------------------------
-- to FIND a hyperplane:
for i from 1 to 100 do
(
--v=vector(toList apply(splice(1..length(pars)), i->sub({-1,1}_(random(0,1)),QQ)));
v=vector(toList apply(splice(1..length(pars)), i->sub(random(-10,10),QQ)));
w=entries(transpose(A)*v);
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)));
r=sort unique(join(toSequence(r)));
if rank A_l==rk and rank A_r==rk then print(toString(v));
)


--------------------------
--------------------------
--------------------------
-- to TEST find a hyperplane:

v=vector({(1, -1, -1, 1,  -1, 1, -1, -1, -1, 1)}) --your hyperplane goes here

w=entries(transpose(A)*v);
l={}; r={};
for el in w do (if el<0 then l=append(l, positions(w,j->j==el)) else if el>0 then r=append(r, positions(w,j->j==el)) );
l=sort unique(join(toSequence(l)));
r=sort unique(join(toSequence(r)));

rank A_l
rank A_r
rk

v=vector({(-5, -5, -8, -8, 4, 4, 1, 1,   0, -2, 0, -2,   9, -8, 6, 6,   2,2, -4,-4, 5,5 ,-1,-1)})
