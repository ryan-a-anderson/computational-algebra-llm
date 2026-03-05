-----------------------------------------------
-- try manual degree-bounded ideal intersection
-----------------------------------------------

restart
pz = flatten apply(subsets({a,b,c,d,e}, 4), el -> permutations el)

R = QQ[T1,T2,T3,T4,g,h,x,y,z,apply(pz, i -> p_i), MonomialOrder => Lex]
--R = QQ[T1,T2,T3,T4,g,h,x,y,z,apply(pz, i -> p_i), MonomialOrder => Eliminate 9] -- this is more efficient 
-- but gives a different generating set!

makeTriple = (s,t, i1,i2,i3,i4) -> return { h*(1-(2/3)*s) + g*(1/3)*t     - p_(join(toSequence sort{sort({i1,i2}), sort({i3,i4})})), 
                                            h*(1/3)*s     + g*(1/3)*t     - p_(join(toSequence sort{sort({i1,i3}), sort({i2,i4})})),
			                    h*(1/3)*s     + g*(1-(2/3)*t) - p_(join(toSequence sort{sort({i1,i4}), sort({i2,i3})}))}
   

makeIdeal= (j1,j2,j3,j4,j5) -> { L = join(makeTriple(z, y, j1,j2,j3,j4), makeTriple(z, x+y, j1,j2,j3,j5), 
                                          makeTriple(y+z, x, j1,j2,j4,j5), makeTriple(y, x,   j1,j3,j4,j5), 
				          {1-(2/3)*y - p_(join(toSequence sort{sort{j2,j3},sort{j4,j5}})), 
					      (1/3)*y - p_(join(toSequence sort{sort{j2,j4},sort{j3,j5}})), 
					      (1/3)*y - p_(join(toSequence sort{sort{j2,j5},sort{j3,j4}}))});
				 return eliminate(ideal(L) + ideal(g + h - 1), {x,y,z,g,h});   }



-- try this for 5 different orderings
I1 = makeIdeal(a,b,c,d,e);
I2 = makeIdeal(b,c,d,e,a);
I3 = makeIdeal(c,d,e,a,b);
I4 = makeIdeal(d,e,a,b,c);
I5 = makeIdeal(e,a,b,c,d);





J1 = T1*I1 + (1-T1)*I2;
J2 = T2*J1 + (1-T2)*I3;
J3 = T3*J2 + (1-T3)*I4;
J4 = T4*J3 + (1-T4)*I5;

J = J4;


time Gs = flatten entries gens gb (J, DegreeLimit => 6);
length Gs

noTs = {};
for el in Gs do { if toList(set{T1, T2, T3, T4} * set support(el)) == {} then noTs = append(noTs, el); }

for el in noTs do (print ((factor el)#0#0 == el))

-- those that print false are irreducible, and hence new!
irred = select(noTs, el -> (factor el)#0#0 == el);
length irred

-- check that each polynomials is in each one of the 5 ideals
for el in irred do print (el % I1 == 0, el % I2 == 0, el % I3 == 0, el % I4 == 0, el % I5 == 0)

-- how many irreducibles?
for ipol in irred do print length support ipol


-- look at the first one 
length terms irred_0   -- how many terms
length support irred_0 -- how many variables


length support irred_5
length support irred_6
length support irred_7





-- check two other circular orders:

K1 = makeIdeal(b,a,c,d,e); 
K2 = makeIdeal(a,c,d,e,b); 
K3 = makeIdeal(c,d,e,b,a); 
K4 = makeIdeal(d,e,b,a,c); 
K5 = makeIdeal(e,b,a,c,d); 


for el in irred do print (length support el, el % K1 == 0, el % K2 == 0, el % K3 == 0, el % K4 == 0, el % K5 == 0)


K1 = makeIdeal(c,b,a,d,e);
K2 = makeIdeal(b,a,d,e,c);
K3 = makeIdeal(a,d,e,c,b);
K4 = makeIdeal(d,e,c,b,a);
K5 = makeIdeal(e,c,b,a,d);


for el in irred do print (length support el, el % K1 == 0, el % K2 == 0, el % K3 == 0, el % K4 == 0, el % K5 == 0)


-- the below two polynomials produce all falses
-- are they the distinguishing ones for the circular order a b c d e?
irred_5 -- add to overleaf
irred_6 -- add to overleaf
irred_7 -- add to overleaf


pol = irred_8





------------------------------------------------------------
-- let's try to check these polynomials for ALL other orders
------------------------------------------------------------

-- this function shifts the cycle l by 1
shiftCycle = l -> toList flatten (l_{1..length l-1}, l_0)

-- this function does n shifts to a given cycle l
multipleShifts = (n, l) -> { 
    newShift = l; 
    for i from 1 to n do { newShift = shiftCycle(newShift); };
    return newShift; 
    }


otherOrders = select(permutations({a,b,c,d,e}), el -> toList(set{el} * set apply(5, i -> multipleShifts(i, {a,b,c,d,e}))) == {})
length otherOrders -- 115 = 120 - 5

-- let's select up to symmetry (should get 115/5 = 23)

blocks = {};
for el in otherOrders do { 
    block = {el};
    for i from 1 to 4 do {
	shifted = multipleShifts(i,el);
        block = block | {shifted}; };
   blocks = blocks | {block}; }

otherOrders = unique (blocks / sort)
length otherOrders -- 23 elements corresponding to 23 other orders



TFs_5 = apply(otherOrders, el -> apply(el, tup -> {idl = makeIdeal(toSequence tup); return irred_5 % idl == 0; }));
TFs_7 = apply(otherOrders, el -> apply(el, tup -> {idl = makeIdeal(toSequence tup); return irred_7 % idl == 0; }));

-- check for all irreducibles 
for i from 1 to length irred - 1 do {
TFs = apply(otherOrders, el -> apply(el, tup -> {idl = makeIdeal(toSequence tup); return irred_i % idl == 0; }));
print TFs_22;
}

-- all trues!!
otherOrders_22








----------------------------
--- TEST DISPLAYED TREES ---
----------------------------


pol = substitute(pol, R)


makeTripleParam = (s,t, i1,i2,i3,i4) -> return  { p_(join(toSequence sort{sort({i1,i2}), sort({i3,i4})})) => h*(1-(2/3)*s) + g*(1/3)*t, 
                                                  p_(join(toSequence sort{sort({i1,i3}), sort({i2,i4})})) => h*(1/3)*s     + g*(1/3)*t,
			                          p_(join(toSequence sort{sort({i1,i4}), sort({i2,i3})})) => h*(1/3)*s     + g*(1-(2/3)*t)}
   
   
   
makeParam = (j1,j2,j3,j4,j5) -> join(makeTripleParam(z, y,j1,j2,j3,j4), makeTripleParam(z, x+y,j1,j2,j3,j5),
                                     makeTripleParam(y+z, x,j1,j2,j4,j5), makeTripleParam(y, x, j1,j3,j4,j5),
	                            {p_(join(toSequence sort{sort{j2,j3},sort{j4,j5}})) => 1-(2/3)*y}, 
				    {p_(join(toSequence sort{sort{j2,j4},sort{j3,j5}})) => (1/3)*y}, 
			            {p_(join(toSequence sort{sort{j2,j5},sort{j3,j4}})) => (1/3)*y});




subParam = (HT, gs, hs, xs, ys, zs) -> applyValues(HT, el -> sub(el, {g => gs, h => hs, x => xs, y => ys, z => zs}))


displayedTrees = (j1,j2,j3,j4,j5) -> apply(5, i -> new HashTable from makeParam(toSequence multipleShifts(i, {j1,j2,j3,j4,j5})))


-- make all displayed  trees for our ordering abcde
DT1 = {}
for el in displayedTrees(a,b,c,d,e) do (
t1 = subParam(el, 0, 1, x, y, z); DT1 = append(DT1, t1);
t2 = subParam(el, 1, 0, x, y, z); DT1 = append(DT1, t2);
)
DT1 = (unique DT1);


for dt in DT1 do (subz = apply(support pol, el -> el => dt#el); print sub(pol, subz);)


-- test other orderings
allTrees = DT1;
for ord in otherOrders do (
    for el in displayedTrees(toSequence ord_0) do (
    t1 = subParam(el, 0, 1, x, y, z); allTrees = append(allTrees, t1);
    t2 = subParam(el, 1, 0, y, z, x); allTrees = append(allTrees, t2););
 )

allTrees = unique allTrees;
length allTrees


for dt in allTrees do (subz = apply(support pol, el -> el => dt#el); print (sub(pol, subz) == 0););


-- true for all polynomials?
for pol in irred do {
    print("next");
    for dt in allTrees do (subz = apply(support pol, el -> el => dt#el); print (sub(pol, subz) == 0););
    }



testOrder = toSequence (otherOrders_3)_0
testTree = new HashTable from makeParam(testOrder)
subz = apply(support pol, el -> el => testTree#el)
sub(sub(pol, subz), {g=>0, h=>1})




-- pick the special order abecd
-- abcde and abecd have one displayed tree in common!
testDT = {}
for el in displayedTrees(testOrder) do (
t1 = subParam(el, 0, 1, x, y, z); testDT = append(testDT, t1);
t2 = subParam(el, 1, 0, x, y, z); testDT = append(testDT, t2);
)
testDT = (unique testDT);
length testDT

for el in testDT do print el



for pol in irred do {
    print("next");
    for dt in testDT do (subz = apply(support pol, el -> el => dt#el); print (sub(pol, subz) == 0););
    }



nice1 = irred_3
nice2 = irred_8
nice3 = irred_9

for dt in allTrees do (subz = apply(support nice1, el -> el => dt#el); print (sub(nice1, subz) == 0););
for dt in allTrees do (subz = apply(support nice2, el -> el => dt#el); print (sub(nice2, subz) == 0););
for dt in allTrees do (subz = apply(support nice3, el -> el => dt#el); print (sub(nice3, subz) == 0););





-- write code that takes the intersection of all true/falses of all polynomials
-- check that the intersection is always 10 for all orders



int = {}
for i from 0 to 9 do (
    
l1 = {};
l2 = {};

if (i == 0) then (
for dt in allTrees do (subz = apply(support irred_i, el -> el => dt#el); l1 = append(l1, (sub(irred_i, subz) == 0)););
for dt in allTrees do (subz = apply(support irred_(i+1), el -> el => dt#el); l2 = append(l2, (sub(irred_(i+1), subz) == 0)););

int = apply(length l1, i -> (l1_i == l2_i and l1_i == true));
)

else(
    for dt in allTrees do (subz = apply(support irred_i, el -> el => dt#el); l1 = append(l1, (sub(irred_i, subz) == 0)););
    int = apply(length l1, i -> (l1_i == int_i and int_i == true));
    )
)

length select(int, el -> el == true)













