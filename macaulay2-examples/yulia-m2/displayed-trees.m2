restart
pz = flatten apply(subsets({a,b,c,d,e}, 4), el -> permutations el)

--R = QQ[T1,T2,T3,T4,g,h,x,y,z,apply(pz, i -> p_i), MonomialOrder => Lex]
R = QQ[T1,T2,T3,T4,g,h,x,y,z,apply(pz, i -> p_i), MonomialOrder => Eliminate 9]


makeTriple = (s,t, i1,i2,i3,i4) -> return { h*(1-(2/3)*s) + g*(1/3)*t     - p_(join(toSequence sort{sort({i1,i2}), sort({i3,i4})})), 
                                            h*(1/3)*s     + g*(1/3)*t     - p_(join(toSequence sort{sort({i1,i3}), sort({i2,i4})})),
			                    h*(1/3)*s     + g*(1-(2/3)*t) - p_(join(toSequence sort{sort({i1,i4}), sort({i2,i3})}))}
   

makeIdeal= (j1,j2,j3,j4,j5) -> { L = join(makeTriple(z, y, j1,j2,j3,j4), makeTriple(z, x+y, j1,j2,j3,j5), 
                                          makeTriple(y+z, x, j1,j2,j4,j5), makeTriple(y, x,   j1,j3,j4,j5), 
				          {1-(2/3)*y - p_(join(toSequence sort{sort{j2,j3},sort{j4,j5}})), 
					      (1/3)*y - p_(join(toSequence sort{sort{j2,j4},sort{j3,j5}})), 
					      (1/3)*y - p_(join(toSequence sort{sort{j2,j5},sort{j3,j4}}))});
				 return eliminate(ideal(L) + ideal(g + h - 1), {x,y,z,g,h});   }

-- this function shifts the cycle l by 1
shiftCycle = l -> toList flatten (l_{1..length l-1}, l_0)

-- this function does n shifts to a given cycle l
multipleShifts = (n, l) -> { 
    newShift = l; 
    for i from 1 to n do { newShift = shiftCycle(newShift); };
    return newShift; 
    }


allOrders = permutations({a,b,c,d,e})

blocks = {};
for el in allOrders do { 
    block = {el};
    for i from 1 to 4 do {
	shifted = multipleShifts(i,el);
        block = block | {shifted}; };
   blocks = blocks | {block}; }

allOrders = unique (blocks / sort)
length allOrders 




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


allTrees = {};
for ord in allOrders do (
    for el in displayedTrees(toSequence ord_0) do (
    t1 = subParam(el, 0, 1, x, y, z); allTrees = append(allTrees, t1);
    t2 = subParam(el, 1, 0, y, z, x); allTrees = append(allTrees, t2););
 )

allTrees = unique allTrees;
length allTrees



for ord in allOrders do (
    I1 = makeIdeal(toSequence ord_0);
    I2 = makeIdeal(toSequence ord_1);
    I3 = makeIdeal(toSequence ord_2);
    I4 = makeIdeal(toSequence ord_3);
    I5 = makeIdeal(toSequence ord_4);


    J1 = T1*I1 + (1-T1)*I2;
    J2 = T2*J1 + (1-T2)*I3;
    J3 = T3*J2 + (1-T3)*I4;
    J4 = T4*J3 + (1-T4)*I5;

    J = J4;
    
    Gs = flatten entries gens gb (J, DegreeLimit => 7);
    
    noTs = {};
    for el in Gs do { if toList(set{T1, T2, T3, T4} * set support(el)) == {} then noTs = append(noTs, el); };
    

    irred = select(noTs, el -> (factor el)#0#0 == el);
    
    int = {};
    for i from 0 to (length irred) - 1 do (
    
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
    	 );
     );

     print (length select(int, el -> el == true));
)
