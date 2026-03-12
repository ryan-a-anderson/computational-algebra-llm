restart
--NB: this code gives correct results only for homogeneous ideals
--the difference with the other program is that we remove one likelihood variable
--since the second row can be multiplied by -U+ by Elizabeth's and Jose's paper
loadPackage("Depth");

--function that takes an ideal in the fourier coordinates and returns an ideal in original coordinates
transformIdealToOriginalCoords=(fourierI)->(
    R:=QQ[q_(0,0,0)..q_(1,1,1),p_(0,0,0)..p_(1,1,1)];
    fourierI=sub(fourierI,R);
    
    --ideal that records relations between the original and Fourier coordinates (p and q)
    K:=matrix{{1,1},{1,-1}};
    H:=K**K**K;
    H=sub(H,R);
    qVec=transpose(matrix{{q_(0,0,0)..q_(1,1,1)}});
    pVec=transpose(matrix{{p_(0,0,0)..p_(1,1,1)}});
    I:=ideal flatten entries(qVec-H*pVec);
        
    --eliminate the fourier coords q's to get an ideal in the original coords p's
    qList:=flatten flatten for i to 1 list for j to 1 list for k to 1 list q_(i,j,k);
    originalI:=eliminate(qList,I+fourierI);
    
    return originalI;
    )

--the case when we introduce extra leaf for the root
--we assume the 0thcoordinate corresponds to the root
transformIdealToOriginalCoordsRooted=(fourierI)->(
    R:=QQ[q_(0,0,0,0)..q_(1,1,1,1),p_(0,0,0)..p_(1,1,1)];
    fourierI=sub(fourierI,R);
    
    --ideal that records relations between the original and Fourier coordinates (p and q)
    K:=matrix{{1,1},{1,-1}};
    H:=K**K**K**K;
    H=sub(H,R);
    qVec=transpose(matrix{{q_(0,0,0,0)..q_(1,1,1,1)}});
    pVec=transpose(matrix{{p_(0,0,0)..p_(1,1,1)}}|(matrix{for i to 7 list 0}));
    I:=ideal flatten entries(qVec-H*pVec);
    
    --eliminate the fourier coords q's to get an ideal in the original coords p's
    qList:=flatten flatten flatten for i to 1 list for j to 1 list for k to 1 list for l to 1 list q_(i,j,k,l);
    originalI:=eliminate(qList,I+fourierI);
    
    return originalI;
    )

--choose a regular sequence from the generators of the ideal to construct a complete intersection
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

--function that constructs the likelihood ideal of an ideal
--NB: the original ideal should not include the summing to one condition
makeLikelihoodIdealFromCompleteIntersection=(originalI)->(        
    c:= (numgens originalI);
    R:=QQ[p_(0,0,0)..p_(1,1,1),l_1..l_c];
    originalI=sub(originalI,R);
    augmentedJacobian:=makeAugmentedJacobian(originalI);
    augmentedJacobian=sub(augmentedJacobian,R);
    
    --construct the left kernel vector and the likelhood ideal
    uSum:=sum entries (transpose augmentedJacobian)_0;
    kernelVector:=matrix{join({1,-uSum},for i from 1  to c list l_i)};
    likelihoodIdeal:=originalI+ideal(kernelVector*augmentedJacobian);
    
    return likelihoodIdeal;
    )

--construct the augmented Jacobian matrix
makeAugmentedJacobian=(originalI)->(
    R2:=QQ[p_(0,0,0)..p_(1,1,1)];
    originalI=sub(originalI,R2);
    -- first row consists of random positive integers
    -- firstRow:=matrix{for i to 7 list random(1,100)};
    firstRow:=matrix{{64,10,36,81,23,44,86,69}};
    -- construct the second to last row of the augmented Jacobian
    -- the second row will correspond to the row of variables
    secondRow:=matrix{for i to 7 list 1};
    J:=transpose jacobian originalI;
    J=secondRow||J;
    -- multiply each column by the corresponding variable
    D:=matrix for i to 7 list for j to 7 list if i==j then (vars R2)_(0,i) else 0;
    lastRows:=J*D;
    augmentedJacobian:=firstRow||lastRows;
    return augmentedJacobian;
    )
    
-- make likelihood ideal from Fourier coordinates    
makeLikelihoodIdealFromFourierCoordinates=(fourierIdeal)->(
    originalIdeal:=transformIdealToOriginalCoords(fourierIdeal);
    completeIntersectionIdeal:=makeCompleteIntersectionIdeal(originalIdeal);
    likelihoodIdeal:=makeLikelihoodIdealFromCompleteIntersection(completeIntersectionIdeal);
    return likelihoodIdeal;
    )    
   
-- make likelihood ideal from original coordinates    
makeLikelihoodIdeal=(myIdeal)->(
    completeIntersectionIdeal:=makeCompleteIntersectionIdeal(myIdeal);
    likelihoodIdeal:=makeLikelihoodIdealFromCompleteIntersection(completeIntersectionIdeal);
    "/Users/kubjask1/Dropbox/Dimitra/programs/likelihoodIdealM2" << toString likelihoodIdeal << endl << toString ring likelihoodIdeal<< close;
    return likelihoodIdeal;
    )




R=QQ[q_(0,0,0)..q_(1,1,1),p_(0,0,0)..p_(1,1,1)];

--ideal defining the Zariski closure
eqnsIFourier=ideal(q_(0,0,1)*q_(1,1,0)-q_(0,0,0)*q_(1,1,1),
    q_(0,1,0)*q_(1,0,1)-q_(0,0,0)*q_(1,1,1),
    q_(1,0,0)*q_(0,1,1)-q_(0,0,0)*q_(1,1,1));
eqnsI=transformIdealToOriginalCoords(eqnsIFourier);

--inequalities for three leaves
R=QQ[q_(0,0,0,0)..q_(1,1,1,1)]
ineqIFourier=ideal(q_(1,1,0,0)*q_(1,0,1,0)-q_(0,1,1,0)*q_(0,0,0,0),
    q_(0,1,1,0)*q_(0,1,0,1)-q_(0,0,1,1)*q_(0,0,0,0),
    q_(0,0,1,1)*q_(1,0,1,0)-q_(1,0,0,1)*q_(0,0,0,0),
    q_(1,0,0,1)*q_(0,1,0,1)-q_(1,1,0,0)*q_(0,0,0,0));
ineqI=transformIdealToOriginalCoordsRooted(ineqIFourier);

--substitute into the same ring
R=QQ[p_(0,0,0)..p_(1,1,1)];
eqnsI=sub(eqnsI,R);
ineqI=sub(ineqI,R);
ineqI2=sub(ineqI2,R);
  
--likelihoodIdeal=MLDegree(eqnsI)
fourierIdeal=ideal(q_(1,1,0));
originalIdeal=transformIdealToOriginalCoords(fourierIdeal); 
likelihoodIdeal=makeLikelihoodIdealFromFourierCoordinates(fourierIdeal);

"/Users/kubjask1/Dropbox/Dimitra/programs/likelihoodIdealM2" << toString likelihoodIdeal << endl << toString ring likelihoodIdeal<< close

--------------------
--ideal for Anton
R=QQ[p_(0,0,0)..p_(1,1,1)];
originalIdeal = ideal(p_(0,0,0)+p_(0,0,1)+p_(0,1,0)+p_(0,1,1)+p_(1,0,0)+p_(1,0,1)+p_(1,1,0)+p_(1,1,1)-1,p_(0,1,0)*p_(1,0,0)-p_(0,1,1)*p_(1,0,1)+p_(0,0,1)*p_(1,1,0)+p_(0,1,0)*p_(1,1,0)+p
     _(0,1,1)*p_(1,1,0)+p_(1,0,0)*p_(1,1,0)+p_(1,0,1)*p_(1,1,0)+p_(1,1,0)^2+p_(0,0,1)*p_(1,1,1)+p_(1,1,0)*p_(1,1,1)-p_(1,1,0),p_(0,0,1)*p_(1,0,0)+p_(0,0,1)*p_(1,0,1)+p_(0,1,0
     )*p_(1,0,1)+p_(0,1,1)*p_(1,0,1)+p_(1,0,0)*p_(1,0,1)+p_(1,0,1)^2-p_(0,1,1)*p_(1,1,0)+p_(1,0,1)*p_(1,1,0)+p_(0,1,0)*p_(1,1,1)+p_(1,0,1)*p_(1,1,1)-p_(1,0,1),p_(0,0,1)*p_(0,
     1,0)+p_(0,0,1)*p_(0,1,1)+p_(0,1,0)*p_(0,1,1)+p_(0,1,1)^2+p_(0,1,1)*p_(1,0,0)+p_(0,1,1)*p_(1,0,1)+p_(0,1,1)*p_(1,1,0)-p_(1,0,1)*p_(1,1,0)+p_(0,1,1)*p_(1,1,1)+p_(1,0,0)*p
     _(1,1,1)-p_(0,1,1))
likelihoodIdeal = makeLikelihoodIdeal(originalIdeal);

--------------------
--this part is for translating inequalities only

translateInequality=(ineq)->(
    R:=QQ[q_(0,0,0,0)..q_(1,1,1,1),p_(0,0,0)..p_(1,1,1)];
    ineq=sub(ineq,R);
    
    --ideal that records relations between the original and Fourier coordinates (p and q)
    K:=matrix{{1,1},{1,-1}};
    H:=K**K**K**K;
    H=sub(H,R);
    qVec=transpose(matrix{{q_(0,0,0,0)..q_(1,1,1,1)}});
    pVec=transpose(matrix{{p_(0,0,0)..p_(1,1,1)}}|(matrix{for i to 7 list 0}));
    substitutionList:=for i to 15 list qVec_(i,0)=>(H*pVec)_(i,0);
    
    ineq=sub(ineq,substitutionList);
    return ineq;
    )

translateInequality2=(ineq)->(
    R:=QQ[q_(0,0,0)..q_(1,1,1),p_(0,0,0)..p_(1,1,1)];
    ineq=sub(ineq,R);
    
    --ideal that records relations between the original and Fourier coordinates (p and q)
    K:=matrix{{1,1},{1,-1}};
    H:=K**K**K;
    H=sub(H,R);
    qVec=transpose(matrix{{q_(0,0,0)..q_(1,1,1)}});
    pVec=transpose(matrix{{p_(0,0,0)..p_(1,1,1)}});
    substitutionList:=for i to 7 list qVec_(i,0)=>(H*pVec)_(i,0);
    
    ineq=sub(ineq,substitutionList);
    return ineq;
    )

--translate inequalities
R=QQ[q_(0,0,0)..q_(1,1,1)];
ineqFourier=-q_(1,0,0)*q_(0,0,1)+q_(1,0,1)*q_(0,0,0);
ineq=translateInequality2(ineqFourier)
toString (1/4*ineq)
