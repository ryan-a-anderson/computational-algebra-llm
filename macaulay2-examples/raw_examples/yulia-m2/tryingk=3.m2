restart

k = 3
l = 5
d = 4

Y = reshape(ZZ^k, ZZ^l, matrix{{1..k*l}})

s = 2 -- columns
t = 3 -- rows

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


HOld = S -> {
    
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
         HS =  join(HS, subsets(cols, t-1));	 
	 }; 
    };


while(true) do{

    twosubz = select(HS, i -> length(i) == 2);
    while(true) do {
    nontwosubz =  select(HS, i -> length(i) > 2);


    for el1 in nontwosubz do {
        for el2 in twosubz do {
	        inters = toList(set(el1) * set(el2));
	        if length inters == 1 then {
	            pos = position(el1, i -> i == inters_0);
	            HS = unique( append(HS, replace(pos, (toList(set(el2) - set(inters)))_0, el1)));
	        };
	    };
    };

    NEWnontwosubz = select(HS, i -> length(i) > 2);
    if  NEWnontwosubz == nontwosubz then break;
    };

    tsubz = select(HS, i -> length(i) == t-1);
    tsubz = unique(apply(tsubz, i->sort i));



    -- print "a";
    for  el in subsets(tsubz, 2) do {
        if length(toList(set (first el) * set (last el))) >= t-2 then 
            HS = join(HS, subsets(toList(set (first el) + set (last el)), t-1));
    };
    -- print "b";
    TSUBZ = select(HS, i -> length(i) == t-1);
    if length unique(apply(tsubz, i->sort i)) == length unique(apply(TSUBZ, i->sort i)) then break;
    TSUBZ = unique(apply(TSUBZ, i->sort i));
    print ((set TSUBZ) - (set tsubz));
    print length unique(apply(TSUBZ, i->sort i));
};
print "finished";


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
	  HS = unique( append(HS, replace(pos, (toList(set(el2) - set(inters)))_0, el1)));
	    };
	};
    };

NEWnontwosubz = select(HS, i -> length(i) > 2);
if  NEWnontwosubz == nontwosubz then break;
};

HS = apply(HS, i->sort i);
return unique HS;
}






























-- check a particular bad A for various sets S

A = {1,0,0,0, 1,0,0,0, 1,0,0,0, 0,1,0,0, 0,1,0,0, 0,0,0,0, 1,0,0,0, 1,0,0,0, 1,0,0,0, 0,0,1,0, 0,0,0,0, 0,0,1,0, 0,0,0,0, 0,0,0,1, 0,0,0,1}

SS = {{6,11,13}, {6}, {11}, {13}, {6,11}, {11,13}, {6,13}}

for S in SS do {
IS = I(H(S));
subs = flatten apply(length(gens R), i -> {(gens R)_i => A_i});
print (unique(flatten entries gens sub(IS, subs)) == {0});
}


print (unique(flatten entries gens sub(IEmpty, subs)) == {0});
------------






















































-- trying for a particular set s
-- three lines

S = {1, 3, 4, 5, 8, 9, 11, 12, 13, 14, 16, 18}
H(S)
IS = I(H(S));
isPrime IS


decompS = decompose(IS);


for el in decompS do {print "New component:"; print netList el_*;}

for el in decompS do print isPrime el
betti mingens  decompS_0
betti mingens IS


L = {}
for el in S do {
    newS = toList(set(S) - set({el}));
    ISnew = I(H(newS));
    L = append(L, ISnew);
    }

Int = intersect(L);


isSubset(Int, IS)



-- trying a matrix A
S = {3, 6, 9, 12, 13, 14}
IS = I(H(S));


S1 = {3, 6, 9, 12, 13, 14, 8, 10}
IS1 = I(H(S1));

A = {1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,1}
subs = flatten apply(length(gens R), i -> {(gens R)_i => A_i})
sub(IS, subs)
sub(IEmpty, subs)






S = {3, 6, 9, 12, 13, 14, 8, 10}
IS = I(H(S));

A = {1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1}
subs = flatten apply(length(gens R), i -> {(gens R)_i => A_i})
sub(IS, subs)

for el in subsets(S) do {
    if el == {} then continue;
    Iel = I(H(el));
    print (select(flatten entries gens sub(Iel, subs), e -> e!=0), el);
    }

