-- Checking if 4' will give us primeness
restart


k = 4
l = 6
d = 5

Y = reshape(ZZ^k, ZZ^l, matrix{{1..k*l}})

s = 2 -- columns
t = 5 -- rows

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
H = S -> {
    
HS = {};
MM = apply(entries Y, el -> apply(el, i -> if any(S, n -> n==i) then 0 else i));
-- MM = for el in MM list if (number(el, i -> i != 0) >= t) then el else continue;


-- make variables
HS = join(HS, apply(S, el -> {el}));


-- make 2-minors
colsY = flatten apply(entries transpose Y, i -> subsets(i, k));
colz = apply(colsY, el -> for i in el list if toList(set({i}) * set(S)) == {} then i else continue);
HS = join(HS, flatten apply(colz, c -> subsets(c, 2)));


-- make (t-1)-minors
for el in subsets(MM, 2) do {
    Z1 = select(l, i -> (first el)_i == 0);
    Z2 = select(l, i -> (last el)_i == 0);
    if ((length(toList(set Z1 - set Z2)) < 1 and length(Z1)!=0) or (length(toList(set Z2 - set Z1))<1 and length(Z2)!=0)) then continue
    else {	
        C1 = select(l, i -> (first el)_i != 0);
        C2 = select(l, i -> (last el)_i != 0);
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
    
    if ((length(toList(set Z1 - (set Z2 + set Z3))) < 1 and length(Z1)!=0) or (length(toList(set Z2 - (set Z1 + set Z3))) < 1 and length(Z2)!=0) or (length(toList(set Z3 - (set Z1 + set Z2))) < 1 and length(Z3)!=0)) then continue
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
    
    if ((length(toList(set Z1 - (set Z2 + set Z3 + set Z4))) < 1 and length(Z1)!=0) or (length(toList(set Z2 - (set Z1 + set Z3 + set Z4))) < 1 and length(Z2)!=0)
    or (length(toList(set Z3 - (set Z1 + set Z2 + set Z4))) < 1 and length(Z3)!=0) or (length(toList(set Z4 - (set Z1 + set Z2 + set Z3))) < 1 and length(Z4)!=0)) then continue

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











-------- testing a bad S --------



S = {1} -- prime
S = {1,4} -- prime
S = {1,4,7} -- prime
S = {6,7,11,19} -- ?


H1 = H(S);
print "1";
IS = I(H1);
print "2";
isPrime IS


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








