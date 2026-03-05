loadPackage "Quasidegrees"; loadPackage "EigenSolver"; load "gfanInterface.m2";
--given A, the algorithm will give the chamber complex
--change A as necessary
A=matrix{{1, 1, 1, 1, 1, 1, 1, 1},
         {0, 0, 0, 0, 1, 1, 2, 2},
         {0, 0, 1, 1, 0, 1, 0, 1},
         {0, 1, 0, 1, 0, 0, 0, 0}}

n=numgens source A

R=QQ[y_1..y_n]; I=toricIdeal(A,R); "ideal" << toString((entries gens I)#0) << endl << close
B = entries generators kernel(A); BB=transpose(matrix B);
secFan = gfanSecondaryFan(B); raysFan = rays secFan; M=A*raysFan;
vs={}; inds={};
for i from 0 to  (numgens source M)-1 do (el=promote(M_i,QQ); s=el_0; vs=append(vs,(1/s)*el); inds=append(inds,i);)
bases={}; for s in subsets(numgens source A,4) do (if det(submatrix(A,,s))!=0 then bases=append(bases, s);)
"bases" << bases << endl << close

--adjust below depending on the dimension of your model
--i.e. k-dim faces will be given by cones(n+k-3,secFan)
verts = vs / entries // toString; "verts" << verts << endl << close --all vertices
edges = cones(n-2,secFan); "edges" << edges << endl << close -- all edges
ridges = cones(n-1,secFan); "ridges" << ridges << endl << close -- all ridges
threedim = cones(n,secFan); "threedim" << threedim << endl << close -- all ridges

