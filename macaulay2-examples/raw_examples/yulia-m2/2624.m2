restart

k = 2
l = 6
d = 4

Y = reshape(ZZ^k, ZZ^l, matrix{{1..k*l}})

s = 2 -- columns
t = 4 -- rows

Delta = join( flatten apply(entries Y, i -> subsets(i, t)),
              flatten apply(entries transpose Y, i -> subsets(i, s)) )
	 

R = QQ[splice apply(k*l, i->x_(1, i+1)..x_(d, i+1)), MonomialOrder => Lex]

X = reshape(R^d, R^(k*l), matrix{gens R})


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







R1 = entries (transpose Y)_0
R2 = entries (transpose Y)_1

-- (1, 1) case:

allIdeals11 = {}

subz1 = subsets(R1, 1);
for el1 in subz1 do {
    subz2 = subsets(toList(set R2 - set apply(el1, i -> i+1)), 1);
    for el2 in subz2 do {
    gs11 = {};
    ESS = join(el1, el2);
    gs11 = flatten append(gs11, flatten apply(ESS, i -> apply(d, j -> x_(j+1, i))));
    cols = entries transpose Y;
    M2 = for el in cols list if toList(set(el) * set(ESS)) == {} then el else continue;
    for el in M2 do { gs11 = flatten append(gs11, flatten entries mingens minors(2, X_(apply(el, i -> i-1)))); };
    
    Cart = apply(((M2_0 ** M2_1) ** M2_2) ** M2_3, i -> toList splice(splice(i)));
    
    
    gs11 = flatten flatten append( gs11, apply(Cart, c ->  flatten entries mingens minors(3, X_(apply(c, j -> j-1)))));
    allIdeals11 = append(allIdeals11, ideal(gs11));
    };
    }


-- (1, 2) case:
allIdeals12 = {}

subz1 = subsets(R1, 1);
for el1 in subz1 do {
    subz2 = subsets(toList(set R2 - set apply(el1, i -> i+1)), 2);
    for el2 in subz2 do {
    gs12 = {};
    ESS = join(el1, el2);
    gs12 = flatten append(gs12, flatten apply(ESS, i -> apply(d, j -> x_(j+1, i))));
    cols = entries transpose Y;
    M2 = for el in cols list if toList(set(el) * set(ESS)) == {} then el else continue;
    for el in M2 do { gs12 = flatten append(gs12, flatten entries mingens minors(2, X_(apply(el, i -> i-1)))); };
    

    Cart = apply(((M2_0 ** M2_1) ** M2_2), i -> toList splice(i));
    gs12 = flatten flatten append( gs12, apply(Cart, c ->  flatten entries mingens minors(3, X_(apply(c, j -> j-1)))));

    Cart = apply(((M2_0 ** M2_1) ** M2_2), i -> toList join(toList(set R1 - set el1 - set flatten M2), splice(i)));
    gs12 =  flatten flatten append( gs12, apply(Cart, c ->  flatten entries mingens minors(4, X_(apply(c, j -> j-1)))));
    
    allIdeals12 = append(allIdeals12, ideal(gs12));
    };
    }


subz1 = subsets(R1, 2);
for el1 in subz1 do {
    subz2 = subsets(toList(set R2 - set apply(el1, i -> i+1)), 1);
    for el2 in subz2 do {
    gs12 = {};
    ESS = join(el1, el2);
    gs12 = flatten append(gs12, flatten apply(ESS, i -> apply(d, j -> x_(j+1, i))));
    cols = entries transpose Y;
    M2 = for el in cols list if toList(set(el) * set(ESS)) == {} then el else continue;
    for el in M2 do { gs12 = flatten append(gs12, flatten entries mingens minors(2, X_(apply(el, i -> i-1)))); };

    Cart = apply(((M2_0 ** M2_1) ** M2_2), i -> toList splice(i));
    gs12 = flatten flatten append( gs12, apply(Cart, c ->  flatten entries mingens minors(3, X_(apply(c, j -> j-1)))));


    Cart = apply(((M2_0 ** M2_1) ** M2_2), i -> toList join(toList(set R2 - set el2 - set flatten M2), splice(i)));
    gs12 =  flatten flatten append( gs12, apply(Cart, c ->  flatten entries mingens minors(4, X_(apply(c, j -> j-1)))));
    
    --allIdeals12 = append(allIdeals12, {ideal(gs12), ESS});
    allIdeals12 = append(allIdeals12, ideal(gs12))
    };
    }


--betti mingens (allIdeals12)_0

-- (1, 3) case:
allIdeals13 = {}

subz1 = subsets(R1, 1);
for el1 in subz1 do {
    subz2 = subsets(toList(set R2 - set apply(el1, i -> i+1)), 3);
    for el2 in subz2 do {
    gs13 = {};
    ESS = join(el1, el2);
    gs13 = flatten append(gs13, flatten apply(ESS, i -> apply(d, j -> x_(j+1, i))));
    cols = entries transpose Y;
    M2 = for el in cols list if toList(set(el) * set(ESS)) == {} then el else continue;
    for el in M2 do { gs13 = flatten append(gs13, flatten entries mingens minors(2, X_(apply(el, i -> i-1)))); };
    
    gs13 = flatten flatten append( gs13, flatten entries mingens minors(4, X_(apply(flatten join(M2, toList(set R1 - set el1 - set flatten M2)), i -> i-1))) );
    
    allIdeals13 = append(allIdeals13, ideal(gs13));
    };
    }

subz1 = subsets(R1, 3);
for el1 in subz1 do {
    subz2 = subsets(toList(set R2 - set apply(el1, i -> i+1)), 1);
    for el2 in subz2 do {
    gs13 = {};
    ESS = join(el1, el2);
    gs13 = flatten append(gs13, flatten apply(ESS, i -> apply(d, j -> x_(j+1, i))));
    cols = entries transpose Y;
    M2 = for el in cols list if toList(set(el) * set(ESS)) == {} then el else continue;
    for el in M2 do { gs13 = flatten append(gs13, flatten entries mingens minors(2, X_(apply(el, i -> i-1)))); };
    
    gs13 = flatten flatten append( gs13, flatten entries mingens minors(4, X_(apply(flatten join(M2, toList(set R2 - set el2 - set flatten M2)), i -> i-1))) );
    
    allIdeals13 = append(allIdeals13, ideal(gs13));
    };
    }





-- (2, 2) case:
allIdeals22 = {}

subz1 = subsets(R1, 2);
for el1 in subz1 do {
    subz2 = subsets(toList(set R2 - set apply(el1, i -> i+1)), 2);
    for el2 in subz2 do {
    gs22 = {};
    ESS = join(el1, el2);
    gs22 = flatten append(gs22, flatten apply(ESS, i -> apply(d, j -> x_(j+1, i))));
    cols = entries transpose Y;
    M2 = for el in cols list if toList(set(el) * set(ESS)) == {} then el else continue;
    for el in M2 do { gs22 = flatten append(gs22, flatten entries mingens minors(2, X_(apply(el, i -> i-1)))); };

    Cart = apply(M2_0 ** M2_1 , i -> toList join(toList(set R1 - set el1 - set flatten M2), splice(i)));
    gs22 =  flatten flatten append( gs22, apply(Cart, c ->  flatten entries mingens minors(4, X_(apply(c, j -> j-1)))));

    Cart = apply(M2_0 ** M2_1, i -> toList join(toList(set R2 - set el2 - set flatten M2), splice(i)));
    gs22 =  flatten flatten append( gs22, apply(Cart, c ->  flatten entries mingens minors(4, X_(apply(c, j -> j-1)))));

    --allIdeals22 = append(allIdeals22, {ideal(gs22), ESS});
    allIdeals22 = append(allIdeals22, ideal(gs22));
    };
    }


--for el in allIdeals22 do {print betti gens gb el_0; print; print el_1; print;}


--el1 = {1,3}
--el2 = {6,8}


-- (2, 3) case:
allIdeals23 = {}

subz1 = subsets(R1, 2);
for el1 in subz1 do {
    subz2 = subsets(toList(set R2 - set apply(el1, i -> i+1)), 3);
    for el2 in subz2 do {
    gs23 = {};
    ESS = join(el1, el2);
    gs23 = flatten append(gs23, flatten apply(ESS, i -> apply(d, j -> x_(j+1, i))));
    cols = entries transpose Y;
    M2 = for el in cols list if toList(set(el) * set(ESS)) == {} then el else continue;
    for el in M2 do { gs23 = flatten append(gs23, flatten entries mingens minors(2, X_(apply(el, i -> i-1)))); };
    
    gs23 = flatten flatten append( gs23, flatten entries mingens minors(4, X_(apply(flatten join(M2, toList(set R1 - set el1 - set flatten M2)), i -> i-1))) );
    
    allIdeals23 = append(allIdeals23, ideal(gs23));
    };
    }


subz1 = subsets(R1, 3);
for el1 in subz1 do {
    subz2 = subsets(toList(set R2 - set apply(el1, i -> i+1)), 2);
    for el2 in subz2 do {
    gs23 = {};
    ESS = join(el1, el2);
    gs23 = flatten append(gs23, flatten apply(ESS, i -> apply(d, j -> x_(j+1, i))));
    cols = entries transpose Y;
    M2 = for el in cols list if toList(set(el) * set(ESS)) == {} then el else continue;
    for el in M2 do { gs23 = flatten append(gs23, flatten entries mingens minors(2, X_(apply(el, i -> i-1)))); };
    
    gs23 = flatten flatten append( gs23, flatten entries mingens minors(4, X_(apply(flatten join(M2, toList(set R2 - set el2 - set flatten M2)), i -> i-1))) );
    
    allIdeals23 = append(allIdeals23, ideal(gs23));
    };
    }




Int = intersect(join(allIdeals11, allIdeals12, allIdeals13, allIdeals22, allIdeals23, {IEmpty}));

