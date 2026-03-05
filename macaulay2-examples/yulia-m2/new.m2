-- the super new definition with all sizes of minors (currently works for k<=4 only)
restart

k = 2
l = 5
d = 4


Y = reshape(ZZ^k, ZZ^l, matrix{{1..k*l}})

s = 2 -- columns
t = 4 -- rows

Delta = join( flatten apply(entries Y, i -> subsets(i, t)),
              flatten apply(entries transpose Y, i -> subsets(i, s)) )
	 

R = QQ[splice apply(k*l, i->x_(1, i+1)..x_(d, i+1)), MonomialOrder => Lex]

X = reshape(R^d, R^(k*l), matrix{gens R})



--****************************
-- makes ideal from hypergraph
--****************************

I = H -> {
    
-- hashtable to store (k, [d] choose k) pairs
U = unique(apply(H, h -> length h));
subz = new MutableHashTable;
for el in U do subz#el = subsets(1..d, el);

-- get all corresponding minors:
mins = {};
for h in H do {
    c = apply(h, i -> i - 1);
    len = length(h);
    rs = subz#len;
    for el in rs do {r = apply(el, i -> i - 1);
	    	     mins = append(mins, det X_c^r);
	             };
    };

-- make the ideal
return ideal(mins);
}


IDelta = I(Delta);
IEmpty = minors(t, X) + IDelta;






--**************************
-- makes hypergraph from set
--**************************
HNEW = S -> {
    
HS = {};
MM = apply(entries Y, el -> apply(el, i -> if any(S, n -> n==i) then 0 else i));
MM = for el in MM list if (number(el, i -> i != 0) >= t) then el else continue;


-- make variables
HS = join(HS, apply(S, el -> {el}));


-- make 2-minors
colsY = flatten apply(entries transpose Y, i -> subsets(i, k));
colz = apply(colsY, el -> for i in el list if toList(set({i}) * set(S)) == {} then i else continue);
HS = join(HS, flatten apply(colz, c -> subsets(c, 2)));


-- make (t-1)-minors
for el in subsets(MM, 2) do {
    C1 = select(l, i -> (first el)_i != 0);
    C2 = select(l, i -> (last el)_i != 0);
    if length(toList(set C1 - set C2)) < 1 or length(toList(set C2 - set C1)) < 1 then continue
    else {	
	 idx = toList(set C1 * set C2);
	 cols = flatten apply(el, i -> apply(idx, j -> i_j));
         HS = unique join(HS, apply(subsets(cols, t-1), el -> sort(el)));	 
	 }; 
    };



-- make (t-2)-minors
for el in subsets(MM, 3) do {
    Z1 = select(l, i -> (el_0)_i == 0);
    Z2 = select(l, i -> (el_1)_i == 0);
    Z3 = select(l, i -> (el_2)_i == 0);
    
    if length(toList(set Z1 - (set Z2 + set Z3))) < 1 or length(toList(set Z2 - (set Z1 + set Z3))) < 1 or length(toList(set Z3 - (set Z1 + set Z2))) < 1 then continue
    else {	
        C1 = select(l, i -> (el_0)_i != 0);
        C2 = select(l, i -> (el_1)_i != 0);
        C3 = select(l, i -> (el_2)_i != 0);
	    idx = toList(set C1 * set C2 * set C3);
	    cols = flatten apply(el, i -> apply(idx, j -> i_j));
         HS = unique join(HS, apply(subsets(cols, t-2), el -> sort(el)));	 
	 }; 
    };



-- make (t-3)-minors
for el in subsets(MM, 4) do {
    Z1 = select(l, i -> (el_0)_i == 0);
    Z2 = select(l, i -> (el_1)_i == 0);
    Z3 = select(l, i -> (el_2)_i == 0);
    Z4 = select(l, i -> (el_3)_i == 0);
    
    if length(toList(set Z1 - (set Z2 + set Z3 + set Z4))) < 1 or length(toList(set Z2 - (set Z1 + set Z3 + set Z4))) < 1 
    or length(toList(set Z3 - (set Z1 + set Z2 + set Z4))) < 1 or length(toList(set Z4 - (set Z1 + set Z2 + set Z3))) < 1 then continue

    else {	
        C1 = select(l, i -> (el_0)_i != 0);
        C2 = select(l, i -> (el_1)_i != 0);
        C3 = select(l, i -> (el_2)_i != 0);
        C4 = select(l, i -> (el_3)_i != 0); 
	 idx = toList(set C1 * set C2 * set C3 * set C4);
	 cols = flatten apply(el, i -> apply(idx, j -> i_j));
         HS = unique join(HS, apply(subsets(cols, t-3), el -> sort(el)));	 
	 }; 
    };



-- make t-minors
rowz = {};
for row in entries Y do {
    for el in S do {
        row = delete(el, row);
	};
rowz = append(rowz, row);};
HS = unique join(HS, flatten apply(rowz, r -> subsets(r, t)));



-- add some missing minors
twosubz = select(HS, i -> length(i) == 2);



while(true) do {
nontwosubz =  select(HS, i -> length(i) > 2);


for el1 in nontwosubz do {
    for el2 in twosubz do {
	inters = toList(set(el1) * set(el2));
	if length inters == 1 then {
	  pos = position(el1, i -> i == inters_0);
	  HS = unique( append(HS, sort(replace(pos, (toList(set(el2) - set(inters)))_0, el1))));
	    };
	};
    };

NEWnontwosubz = select(HS, i -> length(i) > 2);
if  NEWnontwosubz == nontwosubz then break;
};

return HS;
}






S = {1,3} 
IS = I(HNEW(S))

isSubset(IEmpty, IS)



S = {6,11,13} 
IS = I(HNEW(S));

dim IS
degree IS

decomp = decompose IS;
netList (decomp_0)_*
netList (decomp_1)_*



gensIS = set flatten entries gens IS;
gensI1 = set flatten entries gens (decomp_0);
gensI2 = set flatten entries gens (decomp_1);

netList toList (gensI1 - gensIS)
netList toList (gensI2 - gensIS)



for el in gensI2 do {
    if el % IS != 0 then print el;
    }








dim IEmpty
degree IEmpty
--isPrime IS -- false :(

decomp = decompose IS;
length decomp

loops = apply(decomp, el -> select(flatten entries gens el, pol -> ((degree pol)_0 == 1)))

for el in loops do print netList el




Stest = {1,2,4,5,11,12,19,21}
Itest = I(HNEW(Stest));
isPrime Itest
isSubset(Itest, decomp_1) -- true!

Stest = {1,2,4,5,11,12,16,18}
Itest = I(HNEW(Stest));
isPrime Itest
isSubset(Itest, decomp_2) -- true!

Stest = {1,2,4,5,11,12,13,15}
isPrime Itest
Itest = I(HNEW(Stest));
isSubset(Itest, decomp_3) -- true!

Stest = {1,2,4,5,7,9,11,12}
isPrime Itest
Itest = I(HNEW(Stest));
isSubset(Itest, decomp_4) -- true!

Stest = {1,2,4,5,11,12,16,18,19,21}
Itest = I(HNEW(Stest));
isSubset(Itest, decomp_5) -- true!

Stest = {1,2,4,5,11,12,13,15,19,21}
isPrime Itest
Itest = I(HNEW(Stest));
isSubset(Itest, decomp_6) -- true!

Stest = {1,2,4,5,7,9,11,12,19,21}
isPrime Itest
Itest = I(HNEW(Stest));
isSubset(Itest, decomp_7) -- true!

Stest = {1,2,4,5,11,12,13,15,16,18}
Itest = I(HNEW(Stest));
isSubset(Itest, decomp_8) -- true!

Stest = {1,2,4,5,11,12,7,9,16,18}
isPrime Itest
Itest = I(HNEW(Stest));
isSubset(Itest, decomp_9) -- true!

Stest = {1,2,4,5,11,12,7,9,13,15}
isPrime Itest
Itest = I(HNEW(Stest));
isSubset(Itest, decomp_10) -- true!

Stest = {1,2,4,5,11,12,13,15,16,18,19,21}
Itest = I(HNEW(Stest));
isSubset(Itest, decomp_11) -- true!

Stest = {1,2,4,5,11,12,7,9,16,18,19,21}
isPrime Itest
Itest = I(HNEW(Stest));
isSubset(Itest, decomp_12) -- true!

Stest = {1,2,4,5,11,12,7,9,13,15,19,21}
isPrime Itest
Itest = I(HNEW(Stest));
isSubset(Itest, decomp_13) -- true!

Stest = {1,2,4,5,11,12,7,9,13,15,16,18}
isPrime Itest
Itest = I(HNEW(Stest));
isSubset(Itest, decomp_14) -- true!



problem = decomp_0;
betti mingens problem
netList problem_*



test1 = I(HNEW({1,2,4,5,11,12,10}));
--isPrime test1

test2 = I(HNEW({1,2,4,5,11,12,3,6}));
--isPrime test2



int = intersect(test1, test2, IEmpty);
isSubset(int, problem)

for el in flatten entries mingens int do { 
    if el % problem != 0 then print el;
    }






-- try other intersections

test1 = I(HNEW({1,2,4,5,11})); -- prime!!
isPrime test1
isSubset(test1, problem)



-- 1 2 4 5 is already prime
test1 = I(HNEW({1,2,4,5})); -- prime!!


-- 1 2 11 12
test2 = I(HNEW({1,2,11}));
test3 = I(HNEW({1,2,12}));



-- 4 5 11 12
test4 = I(HNEW({4,5,11}));
test5 = I(HNEW({4,5,12}));


int = intersect(test1, test2, test3, test4, test5);
isSubset(int, problem)


for el in flatten entries mingens int do { 
    if el % problem != 0 then print el;
    }

-------------------
-- try another S --
-------------------


S = {1,2,4,5,8,9,11,12,13,15,16,18}
IS = I(HNEW(S));
--isPrime IS -- false :(

decomp = decompose IS;
length decomp

loops = apply(decomp, el -> select(flatten entries gens el, pol -> ((degree pol)_0 == 1)))

for el in loops do print netList el


problem = decomp_0;
betti mingens problem



test1 = I(HNEW({1,2,4,5,8,9,11,12,13,15,16,18,19}));
--isPrime test1


test2 = I(HNEW({1,2,4,5,8,9,11,12,13,15,16,18,20}));
--isPrime test2


test3 = I(HNEW({1,2,4,5,8,9,11,12,13,15,16,18,21}));
--isPrime test3

test4 = I(HNEW({1,2,4,5,8,9,11,12,13,15,16,18,7,10,19}));



int = intersect(test1, test2, test3, test4);
isSubset(int, problem)

for el in flatten entries mingens int do { 
    if el % problem != 0 then print el;
    }











-- try other S...
S = {1,2,11,12} -- not prime, has 31 components
IS = I(HNEW(S));
decomp = decompose IS; 
problem = decomp_0;

test1 = I(HNEW({1})); -- prime
test2 = I(HNEW({5})); -- prime


isSubset(test1, IS)
isSubset(test2, IS)









-------- testing a bad S --------

S = {6,7,11,13,19,20}; --prime
S = {6,11,13};-- ran out of memory
S = {1, 6, 11, 16} -- prime
S = {6,11,13,20} -- prime
S = {1,6} -- didn't terminate
S = {6,7,11,13,19} -- prime

S = {1,2,4,5,8,9,11,12,13,15,16,18}
INEW = I (HNEW (S) )
isPrime INEW


S1 = {1,2,4,5,8,9,11,12,13,15,16,18,19}
INEW1 = I (HNEW (S1) )

S2 = {1,2,4,5,8,9,11,12,13,15,16,18,20}
INEW2 = I (HNEW (S2) )

S3 = {1,2,4,5,8,9,11,12,13,15,16,18,21}
INEW3 = I (HNEW (S3) )

S4 = {1,2,4,5,8,9,11,12,13,15,16,18,19,20,21}
INEW4 = I (HNEW (S4) )

S5 = {1,2,4,5,8,9,11,12,13,15,16,18,19,20}
INEW5 = I (HNEW (S5) )

S6 = {1,2,4,5,8,9,11,12,13,15,16,18,20,21}
INEW6 = I (HNEW (S6) )

S7 = {1,2,4,5,8,9,11,12,13,15,16,18,19,21}
INEW7 = I (HNEW (S7) )

S8 = {1,2,4,5,8,9,11,12,13,15,16}
INEW8 = I (HNEW (S8) )
isSubset(D_0, INEW8)

INTNEW = intersect(INEW1, INEW2, INEW8, INEW3);
set flatten entries mingens INTNEW
for f in flatten entries gens INTNEW do (
    if f % INEW != 0 then print f;
)
isSubset(INTNEW, INEW)
isPrime INEW1

isSubset(IEmpty, INEW4)

isSubset(INEW, INEW4)

D = decompose INEW
D_0





H1 = H(S);
print "1";
IS = I(H1);
print "2";
isPrime IS

H2 = H(S);
IS2  = I(H2)


LL = {}; L = {};
HS = H(S);




-- get all t-2 and t-3 subsets...

for el in subsets(MM, 2) do {
    C1 = select(l, i -> (first el)_i != 0);
    C2 = select(l, i -> (last el)_i != 0);
    if length(toList(set C1 - set C2)) < 1 or length(toList(set C2 - set C1)) < 1 then continue
    else {	
	 idx = toList(set C1 * set C2);
	 cols = flatten apply(el, i -> apply(idx, j -> i_j));
         HS =  join(HS, subsets(cols, t-1));	 
	 }; 
    };










tsubz = select(HS, i -> length(i) == t-1);
for  el in subsets(tsubz, 2) do {
    if length(toList(set (first el) * set (last el))) == t-2 then 
    LL = append(LL, append(HS, toList(set (first el) * set (last el)))); }
LL = unique LL;

for newHS in LL do {
    twosubz = select(newHS, i -> length(i) == 2);

while(true) do {
nontwosubz =  select(newHS, i -> length(i) == t-2);


for el1 in nontwosubz do {
    for el2 in twosubz do {
	inters = toList(set(el1) * set(el2));
	if length inters == 1 then {
	  pos = position(el1, i -> i == inters_0);
	  newHS = unique( append(newHS, replace(pos, (toList(set(el2) - set(inters)))_0, el1)));
	    };
	};
    };

NEWnontwosubz = select(newHS, i -> length(i) == t-2);
if  NEWnontwosubz == nontwosubz then break;
};
    
    L = append(L, unique(apply(newHS, i -> sort(i))));
    };

L = unique(apply(L, i -> sort(i)));

idealz = {};
for el in L do {idl = I(el); idealz = append(idealz, idl); print "a";}

for el in idealz do { print isPrime el; }









---------------
S = {1,2,4,5,12};
I1 = I(HNEW(S));
problem = (decompose I1)_0;

for el in subsets S do {
    I2 = I(HNEW(el));
    print isSubset(I2, problem);
    }



isSubset(I2, problem)

-- all false:
for el in flatten entries mingens int do { 
    if el % problem != 0 then print el;
    }


for el in  subsets ((subsets S), 2) do {
    if (el_0 != {} and el_1 != {} and el_0 != S and el_1 != S) then {
    I2 = I(HNEW(el_0));
    I3 = I(HNEW(el_1));
    int = intersect(I2, I3);
    print (isSubset(int, problem), el);
    }}





for el in  subsets ((subsets S), 3) do {
    if (el_0 != {} and el_1 != {} and el_2 != {} and el_0 != S and el_1 != S and el_2 != S) then {
    I2 = I(HNEW(el_0));
    I3 = I(HNEW(el_1));
    I4 = I(HNEW(el_2));
    int = intersect(I2, I3, I4);
    print (isSubset(int, problem), el);
    }}
