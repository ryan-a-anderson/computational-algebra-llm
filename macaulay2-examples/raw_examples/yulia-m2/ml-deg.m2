---works for complete intersections only; fix d1=d3=3, vary d2
--Approach from Jose+Elizabeth paper
restart
r = 2
d1 = 5
d2 = 2
d3 = 3
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)))
probabilities = toList(p_(1,1,1)..p_(d1,d2,d3))
allVars = join(probabilities,pars)
R = QQ[allVars]

I = ideal flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list p_(i,j,k) -  sum for l from 1 to r list a_(l,i,j)*b_(l,j,k);
startIx = d1*d2*d3
endIx = d1*d2*d3 + r*(d1*d2+d2*d3)-1
endIx-startIx
k = eliminate (I,flatten entries (vars R)_{startIx..endIx});
codim k
numgens k

ls=splice{l_1..l_d2}; 
S=QQ[join(probabilities,ls)];
probabilities = toList(p_(1,1,1)..p_(d1,d2,d3))
m=map(S,R,join(probabilities,toList apply(length(pars),i->0)))
K=m(k);--degree K

probabilities = toList(p_(1,1,1)..p_(d1,d2,d3)); len=length(probabilities);
u=apply(len,i->sub(random(1,100),QQ))

J=transpose(submatrix'(jacobian(K), splice({len..len+3}),));

probabilities = toList(p_(1,1,1)..p_(d1,d2,d3))
u=apply(len,i->sub(random(1,100),QQ))

newJ=matrix(probabilities_0*J_0);
for i from 1 to len-1 do (newJ=newJ|matrix(probabilities_i*J_i));
newJ=matrix({probabilities})||newJ; --this is the jacobian together with the simplex equation
obj=matrix{apply(splice({0..len-1}), i-> u_i)}
augJ=newJ||obj; --this is the augmented Jacobian

Lker=matrix{{-sum(u),l_1..l_d2,1}}
sys=Lker*augJ;

I=ideal(join((flatten entries sys),{sum(probabilities)-1}))+m(k);
degree I --10^d2
dim I




---------------------------------------------------------------------
---------------------------------------------------------------------
---------------------------------------------------------------------
---non-complete intersections only; fix d1=d3=3, vary d2
--Approach from Jose+Elizabeth paper

restart
loadPackage("Depth");

makeCompleteIntersectionIdeal=(myIdeal)->(
    	c:=codim myIdeal;
	gensMyIdeal:=flatten entries gens myIdeal;
	nGens:=#gensMyIdeal;
	subsetsGens:=subsets(nGens,c);
	for i to #subsetsGens-1 do (
	    mySubset:=subsetsGens#i;
	    newGens:=mySubset/(x->gensMyIdeal#x);
	    if(isRegularSequence(newGens)) then (
		return ideal(newGens);
	    );
        );
	return ideal(0);
    )

r = 2
d1 = 4
d2 = 4
d3 = 3
pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)))
probabilities = toList(p_(1,1,1)..p_(d1,d2,d3))
allVars = join(probabilities,pars)
R = QQ[allVars]

I = ideal flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list p_(i,j,k) -  sum for l from 1 to r list a_(l,i,j)*b_(l,j,k);
startIx = d1*d2*d3
endIx = d1*d2*d3 + r*(d1*d2+d2*d3)-1
endIx-startIx
k = eliminate (I,flatten entries (vars R)_{startIx..endIx});
c=codim k
numgens k
 
ls=splice{l_1..l_c}; 
S=QQ[join(probabilities,ls)];
probabilities = toList(p_(1,1,1)..p_(d1,d2,d3))
m=map(S,R,join(probabilities,toList apply(length(pars),i->0)))
K=makeCompleteIntersectionIdeal(m(k));--degree K


probabilities = toList(p_(1,1,1)..p_(d1,d2,d3)); len=length(probabilities);
u=apply(len,i->sub(random(1,100),QQ))

J=transpose(submatrix'(jacobian(K), splice({len..len+3}),));

probabilities = toList(p_(1,1,1)..p_(d1,d2,d3))
u=apply(len,i->sub(random(1,100),QQ))

newJ=matrix(probabilities_0*J_0);
for i from 1 to len-1 do (newJ=newJ|matrix(probabilities_i*J_i));
newJ=matrix({probabilities})||newJ; --this is the jacobian together with the simplex equation
obj=matrix{apply(splice({0..len-1}), i-> u_i)}
augJ=newJ||obj; --this is the augmented Jacobian

Lker=matrix{{-sum(u),l_1..l_c,1}}
sys=Lker*augJ;

I=ideal(join((flatten entries sys),{sum(probabilities)-1}))+m(k);
degree I 
dim I






---
newgens={}
for i from 0 to c-1 do
(
    newg=0;
    for g in flatten(entries(mingens m(k))) do
    (
	newg=newg+random(-10,10)*g;
	);
    newgens=append(newgens, newg);
    )

K=ideal(newgens)




---------------------------------------------------------------------
---------------------------------------------------------------------
---------------------------------------------------------------------
---for a path:

restart
loadPackage("Depth");

makeCompleteIntersectionIdeal=(myIdeal)->(
    	c:=codim myIdeal;
	gensMyIdeal:=flatten entries gens myIdeal;
	nGens:=#gensMyIdeal;
	subsetsGens:=subsets(nGens,c);
	for i to #subsetsGens-1 do (
	    mySubset:=subsetsGens#i;
	    newGens:=mySubset/(x->gensMyIdeal#x);
	    if(isRegularSequence(newGens)) then (
		return ideal(newGens);
	    );
        );
	return ideal(0);
    )

r = 2

d1 = 2
d2 = 3
d3 = 2
d4 = 2

pars = join (toList(a_(1,1,1)..a_(r,d1,d2)), toList (b_(1,1,1)..b_(r,d2,d3)), toList (c_(1,1,1)..c_(r,d3,d4)))
probabilities = toList(p_(1,1,1,1)..p_(d1,d2,d3,d4))
allVars = join(probabilities,pars)
R = QQ[allVars]



I = ideal flatten flatten flatten for i from 1 to d1 list for j from 1 to d2 list for k from 1 to d3 list for m from 1 to d4 list p_(i,j,k,m) -  sum for l from 1 to r list a_(l,i,j)*b_(l,j,k)*c_(l,k,m);
startIx = d1*d2*d3*d4
endIx = d1*d2*d3*d4 + r*(d1*d2+d2*d3+d3*d4)-1
endIx-startIx
k = eliminate (I,flatten entries (vars R)_{startIx..endIx});
c=codim k
numgens k
 
ls=splice{l_1..l_c}; 
S=QQ[join(probabilities,ls)];
probabilities = toList(p_(1,1,1)..p_(d1,d2,d3))
m=map(S,R,join(probabilities,toList apply(length(pars),i->0)))
K=makeCompleteIntersectionIdeal(m(k));--degree K


probabilities = toList(p_(1,1,1)..p_(d1,d2,d3)); len=length(probabilities);
u=apply(len,i->sub(random(1,100),QQ))

J=transpose(submatrix'(jacobian(K), splice({len..len+3}),));

probabilities = toList(p_(1,1,1)..p_(d1,d2,d3))
u=apply(len,i->sub(random(1,100),QQ))

newJ=matrix(probabilities_0*J_0);
for i from 1 to len-1 do (newJ=newJ|matrix(probabilities_i*J_i));
newJ=matrix({probabilities})||newJ; --this is the jacobian together with the simplex equation
obj=matrix{apply(splice({0..len-1}), i-> u_i)}
augJ=newJ||obj; --this is the augmented Jacobian

Lker=matrix{{-sum(u),l_1..l_c,1}}
sys=Lker*augJ;

I=ideal(join((flatten entries sys),{sum(probabilities)-1}))+m(k);
degree I 
dim I
