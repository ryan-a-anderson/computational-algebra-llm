# ComputationsBook Training Data
Downloaded from `Macaulay2/M2` stable branch, `tests/ComputationsBook/`.

---

## completeIntersections / chapter.m2 — chunk 0

### Input

```macaulay2
A = QQ[w,x,y,z]
U = matrix {{w,x},{y,z}}
C = chainComplex U
L = HH_0 C
f = -det U
f * L == 0
s = nullhomotopy (-f * id_C)
s * C.dd + C.dd * s == -f
```

### Output

```
i1 : A = QQ[w,x,y,z]

o1 = A

o1 : PolynomialRing

i2 : U = matrix {{w,x},{y,z}}

o2 = | w x |
     | y z |

             2       2
o2 : Matrix A  <--- A

i3 : C = chainComplex U

2      2
o3 = A  <-- A
             
     0      1

o3 : ChainComplex

i4 : L = HH_0 C

o4 = cokernel | w x |
              | y z |

                            2
o4 : A-module, quotient of A

i5 : f = -det U

o5 = x*y - w*z

o5 : A

i6 : f * L == 0

o6 = true

i7 : s = nullhomotopy (-f * id_C)

2                     2
o7 = 1 : A  <----------------- A  : 0
               {1} | z  -x |
               {1} | -y w  |

o7 : ChainComplexMap

i8 : s * C.dd + C.dd * s == -f

o8 = true
```

---

## completeIntersections / chapter.m2 — chunk 1

### Input

```macaulay2
V = s_0
A = QQ[x,y,z];
f = x^3 + 3*y^3 - 2*y*z^2 + 5*z^3;
B = A/f;
m = ideal(x,y,z)
M = B^1/m^2;
F = resolution(M, LengthLimit=>8)
restrict1 = N -> coker(lift(presentation N,A) | f);
```

### Output

```
i9 : V = s_0

o9 = {1} | z  -x |
     {1} | -y w  |

             2       2
o9 : Matrix A  <--- A

i10 : A = QQ[x,y,z];

i11 : f = x^3 + 3*y^3 - 2*y*z^2 + 5*z^3;

i12 : B = A/f;

i13 : m = ideal(x,y,z)

o13 = ideal (x, y, z)

o13 : Ideal of B

i14 : M = B^1/m^2;

i15 : F = resolution(M, LengthLimit=>8)

1      6      9      9      9      9      9      9      9
o15 = B  <-- B  <-- B  <-- B  <-- B  <-- B  <-- B  <-- B  <-- B
                                                               
      0      1      2      3      4      5      6      7      8

o15 : ChainComplex

i16 : restrict1 = N -> coker(lift(presentation N,A) | f);
```

---

## completeIntersections / chapter.m2 — chunk 2

### Input

```macaulay2
L = restrict1 cokernel F.dd_4;
C = res L;
U = C.dd_1;
print U
{4} | 0  xy x2       y2    0        0        0        yz-5/2z2 0      |
{4} | 0  x2 -3y2     xy    yz-5/2z2 0        yz-5/2z2 0        0      |
{4} | x2 0  -2yz+5z2 0     y2-5/2yz yz-5/2z2 -5/2yz   0        0      |
{5} | 0  0  0        1/3z  0        0        0        1/2y     x      |
{5} | 0  0  -z       0     1/2y     0        1/2y     -1/2x    0      |
{5} | 0  -z 0        0     -1/2x    0        -1/2x    0        3y     |
{5} | 0  0  0        -1/3x 0        1/2y     -1/3z    0        0      |
{5} | -z y  x        0     0        -1/2x    0        0        0      |
{5} | y  0  0        0     0        0        1/3x     0        -2y+5z |
s = nullhomotopy (-f * id_C);
V = s_0;
print V
{6} | 0   0  -x  0         0         -2y2+5yz 0         -2yz+5z2 -3y2 |
{6} | 0   -x 0   0         0         -2yz+5z2 -3xy      -3y2     -3yz |
{6} | -x  y  0   0         -2yz+5z2  0        0         0        0    |
{6} | -3y 0  0   6yz-15z2  0         0        3x2       3xy      3xz  |
{6} | 0   2z -3y -15xz     -15yz     2x2      6yz-15z2  0        3x2  |
{6} | -2x 0  2z  0         -4yz+10z2 0        -6y2      2x2      0    |
{6} | 0   0  3y  -6xy+15xz -6y2+15yz 0        -6yz+15z2 0        -3x2 |
{6} | 2z  0  0   -6y2      2x2       2xy      0         0        0    |
{6} | 0   0  0   -x2       -xy       -y2      -xz       -yz      -z2  |
U*V+f==0
```

### Output

```
i17 : L = restrict1 cokernel F.dd_4;

i18 : C = res L;

i19 : U = C.dd_1;

9       9
o19 : Matrix A  <--- A

i20 : print U
{4} | 0  xy x2       y2    0        0        0        yz-5/2z2 0      |
{4} | 0  x2 -3y2     xy    yz-5/2z2 0        yz-5/2z2 0        0      |
{4} | x2 0  -2yz+5z2 0     y2-5/2yz yz-5/2z2 -5/2yz   0        0      |
{5} | 0  0  0        1/3z  0        0        0        1/2y     x      |
{5} | 0  0  -z       0     1/2y     0        1/2y     -1/2x    0      |
{5} | 0  -z 0        0     -1/2x    0        -1/2x    0        3y     |
{5} | 0  0  0        -1/3x 0        1/2y     -1/3z    0        0      |
{5} | -z y  x        0     0        -1/2x    0        0        0      |
{5} | y  0  0        0     0        0        1/3x     0        -2y+5z |

i21 : s = nullhomotopy (-f * id_C);

i22 : V = s_0;

9       9
o22 : Matrix A  <--- A

i23 : print V
{6} | 0   0  -x  0         0         -2y2+5yz 0         -2yz+5z2 -3y2 |
{6} | 0   -x 0   0         0         -2yz+5z2 -3xy      -3y2     -3yz |
{6} | -x  y  0   0         -2yz+5z2  0        0         0        0    |
{6} | -3y 0  0   6yz-15z2  0         0        3x2       3xy      3xz  |
{6} | 0   2z -3y -15xz     -15yz     2x2      6yz-15z2  0        3x2  |
{6} | -2x 0  2z  0         -4yz+10z2 0        -6y2      2x2      0    |
{6} | 0   0  3y  -6xy+15xz -6y2+15yz 0        -6yz+15z2 0        -3x2 |
{6} | 2z  0  0   -6y2      2x2       2xy      0         0        0    |
{6} | 0   0  0   -x2       -xy       -y2      -xz       -yz      -z2  |

i24 : U*V+f==0

o24 = true
```

---

## completeIntersections / chapter.m2 — chunk 3

### Input

```macaulay2
V*U+f==0
matrixFactorization = M -> (
         B := ring M;
         f := (ideal B)_0;
         e := numgens B;
         F := resolution(M, LengthLimit => e+1);
         L := restrict1 cokernel F.dd_(e+1);
         C := res L;
         U := C.dd_1;
         s := nullhomotopy (-f * id_C);
         V := s_0;
         assert( U*V + f == 0 );
         assert( V*U + f == 0 );
         return (U,V));
time (U,V) = matrixFactorization(B^1/m^3);
     -- used 0.21 seconds
U;
V;
F.dd_3 - F.dd_5 == 0
F.dd_4 - F.dd_6 == 0
F.dd_5 - F.dd_7 == 0
```

### Output

```
i25 : V*U+f==0

o25 = true

i26 : matrixFactorization = M -> (
         B := ring M;
         f := (ideal B)_0;
         e := numgens B;
         F := resolution(M, LengthLimit => e+1);
         L := restrict1 cokernel F.dd_(e+1);
         C := res L;
         U := C.dd_1;
         s := nullhomotopy (-f * id_C);
         V := s_0;
         assert( U*V + f == 0 );
         assert( V*U + f == 0 );
         return (U,V));

i27 : time (U,V) = matrixFactorization(B^1/m^3);
     -- used 0.21 seconds

i28 : U;

15       15
o28 : Matrix A   <--- A

i29 : V;

15       15
o29 : Matrix A   <--- A

i30 : F.dd_3 - F.dd_5 == 0

o30 = false

i31 : F.dd_4 - F.dd_6 == 0

o31 = false

i32 : F.dd_5 - F.dd_7 == 0

o32 = true
```

---

## completeIntersections / chapter.m2 — chunk 4

### Input

```macaulay2
M = B^1/m^2;
G = resolution(M, LengthLimit => 8, Strategy => 0)
G.dd_3 - G.dd_5 == 0
G.dd_4 - G.dd_6 == 0
G.dd_5 - G.dd_7 == 0
M = B^1/m^3;
F = resolution(M, LengthLimit=>8)
M' = restrict1 M;
```

### Output

```
i33 : M = B^1/m^2;

i34 : G = resolution(M, LengthLimit => 8, Strategy => 0)

1      6      9      9      9      9      9      9      9
o34 = B  <-- B  <-- B  <-- B  <-- B  <-- B  <-- B  <-- B  <-- B
                                                               
      0      1      2      3      4      5      6      7      8

o34 : ChainComplex

i35 : G.dd_3 - G.dd_5 == 0

o35 = true

i36 : G.dd_4 - G.dd_6 == 0

o36 = true

i37 : G.dd_5 - G.dd_7 == 0

o37 = true

i38 : M = B^1/m^3;

i39 : F = resolution(M, LengthLimit=>8)

1      10      16      15      15      15      15      15      15
o39 = B  <-- B   <-- B   <-- B   <-- B   <-- B   <-- B   <-- B   <-- B
                                                                      
      0      1       2       3       4       5       6       7       8

o39 : ChainComplex

i40 : M' = restrict1 M;
```

---

## completeIntersections / chapter.m2 — chunk 5

### Input

```macaulay2
C = res M'
K = ZZ/103;
A = K[x,Degrees=>{5}];
B = A/(x^3);
M = B^1/(x^2);
N = B^1/(x);
H = Ext(M,N);
ring H
```

### Output

```
i41 : C = res M'

1      10      15      6
o41 = A  <-- A   <-- A   <-- A  <-- 0
                                     
      0      1       2       3      4

o41 : ChainComplex

i42 : K = ZZ/103;

i43 : A = K[x,Degrees=>{5}];

i44 : B = A/(x^3);

i45 : M = B^1/(x^2);

i46 : N = B^1/(x);

i47 : H = Ext(M,N);

i48 : ring H

o48 = K [$X , x, Degrees => {{-2, -15}, {0, 5}}]
           1

o48 : PolynomialRing
```

---

## completeIntersections / chapter.m2 — chunk 6

### Input

```macaulay2
degree \ gens ring H
S = ring H;
H
A = K[x,y];
J = ideal(x^3,y^2);
B = A/J;
N = cokernel matrix{{x^2,x*y}}
time H = Ext(N,N);
     -- used 0.2 seconds
```

### Output

```
i49 : degree \ gens ring H

o49 = {{-2, -15}, {0, 5}}

o49 : List

i50 : S = ring H;

i51 : H

o51 = cokernel {0, 0}    | 0 x |
               {-1, -10} | x 0 |

                             2
o51 : S-module, quotient of S

i52 : A = K[x,y];

i53 : J = ideal(x^3,y^2);

o53 : Ideal of A

i54 : B = A/J;

i55 : N = cokernel matrix{{x^2,x*y}}

o55 = cokernel | x2 xy |

                             1
o55 : B-module, quotient of B

i56 : time H = Ext(N,N);
     -- used 0.2 seconds
```

---

## completeIntersections / chapter.m2 — chunk 7

### Input

```macaulay2
ring H
S = ring H;
transpose vars S
trim J
H
partSelector = predicate -> H -> (
         R := ring H;
         H' := prune image matrix {
             select(
                 apply(numgens H, i -> H_{i}),
                 f -> predicate first first degrees source f
                 )
             };
         H');
evenPart = partSelector even; oddPart = partSelector odd;
evenPart H
```

### Output

```
i57 : ring H

o57 = K [$X , $X , x, y, Degrees => {{-2, -2}, {-2, -3}, {0, 1}, {0, 1}}]
           1    2

o57 : PolynomialRing

i58 : S = ring H;

i59 : transpose vars S

o59 = {2, 2}  | $X_1 |
      {2, 3}  | $X_2 |
      {0, -1} | x    |
      {0, -1} | y    |

              4       1
o59 : Matrix S  <--- S

i60 : trim J

2   3
o60 = ideal (y , x )

o60 : Ideal of A

i61 : H

o61 = cokernel {-2, -2} | 0 0 0 0 0 0 0 0 0  0  0  y x 0    0    0     0     |
               {-1, -1} | y 0 0 0 0 x 0 0 0  0  0  0 0 $X_1 0    0     0     |
               {-1, -1} | 0 0 0 y 0 0 0 x 0  0  0  0 0 0    $X_1 0     0     |
               {-1, -1} | 0 y 0 0 x 0 0 0 0  0  0  0 0 0    0    0     0     |
               {-1, -1} | 0 0 y 0 0 0 x 0 0  0  0  0 0 0    0    0     0     |
               {0, 0}   | 0 0 0 0 0 0 0 0 y2 xy x2 0 0 0    0    $X_1y $X_1x |

                             6
o61 : S-module, quotient of S

i62 : partSelector = predicate -> H -> (
         R := ring H;
         H' := prune image matrix {
             select(
                 apply(numgens H, i -> H_{i}),
                 f -> predicate first first degrees source f
                 )
             };
         H');

i63 : evenPart = partSelector even; oddPart = partSelector odd;

i65 : evenPart H

o65 = cokernel {-2, -2} | 0  0  0  y x 0     0     |
               {0, 0}   | y2 xy x2 0 0 $X_1y $X_1x |

                             2
o65 : S-module, quotient of S
```

---

## completeIntersections / chapter.m2 — chunk 8

### Input

```macaulay2
oddPart H
print code(Ext,Module,Module)
-- ../../../m2/ext.m2:82-171
Ext(Module,Module) := Module => (M,N) -> (
  cacheModule := youngest(M,N);
  cacheKey := (Ext,M,N);
  if cacheModule#?cacheKey then return cacheModule#cacheKey;
  B := ring M;
  if B =!= ring N
  then error "expected modules over the same ring";
  if not isCommutative B
  then error "'Ext' not implemented yet for noncommutative rings.";
  if not isHomogeneous B
  then error "'Ext' received modules over an inhomogeneous ring";
  if not isHomogeneous N or not isHomogeneous M
  then error "'Ext' received an inhomogeneous module";
  if N == 0 then B^0
  else if M == 0 then B^0
  else (
    p := presentation B;
    A := ring p;
    I := ideal mingens ideal p;
    n := numgens A;
    c := numgens I;
    if c =!= codim B 
    then error "total Ext available only for complete intersections";
    f := apply(c, i -> I_i);
    pM := lift(presentation M,A);
    pN := lift(presentation N,A);
    M' := cokernel ( pM | p ** id_(target pM) );
    N' := cokernel ( pN | p ** id_(target pN) );
    C := complete resolution M';
    X := local X;
    K := coefficientRing A;
    -- compute the fudge factor for the adjustment of bidegrees
    fudge := if #f > 0 then 1 + max(first \ degree \ f) // 2 else 0;
    S := K(monoid [X_1 .. X_c, toSequence A.generatorSymbols,
      Degrees => {
        apply(0 .. c-1, i -> {-2, - first degree f_i}),
        apply(0 .. n-1, j -> { 0,   first degree A_j})
        },
      Adjust => v -> {- fudge * v#0 + v#1, - v#0},
      Repair => w -> {- w#1, - fudge * w#1 + w#0}
      ]);
    -- make a monoid whose monomials can be used as indices
    Rmon := monoid [X_1 .. X_c,Degrees=>{c:{2}}];
    -- make group ring, so 'basis' can enumerate the monomials
    R := K Rmon;
    -- make a hash table to store the blocks of the matrix
    blks := new MutableHashTable;
    blks#(exponents 1_Rmon) = C.dd;
    scan(0 .. c-1, i -> 
         blks#(exponents Rmon_i) = nullhomotopy (- f_i*id_C));
    -- a helper function to list the factorizations of a monomial
    factorizations := (gamma) -> (
      -- Input: gamma is the list of exponents for a monomial
      -- Return a list of pairs of lists of exponents showing the
      -- possible factorizations of gamma.
      if gamma === {} then { ({}, {}) }
      else (
        i := gamma#-1;
        splice apply(factorizations drop(gamma,-1), 
          (alpha,beta) -> apply (0..i, 
               j -> (append(alpha,j), append(beta,i-j))))));
    scan(4 .. length C + 1, 
      d -> if even d then (
        scan( exponents \ leadMonomial \ first entries basis(d,R), 
          gamma -> (
            s := - sum(factorizations gamma,
              (alpha,beta) -> (
                if blks#?alpha and blks#?beta
                then blks#alpha * blks#beta
                else 0));
            -- compute and save the nonzero nullhomotopies
            if s != 0 then blks#gamma = nullhomotopy s;
            ))));
    -- make a free module whose basis elements have the right degrees
    spots := C -> sort select(keys C, i -> class i === ZZ);
    Cstar := S^(apply(spots C,
        i -> toSequence apply(degrees C_i, d -> {i,first d})));
    -- assemble the matrix from its blocks.
    -- We omit the sign (-1)^(n+1) which would ordinarily be used,
    -- which does not affect the homology.
    toS := map(S,A,apply(toList(c .. c+n-1), i -> S_i),
      DegreeMap => prepend_0);
    Delta := map(Cstar, Cstar, 
      transpose sum(keys blks, m -> S_m * toS sum blks#m),
      Degree => {-1,0});
    DeltaBar := Delta ** (toS ** N');
    assert isHomogeneous DeltaBar;
    assert(DeltaBar * DeltaBar == 0);
    -- now compute the total Ext as a single homology module
    cacheModule#cacheKey = prune homology(DeltaBar,DeltaBar)))
A = K[x,y,z];
J = trim ideal(x^3,y^4,z^5)
B = A/J;
f = random (B^3, B^{-2,-3})
f_{1}
M = cokernel f;
```

### Output

```
i66 : oddPart H

o66 = cokernel {-1, -1} | 0 0 y 0 0 0 x 0 0    0    |
               {-1, -1} | 0 y 0 0 x 0 0 0 0    0    |
               {-1, -1} | 0 0 0 y 0 0 0 x 0    $X_1 |
               {-1, -1} | y 0 0 0 0 x 0 0 $X_1 0    |

                             4
o66 : S-module, quotient of S

i67 : print code(Ext,Module,Module)
-- ../../../m2/ext.m2:82-171
Ext(Module,Module) := Module => (M,N) -> (
  cacheModule := youngest(M,N);
  cacheKey := (Ext,M,N);
  if cacheModule#?cacheKey then return cacheModule#cacheKey;
  B := ring M;
  if B =!= ring N
  then error "expected modules over the same ring";
  if not isCommutative B
  then error "'Ext' not implemented yet for noncommutative rings.";
  if not isHomogeneous B
  then error "'Ext' received modules over an inhomogeneous ring";
  if not isHomogeneous N or not isHomogeneous M
  then error "'Ext' received an inhomogeneous module";
  if N == 0 then B^0
  else if M == 0 then B^0
  else (
    p := presentation B;
    A := ring p;
    I := ideal mingens ideal p;
    n := numgens A;
    c := numgens I;
    if c =!= codim B 
    then error "total Ext available only for complete intersections";
    f := apply(c, i -> I_i);
    pM := lift(presentation M,A);
    pN := lift(presentation N,A);
    M' := cokernel ( pM | p ** id_(target pM) );
    N' := cokernel ( pN | p ** id_(target pN) );
    C := complete resolution M';
    X := local X;
    K := coefficientRing A;
    -- compute the fudge factor for the adjustment of bidegrees
    fudge := if #f > 0 then 1 + max(first \ degree \ f) // 2 else 0;
    S := K(monoid [X_1 .. X_c, toSequence A.generatorSymbols,
      Degrees => {
        apply(0 .. c-1, i -> {-2, - first degree f_i}),
        apply(0 .. n-1, j -> { 0,   first degree A_j})
        },
      Adjust => v -> {- fudge * v#0 + v#1, - v#0},
      Repair => w -> {- w#1, - fudge * w#1 + w#0}
      ]);
    -- make a monoid whose monomials can be used as indices
    Rmon := monoid [X_1 .. X_c,Degrees=>{c:{2}}];
    -- make group ring, so 'basis' can enumerate the monomials
    R := K Rmon;
    -- make a hash table to store the blocks of the matrix
    blks := new MutableHashTable;
    blks#(exponents 1_Rmon) = C.dd;
    scan(0 .. c-1, i -> 
         blks#(exponents Rmon_i) = nullhomotopy (- f_i*id_C));
    -- a helper function to list the factorizations of a monomial
    factorizations := (gamma) -> (
      -- Input: gamma is the list of exponents for a monomial
      -- Return a list of pairs of lists of exponents showing the
      -- possible factorizations of gamma.
      if gamma === {} then { ({}, {}) }
      else (
        i := gamma#-1;
        splice apply(factorizations drop(gamma,-1), 
          (alpha,beta) -> apply (0..i, 
               j -> (append(alpha,j), append(beta,i-j))))));
    scan(4 .. length C + 1, 
      d -> if even d then (
        scan( exponents \ leadMonomial \ first entries basis(d,R), 
          gamma -> (
            s := - sum(factorizations gamma,
              (alpha,beta) -> (
                if blks#?alpha and blks#?beta
                then blks#alpha * blks#beta
                else 0));
            -- compute and save the nonzero nullhomotopies
            if s != 0 then blks#gamma = nullhomotopy s;
            ))));
    -- make a free module whose basis elements have the right degrees
    spots := C -> sort select(keys C, i -> class i === ZZ);
    Cstar := S^(apply(spots C,
        i -> toSequence apply(degrees C_i, d -> {i,first d})));
    -- assemble the matrix from its blocks.
    -- We omit the sign (-1)^(n+1) which would ordinarily be used,
    -- which does not affect the homology.
    toS := map(S,A,apply(toList(c .. c+n-1), i -> S_i),
      DegreeMap => prepend_0);
    Delta := map(Cstar, Cstar, 
      transpose sum(keys blks, m -> S_m * toS sum blks#m),
      Degree => {-1,0});
    DeltaBar := Delta ** (toS ** N');
    assert isHomogeneous DeltaBar;
    assert(DeltaBar * DeltaBar == 0);
    -- now compute the total Ext as a single homology module
    cacheModule#cacheKey = prune homology(DeltaBar,DeltaBar)))

i68 : A = K[x,y,z];

i69 : J = trim ideal(x^3,y^4,z^5)

3   4   5
o69 = ideal (x , y , z )

o69 : Ideal of A

i70 : B = A/J;

i71 : f = random (B^3, B^{-2,-3})

o71 = | 27x2+49xy-14y2-23xz-6yz-19z2 38x2y-34xy2+4y3+x2z+16xyz-y2z-5xz2-6yz2+47z3        |
      | -5x2+44xy+38y2+40xz+15yz+4z2 -37x2y+51xy2-36y3+26x2z-38xyz-17y2z+17xz2-11yz2+8z3 |
      | 21x2-30xy+32y2-47xz+7yz-50z2 -6x2y-14xy2-26y3-7x2z+41xyz+50y2z+26xz2+46yz2-44z3  |

              3       2
o71 : Matrix B  <--- B

i72 : f_{1}

o72 = | 38x2y-34xy2+4y3+x2z+16xyz-y2z-5xz2-6yz2+47z3        |
      | -37x2y+51xy2-36y3+26x2z-38xyz-17y2z+17xz2-11yz2+8z3 |
      | -6x2y-14xy2-26y3-7x2z+41xyz+50y2z+26xz2+46yz2-44z3  |

              3       1
o72 : Matrix B  <--- B

i73 : M = cokernel f;
```

---

## completeIntersections / chapter.m2 — chunk 9

### Input

```macaulay2
time P = Ext(M,B^1/(x,y,z));
     -- used 1.64 seconds
S = ring P;
transpose vars S
R = K[X_1..X_3,Degrees => {{-2,-3},{-2,-4},{-2,-5}},
              Adjust => S.Adjust, Repair => S.Repair];
phi = map(R,S,{X_1,X_2,X_3,0,0,0})
P = prune (phi ** P);
transpose vars ring P
evenPart P
```

### Output

```
i74 : time P = Ext(M,B^1/(x,y,z));
     -- used 1.64 seconds

i75 : S = ring P;

i76 : transpose vars S

o76 = {2, 3}  | $X_1 |
      {2, 4}  | $X_2 |
      {2, 5}  | $X_3 |
      {0, -1} | x    |
      {0, -1} | y    |
      {0, -1} | z    |

              6       1
o76 : Matrix S  <--- S

i77 : R = K[X_1..X_3,Degrees => {{-2,-3},{-2,-4},{-2,-5}},
              Adjust => S.Adjust, Repair => S.Repair];

i78 : phi = map(R,S,{X_1,X_2,X_3,0,0,0})

o78 = map(R,S,{X , X , X , 0, 0, 0})
                1   2   3

o78 : RingMap R <--- S

i79 : P = prune (phi ** P);

i80 : transpose vars ring P

o80 = {2, 3} | X_1 |
      {2, 4} | X_2 |
      {2, 5} | X_3 |

              3       1
o80 : Matrix R  <--- R

i81 : evenPart P

o81 = cokernel {-4, -10} | 0   0   0   0   0   0   0   0   0   0    |
               {-4, -10} | 0   0   0   0   0   0   0   0   0   -X_2 |
               {-4, -11} | 0   0   0   0   0   0   0   0   0   X_1  |
               {0, 0}    | 0   0   X_3 0   0   X_2 0   X_1 0   0    |
               {0, 0}    | 0   X_3 0   0   X_2 0   X_1 0   0   0    |
               {0, 0}    | X_3 0   0   X_2 0   0   0   0   X_1 0    |
               {-2, -7}  | 0   0   0   0   0   0   0   0   0   0    |
               {-2, -7}  | 0   0   0   0   0   0   0   0   0   0    |
               {-2, -7}  | 0   0   0   0   0   0   0   0   0   0    |
               {-2, -7}  | 0   0   0   0   0   0   0   0   0   0    |

                             10
o81 : R-module, quotient of R
```

---

## completeIntersections / chapter.m2 — chunk 10

### Input

```macaulay2
oddPart P
changeRing = H -> (
         S := ring H;
         K := coefficientRing S;
         degs := select(degrees source vars S,
              d -> 0 != first d);
         R := K[X_1 .. X_#degs, Degrees => degs,
              Repair => S.Repair, Adjust => S.Adjust];
         phi := map(R,S,join(gens R,(numgens S - numgens R):0));
         prune (phi ** H)
         );
Ext(Module,Ring) := (M,k) -> (
         B := ring M;
         if ideal k != ideal vars B
         then error "expected the residue field of the module";
         changeRing Ext(M,coker vars B)
         );
use B;
k = B/(x,y,z);
use B;
P = Ext(M,k);
time oddPart P
     -- used 0.09 seconds
```

### Output

```
i82 : oddPart P

o82 = cokernel {-1, -2} | X_3 0   X_2 0   0   0   0   X_1 |
               {-3, -9} | 0   0   0   0   0   0   X_1 0   |
               {-3, -9} | 0   0   0   0   0   X_1 0   0   |
               {-3, -9} | 0   0   0   0   X_1 0   0   0   |
               {-1, -3} | 0   X_2 0   X_1 0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |

                             11
o82 : R-module, quotient of R

i83 : changeRing = H -> (
         S := ring H;
         K := coefficientRing S;
         degs := select(degrees source vars S,
              d -> 0 != first d);
         R := K[X_1 .. X_#degs, Degrees => degs,
              Repair => S.Repair, Adjust => S.Adjust];
         phi := map(R,S,join(gens R,(numgens S - numgens R):0));
         prune (phi ** H)
         );

i84 : Ext(Module,Ring) := (M,k) -> (
         B := ring M;
         if ideal k != ideal vars B
         then error "expected the residue field of the module";
         changeRing Ext(M,coker vars B)
         );

i85 : use B;

i86 : k = B/(x,y,z);

i87 : use B;

i88 : P = Ext(M,k);

i89 : time oddPart P
     -- used 0.09 seconds

o89 = cokernel {-1, -2} | X_3 0   X_2 0   0   0   0   X_1 |
               {-3, -9} | 0   0   0   0   0   0   X_1 0   |
               {-3, -9} | 0   0   0   0   0   X_1 0   0   |
               {-3, -9} | 0   0   0   0   X_1 0   0   0   |
               {-1, -3} | 0   X_2 0   X_1 0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |

                                                                                                                                             11
o89 : K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]-module, quotient of K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]
          1   2   3                                                                     1   2   3
```

---

## completeIntersections / chapter.m2 — chunk 11

### Input

```macaulay2
Ext(Ring,Module) := (k,M) -> (
         B := ring M;
         if ideal k != ideal vars B
         then error "expected the residue field of the module";
         changeRing Ext(coker vars B,M)
         );
time I = Ext(k,M);
     -- used 14.81 seconds
evenPart I
oddPart I
T = ZZ[t,u,Inverses=>true,MonomialOrder=>RevLex];
poincareSeries2 = M -> (
         B := ring M;
         k := B/ideal vars B;
         P := Ext(M,k);
         h := hilbertSeries P;
         T':= degreesRing P;
         substitute(h, {T'_0=>t^-1,T'_1=>u^-1})
         );
poincareSeries1 = M -> (
         substitute(poincareSeries2 M, {u=>1_T})
         );
A' = K[x,y,z];
```

### Output

```
i90 : Ext(Ring,Module) := (k,M) -> (
         B := ring M;
         if ideal k != ideal vars B
         then error "expected the residue field of the module";
         changeRing Ext(coker vars B,M)
         );

i91 : time I = Ext(k,M);
     -- used 14.81 seconds

i92 : evenPart I

o92 = cokernel {0, 6} | 37X_2  37X_1  |
               {0, 6} | -18X_2 -18X_1 |
               {0, 6} | -13X_2 -13X_1 |
               {0, 6} | -37X_2 -37X_1 |
               {0, 6} | 22X_2  22X_1  |
               {0, 6} | 0      0      |
               {0, 6} | X_2    X_1    |

                                                                                                                                             7
o92 : K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]-module, quotient of K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]
          1   2   3                                                                     1   2   3

i93 : oddPart I

o93 = cokernel {-1, 5} | -48X_3 13X_3  34X_3  3X_3   0     0      0      5X_1  -20X_1 X_1 |
               {-1, 5} | 3X_3   -40X_3 8X_3   8X_3   0     0      0      33X_1 X_1    0   |
               {-1, 5} | -X_3   37X_3  -13X_3 -35X_3 0     0      0      X_1   0      0   |
               {-1, 4} | 4X_2   20X_2  3X_2   -47X_2 4X_1  20X_1  3X_1   0     0      0   |
               {-1, 4} | 0      51X_2  0      -30X_2 0     51X_1  0      0     0      0   |
               {-1, 4} | 0      12X_2  0      -3X_2  0     12X_1  0      0     0      0   |
               {-1, 4} | 42X_2  12X_2  46X_2  25X_2  42X_1 12X_1  46X_1  0     0      0   |
               {-1, 4} | 45X_2  24X_2  -14X_2 -35X_2 45X_1 24X_1  -14X_1 0     0      0   |
               {-1, 4} | 0      0      X_2    0      0     0      X_1    0     0      0   |
               {-1, 4} | X_2    0      0      0      X_1   0      0      0     0      0   |
               {-1, 4} | 0      -40X_2 0      10X_2  0     -40X_1 0      0     0      0   |
               {-1, 4} | 0      X_2    0      0      0     X_1    0      0     0      0   |
               {-1, 3} | 0      0      0      X_1    0     0      0      0     0      0   |

                                                                                                                                             13
o93 : K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]-module, quotient of K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]
          1   2   3                                                                     1   2   3

i94 : T = ZZ[t,u,Inverses=>true,MonomialOrder=>RevLex];

i95 : poincareSeries2 = M -> (
         B := ring M;
         k := B/ideal vars B;
         P := Ext(M,k);
         h := hilbertSeries P;
         T':= degreesRing P;
         substitute(h, {T'_0=>t^-1,T'_1=>u^-1})
         );

i96 : poincareSeries1 = M -> (
         substitute(poincareSeries2 M, {u=>1_T})
         );

i97 : A' = K[x,y,z];
```

---

## completeIntersections / chapter.m2 — chunk 12

### Input

```macaulay2
B' = A'/(x^2,y^2,z^3);
C' = res(B'^1/(x,y,z), LengthLimit => 6)
M' = coker transpose C'.dd_5
poincareSeries2 M'
p = poincareSeries1 M
load "simplify.m2"
simplify p
T' = QQ[t,Inverses=>true,MonomialOrder=>RevLex];
```

### Output

```
i98 : B' = A'/(x^2,y^2,z^3);

i99 : C' = res(B'^1/(x,y,z), LengthLimit => 6)

1       3       6       10       15       21       28
o99 = B'  <-- B'  <-- B'  <-- B'   <-- B'   <-- B'   <-- B'
                                                          
      0       1       2       3        4        5        6

o99 : ChainComplex

i100 : M' = coker transpose C'.dd_5

o100 = cokernel {-5} | -y 0   0  0  z  0 0 0  0 0  0  0 0  0 0 |
                {-5} | -x -y  0  0  0  z 0 0  0 0  0  0 0  0 0 |
                {-5} | 0  x   -y 0  0  0 z 0  0 0  0  0 0  0 0 |
                {-5} | 0  0   x  -y 0  0 0 z  0 0  0  0 0  0 0 |
                {-5} | 0  0   0  -x 0  0 0 0  z 0  0  0 0  0 0 |
                {-5} | 0  0   0  0  y  0 0 0  0 0  0  0 0  0 0 |
                {-5} | 0  0   0  0  -x y 0 0  0 0  0  0 0  0 0 |
                {-5} | 0  0   0  0  0  x y 0  0 0  0  0 0  0 0 |
                {-5} | 0  0   0  0  0  0 x y  0 0  0  0 0  0 0 |
                {-5} | 0  0   0  0  0  0 0 -x y 0  0  0 0  0 0 |
                {-5} | 0  0   0  0  0  0 0 0  x 0  0  0 0  0 0 |
                {-6} | 0  0   0  0  0  0 0 0  0 -y 0  z 0  0 0 |
                {-6} | 0  0   0  0  0  0 0 0  0 x  -y 0 z  0 0 |
                {-6} | 0  0   0  0  0  0 0 0  0 0  -x 0 0  z 0 |
                {-6} | z2 0   0  0  0  0 0 0  0 0  0  y 0  0 0 |
                {-6} | 0  -z2 0  0  0  0 0 0  0 0  0  x y  0 0 |
                {-6} | 0  0   z2 0  0  0 0 0  0 0  0  0 -x y 0 |
                {-6} | 0  0   0  z2 0  0 0 0  0 0  0  0 0  x 0 |
                {-7} | 0  0   0  0  0  0 0 0  0 0  0  0 0  0 z |
                {-7} | 0  0   0  0  0  0 0 0  0 z2 0  0 0  0 y |
                {-7} | 0  0   0  0  0  0 0 0  0 0  z2 0 0  0 x |

                                21
o100 : B'-module, quotient of B'

i101 : poincareSeries2 M'

-7     -6      -5      -6       -5       -4     2 -5      2 -4      2 -3      2 -2     3 -4      3 -3      3 -2     3 -1     4 -3     4 -2      4 -1      4    5 -2     5 -1     5      5     6 4     7 5    8 4     8 6     9 5    9 7     10 6    11 7
       3u   + 7u   + 11u   + t*u   + 5t*u   + 9t*u   - 6t u   - 14t u   - 22t u   - 11t u   - 2t u   - 10t u   - 18t u   - 9t u   + 3t u   + 7t u   + 11t u   + 15t  + t u   + 5t u   + 9t  + 13t u + t u  + 3t u  - t u  + 3t u  - 3t u  + t u  - 3t  u  - t  u
o101 = ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                2 2 2      2 3
                                                                                                                          (1 - t u ) (1 - t u )

o101 : Divide

i102 : p = poincareSeries1 M

2     3      4    5     6    7
       3 + 2t - 5t  + 4t  + 12t  + t  - 4t  - t
o102 = -----------------------------------------
                      2       2       2
                (1 - t )(1 - t )(1 - t )

o102 : Divide

i103 : load "simplify.m2"

i104 : simplify p

2     3     4     5    6
       3 - t - 4t  + 8t  + 4t  - 3t  - t
o104 = ----------------------------------
                       2       3
                (1 + t) (1 - t)

o104 : Divide

i105 : T' = QQ[t,Inverses=>true,MonomialOrder=>RevLex];
```

---

## completeIntersections / chapter.m2 — chunk 13

### Input

```macaulay2
expansion = (n,q) -> (
           t := T'_0;
           rho := map(T',T,{t,1});
           num := rho value numerator q;
           den := rho value denominator q;
           n = n + first degree den;
           n = max(n, first degree num + 1);
           (num + t^n) // den
           );
expansion(20,p)
psi = map(K,B)
apply(10, i -> rank (psi ** Ext^i(M,coker vars B)))
use T;
complexity = M -> dim Ext(M,coker vars ring M);
complexity M
k = coker vars ring H;
```

### Output

```
i106 : expansion = (n,q) -> (
           t := T'_0;
           rho := map(T',T,{t,1});
           num := rho value numerator q;
           den := rho value denominator q;
           n = n + first degree den;
           n = max(n, first degree num + 1);
           (num + t^n) // den
           );

i107 : expansion(20,p)

2      3      4      5      6      7      8      9      10       11       12       13       14       15       16       17       18       19       20
o107 = 3 + 2t + 4t  + 10t  + 15t  + 25t  + 32t  + 46t  + 55t  + 73t  + 84t   + 106t   + 119t   + 145t   + 160t   + 190t   + 207t   + 241t   + 260t   + 298t   + 319t

o107 : T'

i108 : psi = map(K,B)

o108 = map(K,B,{0, 0, 0})

o108 : RingMap K <--- B

i109 : apply(10, i -> rank (psi ** Ext^i(M,coker vars B)))

o109 = {3, 2, 4, 10, 15, 25, 32, 46, 55, 73}

o109 : List

i110 : use T;

i111 : complexity = M -> dim Ext(M,coker vars ring M);

i112 : complexity M

o112 = 3

i113 : k = coker vars ring H;
```

---

## completeIntersections / chapter.m2 — chunk 14

### Input

```macaulay2
prune Hom(k,H)
criticalDegree = M -> (
          B := ring M;
          k := B / ideal vars B;
          P := Ext(M,k);
          k  = coker vars ring P;
          - min ( first \ degrees source gens prune Hom(k,P))
          );
criticalDegree M
criticalDegree M'
supportVarietyIdeal = M -> (
          B := ring M;
          k := B/ideal vars B;
          ann Ext(M,k)
          );
K'' = ZZ/7;
A'' = K''[x,y,z];
J'' = ideal(x^7,y^7,z^7);
```

### Output

```
i114 : prune Hom(k,H)

o114 = 0

o114 : K [$X , $X , x, y, Degrees => {{-2, -2}, {-2, -3}, {0, 1}, {0, 1}}]-module
            1    2

i115 : criticalDegree = M -> (
          B := ring M;
          k := B / ideal vars B;
          P := Ext(M,k);
          k  = coker vars ring P;
          - min ( first \ degrees source gens prune Hom(k,P))
          );

i116 : criticalDegree M

o116 = 1

i117 : criticalDegree M'

o117 = 5

i118 : supportVarietyIdeal = M -> (
          B := ring M;
          k := B/ideal vars B;
          ann Ext(M,k)
          );

i119 : K'' = ZZ/7;

i120 : A'' = K''[x,y,z];

i121 : J'' = ideal(x^7,y^7,z^7);

o121 : Ideal of A''
```

---

## completeIntersections / chapter.m2 — chunk 15

### Input

```macaulay2
B'' = A''/J'';
scan((1,1) .. (3,3), (r,d) -> (
               V := cokernel random (B''^r,B''^{-d});
               << "------------------------------------------------------------------"
               << endl
               << "V = " << V << endl
               << "support variety ideal = "
               << timing supportVarietyIdeal V
               << endl))
------------------------------------------------------------------
V = cokernel | -2x+3y+2z |
support variety ideal = ideal (X  - 2X , X  + X )
                                2     3   1    3
                        -- 0.7 seconds
------------------------------------------------------------------
V = cokernel | 3x2-2xy+xz-3yz |
support variety ideal = ideal(X  + 3X  + 2X )
                               1     2     3
                        -- 0.48 seconds
------------------------------------------------------------------
V = cokernel | -2x3+3x2y+y3-x2z-3y2z-xz2-3z3 |
support variety ideal = 0
                        -- 1.54 seconds
------------------------------------------------------------------
V = cokernel | -3y+3z |
             | -2x-2y |
support variety ideal = ideal(X  + X  - X )
                               1    2    3
                        -- 0.86 seconds
------------------------------------------------------------------
V = cokernel | -x2+2y2-xz+yz+3z2 |
             | 2xy-3xz-3yz-2z2   |
support variety ideal = 0
                        -- 1.31 seconds
------------------------------------------------------------------
V = cokernel | -x3-2x2y-xy2-2xyz+3y2z+2xz2-yz2-2z3 |
             | 2xy2+3y3-3x2z-2y2z+2xz2+2yz2        |
support variety ideal = 0
                        -- 2.21 seconds
------------------------------------------------------------------
V = cokernel | 3x-y-z   |
             | -3x-y+2z |
             | x-2y+3z  |
support variety ideal = 0
                        -- 1.1 seconds
------------------------------------------------------------------
V = cokernel | 2x2-2xy+2y2+2xz-3z2   |
             | -x2+2xy+y2+3xz+3yz-z2 |
             | -2xz+2yz+2z2          |
support variety ideal = 0
                        -- 1.67 seconds
------------------------------------------------------------------
V = cokernel | 2x3-x2y+2xy2-y3-2xyz+3y2z+xz2+3yz2+z3  |
             | -3x3-3x2y+3xy2+2x2z+3xyz-3y2z-xz2      |
             | -3x3-2x2y-xy2-2y3-2xyz+y2z+xz2+3yz2-z3 |
support variety ideal = 0
                        -- 1.92 seconds
bassSeries2 = M -> (
          B := ring M;
          k := B/ideal vars B;
          I := Ext(k,M);
          h := hilbertSeries I;
          T':= degreesRing I;
          substitute(h, {T'_0=>t^-1, T'_1=>u})
          );
bassSeries1 = M -> (
          substitute(bassSeries2 M, {u=>1_T})
          );
use B;
L = B^1/(x,y,z);
p = poincareSeries2 L
b = bassSeries2 L
```

### Output

```
i122 : B'' = A''/J'';

i123 : scan((1,1) .. (3,3), (r,d) -> (
               V := cokernel random (B''^r,B''^{-d});
               << "------------------------------------------------------------------"
               << endl
               << "V = " << V << endl
               << "support variety ideal = "
               << timing supportVarietyIdeal V
               << endl))
------------------------------------------------------------------
V = cokernel | -2x+3y+2z |
support variety ideal = ideal (X  - 2X , X  + X )
                                2     3   1    3
                        -- 0.7 seconds
------------------------------------------------------------------
V = cokernel | 3x2-2xy+xz-3yz |
support variety ideal = ideal(X  + 3X  + 2X )
                               1     2     3
                        -- 0.48 seconds
------------------------------------------------------------------
V = cokernel | -2x3+3x2y+y3-x2z-3y2z-xz2-3z3 |
support variety ideal = 0
                        -- 1.54 seconds
------------------------------------------------------------------
V = cokernel | -3y+3z |
             | -2x-2y |
support variety ideal = ideal(X  + X  - X )
                               1    2    3
                        -- 0.86 seconds
------------------------------------------------------------------
V = cokernel | -x2+2y2-xz+yz+3z2 |
             | 2xy-3xz-3yz-2z2   |
support variety ideal = 0
                        -- 1.31 seconds
------------------------------------------------------------------
V = cokernel | -x3-2x2y-xy2-2xyz+3y2z+2xz2-yz2-2z3 |
             | 2xy2+3y3-3x2z-2y2z+2xz2+2yz2        |
support variety ideal = 0
                        -- 2.21 seconds
------------------------------------------------------------------
V = cokernel | 3x-y-z   |
             | -3x-y+2z |
             | x-2y+3z  |
support variety ideal = 0
                        -- 1.1 seconds
------------------------------------------------------------------
V = cokernel | 2x2-2xy+2y2+2xz-3z2   |
             | -x2+2xy+y2+3xz+3yz-z2 |
             | -2xz+2yz+2z2          |
support variety ideal = 0
                        -- 1.67 seconds
------------------------------------------------------------------
V = cokernel | 2x3-x2y+2xy2-y3-2xyz+3y2z+xz2+3yz2+z3  |
             | -3x3-3x2y+3xy2+2x2z+3xyz-3y2z-xz2      |
             | -3x3-2x2y-xy2-2y3-2xyz+y2z+xz2+3yz2-z3 |
support variety ideal = 0
                        -- 1.92 seconds

i124 : bassSeries2 = M -> (
          B := ring M;
          k := B/ideal vars B;
          I := Ext(k,M);
          h := hilbertSeries I;
          T':= degreesRing I;
          substitute(h, {T'_0=>t^-1, T'_1=>u})
          );

i125 : bassSeries1 = M -> (
          substitute(bassSeries2 M, {u=>1_T})
          );

i126 : use B;

i127 : L = B^1/(x,y,z);

i128 : p = poincareSeries2 L

2 2    3 3
           1 + 3t*u + 3t u  + t u
o128 = ------------------------------
             2 3       2 4       2 5
       (1 - t u )(1 - t u )(1 - t u )

o128 : Divide

i129 : b = bassSeries2 L

-1     2 -2    3 -3
          1 + 3t*u   + 3t u   + t u
o129 = ---------------------------------
             2 -3       2 -4       2 -5
       (1 - t u  )(1 - t u  )(1 - t u  )

o129 : Divide
```

---

## completeIntersections / chapter.m2 — chunk 16

### Input

```macaulay2
b2 = bassSeries2 M
b1 = bassSeries1 M;
simplify b1
ext = (M,N) -> changeRing Ext(M,N);
use B;
N = B^1/(x^2 + z^2,y^3);
time rH = ext(M,N);
     -- used 15.91 seconds
evenPart rH
```

### Output

```
i130 : b2 = bassSeries2 M

6      3       4       5    2 2    2 3     3     3      3 2    4 -1     5 -3
       7u  + t*u  + 9t*u  + 3t*u  - t u  - t u  - 4t  - 3t u - 3t u  + t u   + 3t u
o130 = ------------------------------------------------------------------------------
                                    2 -3       2 -4       2 -5
                              (1 - t u  )(1 - t u  )(1 - t u  )

o130 : Divide

i131 : b1 = bassSeries1 M;

i132 : simplify b1

2     3     4
       7 + 6t - 8t  - 2t  + 3t
o132 = ------------------------
                  2       3
           (1 + t) (1 - t)

o132 : Divide

i133 : ext = (M,N) -> changeRing Ext(M,N);

i134 : use B;

i135 : N = B^1/(x^2 + z^2,y^3);

i136 : time rH = ext(M,N);
     -- used 15.91 seconds

i137 : evenPart rH

o137 = cokernel {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0      0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_1 |
                {0, 2}   | 0   0   0   0   0   0   0   X_3 0   0   0   0   0   0   0   0   X_2 0      0      0   0   0   0   0   0   0   0   X_1 0   0   0   0   0   0   0   0   |
                {0, 2}   | 0   0   0   0   0   X_3 0   0   0   0   0   0   0   0   0   X_2 0   0      0      0   0   0   0   0   0   0   X_1 0   0   0   0   0   0   0   0   0   |
                {0, 2}   | 0   0   0   0   0   0   X_3 0   0   0   0   0   0   0   X_2 0   0   0      0      0   0   0   0   0   0   X_1 0   0   0   0   0   0   0   0   0   0   |
                {0, 2}   | 0   0   0   0   X_3 0   0   0   0   0   0   0   0   X_2 0   0   0   0      0      0   0   0   0   0   X_1 0   0   0   0   0   0   0   0   0   0   0   |
                {0, 2}   | 0   0   0   X_3 0   0   0   0   0   0   0   0   X_2 0   0   0   0   0      0      0   0   0   0   X_1 0   0   0   0   0   0   0   0   0   0   0   0   |
                {0, 2}   | 0   0   X_3 0   0   0   0   0   0   0   0   X_2 0   0   0   0   0   0      0      0   0   0   X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   |
                {0, 2}   | 0   X_3 0   0   0   0   0   0   0   0   X_2 0   0   0   0   0   0   0      0      0   0   X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   |
                {0, 2}   | X_3 0   0   0   0   0   0   0   0   X_2 0   0   0   0   0   0   0   0      0      0   X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   -4X_2  -22X_2 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_1 0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   -50X_2 8X_2   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_1 0   0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   46X_2  9X_2   0   0   0   0   0   0   0   0   0   0   0   0   0   X_1 0   0   0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   16X_2  -14X_2 0   0   0   0   0   0   0   0   0   0   0   0   X_1 0   0   0   0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   7X_2   -48X_2 0   0   0   0   0   0   0   0   0   0   0   X_1 0   0   0   0   0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      X_2    0   0   0   0   0   0   0   0   0   0   X_1 0   0   0   0   0   0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_2    0      0   0   0   0   0   0   0   0   0   X_1 0   0   0   0   0   0   0   |
                {0, 1}   | 0   0   0   0   0   0   0   0   X_2 0   0   0   0   0   0   0   0   0      0      X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   |

                                                                                                                                              17
o137 : K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]-module, quotient of K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]
           1   2   3                                                                     1   2   3
```

---

## completeIntersections / chapter.m2 — chunk 17

### Input

```macaulay2
oddPart rH
N' = B^1/(x^2 + z^2,y^3 - 2*z^3);
time rH' = ext(M,N');
     -- used 20.26 seconds
evenPart rH'
oddPart rH'
extgenSeries2 = (M,N) -> (
          H := ext(M,N);
          h := hilbertSeries H;
          T':= degreesRing H;
          substitute(h, {T'_0=>t^-1,T'_1=>u^-1})
          );
extgenSeries1 = (M,N) -> (
          substitute(extgenSeries2(M,N), {u=>1_T})
          );
time extgenSeries2(M,N)
     -- used 0.44 seconds
```

### Output

```
i138 : oddPart rH

o138 = cokernel {-3, -6} | 0      0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   -45X_1 4X_1   -31X_1 -13X_1 X_1 |
                {-3, -6} | 0      0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   -41X_1 7X_1   -43X_1 X_1    0   |
                {-3, -6} | 0      0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   10X_1  -32X_1 X_1    0      0   |
                {-3, -6} | 0      0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   4X_1   X_1    0      0      0   |
                {-3, -6} | 0      0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_1    0      0      0      0   |
                {-1, -1} | -39X_3 0   0   0   0   0   0   0   X_2 0   0   0   0   0   0   0   0   X_1 0      0      0      0      0   |
                {-1, -1} | 31X_3  0   0   0   0   0   0   X_2 0   0   0   0   0   0   0   0   X_1 0   0      0      0      0      0   |
                {-1, -1} | -34X_3 0   0   0   0   0   X_2 0   0   0   0   0   0   0   0   X_1 0   0   0      0      0      0      0   |
                {-1, -1} | -35X_3 0   0   0   0   X_2 0   0   0   0   0   0   0   0   X_1 0   0   0   0      0      0      0      0   |
                {-1, -1} | -29X_3 0   0   0   X_2 0   0   0   0   0   0   0   0   X_1 0   0   0   0   0      0      0      0      0   |
                {-1, -1} | 12X_3  0   0   X_2 0   0   0   0   0   0   0   0   X_1 0   0   0   0   0   0      0      0      0      0   |
                {-1, -1} | -8X_3  0   X_2 0   0   0   0   0   0   0   0   X_1 0   0   0   0   0   0   0      0      0      0      0   |
                {-1, -1} | X_3    X_2 0   0   0   0   0   0   0   0   X_1 0   0   0   0   0   0   0   0      0      0      0      0   |
                {-3, -7} | 0      0   0   0   0   0   0   0   0   X_1 0   0   0   0   0   0   0   0   0      0      0      0      0   |

                                                                                                                                              14
o138 : K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]-module, quotient of K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]
           1   2   3                                                                     1   2   3

i139 : N' = B^1/(x^2 + z^2,y^3 - 2*z^3);

i140 : time rH' = ext(M,N');
     -- used 20.26 seconds

i141 : evenPart rH'

o141 = cokernel {-4, -8} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     0      0      0      0      0      0      0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     0         48X_2             -48X_2            47X_2            -45X_2            -17X_2         |
                {-4, -8} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     0      0      0      0      0      0      0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     0         -5X_2             44X_2             -23X_2           0                 0              |
                {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     0      0      0      0      0      0      0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     -51X_1    42X_1             11X_1             19X_1            -X_1              30X_1          |
                {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     0      0      0      0      0      0      0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     -32X_1    -11X_1            -49X_1            -49X_1           45X_1             44X_1          |
                {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     0      0      0      0      0      0      0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     35X_1     48X_1             -13X_1            25X_1            -33X_1            -35X_1         |
                {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     0      0      0      0      0      0      0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     -51X_1    -3X_1             -8X_1             -16X_1           17X_1             -24X_1         |
                {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     0      0      0      0      0      0      0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     -46X_1    34X_1             -27X_1            11X_1            -5X_1             -41X_1         |
                {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     0      0      0      0      0      0      0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     -24X_1    -17X_1            16X_1             -7X_1            24X_1             -5X_1          |
                {0, 2}   | 0   0   0   0   0   0   X_3 0   0   0   0   0   0     0   0   0   X_2 0      0      0      0     0      0      0      0      0      0      0   0   0   0   0   0   0   0   X_1 0      0      0     0      0      0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {0, 2}   | 0   0   0   0   0   X_3 0   0   0   0   0   0   0     0   0   X_2 0   0      0      0      0     0      0      0      0      0      0      0   0   0   0   0   0   0   X_1 0   0      0      0     0      0      0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   4X_2  0   0   0   0   -14X_2 -4X_2  12X_2  47X_2 18X_2  -45X_2 31X_2  37X_2  3X_2   45X_2  0   0   0   0   0   0   0   0   0   49X_1  -43X_1 26X_1 -40X_1 X_1    32X_1  0     -49X_1 21X_1  -13X_1 -44X_1 30X_1 19X_1X_3  -14X_2^2+2X_1X_3  -29X_2^2-7X_1X_3  -2X_2^2-32X_1X_3 -23X_2^2+12X_1X_3 X_2^2+13X_1X_3 |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   41X_2 0   0   0   0   8X_2   -44X_2 9X_2   12X_2 48X_2  -7X_2  0      -22X_2 -50X_2 11X_2  0   0   0   0   0   0   0   0   0   -8X_1  35X_1  -8X_1 29X_1  -2X_1  3X_1   47X_1 7X_1   0      -28X_1 -34X_1 36X_1 39X_1X_3  -33X_2^2+20X_1X_3 -47X_2^2-21X_1X_3 -6X_2^2+41X_1X_3 X_2^2+2X_1X_3     33X_1X_3       |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   14X_2 0   0   0   0   -42X_2 17X_2  40X_2  40X_2 23X_2  42X_2  -44X_2 39X_2  -41X_2 5X_2   0   0   0   0   0   0   0   0   0   -18X_1 45X_1  30X_1 -10X_1 -28X_1 -19X_1 10X_1 -10X_1 -16X_1 7X_1   -37X_1 13X_1 -27X_1X_3 10X_2^2+35X_1X_3  -40X_2^2+17X_1X_3 X_2^2+29X_1X_3   -33X_1X_3         -48X_1X_3      |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   24X_2 0   0   0   0   19X_2  -16X_2 49X_2  51X_2 -49X_2 31X_2  -33X_2 -48X_2 18X_2  -46X_2 0   0   0   0   0   0   0   0   0   13X_1  -38X_1 11X_1 -39X_1 -11X_1 46X_1  20X_1 -2X_1  20X_1  -17X_1 49X_1  27X_1 X_1X_3    32X_2^2           X_2^2             0                0                 0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   50X_2 0   0   0   0   25X_2  -X_2   -12X_2 29X_2 27X_2  50X_2  37X_2  28X_2  28X_2  27X_2  0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      X_1   0         X_2^2             0                 0                0                 0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     0      0      0      0      0      X_2    0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      X_1    0     0         0                 0                 0                0                 0              |
                {0, 2}   | 0   0   0   0   X_3 0   0   0   0   0   0   0   0     0   X_2 0   0   0      0      0      0     0      0      0      0      0      0      0   0   0   0   0   0   X_1 0   0   0      0      0     0      0      0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {0, 2}   | 0   0   X_3 0   0   0   0   0   0   0   X_2 0   0     0   0   0   0   0      0      0      0     0      0      0      0      0      0      0   0   0   X_1 0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     0      0      0      0      X_2    0      0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      X_1    0      0     0         0                 0                 0                0                 0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     0      0      0      X_2    0      0      0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      X_1    0      0      0     0         0                 0                 0                0                 0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     0      0      X_2    0      0      0      0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     X_1    0      0      0      0     0         0                 0                 0                0                 0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     0      X_2    0      0      0      0      0   0   0   0   0   0   0   0   0   0      0      0     0      0      0      X_1   0      0      0      0      0     0         0                 0                 0                0                 0              |
                {0, 2}   | 0   0   0   X_3 0   0   0   0   0   0   0   0   0     X_2 0   0   0   0      0      0      0     0      0      0      0      0      0      0   0   0   0   0   X_1 0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {0, 2}   | 0   X_3 0   0   0   0   0   0   0   X_2 0   0   0     0   0   0   0   0      0      0      0     0      0      0      0      0      0      0   0   X_1 0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      0     X_2    0      0      0      0      0      0   0   0   0   0   0   0   0   0   0      0      0     0      0      X_1    0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      0      X_2   0      0      0      0      0      0      0   0   0   0   0   0   0   0   0   0      0      0     0      X_1    0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      0      X_2    0     0      0      0      0      0      0      0   0   0   0   0   0   0   0   0   0      0      0     X_1    0      0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   0      X_2    0      0     0      0      0      0      0      0      0   0   0   0   0   0   0   0   0   0      0      X_1   0      0      0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0     0   0   0   0   X_2    0      0      0     0      0      0      0      0      0      0   0   0   0   0   0   0   0   0   0      X_1    0     0      0      0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   X_2   0   0   0   0   0      0      0      0     0      0      0      0      0      0      0   0   0   0   0   0   0   0   0   X_1    0      0     0      0      0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {0, 2}   | X_3 0   0   0   0   0   0   0   0   0   0   X_2 0     0   0   0   0   0      0      0      0     0      0      0      0      0      0      0   0   0   0   X_1 0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {0, 1}   | 0   0   0   0   0   0   0   X_2 0   0   0   0   0     0   0   0   0   0      0      0      0     0      0      0      0      0      0      X_1 0   0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |
                {0, 1}   | 0   0   0   0   0   0   0   0   X_2 0   0   0   0     0   0   0   0   0      0      0      0     0      0      0      0      0      0      0   X_1 0   0   0   0   0   0   0   0      0      0     0      0      0      0     0      0      0      0      0     0         0                 0                 0                0                 0              |

                                                                                                                                              33
o141 : K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]-module, quotient of K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]
           1   2   3                                                                     1   2   3

i142 : oddPart rH'

o142 = cokernel {-3, -6} | 0   0   0   0   0   0   0   0   -42X_2 21X_2  -47X_2 -13X_2 32X_2  49X_2  |
                {-3, -6} | 0   0   0   0   0   0   0   0   -6X_2  -32X_2 -38X_2 -27X_2 -11X_2 -47X_2 |
                {-3, -6} | 0   0   0   0   0   0   0   0   -8X_2  12X_2  -12X_2 -34X_2 -12X_2 -5X_2  |
                {-3, -6} | 0   0   0   0   0   0   0   0   26X_2  -36X_2 36X_2  21X_2  47X_2  29X_2  |
                {-3, -6} | 0   0   0   0   0   0   0   0   50X_2  18X_2  -37X_2 23X_2  -12X_2 42X_2  |
                {-3, -6} | 0   0   0   0   0   0   0   0   31X_2  7X_2   -49X_2 -34X_2 -46X_2 11X_2  |
                {-3, -7} | 0   0   0   0   0   0   0   0   0      0      0      0      0      X_1    |
                {-3, -7} | 0   0   0   0   0   0   0   0   0      0      0      0      X_1    0      |
                {-3, -7} | 0   0   0   0   0   0   0   0   0      0      0      X_1    0      0      |
                {-3, -7} | 0   0   0   0   0   0   0   0   0      0      X_1    0      0      0      |
                {-3, -7} | 0   0   0   0   0   0   0   0   0      X_1    0      0      0      0      |
                {-3, -7} | 0   0   0   0   0   0   0   0   X_1    0      0      0      0      0      |
                {-1, -2} | 0   0   0   X_2 0   0   0   X_1 0      0      0      0      0      0      |
                {-1, -2} | 0   0   X_2 0   0   0   X_1 0   0      0      0      0      0      0      |
                {-1, -2} | 0   X_2 0   0   0   X_1 0   0   0      0      0      0      0      0      |
                {-1, -2} | X_2 0   0   0   X_1 0   0   0   0      0      0      0      0      0      |

                                                                                                                                              16
o142 : K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]-module, quotient of K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]
           1   2   3                                                                     1   2   3

i143 : extgenSeries2 = (M,N) -> (
          H := ext(M,N);
          h := hilbertSeries H;
          T':= degreesRing H;
          substitute(h, {T'_0=>t^-1,T'_1=>u^-1})
          );

i144 : extgenSeries1 = (M,N) -> (
          substitute(extgenSeries2(M,N), {u=>1_T})
          );

i145 : time extgenSeries2(M,N)
     -- used 0.44 seconds

-2    -1            2      2 2     2 3     2 4     3 4     3 5     3 6    3 7     4 5     4 6    4 7     4 8    4 9     5 8     5 9     6 10     6 11    6 12    7 13
       8u   + u   + 8t*u - 8t u - 9t u  - 9t u  + 7t u  - 8t u  - 8t u  + 4t u  + t u  + 8t u  + 9t u  + t u  - 2t u  + t u  + 8t u  - 4t u  - 8t u   + 2t u   - t u   - t u
o145 = -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                  2 3       2 4       2 5
                                                                            (1 - t u )(1 - t u )(1 - t u )

o145 : Divide
```

---

## completeIntersections / chapter.m2 — chunk 18

### Input

```macaulay2
g=time extgenSeries1(M,N)
     -- used 0.13 seconds
simplify g
time extgenSeries2(M,N')
     -- used 0.15 seconds
g'=time extgenSeries1(M,N')
     -- used 0.18 seconds
simplify g'
complexityPair = (M,N) -> dim ext(M,N);
time complexityPair(M,N)
     -- used 0.39 seconds
time complexityPair(M,N')
     -- used 0.12 seconds
```

### Output

```
i146 : g=time extgenSeries1(M,N)
     -- used 0.13 seconds

2      3      4     5     6    7
       9 + 8t - 19t  - 11t  + 17t  + 4t  - 7t  - t
o146 = --------------------------------------------
                       2       2       2
                 (1 - t )(1 - t )(1 - t )

o146 : Divide

i147 : simplify g

2     3    4
       9 - t - 9t  + 6t  + t
o147 = ----------------------
                         2
           (1 + t)(1 - t)

o147 : Divide

i148 : time extgenSeries2(M,N')
     -- used 0.15 seconds

-2     -1       2     2      2 2     2 3      2 4     3 5     3 6     3 7     4 5     4 6     4 7     4 8     4 9     5 9     5 10     6 10      6 11     6 12
       7u   + 2u   + 4t*u  - 7t u - 9t u  - 9t u  + 16t u  - 4t u  + 2t u  + 6t u  + 7t u  + 9t u  - 5t u  - 9t u  + 6t u  + 4t u  - 6t u   - 7t u   + 11t u   - 6t u
o148 = ----------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                              2 3       2 4       2 5
                                                                        (1 - t u )(1 - t u )(1 - t u )

o148 : Divide

i149 : g'=time extgenSeries1(M,N')
     -- used 0.18 seconds

2     3     4     5     6
       9 + 4t - 9t  + 4t  + 8t  - 2t  - 2t
o149 = ------------------------------------
                   2       2       2
             (1 - t )(1 - t )(1 - t )

o149 : Divide

i150 : simplify g'

2     3     5
       9 - 5t - 4t  + 8t  - 2t
o150 = ------------------------
                  2       3
           (1 + t) (1 - t)

o150 : Divide

i151 : complexityPair = (M,N) -> dim ext(M,N);

i152 : time complexityPair(M,N)
     -- used 0.39 seconds

o152 = 2

i153 : time complexityPair(M,N')
     -- used 0.12 seconds

o153 = 3
```

---

## completeIntersections / chapter.m2 — chunk 19

### Input

```macaulay2
supportVarietyPairIdeal = (M,N) -> ann ext(M,N);
time supportVarietyPairIdeal(M,N)
     -- used 0.97 seconds
time supportVarietyPairIdeal(M,N')
     -- used 1.73 seconds
i157 :
```

### Output

```
i154 : supportVarietyPairIdeal = (M,N) -> ann ext(M,N);

i155 : time supportVarietyPairIdeal(M,N)
     -- used 0.97 seconds

o155 = ideal X
              1

o155 : Ideal of K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]
                    1   2   3

i156 : time supportVarietyPairIdeal(M,N')
     -- used 1.73 seconds

o156 = 0

o156 : Ideal of K [X , X , X , Degrees => {{-2, -3}, {-2, -4}, {-2, -5}}]
                    1   2   3

i157 :
```

---

## completeIntersections / test.m2 — chunk 0

### Input

```macaulay2
setRandomSeed();
 -- initializing random seed
A = QQ[w,x,y,z]
U = matrix {{w,x},{y,z}}
C = chainComplex U
L = HH_0 C
f = -det U
f * L == 0
s = nullhomotopy (-f * id_C)
```

### Output

```
i1 : setRandomSeed();
 -- initializing random seed

i2 : A = QQ[w,x,y,z]

o2 = A

o2 : PolynomialRing

i3 : U = matrix {{w,x},{y,z}}

o3 = | w x |
     | y z |

             2      2
o3 : Matrix A  <-- A

i4 : C = chainComplex U

2      2
o4 = A  <-- A
             
     0      1

o4 : ChainComplex

i5 : L = HH_0 C

o5 = cokernel | w x |
              | y z |

                            2
o5 : A-module, quotient of A

i6 : f = -det U

o6 = x*y - w*z

o6 : A

i7 : f * L == 0

o7 = true

i8 : s = nullhomotopy (-f * id_C)

2                     2
o8 = 1 : A  <----------------- A  : 0
               {1} | z  -x |
               {1} | -y w  |

o8 : ChainComplexMap
```

---

## completeIntersections / test.m2 — chunk 1

### Input

```macaulay2
s * C.dd + C.dd * s == -f
V = s_0
A = QQ[x,y,z];
f = x^3 + 3*y^3 - 2*y*z^2 + 5*z^3;
B = A/f;
m = ideal(x,y,z)
M = B^1/m^2;
F = resolution(M, LengthLimit=>8)
```

### Output

```
i9 : s * C.dd + C.dd * s == -f

o9 = true

i10 : V = s_0

o10 = {1} | z  -x |
      {1} | -y w  |

              2      2
o10 : Matrix A  <-- A

i11 : A = QQ[x,y,z];

i12 : f = x^3 + 3*y^3 - 2*y*z^2 + 5*z^3;

i13 : B = A/f;

i14 : m = ideal(x,y,z)

o14 = ideal (x, y, z)

o14 : Ideal of B

i15 : M = B^1/m^2;

i16 : F = resolution(M, LengthLimit=>8)

1      6      9      9      9      9      9      9      9
o16 = B  <-- B  <-- B  <-- B  <-- B  <-- B  <-- B  <-- B  <-- B
                                                               
      0      1      2      3      4      5      6      7      8

o16 : ChainComplex
```

---

## completeIntersections / test.m2 — chunk 2

### Input

```macaulay2
restrict1 = N -> coker(lift(presentation N,A) | f);
L = restrict1 cokernel F.dd_4;
C = res L;
U = C.dd_1;
print U
{4} | x2 0  -2yz+5z2 0     y2-5/2yz yz-5/2z2 -5/2yz   0        0      |
{4} | 0  x2 -3y2     xy    yz-5/2z2 0        yz-5/2z2 0        0      |
{4} | 0  xy x2       y2    0        0        0        yz-5/2z2 0      |
{5} | y  0  0        0     0        0        1/3x     0        -2y+5z |
{5} | -z y  x        0     0        -1/2x    0        0        0      |
{5} | 0  0  0        -1/3x 0        1/2y     -1/3z    0        0      |
{5} | 0  -z 0        0     -1/2x    0        -1/2x    0        3y     |
{5} | 0  0  -z       0     1/2y     0        1/2y     -1/2x    0      |
{5} | 0  0  0        1/3z  0        0        0        1/2y     x      |
s = nullhomotopy (-f * id_C);
V = s_0;
print V
{6} | -x  0  0   -3y2 -2yz+5z2 0         -2y2+5yz 0         0         |
{6} | 0   -x 0   -3yz -3y2     -3xy      -2yz+5z2 0         0         |
{6} | 0   y  -x  0    0        0         0        -2yz+5z2  0         |
{6} | 0   0  -3y 3xz  3xy      3x2       0        0         6yz-15z2  |
{6} | -3y 2z 0   3x2  0        6yz-15z2  2x2      -15yz     -15xz     |
{6} | 2z  0  -2x 0    2x2      -6y2      0        -4yz+10z2 0         |
{6} | 3y  0  0   -3x2 0        -6yz+15z2 0        -6y2+15yz -6xy+15xz |
{6} | 0   0  2z  0    0        0         2xy      2x2       -6y2      |
{6} | 0   0  0   -z2  -yz      -xz       -y2      -xy       -x2       |
```

### Output

```
i17 : restrict1 = N -> coker(lift(presentation N,A) | f);

i18 : L = restrict1 cokernel F.dd_4;

i19 : C = res L;

i20 : U = C.dd_1;

9      9
o20 : Matrix A  <-- A

i21 : print U
{4} | x2 0  -2yz+5z2 0     y2-5/2yz yz-5/2z2 -5/2yz   0        0      |
{4} | 0  x2 -3y2     xy    yz-5/2z2 0        yz-5/2z2 0        0      |
{4} | 0  xy x2       y2    0        0        0        yz-5/2z2 0      |
{5} | y  0  0        0     0        0        1/3x     0        -2y+5z |
{5} | -z y  x        0     0        -1/2x    0        0        0      |
{5} | 0  0  0        -1/3x 0        1/2y     -1/3z    0        0      |
{5} | 0  -z 0        0     -1/2x    0        -1/2x    0        3y     |
{5} | 0  0  -z       0     1/2y     0        1/2y     -1/2x    0      |
{5} | 0  0  0        1/3z  0        0        0        1/2y     x      |

i22 : s = nullhomotopy (-f * id_C);

i23 : V = s_0;

9      9
o23 : Matrix A  <-- A

i24 : print V
{6} | -x  0  0   -3y2 -2yz+5z2 0         -2y2+5yz 0         0         |
{6} | 0   -x 0   -3yz -3y2     -3xy      -2yz+5z2 0         0         |
{6} | 0   y  -x  0    0        0         0        -2yz+5z2  0         |
{6} | 0   0  -3y 3xz  3xy      3x2       0        0         6yz-15z2  |
{6} | -3y 2z 0   3x2  0        6yz-15z2  2x2      -15yz     -15xz     |
{6} | 2z  0  -2x 0    2x2      -6y2      0        -4yz+10z2 0         |
{6} | 3y  0  0   -3x2 0        -6yz+15z2 0        -6y2+15yz -6xy+15xz |
{6} | 0   0  2z  0    0        0         2xy      2x2       -6y2      |
{6} | 0   0  0   -z2  -yz      -xz       -y2      -xy       -x2       |
```

---

## completeIntersections / test.m2 — chunk 3

### Input

```macaulay2
U*V+f==0
V*U+f==0
matrixFactorization = M -> (
         B := ring M;
         f := (ideal B)_0;
         e := numgens B;
         F := resolution(M, LengthLimit => e+1);
         L := restrict1 cokernel F.dd_(e+1);
         C := res L;
         U := C.dd_1;
         s := nullhomotopy (-f * id_C);
         V := s_0;
         assert( U*V + f == 0 );
         assert( V*U + f == 0 );
         return (U,V));
time (U,V) = matrixFactorization(B^1/m^3);
     -- used 0.039071 seconds
U;
V;
F.dd_3 - F.dd_5 == 0
F.dd_4 - F.dd_6 == 0
```

### Output

```
i25 : U*V+f==0

o25 = true

i26 : V*U+f==0

o26 = true

i27 : matrixFactorization = M -> (
         B := ring M;
         f := (ideal B)_0;
         e := numgens B;
         F := resolution(M, LengthLimit => e+1);
         L := restrict1 cokernel F.dd_(e+1);
         C := res L;
         U := C.dd_1;
         s := nullhomotopy (-f * id_C);
         V := s_0;
         assert( U*V + f == 0 );
         assert( V*U + f == 0 );
         return (U,V));

i28 : time (U,V) = matrixFactorization(B^1/m^3);
     -- used 0.039071 seconds

i29 : U;

15      15
o29 : Matrix A   <-- A

i30 : V;

15      15
o30 : Matrix A   <-- A

i31 : F.dd_3 - F.dd_5 == 0

o31 = false

i32 : F.dd_4 - F.dd_6 == 0

o32 = false
```

---

## completeIntersections / test.m2 — chunk 4

### Input

```macaulay2
F.dd_5 - F.dd_7 == 0
M = B^1/m^2;
G = resolution(M, LengthLimit => 8, Strategy => 0)
G.dd_3 - G.dd_5 == 0
G.dd_4 - G.dd_6 == 0
G.dd_5 - G.dd_7 == 0
M = B^1/m^3;
F = resolution(M, LengthLimit=>8)
```

### Output

```
i33 : F.dd_5 - F.dd_7 == 0

o33 = false

i34 : M = B^1/m^2;

i35 : G = resolution(M, LengthLimit => 8, Strategy => 0)

1      6      9      9      9      9      9      9      9
o35 = B  <-- B  <-- B  <-- B  <-- B  <-- B  <-- B  <-- B  <-- B
                                                               
      0      1      2      3      4      5      6      7      8

o35 : ChainComplex

i36 : G.dd_3 - G.dd_5 == 0

o36 = true

i37 : G.dd_4 - G.dd_6 == 0

o37 = true

i38 : G.dd_5 - G.dd_7 == 0

o38 = true

i39 : M = B^1/m^3;

i40 : F = resolution(M, LengthLimit=>8)

1      10      16      15      15      15      15      15      15
o40 = B  <-- B   <-- B   <-- B   <-- B   <-- B   <-- B   <-- B   <-- B
                                                                      
      0      1       2       3       4       5       6       7       8

o40 : ChainComplex
```

---

## completeIntersections / test.m2 — chunk 5

### Input

```macaulay2
M' = restrict1 M;
C = res M'
K = ZZ/103;
A = K[x,Degrees=>{5}];
B = A/(x^3);
M = B^1/(x^2);
N = B^1/(x);
H = Ext(M,N);
```

### Output

```
i41 : M' = restrict1 M;

i42 : C = res M'

1      10      15      6
o42 = A  <-- A   <-- A   <-- A  <-- 0
                                     
      0      1       2       3      4

o42 : ChainComplex

i43 : K = ZZ/103;

i44 : A = K[x,Degrees=>{5}];

i45 : B = A/(x^3);

i46 : M = B^1/(x^2);

i47 : N = B^1/(x);

i48 : H = Ext(M,N);
```

---

## completeIntersections / test.m2 — chunk 6

### Input

```macaulay2
ring H
degree \ gens ring H
S = ring H;
H
A = K[x,y];
J = ideal(x^3,y^2);
B = A/J;
N = cokernel matrix{{x^2,x*y}}
```

### Output

```
i49 : ring H

o49 = K[X , x]
         1

o49 : PolynomialRing

i50 : degree \ gens ring H

o50 = {{-2, -15}, {0, 5}}

o50 : List

i51 : S = ring H;

i52 : H

o52 = cokernel {0, 0}    | 0 x |
               {-1, -10} | x 0 |

                             2
o52 : S-module, quotient of S

i53 : A = K[x,y];

i54 : J = ideal(x^3,y^2);

o54 : Ideal of A

i55 : B = A/J;

i56 : N = cokernel matrix{{x^2,x*y}}

o56 = cokernel | x2 xy |

                             1
o56 : B-module, quotient of B
```

---

## completeIntersections / test.m2 — chunk 7

### Input

```macaulay2
time H = Ext(N,N);
     -- used 0.007732 seconds
ring H
S = ring H;
transpose vars S
trim J
H
partSelector = predicate -> H -> (
         R := ring H;
         H' := prune image matrix {
             select(
                 apply(numgens H, i -> H_{i}),
                 f -> predicate first first degrees source f
                 )
             };
         H');
evenPart = partSelector even; oddPart = partSelector odd;
```

### Output

```
i57 : time H = Ext(N,N);
     -- used 0.007732 seconds

i58 : ring H

o58 = K[X ..X , x..y]
         1   2

o58 : PolynomialRing

i59 : S = ring H;

i60 : transpose vars S

o60 = {2, 2}  | X_1 |
      {2, 3}  | X_2 |
      {0, -1} | x   |
      {0, -1} | y   |

              4      1
o60 : Matrix S  <-- S

i61 : trim J

2   3
o61 = ideal (y , x )

o61 : Ideal of A

i62 : H

o62 = cokernel {0, 0}   | y2 xy x2 0 0 0 0 0 0 0 0 X_1y X_1x 0   0   0 0 |
               {-1, -1} | 0  0  0  y x 0 0 0 0 0 0 0    0    X_1 0   0 0 |
               {-1, -1} | 0  0  0  0 0 y x 0 0 0 0 0    0    0   X_1 0 0 |
               {-1, -1} | 0  0  0  0 0 0 0 y x 0 0 0    0    0   X_1 0 0 |
               {-1, -1} | 0  0  0  0 0 0 0 0 0 y x 0    0    0   0   0 0 |
               {-2, -2} | 0  0  0  0 0 0 0 0 0 0 0 0    0    0   0   y x |

                             6
o62 : S-module, quotient of S

i63 : partSelector = predicate -> H -> (
         R := ring H;
         H' := prune image matrix {
             select(
                 apply(numgens H, i -> H_{i}),
                 f -> predicate first first degrees source f
                 )
             };
         H');

i64 : evenPart = partSelector even; oddPart = partSelector odd;
```

---

## completeIntersections / test.m2 — chunk 8

### Input

```macaulay2
evenPart H
oddPart H
print code(Ext,Module,Module)
-- code for method: Ext(Module,Module)
/Users/mike/src/M2/M2/Macaulay2/m2/ext.m2:89:39-179:3: --source code:
Ext(Module,Module) := Module => (M,N) -> (
  cacheModule := M; -- we have no way to tell whether N is younger than M, sigh
  cacheKey := (Ext,M,N);
  if cacheModule.cache#?cacheKey then return cacheModule.cache#cacheKey;
  B := ring M;
  if B =!= ring N
  then error "expected modules over the same ring";
  if not isCommutative B
  then error "'Ext' not implemented yet for noncommutative rings.";
  if not isHomogeneous B
  then error "'Ext' received modules over an inhomogeneous ring";
  if not isHomogeneous N or not isHomogeneous M
  then error "'Ext' received an inhomogeneous module";
  if N == 0 or M == 0 then return cacheModule.cache#cacheKey = B^0;
  p := presentation B;
  A := ring p;
  I := ideal mingens ideal p;
  n := numgens A;
  c := numgens I;
  if c =!= codim B 
  then error "total Ext available only for complete intersections";
  f := apply(c, i -> I_i);
  pM := lift(presentation M,A);
  pN := lift(presentation N,A);
  M' := cokernel ( pM | p ** id_(target pM) );
  N' := cokernel ( pN | p ** id_(target pN) );
  assert isHomogeneous M';
  assert isHomogeneous N';
  C := complete resolution M';
  X := getSymbol "X";
  K := coefficientRing A;
  S := K(monoid [X_1 .. X_c, toSequence A.generatorSymbols,
    Degrees => {
      apply(0 .. c-1, i -> prepend(-2, - degree f_i)),
      apply(0 .. n-1, j -> prepend( 0,   degree A_j))
      }]);
  -- make a monoid whose monomials can be used as indices
  Rmon := monoid [X_1 .. X_c,Degrees=>{c:{2}}];
  -- make group ring, so 'basis' can enumerate the monomials
  R := K Rmon;
  -- make a hash table to store the blocks of the matrix
  blks := new MutableHashTable;
  blks#(exponents 1_Rmon) = C.dd;
  scan(0 .. c-1, i -> 
       blks#(exponents Rmon_i) = nullhomotopy (- f_i*id_C));
  -- a helper function to list the factorizations of a monomial
  factorizations := (gamma) -> (
    -- Input: gamma is the list of exponents for a monomial
    -- Return a list of pairs of lists of exponents showing the
    -- possible factorizations of gamma.
    if gamma === {} then { ({}, {}) }
    else (
      i := gamma#-1;
      splice apply(factorizations drop(gamma,-1), 
        (alpha,beta) -> apply (0..i, 
             j -> (append(alpha,j), append(beta,i-j))))));
  scan(4 .. length C + 1, 
    d -> if even d then (
      scan( flatten \ exponents \ leadMonomial \ first entries basis(d,R), 
        gamma -> (
          s := - sum(factorizations gamma,
            (alpha,beta) -> (
              if blks#?alpha and blks#?beta
              then blks#alpha * blks#beta
              else 0));
          -- compute and save the nonzero nullhomotopies
          if s != 0 then blks#gamma = nullhomotopy s;
          ))));
  -- make a free module whose basis elements have the right degrees
  spots := C -> sort select(keys C, i -> class i === ZZ);
  Cstar := S^(apply(spots C,
      i -> toSequence apply(degrees C_i, d -> prepend(i,d))));
  -- assemble the matrix from its blocks.
  -- We omit the sign (-1)^(n+1) which would ordinarily be used,
  -- which does not affect the homology.
  toS := map(S,A,apply(toList(c .. c+n-1), i -> S_i),
    DegreeMap => prepend_0);
  Delta := map(Cstar, Cstar, 
    transpose sum(keys blks, m -> S_m * toS sum blks#m),
    Degree => { -1, degreeLength A:0 });
  DeltaBar := Delta ** (toS ** N');
  if debugLevel > 10 then (
       assert isHomogeneous DeltaBar;
       assert(DeltaBar * DeltaBar == 0);
       stderr << describe ring DeltaBar <<endl;
       stderr << toExternalString DeltaBar << endl;
       );
  -- now compute the total Ext as a single homology module
  tot := minimalPresentation homology(DeltaBar,DeltaBar);
  cacheModule.cache#cacheKey = tot;
  tot)
A = K[x,y,z];
J = trim ideal(x^3,y^4,z^5)
B = A/J;
f = random (B^3, B^{-2,-3})
f_{1}
```

### Output

```
i66 : evenPart H

o66 = cokernel {0, 0}   | y2 xy x2 X_1y X_1x 0 0 |
               {-2, -2} | 0  0  0  0    0    y x |

                             2
o66 : S-module, quotient of S

i67 : oddPart H

o67 = cokernel {-1, -1} | y x 0 0 0 0 0 0 X_1 0   |
               {-1, -1} | 0 0 y x 0 0 0 0 0   X_1 |
               {-1, -1} | 0 0 0 0 y x 0 0 0   X_1 |
               {-1, -1} | 0 0 0 0 0 0 y x 0   0   |

                             4
o67 : S-module, quotient of S

i68 : print code(Ext,Module,Module)
-- code for method: Ext(Module,Module)
/Users/mike/src/M2/M2/Macaulay2/m2/ext.m2:89:39-179:3: --source code:
Ext(Module,Module) := Module => (M,N) -> (
  cacheModule := M; -- we have no way to tell whether N is younger than M, sigh
  cacheKey := (Ext,M,N);
  if cacheModule.cache#?cacheKey then return cacheModule.cache#cacheKey;
  B := ring M;
  if B =!= ring N
  then error "expected modules over the same ring";
  if not isCommutative B
  then error "'Ext' not implemented yet for noncommutative rings.";
  if not isHomogeneous B
  then error "'Ext' received modules over an inhomogeneous ring";
  if not isHomogeneous N or not isHomogeneous M
  then error "'Ext' received an inhomogeneous module";
  if N == 0 or M == 0 then return cacheModule.cache#cacheKey = B^0;
  p := presentation B;
  A := ring p;
  I := ideal mingens ideal p;
  n := numgens A;
  c := numgens I;
  if c =!= codim B 
  then error "total Ext available only for complete intersections";
  f := apply(c, i -> I_i);
  pM := lift(presentation M,A);
  pN := lift(presentation N,A);
  M' := cokernel ( pM | p ** id_(target pM) );
  N' := cokernel ( pN | p ** id_(target pN) );
  assert isHomogeneous M';
  assert isHomogeneous N';
  C := complete resolution M';
  X := getSymbol "X";
  K := coefficientRing A;
  S := K(monoid [X_1 .. X_c, toSequence A.generatorSymbols,
    Degrees => {
      apply(0 .. c-1, i -> prepend(-2, - degree f_i)),
      apply(0 .. n-1, j -> prepend( 0,   degree A_j))
      }]);
  -- make a monoid whose monomials can be used as indices
  Rmon := monoid [X_1 .. X_c,Degrees=>{c:{2}}];
  -- make group ring, so 'basis' can enumerate the monomials
  R := K Rmon;
  -- make a hash table to store the blocks of the matrix
  blks := new MutableHashTable;
  blks#(exponents 1_Rmon) = C.dd;
  scan(0 .. c-1, i -> 
       blks#(exponents Rmon_i) = nullhomotopy (- f_i*id_C));
  -- a helper function to list the factorizations of a monomial
  factorizations := (gamma) -> (
    -- Input: gamma is the list of exponents for a monomial
    -- Return a list of pairs of lists of exponents showing the
    -- possible factorizations of gamma.
    if gamma === {} then { ({}, {}) }
    else (
      i := gamma#-1;
      splice apply(factorizations drop(gamma,-1), 
        (alpha,beta) -> apply (0..i, 
             j -> (append(alpha,j), append(beta,i-j))))));
  scan(4 .. length C + 1, 
    d -> if even d then (
      scan( flatten \ exponents \ leadMonomial \ first entries basis(d,R), 
        gamma -> (
          s := - sum(factorizations gamma,
            (alpha,beta) -> (
              if blks#?alpha and blks#?beta
              then blks#alpha * blks#beta
              else 0));
          -- compute and save the nonzero nullhomotopies
          if s != 0 then blks#gamma = nullhomotopy s;
          ))));
  -- make a free module whose basis elements have the right degrees
  spots := C -> sort select(keys C, i -> class i === ZZ);
  Cstar := S^(apply(spots C,
      i -> toSequence apply(degrees C_i, d -> prepend(i,d))));
  -- assemble the matrix from its blocks.
  -- We omit the sign (-1)^(n+1) which would ordinarily be used,
  -- which does not affect the homology.
  toS := map(S,A,apply(toList(c .. c+n-1), i -> S_i),
    DegreeMap => prepend_0);
  Delta := map(Cstar, Cstar, 
    transpose sum(keys blks, m -> S_m * toS sum blks#m),
    Degree => { -1, degreeLength A:0 });
  DeltaBar := Delta ** (toS ** N');
  if debugLevel > 10 then (
       assert isHomogeneous DeltaBar;
       assert(DeltaBar * DeltaBar == 0);
       stderr << describe ring DeltaBar <<endl;
       stderr << toExternalString DeltaBar << endl;
       );
  -- now compute the total Ext as a single homology module
  tot := minimalPresentation homology(DeltaBar,DeltaBar);
  cacheModule.cache#cacheKey = tot;
  tot)

i69 : A = K[x,y,z];

i70 : J = trim ideal(x^3,y^4,z^5)

3   4   5
o70 = ideal (x , y , z )

o70 : Ideal of A

i71 : B = A/J;

i72 : f = random (B^3, B^{-2,-3})

o72 = | -28x2-31xy-24y2-4xz-49yz-19z2  -44x2y-4xy2-49y3+30x2z-51xyz+51y2z+23xz2-19yz2+42z3 |
      | 47x2-6xy-49y2+9xz+47yz-25z2    16x2y-9xy2-31y3+34x2z-2xyz-16y2z-23xz2+14yz2+50z3   |
      | -36x2-44xy-18y2+11xz-18yz+21z2 -36x2y+28xy2-21y3-x2z-8xyz+6y2z+37xz2+27yz2+43z3    |

              3      2
o72 : Matrix B  <-- B

i73 : f_{1}

o73 = | -44x2y-4xy2-49y3+30x2z-51xyz+51y2z+23xz2-19yz2+42z3 |
      | 16x2y-9xy2-31y3+34x2z-2xyz-16y2z-23xz2+14yz2+50z3   |
      | -36x2y+28xy2-21y3-x2z-8xyz+6y2z+37xz2+27yz2+43z3    |

              3      1
o73 : Matrix B  <-- B
```

---

## completeIntersections / test.m2 — chunk 9

### Input

```macaulay2
M = cokernel f;
time P = Ext(M,B^1/(x,y,z));
     -- used 0.332459 seconds
S = ring P;
transpose vars S
R = K[X_1..X_3,Degrees => {{-2,-3},{-2,-4},{-2,-5}}];
phi = map(R,S,{X_1,X_2,X_3,0,0,0})
P = prune (phi ** P);
transpose vars ring P
```

### Output

```
i74 : M = cokernel f;

i75 : time P = Ext(M,B^1/(x,y,z));
     -- used 0.332459 seconds

i76 : S = ring P;

i77 : transpose vars S

o77 = {2, 3}  | X_1 |
      {2, 4}  | X_2 |
      {2, 5}  | X_3 |
      {0, -1} | x   |
      {0, -1} | y   |
      {0, -1} | z   |

              6      1
o77 : Matrix S  <-- S

i78 : R = K[X_1..X_3,Degrees => {{-2,-3},{-2,-4},{-2,-5}}];

i79 : phi = map(R,S,{X_1,X_2,X_3,0,0,0})

o79 = map (R, S, {X , X , X , 0, 0, 0})
                   1   2   3

o79 : RingMap R <-- S

i80 : P = prune (phi ** P);

i81 : transpose vars ring P

o81 = {2, 3} | X_1 |
      {2, 4} | X_2 |
      {2, 5} | X_3 |

              3      1
o81 : Matrix R  <-- R
```

---

## completeIntersections / test.m2 — chunk 10

### Input

```macaulay2
evenPart P
oddPart P
changeRing = H -> (
         S := ring H;
         K := coefficientRing S;
         degs := select(degrees source vars S,
              d -> 0 != first d);
         R := K[X_1 .. X_#degs, Degrees => degs];
         phi := map(R,S,join(gens R,(numgens S - numgens R):0));
         prune (phi ** H)
         );
Ext(Module,Ring) := o -> (M,k) -> (
         B := ring M;
         if ideal k != ideal vars B
         then error "expected the residue field of the module";
         changeRing Ext(M,coker vars B)
         );
use B;
k = B/(x,y,z);
use B;
P = Ext(M,k);
```

### Output

```
i82 : evenPart P

o82 = cokernel {-2, -7}  | 0   0   0   0   0   0   0   0   0   0    |
               {-2, -7}  | 0   0   0   0   0   0   0   0   0   0    |
               {-2, -7}  | 0   0   0   0   0   0   0   0   0   0    |
               {-2, -7}  | 0   0   0   0   0   0   0   0   0   0    |
               {0, 0}    | X_3 X_2 X_1 0   0   0   0   0   0   0    |
               {0, 0}    | 0   0   0   X_3 X_2 X_1 0   0   0   0    |
               {0, 0}    | 0   0   0   0   0   0   X_3 X_2 X_1 0    |
               {-4, -11} | 0   0   0   0   0   0   0   0   0   X_1  |
               {-4, -10} | 0   0   0   0   0   0   0   0   0   0    |
               {-4, -10} | 0   0   0   0   0   0   0   0   0   -X_2 |

                             10
o82 : R-module, quotient of R

i83 : oddPart P

o83 = cokernel {-1, -3} | X_2 X_1 0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   X_1 0   0   |
               {-3, -9} | 0   0   0   0   0   0   X_1 0   |
               {-3, -9} | 0   0   0   0   0   0   0   X_1 |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-1, -2} | 0   0   X_3 X_2 X_1 0   0   0   |

                             11
o83 : R-module, quotient of R

i84 : changeRing = H -> (
         S := ring H;
         K := coefficientRing S;
         degs := select(degrees source vars S,
              d -> 0 != first d);
         R := K[X_1 .. X_#degs, Degrees => degs];
         phi := map(R,S,join(gens R,(numgens S - numgens R):0));
         prune (phi ** H)
         );

i85 : Ext(Module,Ring) := o -> (M,k) -> (
         B := ring M;
         if ideal k != ideal vars B
         then error "expected the residue field of the module";
         changeRing Ext(M,coker vars B)
         );

i86 : use B;

i87 : k = B/(x,y,z);

i88 : use B;

i89 : P = Ext(M,k);
```

---

## completeIntersections / test.m2 — chunk 11

### Input

```macaulay2
time oddPart P
     -- used 0.001676 seconds
Ext(Ring,Module) := o -> (k,M) -> (
         B := ring M;
         if ideal k != ideal vars B
         then error "expected the residue field of the module";
         changeRing Ext(coker vars B,M)
         );
time I = Ext(k,M);
     -- used 0.807293 seconds
evenPart I
oddPart I
T = ZZ[t,u,Inverses=>true,MonomialOrder=>RevLex,Weights=>{-3,-1}];
poincareSeries2 = M -> (
         B := ring M;
         k := B/ideal vars B;
         P := Ext(M,k);
         h := hilbertSeries P;
         T':= degreesRing ring P;
         substitute(h, {T'_0=>t^-1,T'_1=>u^-1})
         );
poincareSeries1 = M -> (
         substitute(poincareSeries2 M, {u=>1_T})
         );
```

### Output

```
i90 : time oddPart P
     -- used 0.001676 seconds

o90 = cokernel {-1, -3} | X_2 X_1 0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   X_1 0   0   |
               {-3, -9} | 0   0   0   0   0   0   X_1 0   |
               {-3, -9} | 0   0   0   0   0   0   0   X_1 |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-3, -9} | 0   0   0   0   0   0   0   0   |
               {-1, -2} | 0   0   X_3 X_2 X_1 0   0   0   |

                                               11
o90 : K[X ..X ]-module, quotient of (K[X ..X ])
         1   3                          1   3

i91 : Ext(Ring,Module) := o -> (k,M) -> (
         B := ring M;
         if ideal k != ideal vars B
         then error "expected the residue field of the module";
         changeRing Ext(coker vars B,M)
         );

i92 : time I = Ext(k,M);
     -- used 0.807293 seconds

i93 : evenPart I

o93 = cokernel {0, 6} | 11X_2  11X_1  |
               {0, 6} | -16X_2 -16X_1 |
               {0, 6} | -44X_2 -44X_1 |
               {0, 6} | 32X_2  32X_1  |
               {0, 6} | -41X_2 -41X_1 |
               {0, 6} | 11X_2  11X_1  |
               {0, 6} | X_2    X_1    |

                                               7
o93 : K[X ..X ]-module, quotient of (K[X ..X ])
         1   3                          1   3

i94 : oddPart I

o94 = cokernel {-1, 3} | 0      0      0      0   0   X_1    0      0      0      0   |
               {-1, 4} | -41X_1 21X_1  -4X_1  0   0   X_2    21X_2  -4X_2  -41X_2 0   |
               {-1, 4} | -44X_1 22X_1  -9X_1  0   0   -40X_2 22X_2  -9X_2  -44X_2 0   |
               {-1, 4} | -14X_1 37X_1  4X_1   0   0   -18X_2 37X_2  4X_2   -14X_2 0   |
               {-1, 4} | 17X_1  -22X_1 49X_1  0   0   -45X_2 -22X_2 49X_2  17X_2  0   |
               {-1, 4} | -28X_1 -41X_1 -13X_1 0   0   16X_2  -41X_2 -13X_2 -28X_2 0   |
               {-1, 4} | 37X_1  45X_1  23X_1  0   0   17X_2  45X_2  23X_2  37X_2  0   |
               {-1, 4} | X_1    0      0      0   0   0      0      0      X_2    0   |
               {-1, 4} | 0      X_1    0      0   0   0      X_2    0      0      0   |
               {-1, 4} | 0      0      X_1    0   0   0      0      X_2    0      0   |
               {-1, 5} | 0      0      0      X_1 0   3X_3   4X_3   -16X_3 14X_3  0   |
               {-1, 5} | 0      0      0      0   X_1 -17X_3 18X_3  13X_3  -17X_3 0   |
               {-1, 5} | 0      0      0      0   0   -3X_3  -13X_3 -15X_3 -30X_3 X_1 |

                                               13
o94 : K[X ..X ]-module, quotient of (K[X ..X ])
         1   3                          1   3

i95 : T = ZZ[t,u,Inverses=>true,MonomialOrder=>RevLex,Weights=>{-3,-1}];

i96 : poincareSeries2 = M -> (
         B := ring M;
         k := B/ideal vars B;
         P := Ext(M,k);
         h := hilbertSeries P;
         T':= degreesRing ring P;
         substitute(h, {T'_0=>t^-1,T'_1=>u^-1})
         );

i97 : poincareSeries1 = M -> (
         substitute(poincareSeries2 M, {u=>1_T})
         );
```

---

## completeIntersections / test.m2 — chunk 12

### Input

```macaulay2
A' = K[x,y,z];
B' = A'/(x^2,y^2,z^3);
C' = res(B'^1/(x,y,z), LengthLimit => 6)
M' = coker transpose C'.dd_5
poincareSeries2 M'
p = poincareSeries1 M
load "simplify.m2"
simplify p
```

### Output

```
i98 : A' = K[x,y,z];

i99 : B' = A'/(x^2,y^2,z^3);

i100 : C' = res(B'^1/(x,y,z), LengthLimit => 6)

1       3       6       10       15       21       28
o100 = B'  <-- B'  <-- B'  <-- B'   <-- B'   <-- B'   <-- B'
                                                           
       0       1       2       3        4        5        6

o100 : ChainComplex

i101 : M' = coker transpose C'.dd_5

o101 = cokernel {-5} | -y 0   0  0  z  0 0 0  0 0  0  0 0  0 0 |
                {-5} | -x -y  0  0  0  z 0 0  0 0  0  0 0  0 0 |
                {-5} | 0  x   -y 0  0  0 z 0  0 0  0  0 0  0 0 |
                {-5} | 0  0   x  -y 0  0 0 z  0 0  0  0 0  0 0 |
                {-5} | 0  0   0  -x 0  0 0 0  z 0  0  0 0  0 0 |
                {-5} | 0  0   0  0  y  0 0 0  0 0  0  0 0  0 0 |
                {-5} | 0  0   0  0  -x y 0 0  0 0  0  0 0  0 0 |
                {-5} | 0  0   0  0  0  x y 0  0 0  0  0 0  0 0 |
                {-5} | 0  0   0  0  0  0 x y  0 0  0  0 0  0 0 |
                {-5} | 0  0   0  0  0  0 0 -x y 0  0  0 0  0 0 |
                {-5} | 0  0   0  0  0  0 0 0  x 0  0  0 0  0 0 |
                {-6} | 0  0   0  0  0  0 0 0  0 -y 0  z 0  0 0 |
                {-6} | 0  0   0  0  0  0 0 0  0 x  -y 0 z  0 0 |
                {-6} | 0  0   0  0  0  0 0 0  0 0  -x 0 0  z 0 |
                {-6} | z2 0   0  0  0  0 0 0  0 0  0  y 0  0 0 |
                {-6} | 0  -z2 0  0  0  0 0 0  0 0  0  x y  0 0 |
                {-6} | 0  0   z2 0  0  0 0 0  0 0  0  0 -x y 0 |
                {-6} | 0  0   0  z2 0  0 0 0  0 0  0  0 0  x 0 |
                {-7} | 0  0   0  0  0  0 0 0  0 z2 0  0 0  0 y |
                {-7} | 0  0   0  0  0  0 0 0  0 0  z2 0 0  0 x |
                {-7} | 0  0   0  0  0  0 0 0  0 0  0  0 0  0 z |

                                21
o101 : B'-module, quotient of B'

i102 : poincareSeries2 M'

-7     -6      -5      -6       -5       -4     2 -5      2 -4      2 -3      2 -2     3 -4      3 -3      3 -2     3 -1     4 -3     4 -2      4 -1      4    5 -2     5 -1     5      5     6 4     7 5    8 4     8 6     9 5    9 7     10 6    11 7
       3u   + 7u   + 11u   + t*u   + 5t*u   + 9t*u   - 6t u   - 14t u   - 22t u   - 11t u   - 2t u   - 10t u   - 18t u   - 9t u   + 3t u   + 7t u   + 11t u   + 15t  + t u   + 5t u   + 9t  + 13t u + t u  + 3t u  - t u  + 3t u  - 3t u  + t u  - 3t  u  - t  u
o102 = ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                2 3       2 2 2
                                                                                                                          (1 - t u )(1 - t u )

o102 : Expression of class Divide

i103 : p = poincareSeries1 M

2     3      4    5     6    7
       3 + 2t - 5t  + 4t  + 12t  + t  - 4t  - t
o103 = -----------------------------------------
                      2       2       2
                (1 - t )(1 - t )(1 - t )

o103 : Expression of class Divide

i104 : load "simplify.m2"

i105 : simplify p

2     3     4     5    6
       3 - t - 4t  + 8t  + 4t  - 3t  - t
o105 = ----------------------------------
                       2       3
                (1 + t) (1 - t)

o105 : Expression of class Divide
```

---

## completeIntersections / test.m2 — chunk 13

### Input

```macaulay2
T' = QQ[t,Inverses=>true,MonomialOrder=>RevLex,Weights=>{-1}];
expansion = (n,q) -> (
           t := T'_0;
           rho := map(T',T,{t,1});
           num := rho value numerator q;
           den := rho value denominator q;
           n = n + first degree den;
           n = max(n, first degree num + 1);
           (num + t^n) // den
           );
expansion(20,p)
psi = map(K,B)
apply(10, i -> rank (psi ** Ext^i(M,coker vars B)))
use T;
complexity = M -> dim Ext(M,coker vars ring M);
complexity M
```

### Output

```
i106 : T' = QQ[t,Inverses=>true,MonomialOrder=>RevLex,Weights=>{-1}];

i107 : expansion = (n,q) -> (
           t := T'_0;
           rho := map(T',T,{t,1});
           num := rho value numerator q;
           den := rho value denominator q;
           n = n + first degree den;
           n = max(n, first degree num + 1);
           (num + t^n) // den
           );

i108 : expansion(20,p)

2      3      4      5      6      7      8      9      10       11       12       13       14       15       16       17       18       19       20
o108 = 3 + 2t + 4t  + 10t  + 15t  + 25t  + 32t  + 46t  + 55t  + 73t  + 84t   + 106t   + 119t   + 145t   + 160t   + 190t   + 207t   + 241t   + 260t   + 298t   + 319t

o108 : T'

i109 : psi = map(K,B)

o109 = map (K, B, {0, 0, 0})

o109 : RingMap K <-- B

i110 : apply(10, i -> rank (psi ** Ext^i(M,coker vars B)))

o110 = {3, 2, 4, 10, 15, 25, 32, 46, 55, 73}

o110 : List

i111 : use T;

i112 : complexity = M -> dim Ext(M,coker vars ring M);

i113 : complexity M

o113 = 3
```

---

## completeIntersections / test.m2 — chunk 14

### Input

```macaulay2
k = coker vars ring H;
prune Hom(k,H)
criticalDegree = M -> (
          B := ring M;
          k := B / ideal vars B;
          P := Ext(M,k);
          k  = coker vars ring P;
          - min ( first \ degrees source gens prune Hom(k,P))
          );
criticalDegree M
criticalDegree M'
supportVarietyIdeal = M -> (
          B := ring M;
          k := B/ideal vars B;
          ann Ext(M,k)
          );
K'' = ZZ/7;
A'' = K''[x,y,z];
```

### Output

```
i114 : k = coker vars ring H;

i115 : prune Hom(k,H)

o115 = 0

o115 : K[X ..X , x..y]-module
          1   2

i116 : criticalDegree = M -> (
          B := ring M;
          k := B / ideal vars B;
          P := Ext(M,k);
          k  = coker vars ring P;
          - min ( first \ degrees source gens prune Hom(k,P))
          );

i117 : criticalDegree M

o117 = 1

i118 : criticalDegree M'

o118 = 5

i119 : supportVarietyIdeal = M -> (
          B := ring M;
          k := B/ideal vars B;
          ann Ext(M,k)
          );

i120 : K'' = ZZ/7;

i121 : A'' = K''[x,y,z];
```

---

## completeIntersections / test.m2 — chunk 15

### Input

```macaulay2
J'' = ideal(x^7,y^7,z^7);
B'' = A''/J'';
scan((1,1) .. (3,3), (r,d) -> (
               V := cokernel random (B''^r,B''^{-d});
               << "------------------------------------------------------------------"
               << endl
               << "V = " << V << endl
               << "support variety ideal = "
               << timing supportVarietyIdeal V
               << endl))
------------------------------------------------------------------
V = cokernel | 2x+z |
support variety ideal = ideal (X , X  + 3X )
                                2   1     3
                        -- .019386 seconds
------------------------------------------------------------------
V = cokernel | 3xy-y2+3xz-3yz+3z2 |
support variety ideal = ideal ()
                        -- .125895 seconds
------------------------------------------------------------------
V = cokernel | 3x2y-2xy2-3y3-x2z+3xyz-3y2z+3xz2 |
support variety ideal = ideal ()
                        -- .159221 seconds
------------------------------------------------------------------
V = cokernel | 3x-2y  |
             | x-3y+z |
support variety ideal = ideal(X  + 3X )
                               2     3
                        -- .026892 seconds
------------------------------------------------------------------
V = cokernel | -2xy+2xz-3yz+2z2       |
             | 3x2+2xy+3y2+xz-2yz+3z2 |
support variety ideal = ideal ()
                        -- .075065 seconds
------------------------------------------------------------------
V = cokernel | 3xyz-y2z+3xz2-2yz2+z3           |
             | 2xy2+2y3+2x2z-xyz+3xz2-3yz2+2z3 |
support variety ideal = ideal ()
                        -- .173907 seconds
------------------------------------------------------------------
V = cokernel | -3x+3y-2z |
             | -3x+2y    |
             | 2x-y-3z   |
support variety ideal = ideal(X  + 2X  - X )
                               1     2    3
                        -- .077985 seconds
------------------------------------------------------------------
V = cokernel | -xy+2y2+xz-3yz-3z2 |
             | -3xy+y2-xz         |
             | -xy+3y2-xz+yz+3z2  |
support variety ideal = ideal ()
                        -- .245207 seconds
------------------------------------------------------------------
V = cokernel | 3x2y-xy2-3y3-xyz-2xz2+2yz2                 |
             | x3+3x2y-xy2-2y3+3x2z+2xyz-y2z+3xz2+3yz2-z3 |
             | 3x3-3x2y-2xy2+y3-3x2z+2xyz-y2z+xz2+3yz2    |
support variety ideal = ideal ()
                        -- .216556 seconds
bassSeries2 = M -> (
          B := ring M;
          k := B/ideal vars B;
          I := Ext(k,M);
          h := hilbertSeries I;
          T':= degreesRing ring I;
          substitute(h, {T'_0=>t^-1, T'_1=>u})
          );
bassSeries1 = M -> (
          substitute(bassSeries2 M, {u=>1_T})
          );
use B;
L = B^1/(x,y,z);
p = poincareSeries2 L
```

### Output

```
i122 : J'' = ideal(x^7,y^7,z^7);

o122 : Ideal of A''

i123 : B'' = A''/J'';

i124 : scan((1,1) .. (3,3), (r,d) -> (
               V := cokernel random (B''^r,B''^{-d});
               << "------------------------------------------------------------------"
               << endl
               << "V = " << V << endl
               << "support variety ideal = "
               << timing supportVarietyIdeal V
               << endl))
------------------------------------------------------------------
V = cokernel | 2x+z |
support variety ideal = ideal (X , X  + 3X )
                                2   1     3
                        -- .019386 seconds
------------------------------------------------------------------
V = cokernel | 3xy-y2+3xz-3yz+3z2 |
support variety ideal = ideal ()
                        -- .125895 seconds
------------------------------------------------------------------
V = cokernel | 3x2y-2xy2-3y3-x2z+3xyz-3y2z+3xz2 |
support variety ideal = ideal ()
                        -- .159221 seconds
------------------------------------------------------------------
V = cokernel | 3x-2y  |
             | x-3y+z |
support variety ideal = ideal(X  + 3X )
                               2     3
                        -- .026892 seconds
------------------------------------------------------------------
V = cokernel | -2xy+2xz-3yz+2z2       |
             | 3x2+2xy+3y2+xz-2yz+3z2 |
support variety ideal = ideal ()
                        -- .075065 seconds
------------------------------------------------------------------
V = cokernel | 3xyz-y2z+3xz2-2yz2+z3           |
             | 2xy2+2y3+2x2z-xyz+3xz2-3yz2+2z3 |
support variety ideal = ideal ()
                        -- .173907 seconds
------------------------------------------------------------------
V = cokernel | -3x+3y-2z |
             | -3x+2y    |
             | 2x-y-3z   |
support variety ideal = ideal(X  + 2X  - X )
                               1     2    3
                        -- .077985 seconds
------------------------------------------------------------------
V = cokernel | -xy+2y2+xz-3yz-3z2 |
             | -3xy+y2-xz         |
             | -xy+3y2-xz+yz+3z2  |
support variety ideal = ideal ()
                        -- .245207 seconds
------------------------------------------------------------------
V = cokernel | 3x2y-xy2-3y3-xyz-2xz2+2yz2                 |
             | x3+3x2y-xy2-2y3+3x2z+2xyz-y2z+3xz2+3yz2-z3 |
             | 3x3-3x2y-2xy2+y3-3x2z+2xyz-y2z+xz2+3yz2    |
support variety ideal = ideal ()
                        -- .216556 seconds

i125 : bassSeries2 = M -> (
          B := ring M;
          k := B/ideal vars B;
          I := Ext(k,M);
          h := hilbertSeries I;
          T':= degreesRing ring I;
          substitute(h, {T'_0=>t^-1, T'_1=>u})
          );

i126 : bassSeries1 = M -> (
          substitute(bassSeries2 M, {u=>1_T})
          );

i127 : use B;

i128 : L = B^1/(x,y,z);

i129 : p = poincareSeries2 L

2 2    3 3
           1 + 3t*u + 3t u  + t u
o129 = ------------------------------
             2 5       2 4       2 3
       (1 - t u )(1 - t u )(1 - t u )

o129 : Expression of class Divide
```

---

## completeIntersections / test.m2 — chunk 16

### Input

```macaulay2
b = bassSeries2 L
b2 = bassSeries2 M
b1 = bassSeries1 M;
simplify b1
ext = (M,N) -> changeRing Ext(M,N);
use B;
N = B^1/(x^2 + z^2,y^3);
time rH = ext(M,N);
     -- used 1.22413 seconds
```

### Output

```
i130 : b = bassSeries2 L

-1     2 -2    3 -3
          1 + 3t*u   + 3t u   + t u
o130 = ---------------------------------
             2 -5       2 -4       2 -3
       (1 - t u  )(1 - t u  )(1 - t u  )

o130 : Expression of class Divide

i131 : b2 = bassSeries2 M

6      3       4       5    2 2    2 3     3     3      3 2    4 -1     5 -3
       7u  + t*u  + 9t*u  + 3t*u  - t u  - t u  - 4t  - 3t u - 3t u  + t u   + 3t u
o131 = ------------------------------------------------------------------------------
                                    2 -5       2 -4       2 -3
                              (1 - t u  )(1 - t u  )(1 - t u  )

o131 : Expression of class Divide

i132 : b1 = bassSeries1 M;

i133 : simplify b1

2     3     4
       7 + 6t - 8t  - 2t  + 3t
o133 = ------------------------
                  2       3
           (1 + t) (1 - t)

o133 : Expression of class Divide

i134 : ext = (M,N) -> changeRing Ext(M,N);

i135 : use B;

i136 : N = B^1/(x^2 + z^2,y^3);

i137 : time rH = ext(M,N);
     -- used 1.22413 seconds
```

---

## completeIntersections / test.m2 — chunk 17

### Input

```macaulay2
evenPart rH
oddPart rH
N' = B^1/(x^2 + z^2,y^3 - 2*z^3);
time rH' = ext(M,N');
     -- used 1.12031 seconds
evenPart rH'
oddPart rH'
extgenSeries2 = (M,N) -> (
          H := ext(M,N);
          h := hilbertSeries H;
          T':= degreesRing ring H;
          substitute(h, {T'_0=>t^-1,T'_1=>u^-1})
          );
extgenSeries1 = (M,N) -> (
          substitute(extgenSeries2(M,N), {u=>1_T})
          );
```

### Output

```
i138 : evenPart rH

o138 = cokernel {0, 1}   | X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   0     0   0   |
                {0, 2}   | 0   0   X_3 X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   0     0   0   |
                {0, 2}   | 0   0   0   0   0   X_3 X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   0     0   0   |
                {0, 2}   | 0   0   0   0   0   0   0   0   X_3 X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   0     0   0   |
                {0, 2}   | 0   0   0   0   0   0   0   0   0   0   0   X_3 X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   0     0   0   |
                {0, 2}   | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_3 X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   0     0   0   |
                {0, 2}   | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_3 X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0      0   0     0   0   |
                {0, 2}   | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_3 X_2 X_1 0   0   0   0   0   0   0   0   0      0   0     0   0   |
                {0, 2}   | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_3 X_2 X_1 0   0   0   0   0   0      0   0     0   0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_1 0   0   0   0   -46X_2 0   33X_2 0   0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_1 0   0   0   34X_2  0   8X_2  0   0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_1 0   0   26X_2  0   0     0   0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_1 0   -15X_2 0   -6X_2 0   0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_1 -47X_2 0   10X_2 0   0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_2    X_1 0     0   0   |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   X_2   X_1 0   |
                {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   0     0   X_1 |

                                                17
o138 : K[X ..X ]-module, quotient of (K[X ..X ])
          1   3                          1   3

i139 : oddPart rH

o139 = cokernel {-1, -1} | X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0   -18X_3 0   0   0   0   0   0   0   0   |
                {-1, -1} | 0   0   X_2 X_1 0   0   0   0   0   0   0   0   0   0   9X_3   0   0   0   0   0   0   0   0   |
                {-1, -1} | 0   0   0   0   X_2 X_1 0   0   0   0   0   0   0   0   24X_3  0   0   0   0   0   0   0   0   |
                {-1, -1} | 0   0   0   0   0   0   X_2 X_1 0   0   0   0   0   0   -31X_3 0   0   0   0   0   0   0   0   |
                {-1, -1} | 0   0   0   0   0   0   0   0   X_2 X_1 0   0   0   0   38X_3  0   0   0   0   0   0   0   0   |
                {-1, -1} | 0   0   0   0   0   0   0   0   0   0   X_2 X_1 0   0   47X_3  0   0   0   0   0   0   0   0   |
                {-1, -1} | 0   0   0   0   0   0   0   0   0   0   0   0   X_2 X_1 47X_3  0   0   0   0   0   0   0   0   |
                {-1, -1} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_3    X_2 X_1 0   0   0   0   0   0   |
                {-3, -7} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   0   X_1 0   0   0   0   0   |
                {-3, -6} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   0   0   X_1 0   0   0   0   |
                {-3, -6} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   0   0   0   X_1 0   0   0   |
                {-3, -6} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   0   0   0   0   X_1 0   0   |
                {-3, -6} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   0   0   0   0   0   X_1 0   |
                {-3, -6} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0   0   0   0   0   0   0   X_1 |

                                                14
o139 : K[X ..X ]-module, quotient of (K[X ..X ])
          1   3                          1   3

i140 : N' = B^1/(x^2 + z^2,y^3 - 2*z^3);

i141 : time rH' = ext(M,N');
     -- used 1.12031 seconds

i142 : evenPart rH'

o142 = cokernel {0, 1}   | X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {0, 1}   | 0   0   X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {0, 2}   | 0   0   0   0   X_3 X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {0, 2}   | 0   0   0   0   0   0   0   X_3 X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {0, 2}   | 0   0   0   0   0   0   0   0   0   0   X_3 X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {0, 2}   | 0   0   0   0   0   0   0   0   0   0   0   0   0   X_3 X_2 X_1 0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {0, 2}   | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_3 X_2 X_1 0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {0, 2}   | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_3 X_2 X_1 0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {0, 2}   | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_3 X_2 X_1 0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   44X_1  45X_2 -29X_1 24X_2  -34X_1 -34X_2 -43X_1 0   0   23X_2  -2X_1  -27X_2 -2X_1 7X_2   40X_1 -20X_2 19X_1  0   0   -18X_2 19X_1  -35X_1X_3 48X_1X_3  31X_1X_3       2X_1X_3   -50X_1X_3      X_2^2-44X_1X_3 |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_1    10X_2 13X_1  5X_2   -X_1   22X_2  -18X_1 0   0   24X_2  -7X_1  18X_2  49X_1 -43X_2 35X_1 0      36X_1  0   0   -16X_2 34X_1  X_1X_3    31X_1X_3  5X_1X_3        -3X_1X_3  X_2^2-28X_1X_3 -37X_1X_3      |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   14X_1  18X_2 -43X_1 21X_2  40X_1  -51X_2 7X_1   0   0   -29X_2 -51X_1 17X_2  39X_1 -32X_2 30X_1 17X_2  6X_1   0   0   3X_2   -18X_1 X_1X_3    -13X_1X_3 X_2^2+25X_1X_3 -51X_1X_3 -39X_1X_3      -8X_1X_3       |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   -24X_1 34X_2 -38X_1 -12X_2 29X_1  -33X_2 0      0   0   40X_2  -40X_1 21X_2  -2X_1 35X_2  17X_1 2X_2   -38X_1 0   0   -13X_2 23X_1  X_1X_3    X_2^2     0              0         0              0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_2 X_1 0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   X_1    -3X_2 0      6X_2   0      40X_2  0      0   0   31X_2  0      -31X_2 0     25X_2  0     -36X_2 0      0   0   -50X_2 0      0         0         0              X_2^2     0              0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      X_2   X_1    0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      X_2    X_1    0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      X_2    X_1    0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      X_2 X_1 0      0      0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   X_2    X_1    0      0     0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      X_2    X_1   0      0     0      0      0   0   0      0      0         0         0              0         0              0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     X_2    X_1   0      0      0   0   0      0      0         0         0              0         0              0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     X_2    X_1    0   0   0      0      0         0         0              0         0              0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      X_2 X_1 0      0      0         0         0              0         0              0              |
                {-2, -4} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   X_2    X_1    0         0         0              0         0              0              |
                {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      -28X_1    -25X_1    20X_1          -39X_1    10X_1          -49X_1         |
                {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      15X_1     33X_1     -19X_1         -48X_1    18X_1          22X_1          |
                {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      -17X_1    -43X_1    19X_1          -45X_1    -26X_1         16X_1          |
                {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      15X_1     45X_1     -29X_1         -14X_1    -40X_1         -16X_1         |
                {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      -49X_1    -37X_1    19X_1          49X_1     -23X_1         -17X_1         |
                {-4, -9} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      10X_1     6X_1      24X_1          -46X_1    4X_1           27X_1          |
                {-4, -8} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         -20X_2    -13X_2         -45X_2    45X_2          -47X_2         |
                {-4, -8} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      0     0      0      0      0      0      0   0   0      0      0      0     0      0     0      0      0   0   0      0      0         0         50X_2          41X_2     31X_2          18X_2          |

                                                33
o142 : K[X ..X ]-module, quotient of (K[X ..X ])
          1   3                          1   3

i143 : oddPart rH'

o143 = cokernel {-1, -2} | X_2 X_1 0   0   0   0   0   0   0      0      0      0      0      0      |
                {-1, -2} | 0   0   X_2 X_1 0   0   0   0   0      0      0      0      0      0      |
                {-1, -2} | 0   0   0   0   X_2 X_1 0   0   0      0      0      0      0      0      |
                {-1, -2} | 0   0   0   0   0   0   X_2 X_1 0      0      0      0      0      0      |
                {-3, -7} | 0   0   0   0   0   0   0   0   X_1    0      0      0      0      0      |
                {-3, -7} | 0   0   0   0   0   0   0   0   0      0      0      0      X_1    0      |
                {-3, -7} | 0   0   0   0   0   0   0   0   0      X_1    0      0      0      0      |
                {-3, -7} | 0   0   0   0   0   0   0   0   0      0      X_1    0      0      0      |
                {-3, -7} | 0   0   0   0   0   0   0   0   0      0      0      X_1    0      0      |
                {-3, -7} | 0   0   0   0   0   0   0   0   0      0      0      0      0      X_1    |
                {-3, -6} | 0   0   0   0   0   0   0   0   37X_2  31X_2  15X_2  -10X_2 -35X_2 -42X_2 |
                {-3, -6} | 0   0   0   0   0   0   0   0   11X_2  -41X_2 -14X_2 -7X_2  -34X_2 -44X_2 |
                {-3, -6} | 0   0   0   0   0   0   0   0   17X_2  12X_2  26X_2  -28X_2 -43X_2 -12X_2 |
                {-3, -6} | 0   0   0   0   0   0   0   0   -24X_2 50X_2  31X_2  40X_2  9X_2   19X_2  |
                {-3, -6} | 0   0   0   0   0   0   0   0   -41X_2 -30X_2 -24X_2 -28X_2 -37X_2 -47X_2 |
                {-3, -6} | 0   0   0   0   0   0   0   0   -22X_2 -36X_2 48X_2  44X_2  25X_2  23X_2  |

                                                16
o143 : K[X ..X ]-module, quotient of (K[X ..X ])
          1   3                          1   3

i144 : extgenSeries2 = (M,N) -> (
          H := ext(M,N);
          h := hilbertSeries H;
          T':= degreesRing ring H;
          substitute(h, {T'_0=>t^-1,T'_1=>u^-1})
          );

i145 : extgenSeries1 = (M,N) -> (
          substitute(extgenSeries2(M,N), {u=>1_T})
          );
```

---

## completeIntersections / test.m2 — chunk 18

### Input

```macaulay2
time extgenSeries2(M,N)
     -- used 0.00583 seconds
g=time extgenSeries1(M,N)
     -- used 0.067629 seconds
simplify g
time extgenSeries2(M,N')
     -- used 0.011802 seconds
g'=time extgenSeries1(M,N')
     -- used 0.008228 seconds
simplify g'
complexityPair = (M,N) -> dim ext(M,N);
time complexityPair(M,N)
     -- used 0.002071 seconds
```

### Output

```
i146 : time extgenSeries2(M,N)
     -- used 0.00583 seconds

-2    -1            2      2 2     2 3     2 4     3 4     3 5     3 6    3 7     4 5     4 6    4 7     4 8    4 9     5 8     5 9     6 10     6 11    6 12    7 13
       8u   + u   + 8t*u - 8t u - 9t u  - 9t u  + 7t u  - 8t u  - 8t u  + 4t u  + t u  + 8t u  + 9t u  + t u  - 2t u  + t u  + 8t u  - 4t u  - 8t u   + 2t u   - t u   - t u
o146 = -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                  2 5       2 4       2 3
                                                                            (1 - t u )(1 - t u )(1 - t u )

o146 : Expression of class Divide

i147 : g=time extgenSeries1(M,N)
     -- used 0.067629 seconds

2      3      4     5     6    7
       9 + 8t - 19t  - 11t  + 17t  + 4t  - 7t  - t
o147 = --------------------------------------------
                       2       2       2
                 (1 - t )(1 - t )(1 - t )

o147 : Expression of class Divide

i148 : simplify g

2     3    4
       9 - t - 9t  + 6t  + t
o148 = ----------------------
                         2
           (1 + t)(1 - t)

o148 : Expression of class Divide

i149 : time extgenSeries2(M,N')
     -- used 0.011802 seconds

-2     -1       2     2      2 2     2 3      2 4     3 5     3 6     3 7     4 5     4 6     4 7     4 8     4 9     5 9     5 10     6 10      6 11     6 12
       7u   + 2u   + 4t*u  - 7t u - 9t u  - 9t u  + 16t u  - 4t u  + 2t u  + 6t u  + 7t u  + 9t u  - 5t u  - 9t u  + 6t u  + 4t u  - 6t u   - 7t u   + 11t u   - 6t u
o149 = ----------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                              2 5       2 4       2 3
                                                                        (1 - t u )(1 - t u )(1 - t u )

o149 : Expression of class Divide

i150 : g'=time extgenSeries1(M,N')
     -- used 0.008228 seconds

2     3     4     5     6
       9 + 4t - 9t  + 4t  + 8t  - 2t  - 2t
o150 = ------------------------------------
                   2       2       2
             (1 - t )(1 - t )(1 - t )

o150 : Expression of class Divide

i151 : simplify g'

2     3     5
       9 - 5t - 4t  + 8t  - 2t
o151 = ------------------------
                  2       3
           (1 + t) (1 - t)

o151 : Expression of class Divide

i152 : complexityPair = (M,N) -> dim ext(M,N);

i153 : time complexityPair(M,N)
     -- used 0.002071 seconds

o153 = 2
```

---

## completeIntersections / test.m2 — chunk 19

### Input

```macaulay2
time complexityPair(M,N')
     -- used 0.003015 seconds
supportVarietyPairIdeal = (M,N) -> ann ext(M,N);
time supportVarietyPairIdeal(M,N)
     -- used 0.079569 seconds
time supportVarietyPairIdeal(M,N')
     -- used 0.03777 seconds
i158 :
```

### Output

```
i154 : time complexityPair(M,N')
     -- used 0.003015 seconds

o154 = 3

i155 : supportVarietyPairIdeal = (M,N) -> ann ext(M,N);

i156 : time supportVarietyPairIdeal(M,N)
     -- used 0.079569 seconds

o156 = ideal X
              1

o156 : Ideal of K[X ..X ]
                   1   3

i157 : time supportVarietyPairIdeal(M,N')
     -- used 0.03777 seconds

o157 = ideal ()

o157 : Ideal of K[X ..X ]
                   1   3

i158 :
```

---

## constructions / chapter.m2 — chunk 0

### Input

```macaulay2
randomPlanePoints = (delta,R) -> (
          k:=ceiling((-3+sqrt(9.0+8*delta))/2);
          eps:=delta-binomial(k+1,2);
          if k-2*eps>=0 
          then minors(k-eps,
               random(R^(k+1-eps),R^{k-2*eps:-1,eps:-2}))
          else minors(eps,
               random(R^{k+1-eps:0,2*eps-k:-1},R^{eps:-2})));
distinctPoints = (J) -> (
          singJ:=minors(2,jacobian J)+J;
          codim singJ == 3);
randomNodalCurve = method();
randomNodalCurve (ZZ,ZZ,Ring) := (d,g,R) -> (
          delta:=binomial(d-1,2)-g;
          K:=coefficientRing R;
          if (delta==0) 
          then (     --no double points
               ideal random(R^1,R^{-d}))
          else (      --delta double points            
               Ip:=randomPlanePoints(delta,R);
               --choose the curve
               Ip2:=saturate Ip^2;
               ideal (gens Ip2 * random(source gens Ip2, R^{-d}))));
isNodalCurve = (I) -> (
          singI:=ideal jacobian I +I;delta:=degree singI;
          d:=degree I;g:=binomial(d-1,2)-delta;
          {distinctPoints(singI),delta,g});
randomGenus11Curve = (R) -> (
          correctCodimAndDegree:=false;
          while not correctCodimAndDegree do (
               Mt=coker random(R^{3:8},R^{6:7,2:6});
               M=coker (transpose (res Mt).dd_4);
               Gt:=transpose (res M).dd_3;
               I:=ideal syz (Gt*random(source Gt,R^{6:5}));
               correctCodimAndDegree=(codim I==2 and degree I==12););
          I);
isSmoothSpaceCurve = (I) -> (
          --I generates the ideal sheaf of a pure codim 2 scheme in P3
          singI:=I+minors(2,jacobian I);
          codim singI==4);
K=ZZ/101;
```

### Output

```
i1 : randomPlanePoints = (delta,R) -> (
          k:=ceiling((-3+sqrt(9.0+8*delta))/2);
          eps:=delta-binomial(k+1,2);
          if k-2*eps>=0 
          then minors(k-eps,
               random(R^(k+1-eps),R^{k-2*eps:-1,eps:-2}))
          else minors(eps,
               random(R^{k+1-eps:0,2*eps-k:-1},R^{eps:-2})));

i2 : distinctPoints = (J) -> (
          singJ:=minors(2,jacobian J)+J;
          codim singJ == 3);

i3 : randomNodalCurve = method();

i4 : randomNodalCurve (ZZ,ZZ,Ring) := (d,g,R) -> (
          delta:=binomial(d-1,2)-g;
          K:=coefficientRing R;
          if (delta==0) 
          then (     --no double points
               ideal random(R^1,R^{-d}))
          else (      --delta double points            
               Ip:=randomPlanePoints(delta,R);
               --choose the curve
               Ip2:=saturate Ip^2;
               ideal (gens Ip2 * random(source gens Ip2, R^{-d}))));

i5 : isNodalCurve = (I) -> (
          singI:=ideal jacobian I +I;delta:=degree singI;
          d:=degree I;g:=binomial(d-1,2)-delta;
          {distinctPoints(singI),delta,g});

i6 : randomGenus11Curve = (R) -> (
          correctCodimAndDegree:=false;
          while not correctCodimAndDegree do (
               Mt=coker random(R^{3:8},R^{6:7,2:6});
               M=coker (transpose (res Mt).dd_4);
               Gt:=transpose (res M).dd_3;
               I:=ideal syz (Gt*random(source Gt,R^{6:5}));
               correctCodimAndDegree=(codim I==2 and degree I==12););
          I);

i7 : isSmoothSpaceCurve = (I) -> (
          --I generates the ideal sheaf of a pure codim 2 scheme in P3
          singI:=I+minors(2,jacobian I);
          codim singI==4);

i8 : K=ZZ/101;
```

---

## constructions / chapter.m2 — chunk 1

### Input

```macaulay2
R=K[x_0..x_3];
C=randomGenus11Curve(R);
isSmoothSpaceCurve(C)
Omega=prune Ext^2(coker gens C,R^{-4});
betti Omega
randomGenus12Curve = (R) -> (
           correctCodimAndDegree:=false;
           while not correctCodimAndDegree do (
                M:=coker random(R^{3:-2},R^{7:-3});
                Gt:=transpose (res M).dd_3;
                I:=ideal syz (Gt*random(source Gt,R^{7:5}));
                correctCodimAndDegree=(codim I==2 and degree I==12););
           I);
randomGenus13Curve = (R) -> (
           kappa:=koszul(3,vars R);
           correctCodimAndDegree:=false;
           while not correctCodimAndDegree do (
                test:=false;while test==false do ( 
                     alpha:=random(R^{4:-2},R^{6:-2});
                     beta:=random(R^{4:-2},R^{5:-3});
                     M:=coker(alpha*kappa|beta);
                     test=(codim M==4 and degree M==16););
                Gt:=transpose (res M).dd_3;
                --up to change of basis we can reduce phi to this form
                phi:=random(R^6,R^3)++id_(R^6);
                I:=ideal syz(Gt_{1..12}*phi);
                correctCodimAndDegree=(codim I==2 and degree I==13););
           I);
testModulesForGenus14Curves = (N,p) ->(
           x := local x;
           R := ZZ/p[x_0..x_3];
           i:=0;j:=0;
           kappa:=koszul(3,vars R);
           kappakappa:=kappa++kappa;
           utime:=timing while (i<N) do (
                test:=false;
                alpha:=random(R^{5:-2},R^{12:-2});
                beta:=random(R^{5:-2},R^{3:-3});
                M:=coker (alpha*kappakappa|beta);
                fM:=res (M,DegreeLimit =>3);
                if (tally degrees fM_2)_{5}==3 then (
                     --further checks to pick up the right module
                     test=(tally degrees fM_2)_{4}==2 and
                     codim M==4 and degree M==23;);
                i=i+1;if test==true then (j=j+1;););
           timeForNModules:=utime#0; numberOfGoodModules:=j;
           {timeForNModules,numberOfGoodModules});
```

### Output

```
i9 : R=K[x_0..x_3];

i10 : C=randomGenus11Curve(R);

o10 : Ideal of R

i11 : isSmoothSpaceCurve(C)

o11 = true

i12 : Omega=prune Ext^2(coker gens C,R^{-4});

i13 : betti Omega

o13 = relations : total: 5 10
                     -1: 2  .
                      0: 3 10

i14 : randomGenus12Curve = (R) -> (
           correctCodimAndDegree:=false;
           while not correctCodimAndDegree do (
                M:=coker random(R^{3:-2},R^{7:-3});
                Gt:=transpose (res M).dd_3;
                I:=ideal syz (Gt*random(source Gt,R^{7:5}));
                correctCodimAndDegree=(codim I==2 and degree I==12););
           I);

i15 : randomGenus13Curve = (R) -> (
           kappa:=koszul(3,vars R);
           correctCodimAndDegree:=false;
           while not correctCodimAndDegree do (
                test:=false;while test==false do ( 
                     alpha:=random(R^{4:-2},R^{6:-2});
                     beta:=random(R^{4:-2},R^{5:-3});
                     M:=coker(alpha*kappa|beta);
                     test=(codim M==4 and degree M==16););
                Gt:=transpose (res M).dd_3;
                --up to change of basis we can reduce phi to this form
                phi:=random(R^6,R^3)++id_(R^6);
                I:=ideal syz(Gt_{1..12}*phi);
                correctCodimAndDegree=(codim I==2 and degree I==13););
           I);

i16 : testModulesForGenus14Curves = (N,p) ->(
           x := local x;
           R := ZZ/p[x_0..x_3];
           i:=0;j:=0;
           kappa:=koszul(3,vars R);
           kappakappa:=kappa++kappa;
           utime:=timing while (i<N) do (
                test:=false;
                alpha:=random(R^{5:-2},R^{12:-2});
                beta:=random(R^{5:-2},R^{3:-3});
                M:=coker (alpha*kappakappa|beta);
                fM:=res (M,DegreeLimit =>3);
                if (tally degrees fM_2)_{5}==3 then (
                     --further checks to pick up the right module
                     test=(tally degrees fM_2)_{4}==2 and
                     codim M==4 and degree M==23;);
                i=i+1;if test==true then (j=j+1;););
           timeForNModules:=utime#0; numberOfGoodModules:=j;
           {timeForNModules,numberOfGoodModules});
```

---

## constructions / chapter.m2 — chunk 2

### Input

```macaulay2
testModulesForGenus14Curves(1000,5)
randomGenus14Curve = (R) -> (
           kappa:=koszul(3,vars R);
           kappakappa:=kappa++kappa;
           correctCodimAndDegree:=false;
           count:=0;while not correctCodimAndDegree do (
                test:=false;
                t:=timing while test==false do (
                     alpha=random(R^{5:-2},R^{12:-2});
                     beta=random(R^{5:-2},R^{3:-3});
                     M:=coker (alpha*kappakappa|beta);
                     fM:=res (M,DegreeLimit =>3);
                     if (tally degrees fM_2)_{5}==3 then (
                          --further checks to pick up the right module
                          test=(tally degrees fM_2)_{4}==2 and
                          codim M==4 and degree M==23;);
                     count=count+1;);
                Gt:=transpose (res M).dd_3;
                I:=ideal syz (Gt_{5..17});
                correctCodimAndDegree=(codim I==2 and degree I==14););
           <<"     -- "<<t#0<<" seconds used for ";
           <<count<<" modules"<<endl;
           I);
testModulesForDeg17CY = (N,k,p) -> (
           x:=symbol x;R:=(ZZ/p)[x_0..x_6];
           numberOfGoodModules:=0;i:=0;
           usedTime:=timing while (i<N) do (
                b:=random(R^3,R^{16:-1});
                --we put SyzygyLimit=>60 because we expect 
                --k<16 syzygies, so 16+28+k<=60
                fb:=res(coker b, 
                     DegreeLimit =>0,SyzygyLimit=>60,LengthLimit =>3);
                if rank fb_3>=k and (dim coker b)==0 then (
                     fb=res(coker b, DegreeLimit =>0,LengthLimit =>4);
                     if rank fb_4==0 
                     then numberOfGoodModules=numberOfGoodModules+1;);
                i=i+1;);
           collectGarbage();
           timeForNModules:=usedTime#0;
           {timeForNModules,numberOfGoodModules});
randomModuleForDeg17CY = (k,R) -> (
           isGoodModule:=false;i:=0;
           while not isGoodModule do (
                b:=random(R^3,R^{16:-1});
                --we put SyzygyLimit=>60 because we expect 
                --k<16 syzygies, so 16+28+k<=60
                fb:=res(coker b, 
                     DegreeLimit =>0,SyzygyLimit=>60,LengthLimit =>3);
                if rank fb_3>=k and (dim coker b)==0 then (
                     fb=res(coker b, DegreeLimit =>0,LengthLimit =>4);
                     if rank fb_4==0 then isGoodModule=true;);
                i=i+1;);
           <<"     -- Trial n. " << i <<", k="<< rank fb_3 <<endl;
           b);
getDeltaForDeg17CY = (b,f1) -> (
           fb:=res(coker b, LengthLimit =>3);
           k:=numgens target fb.dd_3-28; --# of linear syzygies
           b1:=fb.dd_1;b2:=fb.dd_2_{0..27};b2':=fb.dd_2_{28..28+k-1};
           b3:=fb.dd_3_{0..k-1}^{0..27};
           --the equation for f2 is b1*f2+f1*b2=0, 
           --so f2 is a lift of (-f1*b2) through b1 
           f2:=-(f1*b2)//b1;
           --the equation for A=(f3||Delta) is -f2*b3 = (b2|b2') * A
           A:=(-f2*b3)//(b2l|b2');
           Delta:=A^{28..28+k-1});
codimInfDefModuleForDeg17CY = (b) -> (
           --we create a parameter ring for the matrices f1's
           R:=ring b;K:=coefficientRing R;
           u:=symbol u;U:=K[u_0..u_(3*16*7-1)];
           i:=0;while i<3 do (
                <<endl<< " " << i+1 <<":" <<endl;
                j:=0;while j<16 do(
                     << "    " << j+1 <<". "<<endl;
                     k:=0;while k<7 do (
                        l=16*7*i+7*j+k; --index parametrizing the f1's
                        f1:=matrix(R,apply(3,m->apply(16,n->
                             if m==i and n==j then x_k else 0)));
                        Delta:=substitute(getDeltaForDeg17CY(b,f1),U);
                        if l==0 then (equations=u_l*Delta;) else (
                             equations=equations+u_l*Delta;);
                        k=k+1;);
                     collectGarbage(); --frees up memory in the stack
                     j=j+1;);
                i=i+1;);
           codim ideal equations);
skewSymMorphismsForDeg17CY = (b) -> (
           --we create a parameter ring for the morphisms: 
           K:=coefficientRing ring b;
           u:=symbol u;U:=K[u_0..u_(binomial(16,2)-1)];
           --now we compute the equations for the u_i's:
           UU:=U**ring b;
           equationsInUU:=flatten (substitute(b,UU)*
                substitute(genericSkewMatrix(U,u_0,16),UU));
           uu:=substitute(vars U,UU);
           equations:=substitute(
                diff(uu,transpose equationsInUU),ring b);
           syz(equations,DegreeLimit =>0));
getMorphismForDeg17CY = (SkewSymMorphism) -> (
           u:=symbol u;U:=K[u_0..u_(binomial(16,2)-1)];
           f=map(ring SkewSymMorphism,U,transpose SkewSymMorphism);
           f genericSkewMatrix(U,u_0,16));
```

### Output

```
i17 : testModulesForGenus14Curves(1000,5)

o17 = {41.02, 10}

o17 : List

i18 : randomGenus14Curve = (R) -> (
           kappa:=koszul(3,vars R);
           kappakappa:=kappa++kappa;
           correctCodimAndDegree:=false;
           count:=0;while not correctCodimAndDegree do (
                test:=false;
                t:=timing while test==false do (
                     alpha=random(R^{5:-2},R^{12:-2});
                     beta=random(R^{5:-2},R^{3:-3});
                     M:=coker (alpha*kappakappa|beta);
                     fM:=res (M,DegreeLimit =>3);
                     if (tally degrees fM_2)_{5}==3 then (
                          --further checks to pick up the right module
                          test=(tally degrees fM_2)_{4}==2 and
                          codim M==4 and degree M==23;);
                     count=count+1;);
                Gt:=transpose (res M).dd_3;
                I:=ideal syz (Gt_{5..17});
                correctCodimAndDegree=(codim I==2 and degree I==14););
           <<"     -- "<<t#0<<" seconds used for ";
           <<count<<" modules"<<endl;
           I);

i19 : testModulesForDeg17CY = (N,k,p) -> (
           x:=symbol x;R:=(ZZ/p)[x_0..x_6];
           numberOfGoodModules:=0;i:=0;
           usedTime:=timing while (i<N) do (
                b:=random(R^3,R^{16:-1});
                --we put SyzygyLimit=>60 because we expect 
                --k<16 syzygies, so 16+28+k<=60
                fb:=res(coker b, 
                     DegreeLimit =>0,SyzygyLimit=>60,LengthLimit =>3);
                if rank fb_3>=k and (dim coker b)==0 then (
                     fb=res(coker b, DegreeLimit =>0,LengthLimit =>4);
                     if rank fb_4==0 
                     then numberOfGoodModules=numberOfGoodModules+1;);
                i=i+1;);
           collectGarbage();
           timeForNModules:=usedTime#0;
           {timeForNModules,numberOfGoodModules});

i20 : randomModuleForDeg17CY = (k,R) -> (
           isGoodModule:=false;i:=0;
           while not isGoodModule do (
                b:=random(R^3,R^{16:-1});
                --we put SyzygyLimit=>60 because we expect 
                --k<16 syzygies, so 16+28+k<=60
                fb:=res(coker b, 
                     DegreeLimit =>0,SyzygyLimit=>60,LengthLimit =>3);
                if rank fb_3>=k and (dim coker b)==0 then (
                     fb=res(coker b, DegreeLimit =>0,LengthLimit =>4);
                     if rank fb_4==0 then isGoodModule=true;);
                i=i+1;);
           <<"     -- Trial n. " << i <<", k="<< rank fb_3 <<endl;
           b);

i21 : getDeltaForDeg17CY = (b,f1) -> (
           fb:=res(coker b, LengthLimit =>3);
           k:=numgens target fb.dd_3-28; --# of linear syzygies
           b1:=fb.dd_1;b2:=fb.dd_2_{0..27};b2':=fb.dd_2_{28..28+k-1};
           b3:=fb.dd_3_{0..k-1}^{0..27};
           --the equation for f2 is b1*f2+f1*b2=0, 
           --so f2 is a lift of (-f1*b2) through b1 
           f2:=-(f1*b2)//b1;
           --the equation for A=(f3||Delta) is -f2*b3 = (b2|b2') * A
           A:=(-f2*b3)//(b2l|b2');
           Delta:=A^{28..28+k-1});

i22 : codimInfDefModuleForDeg17CY = (b) -> (
           --we create a parameter ring for the matrices f1's
           R:=ring b;K:=coefficientRing R;
           u:=symbol u;U:=K[u_0..u_(3*16*7-1)];
           i:=0;while i<3 do (
                <<endl<< " " << i+1 <<":" <<endl;
                j:=0;while j<16 do(
                     << "    " << j+1 <<". "<<endl;
                     k:=0;while k<7 do (
                        l=16*7*i+7*j+k; --index parametrizing the f1's
                        f1:=matrix(R,apply(3,m->apply(16,n->
                             if m==i and n==j then x_k else 0)));
                        Delta:=substitute(getDeltaForDeg17CY(b,f1),U);
                        if l==0 then (equations=u_l*Delta;) else (
                             equations=equations+u_l*Delta;);
                        k=k+1;);
                     collectGarbage(); --frees up memory in the stack
                     j=j+1;);
                i=i+1;);
           codim ideal equations);

i23 : skewSymMorphismsForDeg17CY = (b) -> (
           --we create a parameter ring for the morphisms: 
           K:=coefficientRing ring b;
           u:=symbol u;U:=K[u_0..u_(binomial(16,2)-1)];
           --now we compute the equations for the u_i's:
           UU:=U**ring b;
           equationsInUU:=flatten (substitute(b,UU)*
                substitute(genericSkewMatrix(U,u_0,16),UU));
           uu:=substitute(vars U,UU);
           equations:=substitute(
                diff(uu,transpose equationsInUU),ring b);
           syz(equations,DegreeLimit =>0));

i24 : getMorphismForDeg17CY = (SkewSymMorphism) -> (
           u:=symbol u;U:=K[u_0..u_(binomial(16,2)-1)];
           f=map(ring SkewSymMorphism,U,transpose SkewSymMorphism);
           f genericSkewMatrix(U,u_0,16));
```

---

## constructions / chapter.m2 — chunk 3

### Input

```macaulay2
checkBasePtsForDeg17CY = b -> (
           --firstly the number of linear syzygies
           fb:=res(coker b, DegreeLimit=>0, LengthLimit =>4);
           k:=#select(degrees source fb.dd_3,i->i=={3});
           --then the check
           a=symbol a;A=K[a_0..a_2];
           mult:=(id_(A^7)**vars A)*substitute(
                syz transpose jacobian b,A);
           basePts=ideal mingens minors(5,mult);
           codim basePts==2 and degree basePts==k and distinctPoints(
                basePts));
checkMorphismsForDeg17CY = (b,skewSymMorphisms) -> (
           --first the number of linear syzygies
           fb:=res(coker b, DegreeLimit=>0, LengthLimit =>4);
           k:=#select(degrees source fb.dd_3,i->i=={3});
           if (numgens source skewSymMorphisms)!=k then (
                error "the number of skew-sym morphisms is wrong";);
           --we parametrize the morphisms:
           R:=ring b;K:=coefficientRing R;
           w:=symbol w;W:=K[w_0..w_(k-1)];
           WW:=R**W;ww:=substitute(vars W,WW);
           genericMorphism:=getMorphismForDeg17CY(
                substitute(skewSymMorphisms,WW)*transpose ww);
           --we compute the scheme of the 3x3 morphisms:
           equations:=mingens pfaffians(4,genericMorphism);
           equations=diff(
                substitute(symmetricPower(2,vars R),WW),equations);
           equations=saturate ideal flatten substitute(equations,W);
           CorrectDimensionAndDegree:=(
                dim equations==1 and degree equations==k);
           isNonDegenerate:=#select(
                (flatten degrees source gens equations),i->i==1)==0;
           collectGarbage();
           isOK:=CorrectDimensionAndDegree and isNonDegenerate;
           if isOK then (
                --in this case we also look for a skew-morphism f 
                --which is a linear combination of the special 
                --morphisms with all coefficients nonzero.
                isGoodMorphism:=false;while isGoodMorphism==false do (
                     evRandomMorphism:=random(K^1,K^k);
                     itsIdeal:=ideal(
                          vars W*substitute(syz evRandomMorphism,W));
                     isGoodMorphism=isGorenstein(
                          intersect(itsIdeal,equations));
                     collectGarbage());
                f=map(R,WW,vars R|substitute(evRandomMorphism,R));
                randomMorphism:=f(genericMorphism);
                {isOK,randomMorphism}) else {isOK});
isGorenstein = (I) -> (
           codim I==length res I and rank (res I)_(length res I)==1);
randomModule2ForDeg17CY = (k,R) -> (
           isGoodModule:=false;i:=0;
           while not isGoodModule do (
                b:=(random(R^1,R^{3:-1})++
                     random(R^1,R^{3:-1})++
                     random(R^1,R^{3:-1})|
                     matrix(R,{{1},{1},{1}})**random(R^1,R^{3:-1})|
                     random(R^3,R^1)**random(R^1,R^{3:-1})|
                     random(R^3,R^{1:-1}));
                --we put SyzygyLimit=>60 because we expect 
                --k<16 syzygies, so 16+28+k<=60
                fb:=res(coker b, 
                     DegreeLimit =>0,SyzygyLimit=>60,LengthLimit =>3);
                if rank fb_3>=k and dim coker b==0 then (
                     fb=res(coker b, DegreeLimit =>0,LengthLimit =>4);
                     if rank fb_4==0 then isGoodModule=true;);
                i=i+1;);
           <<"     -- Trial n. " << i <<", k="<< rank fb_3 <<endl;
           b);
K=ZZ/13;
R=K[x_0..x_6];
time b=randomModule2ForDeg17CY(8,R);
     -- Trial n. 1757, k=8
     -- used 764.06 seconds
betti res coker b
```

### Output

```
i25 : checkBasePtsForDeg17CY = b -> (
           --firstly the number of linear syzygies
           fb:=res(coker b, DegreeLimit=>0, LengthLimit =>4);
           k:=#select(degrees source fb.dd_3,i->i=={3});
           --then the check
           a=symbol a;A=K[a_0..a_2];
           mult:=(id_(A^7)**vars A)*substitute(
                syz transpose jacobian b,A);
           basePts=ideal mingens minors(5,mult);
           codim basePts==2 and degree basePts==k and distinctPoints(
                basePts));

i26 : checkMorphismsForDeg17CY = (b,skewSymMorphisms) -> (
           --first the number of linear syzygies
           fb:=res(coker b, DegreeLimit=>0, LengthLimit =>4);
           k:=#select(degrees source fb.dd_3,i->i=={3});
           if (numgens source skewSymMorphisms)!=k then (
                error "the number of skew-sym morphisms is wrong";);
           --we parametrize the morphisms:
           R:=ring b;K:=coefficientRing R;
           w:=symbol w;W:=K[w_0..w_(k-1)];
           WW:=R**W;ww:=substitute(vars W,WW);
           genericMorphism:=getMorphismForDeg17CY(
                substitute(skewSymMorphisms,WW)*transpose ww);
           --we compute the scheme of the 3x3 morphisms:
           equations:=mingens pfaffians(4,genericMorphism);
           equations=diff(
                substitute(symmetricPower(2,vars R),WW),equations);
           equations=saturate ideal flatten substitute(equations,W);
           CorrectDimensionAndDegree:=(
                dim equations==1 and degree equations==k);
           isNonDegenerate:=#select(
                (flatten degrees source gens equations),i->i==1)==0;
           collectGarbage();
           isOK:=CorrectDimensionAndDegree and isNonDegenerate;
           if isOK then (
                --in this case we also look for a skew-morphism f 
                --which is a linear combination of the special 
                --morphisms with all coefficients nonzero.
                isGoodMorphism:=false;while isGoodMorphism==false do (
                     evRandomMorphism:=random(K^1,K^k);
                     itsIdeal:=ideal(
                          vars W*substitute(syz evRandomMorphism,W));
                     isGoodMorphism=isGorenstein(
                          intersect(itsIdeal,equations));
                     collectGarbage());
                f=map(R,WW,vars R|substitute(evRandomMorphism,R));
                randomMorphism:=f(genericMorphism);
                {isOK,randomMorphism}) else {isOK});

i27 : isGorenstein = (I) -> (
           codim I==length res I and rank (res I)_(length res I)==1);

i28 : randomModule2ForDeg17CY = (k,R) -> (
           isGoodModule:=false;i:=0;
           while not isGoodModule do (
                b:=(random(R^1,R^{3:-1})++
                     random(R^1,R^{3:-1})++
                     random(R^1,R^{3:-1})|
                     matrix(R,{{1},{1},{1}})**random(R^1,R^{3:-1})|
                     random(R^3,R^1)**random(R^1,R^{3:-1})|
                     random(R^3,R^{1:-1}));
                --we put SyzygyLimit=>60 because we expect 
                --k<16 syzygies, so 16+28+k<=60
                fb:=res(coker b, 
                     DegreeLimit =>0,SyzygyLimit=>60,LengthLimit =>3);
                if rank fb_3>=k and dim coker b==0 then (
                     fb=res(coker b, DegreeLimit =>0,LengthLimit =>4);
                     if rank fb_4==0 then isGoodModule=true;);
                i=i+1;);
           <<"     -- Trial n. " << i <<", k="<< rank fb_3 <<endl;
           b);

i29 : K=ZZ/13;

i30 : R=K[x_0..x_6];

i31 : time b=randomModule2ForDeg17CY(8,R);
     -- Trial n. 1757, k=8
     -- used 764.06 seconds

3       16
o31 : Matrix R  <--- R

i32 : betti res coker b

o32 = total: 3 16 36 78 112 84 32 5
          0: 3 16 28  8   .  .  . .
          1: .  .  8 70 112 84 32 5
```

---

## constructions / chapter.m2 — chunk 4

### Input

```macaulay2
betti (skewSymMorphisms=skewSymMorphismsForDeg17CY b)
checkBasePtsForDeg17CY b
finalTest=checkMorphismsForDeg17CY(b,skewSymMorphisms);
finalTest#0
n=finalTest#1;
betti (nn=syz n)
n2t=transpose submatrix(nn,{0..15},{3});
b2:=syz b;
```

### Output

```
i33 : betti (skewSymMorphisms=skewSymMorphismsForDeg17CY b)

o33 = total: 120 8
         -1: 120 8

i34 : checkBasePtsForDeg17CY b

o34 = true

i35 : finalTest=checkMorphismsForDeg17CY(b,skewSymMorphisms);

i36 : finalTest#0

o36 = true

i37 : n=finalTest#1;

16       16
o37 : Matrix R   <--- R

i38 : betti (nn=syz n)

o38 = total: 16 4
          1: 16 3
          2:  . .
          3:  . 1

i39 : n2t=transpose submatrix(nn,{0..15},{3});

1       16
o39 : Matrix R  <--- R

i40 : b2:=syz b;

16       36
o40 : Matrix R   <--- R
```

---

## constructions / chapter.m2 — chunk 5

### Input

```macaulay2
j:=ideal mingens ideal flatten(n2t*b2);
degree j
codim j
betti res j
i45 :
```

### Output

```
i41 : j:=ideal mingens ideal flatten(n2t*b2);

o41 : Ideal of R

i42 : degree j

o42 = 17

i43 : codim j

o43 = 3

i44 : betti res j

o44 = total: 1 20 75 113 84 32 5
          0: 1  .  .   .  .  . .
          1: .  .  .   .  .  . .
          2: .  .  .   .  .  . .
          3: . 12  5   .  .  . .
          4: .  8 70 113 84 32 5

i45 :
```

---

## constructions / test.m2 — chunk 0

### Input

```macaulay2
setRandomSeed 1;
 -- setting random seed to 1
randomPlanePoints = (delta,R) -> (
          k:=ceiling((-3+sqrt(9.0+8*delta))/2);
          eps:=delta-binomial(k+1,2);
          if k-2*eps>=0 
          then minors(k-eps,
               random(R^(k+1-eps),R^{k-2*eps:-1,eps:-2}))
          else minors(eps,
               random(R^{k+1-eps:0,2*eps-k:-1},R^{eps:-2})));
distinctPoints = (J) -> (
          singJ:=minors(2,jacobian J)+J;
          codim singJ == 3);
randomNodalCurve = method();
randomNodalCurve (ZZ,ZZ,Ring) := (d,g,R) -> (
          delta:=binomial(d-1,2)-g;
          K:=coefficientRing R;
          if (delta==0) 
          then (     --no double points
               ideal random(R^1,R^{-d}))
          else (      --delta double points            
               Ip:=randomPlanePoints(delta,R);
               --choose the curve
               Ip2:=saturate Ip^2;
               ideal (gens Ip2 * random(source gens Ip2, R^{-d}))));
isNodalCurve = (I) -> (
          singI:=ideal jacobian I +I;delta:=degree singI;
          d:=degree I;g:=binomial(d-1,2)-delta;
          {distinctPoints(singI),delta,g});
randomGenus11Curve = (R) -> (
          correctCodimAndDegree:=false;
          while not correctCodimAndDegree do (
               Mt=coker random(R^{3:8},R^{6:7,2:6});
               M=coker (transpose (res Mt).dd_4);
               Gt:=transpose (res M).dd_3;
               I:=ideal syz (Gt*random(source Gt,R^{6:5}));
               correctCodimAndDegree=(codim I==2 and degree I==12););
          I);
isSmoothSpaceCurve = (I) -> (
          --I generates the ideal sheaf of a pure codim 2 scheme in P3
          singI:=I+minors(2,jacobian I);
          codim singI==4);
```

### Output

```
i1 : setRandomSeed 1;
 -- setting random seed to 1

i2 : randomPlanePoints = (delta,R) -> (
          k:=ceiling((-3+sqrt(9.0+8*delta))/2);
          eps:=delta-binomial(k+1,2);
          if k-2*eps>=0 
          then minors(k-eps,
               random(R^(k+1-eps),R^{k-2*eps:-1,eps:-2}))
          else minors(eps,
               random(R^{k+1-eps:0,2*eps-k:-1},R^{eps:-2})));

i3 : distinctPoints = (J) -> (
          singJ:=minors(2,jacobian J)+J;
          codim singJ == 3);

i4 : randomNodalCurve = method();

i5 : randomNodalCurve (ZZ,ZZ,Ring) := (d,g,R) -> (
          delta:=binomial(d-1,2)-g;
          K:=coefficientRing R;
          if (delta==0) 
          then (     --no double points
               ideal random(R^1,R^{-d}))
          else (      --delta double points            
               Ip:=randomPlanePoints(delta,R);
               --choose the curve
               Ip2:=saturate Ip^2;
               ideal (gens Ip2 * random(source gens Ip2, R^{-d}))));

i6 : isNodalCurve = (I) -> (
          singI:=ideal jacobian I +I;delta:=degree singI;
          d:=degree I;g:=binomial(d-1,2)-delta;
          {distinctPoints(singI),delta,g});

i7 : randomGenus11Curve = (R) -> (
          correctCodimAndDegree:=false;
          while not correctCodimAndDegree do (
               Mt=coker random(R^{3:8},R^{6:7,2:6});
               M=coker (transpose (res Mt).dd_4);
               Gt:=transpose (res M).dd_3;
               I:=ideal syz (Gt*random(source Gt,R^{6:5}));
               correctCodimAndDegree=(codim I==2 and degree I==12););
          I);

i8 : isSmoothSpaceCurve = (I) -> (
          --I generates the ideal sheaf of a pure codim 2 scheme in P3
          singI:=I+minors(2,jacobian I);
          codim singI==4);
```

---

## constructions / test.m2 — chunk 1

### Input

```macaulay2
K=ZZ/101;
R=K[x_0..x_3];
C=randomGenus11Curve(R);
isSmoothSpaceCurve(C)
Omega=prune Ext^2(coker gens C,R^{-4});
betti Omega
randomGenus12Curve = (R) -> (
           correctCodimAndDegree:=false;
           while not correctCodimAndDegree do (
                M:=coker random(R^{3:-2},R^{7:-3});
                Gt:=transpose (res M).dd_3;
                I:=ideal syz (Gt*random(source Gt,R^{7:5}));
                correctCodimAndDegree=(codim I==2 and degree I==12););
           I);
randomGenus13Curve = (R) -> (
           kappa:=koszul(3,vars R);
           correctCodimAndDegree:=false;
           while not correctCodimAndDegree do (
                test:=false;while test==false do ( 
                     alpha:=random(R^{4:-2},R^{6:-2});
                     beta:=random(R^{4:-2},R^{5:-3});
                     M:=coker(alpha*kappa|beta);
                     test=(codim M==4 and degree M==16););
                Gt:=transpose (res M).dd_3;
                --up to change of basis we can reduce phi to this form
                phi:=random(R^6,R^3)++id_(R^6);
                I:=ideal syz(Gt_{1..12}*phi);
                correctCodimAndDegree=(codim I==2 and degree I==13););
           I);
```

### Output

```
i9 : K=ZZ/101;

i10 : R=K[x_0..x_3];

i11 : C=randomGenus11Curve(R);

o11 : Ideal of R

i12 : isSmoothSpaceCurve(C)

o12 = true

i13 : Omega=prune Ext^2(coker gens C,R^{-4});

i14 : betti Omega

0  1
o14 = total: 5 10
         -1: 2  .
          0: 3 10

o14 : BettiTally

i15 : randomGenus12Curve = (R) -> (
           correctCodimAndDegree:=false;
           while not correctCodimAndDegree do (
                M:=coker random(R^{3:-2},R^{7:-3});
                Gt:=transpose (res M).dd_3;
                I:=ideal syz (Gt*random(source Gt,R^{7:5}));
                correctCodimAndDegree=(codim I==2 and degree I==12););
           I);

i16 : randomGenus13Curve = (R) -> (
           kappa:=koszul(3,vars R);
           correctCodimAndDegree:=false;
           while not correctCodimAndDegree do (
                test:=false;while test==false do ( 
                     alpha:=random(R^{4:-2},R^{6:-2});
                     beta:=random(R^{4:-2},R^{5:-3});
                     M:=coker(alpha*kappa|beta);
                     test=(codim M==4 and degree M==16););
                Gt:=transpose (res M).dd_3;
                --up to change of basis we can reduce phi to this form
                phi:=random(R^6,R^3)++id_(R^6);
                I:=ideal syz(Gt_{1..12}*phi);
                correctCodimAndDegree=(codim I==2 and degree I==13););
           I);
```

---

## constructions / test.m2 — chunk 2

### Input

```macaulay2
testModulesForGenus14Curves = (N,p) ->(
           x := local x;
           R := ZZ/p[x_0..x_3];
           i:=0;j:=0;
           kappa:=koszul(3,vars R);
           kappakappa:=kappa++kappa;
           utime:=timing while (i<N) do (
                test:=false;
                alpha:=random(R^{5:-2},R^{12:-2});
                beta:=random(R^{5:-2},R^{3:-3});
                M:=coker (alpha*kappakappa|beta);
                fM:=res (M,DegreeLimit =>3);
                if (tally degrees fM_2)_{5}==3 then (
                     --further checks to pick up the right module
                     test=(tally degrees fM_2)_{4}==2 and
                     codim M==4 and degree M==23;);
                i=i+1;if test==true then (j=j+1;););
           timeForNModules:=utime#0; numberOfGoodModules:=j;
           {timeForNModules,numberOfGoodModules});
testModulesForGenus14Curves(1000,5)
randomGenus14Curve = (R) -> (
           kappa:=koszul(3,vars R);
           kappakappa:=kappa++kappa;
           correctCodimAndDegree:=false;
           count:=0;while not correctCodimAndDegree do (
                test:=false;
                t:=timing while test==false do (
                     alpha=random(R^{5:-2},R^{12:-2});
                     beta=random(R^{5:-2},R^{3:-3});
                     M:=coker (alpha*kappakappa|beta);
                     fM:=res (M,DegreeLimit =>3);
                     if (tally degrees fM_2)_{5}==3 then (
                          --further checks to pick up the right module
                          test=(tally degrees fM_2)_{4}==2 and
                          codim M==4 and degree M==23;);
                     count=count+1;);
                Gt:=transpose (res M).dd_3;
                I:=ideal syz (Gt_{5..17});
                correctCodimAndDegree=(codim I==2 and degree I==14););
           <<"     -- "<<t#0<<" seconds used for ";
           <<count<<" modules"<<endl;
           I);
testModulesForDeg17CY = (N,k,p) -> (
           x:=symbol x;R:=(ZZ/p)[x_0..x_6];
           numberOfGoodModules:=0;i:=0;
           usedTime:=timing while (i<N) do (
                b:=random(R^3,R^{16:-1});
                --we put SyzygyLimit=>60 because we expect 
                --k<16 syzygies, so 16+28+k<=60
                fb:=res(coker b, 
                     DegreeLimit =>0,SyzygyLimit=>60,LengthLimit =>3);
                if rank fb_3>=k and (dim coker b)==0 then (
                     fb=res(coker b, DegreeLimit =>0,LengthLimit =>4);
                     if rank fb_4==0 
                     then numberOfGoodModules=numberOfGoodModules+1;);
                i=i+1;);
           collectGarbage();
           timeForNModules:=usedTime#0;
           {timeForNModules,numberOfGoodModules});
randomModuleForDeg17CY = (k,R) -> (
           isGoodModule:=false;i:=0;
           while not isGoodModule do (
                b:=random(R^3,R^{16:-1});
                --we put SyzygyLimit=>60 because we expect 
                --k<16 syzygies, so 16+28+k<=60
                fb:=res(coker b, 
                     DegreeLimit =>0,SyzygyLimit=>60,LengthLimit =>3);
                if rank fb_3>=k and (dim coker b)==0 then (
                     fb=res(coker b, DegreeLimit =>0,LengthLimit =>4);
                     if rank fb_4==0 then isGoodModule=true;);
                i=i+1;);
           <<"     -- Trial n. " << i <<", k="<< rank fb_3 <<endl;
           b);
getDeltaForDeg17CY = (b,f1) -> (
           fb:=res(coker b, LengthLimit =>3);
           k:=numgens target fb.dd_3-28; --# of linear syzygies
           b1:=fb.dd_1;b2:=fb.dd_2_{0..27};b2':=fb.dd_2_{28..28+k-1};
           b3:=fb.dd_3_{0..k-1}^{0..27};
           --the equation for f2 is b1*f2+f1*b2=0, 
           --so f2 is a lift of (-f1*b2) through b1 
           f2:=-(f1*b2)//b1;
           --the equation for A=(f3||Delta) is -f2*b3 = (b2|b2') * A
           A:=(-f2*b3)//(b2l|b2');
           Delta:=A^{28..28+k-1});
codimInfDefModuleForDeg17CY = (b) -> (
           --we create a parameter ring for the matrices f1's
           R:=ring b;K:=coefficientRing R;
           u:=symbol u;U:=K[u_0..u_(3*16*7-1)];
           i:=0;while i<3 do (
                <<endl<< " " << i+1 <<":" <<endl;
                j:=0;while j<16 do(
                     << "    " << j+1 <<". "<<endl;
                     k:=0;while k<7 do (
                        l=16*7*i+7*j+k; --index parametrizing the f1's
                        f1:=matrix(R,apply(3,m->apply(16,n->
                             if m==i and n==j then x_k else 0)));
                        Delta:=substitute(getDeltaForDeg17CY(b,f1),U);
                        if l==0 then (equations=u_l*Delta;) else (
                             equations=equations+u_l*Delta;);
                        k=k+1;);
                     collectGarbage(); --frees up memory in the stack
                     j=j+1;);
                i=i+1;);
           codim ideal equations);
skewSymMorphismsForDeg17CY = (b) -> (
           --we create a parameter ring for the morphisms: 
           K:=coefficientRing ring b;
           u:=symbol u;U:=K[u_0..u_(binomial(16,2)-1)];
           --now we compute the equations for the u_i's:
           UU:=tensor(U,ring b,DegreeRank => 1);     
           equationsInUU:=flatten (substitute(b,UU)*
                substitute(genericSkewMatrix(U,u_0,16),UU));
           uu:=substitute(vars U,UU);
           equations:=substitute(
                diff(uu,transpose equationsInUU),ring b);
           syz(equations,DegreeLimit =>0));
```

### Output

```
i17 : testModulesForGenus14Curves = (N,p) ->(
           x := local x;
           R := ZZ/p[x_0..x_3];
           i:=0;j:=0;
           kappa:=koszul(3,vars R);
           kappakappa:=kappa++kappa;
           utime:=timing while (i<N) do (
                test:=false;
                alpha:=random(R^{5:-2},R^{12:-2});
                beta:=random(R^{5:-2},R^{3:-3});
                M:=coker (alpha*kappakappa|beta);
                fM:=res (M,DegreeLimit =>3);
                if (tally degrees fM_2)_{5}==3 then (
                     --further checks to pick up the right module
                     test=(tally degrees fM_2)_{4}==2 and
                     codim M==4 and degree M==23;);
                i=i+1;if test==true then (j=j+1;););
           timeForNModules:=utime#0; numberOfGoodModules:=j;
           {timeForNModules,numberOfGoodModules});

i18 : testModulesForGenus14Curves(1000,5)

o18 = {7.50277, 8}

o18 : List

i19 : randomGenus14Curve = (R) -> (
           kappa:=koszul(3,vars R);
           kappakappa:=kappa++kappa;
           correctCodimAndDegree:=false;
           count:=0;while not correctCodimAndDegree do (
                test:=false;
                t:=timing while test==false do (
                     alpha=random(R^{5:-2},R^{12:-2});
                     beta=random(R^{5:-2},R^{3:-3});
                     M:=coker (alpha*kappakappa|beta);
                     fM:=res (M,DegreeLimit =>3);
                     if (tally degrees fM_2)_{5}==3 then (
                          --further checks to pick up the right module
                          test=(tally degrees fM_2)_{4}==2 and
                          codim M==4 and degree M==23;);
                     count=count+1;);
                Gt:=transpose (res M).dd_3;
                I:=ideal syz (Gt_{5..17});
                correctCodimAndDegree=(codim I==2 and degree I==14););
           <<"     -- "<<t#0<<" seconds used for ";
           <<count<<" modules"<<endl;
           I);

i20 : testModulesForDeg17CY = (N,k,p) -> (
           x:=symbol x;R:=(ZZ/p)[x_0..x_6];
           numberOfGoodModules:=0;i:=0;
           usedTime:=timing while (i<N) do (
                b:=random(R^3,R^{16:-1});
                --we put SyzygyLimit=>60 because we expect 
                --k<16 syzygies, so 16+28+k<=60
                fb:=res(coker b, 
                     DegreeLimit =>0,SyzygyLimit=>60,LengthLimit =>3);
                if rank fb_3>=k and (dim coker b)==0 then (
                     fb=res(coker b, DegreeLimit =>0,LengthLimit =>4);
                     if rank fb_4==0 
                     then numberOfGoodModules=numberOfGoodModules+1;);
                i=i+1;);
           collectGarbage();
           timeForNModules:=usedTime#0;
           {timeForNModules,numberOfGoodModules});

i21 : randomModuleForDeg17CY = (k,R) -> (
           isGoodModule:=false;i:=0;
           while not isGoodModule do (
                b:=random(R^3,R^{16:-1});
                --we put SyzygyLimit=>60 because we expect 
                --k<16 syzygies, so 16+28+k<=60
                fb:=res(coker b, 
                     DegreeLimit =>0,SyzygyLimit=>60,LengthLimit =>3);
                if rank fb_3>=k and (dim coker b)==0 then (
                     fb=res(coker b, DegreeLimit =>0,LengthLimit =>4);
                     if rank fb_4==0 then isGoodModule=true;);
                i=i+1;);
           <<"     -- Trial n. " << i <<", k="<< rank fb_3 <<endl;
           b);

i22 : getDeltaForDeg17CY = (b,f1) -> (
           fb:=res(coker b, LengthLimit =>3);
           k:=numgens target fb.dd_3-28; --# of linear syzygies
           b1:=fb.dd_1;b2:=fb.dd_2_{0..27};b2':=fb.dd_2_{28..28+k-1};
           b3:=fb.dd_3_{0..k-1}^{0..27};
           --the equation for f2 is b1*f2+f1*b2=0, 
           --so f2 is a lift of (-f1*b2) through b1 
           f2:=-(f1*b2)//b1;
           --the equation for A=(f3||Delta) is -f2*b3 = (b2|b2') * A
           A:=(-f2*b3)//(b2l|b2');
           Delta:=A^{28..28+k-1});

i23 : codimInfDefModuleForDeg17CY = (b) -> (
           --we create a parameter ring for the matrices f1's
           R:=ring b;K:=coefficientRing R;
           u:=symbol u;U:=K[u_0..u_(3*16*7-1)];
           i:=0;while i<3 do (
                <<endl<< " " << i+1 <<":" <<endl;
                j:=0;while j<16 do(
                     << "    " << j+1 <<". "<<endl;
                     k:=0;while k<7 do (
                        l=16*7*i+7*j+k; --index parametrizing the f1's
                        f1:=matrix(R,apply(3,m->apply(16,n->
                             if m==i and n==j then x_k else 0)));
                        Delta:=substitute(getDeltaForDeg17CY(b,f1),U);
                        if l==0 then (equations=u_l*Delta;) else (
                             equations=equations+u_l*Delta;);
                        k=k+1;);
                     collectGarbage(); --frees up memory in the stack
                     j=j+1;);
                i=i+1;);
           codim ideal equations);

i24 : skewSymMorphismsForDeg17CY = (b) -> (
           --we create a parameter ring for the morphisms: 
           K:=coefficientRing ring b;
           u:=symbol u;U:=K[u_0..u_(binomial(16,2)-1)];
           --now we compute the equations for the u_i's:
           UU:=tensor(U,ring b,DegreeRank => 1);     
           equationsInUU:=flatten (substitute(b,UU)*
                substitute(genericSkewMatrix(U,u_0,16),UU));
           uu:=substitute(vars U,UU);
           equations:=substitute(
                diff(uu,transpose equationsInUU),ring b);
           syz(equations,DegreeLimit =>0));
```

---

## constructions / test.m2 — chunk 3

### Input

```macaulay2
getMorphismForDeg17CY = (SkewSymMorphism) -> (
           u:=symbol u;U:=K[u_0..u_(binomial(16,2)-1)];
           f=map(ring SkewSymMorphism,U,transpose SkewSymMorphism);
           f genericSkewMatrix(U,u_0,16));
checkBasePtsForDeg17CY = b -> (
           --firstly the number of linear syzygies
           fb:=res(coker b, DegreeLimit=>0, LengthLimit =>4);
           k:=#select(degrees source fb.dd_3,i->i=={3});
           --then the check
           a=symbol a;A=K[a_0..a_2];
           mult:=(id_(A^7)**vars A)*substitute(
                syz transpose jacobian b,A);
           basePts=ideal mingens minors(5,mult);
           codim basePts==2 and degree basePts==k and distinctPoints(
                basePts));
checkMorphismsForDeg17CY = (b,skewSymMorphisms) -> (
           --first the number of linear syzygies
           fb:=res(coker b, DegreeLimit=>0, LengthLimit =>4);
           k:=#select(degrees source fb.dd_3,i->i=={3});
           if (numgens source skewSymMorphisms)!=k then (
                error "the number of skew-sym morphisms is wrong";);
           --we parametrize the morphisms:
           R:=ring b;K:=coefficientRing R;
           w:=symbol w;W:=K[w_0..w_(k-1)];
           WW:=tensor(R,W,DegreeRank=>1);
           ww:=substitute(vars W,WW);
           genericMorphism:=getMorphismForDeg17CY(
                substitute(skewSymMorphisms,WW)*transpose ww);
           --we compute the scheme of the 3x3 morphisms:
           equations:=mingens pfaffians(4,genericMorphism);
           equations=diff(
                substitute(symmetricPower(2,vars R),WW),equations);
           equations=saturate ideal flatten substitute(equations,W);
           CorrectDimensionAndDegree:=(
                dim equations==1 and degree equations==k);
           isNonDegenerate:=#select(
                (flatten degrees source gens equations),i->i==1)==0;
           collectGarbage();
           isOK:=CorrectDimensionAndDegree and isNonDegenerate;
           if isOK then (
                --in this case we also look for a skew-morphism f 
                --which is a linear combination of the special 
                --morphisms with all coefficients nonzero.
                isGoodMorphism:=false;while isGoodMorphism==false do (
                     evRandomMorphism:=random(K^1,K^k);
                     itsIdeal:=ideal(
                          vars W*substitute(syz evRandomMorphism,W));
                     isGoodMorphism=isGorenstein(
                          intersect(itsIdeal,equations));
                     collectGarbage());
                f=map(R,WW,vars R|substitute(evRandomMorphism,R));
                randomMorphism:=f(genericMorphism);
                {isOK,randomMorphism}) else {isOK});
isGorenstein = (I) -> (
           codim I==length res I and rank (res I)_(length res I)==1);
randomModule2ForDeg17CY = (k,R) -> (
           isGoodModule:=false;i:=0;
           while not isGoodModule do (
                b:=(random(R^1,R^{3:-1})++
                     random(R^1,R^{3:-1})++
                     random(R^1,R^{3:-1})|
                     matrix(R,{{1},{1},{1}})**random(R^1,R^{3:-1})|
                     random(R^3,R^1)**random(R^1,R^{3:-1})|
                     random(R^3,R^{1:-1}));
                --we put SyzygyLimit=>60 because we expect 
                --k<16 syzygies, so 16+28+k<=60
                fb:=res(coker b, 
                     DegreeLimit =>0,SyzygyLimit=>60,LengthLimit =>3);
                if rank fb_3>=k and dim coker b==0 then (
                     fb=res(coker b, DegreeLimit =>0,LengthLimit =>4);
                     if rank fb_4==0 then isGoodModule=true;);
                i=i+1;);
           <<"     -- Trial n. " << i <<", k="<< rank fb_3 <<endl;
           b);
K=ZZ/13;
R=K[x_0..x_6];
time b=randomModule2ForDeg17CY(8,R);
     -- used 12.3878 seconds
     -- Trial n. 759, k=8
```

### Output

```
i25 : getMorphismForDeg17CY = (SkewSymMorphism) -> (
           u:=symbol u;U:=K[u_0..u_(binomial(16,2)-1)];
           f=map(ring SkewSymMorphism,U,transpose SkewSymMorphism);
           f genericSkewMatrix(U,u_0,16));

i26 : checkBasePtsForDeg17CY = b -> (
           --firstly the number of linear syzygies
           fb:=res(coker b, DegreeLimit=>0, LengthLimit =>4);
           k:=#select(degrees source fb.dd_3,i->i=={3});
           --then the check
           a=symbol a;A=K[a_0..a_2];
           mult:=(id_(A^7)**vars A)*substitute(
                syz transpose jacobian b,A);
           basePts=ideal mingens minors(5,mult);
           codim basePts==2 and degree basePts==k and distinctPoints(
                basePts));

i27 : checkMorphismsForDeg17CY = (b,skewSymMorphisms) -> (
           --first the number of linear syzygies
           fb:=res(coker b, DegreeLimit=>0, LengthLimit =>4);
           k:=#select(degrees source fb.dd_3,i->i=={3});
           if (numgens source skewSymMorphisms)!=k then (
                error "the number of skew-sym morphisms is wrong";);
           --we parametrize the morphisms:
           R:=ring b;K:=coefficientRing R;
           w:=symbol w;W:=K[w_0..w_(k-1)];
           WW:=tensor(R,W,DegreeRank=>1);
           ww:=substitute(vars W,WW);
           genericMorphism:=getMorphismForDeg17CY(
                substitute(skewSymMorphisms,WW)*transpose ww);
           --we compute the scheme of the 3x3 morphisms:
           equations:=mingens pfaffians(4,genericMorphism);
           equations=diff(
                substitute(symmetricPower(2,vars R),WW),equations);
           equations=saturate ideal flatten substitute(equations,W);
           CorrectDimensionAndDegree:=(
                dim equations==1 and degree equations==k);
           isNonDegenerate:=#select(
                (flatten degrees source gens equations),i->i==1)==0;
           collectGarbage();
           isOK:=CorrectDimensionAndDegree and isNonDegenerate;
           if isOK then (
                --in this case we also look for a skew-morphism f 
                --which is a linear combination of the special 
                --morphisms with all coefficients nonzero.
                isGoodMorphism:=false;while isGoodMorphism==false do (
                     evRandomMorphism:=random(K^1,K^k);
                     itsIdeal:=ideal(
                          vars W*substitute(syz evRandomMorphism,W));
                     isGoodMorphism=isGorenstein(
                          intersect(itsIdeal,equations));
                     collectGarbage());
                f=map(R,WW,vars R|substitute(evRandomMorphism,R));
                randomMorphism:=f(genericMorphism);
                {isOK,randomMorphism}) else {isOK});

i28 : isGorenstein = (I) -> (
           codim I==length res I and rank (res I)_(length res I)==1);

i29 : randomModule2ForDeg17CY = (k,R) -> (
           isGoodModule:=false;i:=0;
           while not isGoodModule do (
                b:=(random(R^1,R^{3:-1})++
                     random(R^1,R^{3:-1})++
                     random(R^1,R^{3:-1})|
                     matrix(R,{{1},{1},{1}})**random(R^1,R^{3:-1})|
                     random(R^3,R^1)**random(R^1,R^{3:-1})|
                     random(R^3,R^{1:-1}));
                --we put SyzygyLimit=>60 because we expect 
                --k<16 syzygies, so 16+28+k<=60
                fb:=res(coker b, 
                     DegreeLimit =>0,SyzygyLimit=>60,LengthLimit =>3);
                if rank fb_3>=k and dim coker b==0 then (
                     fb=res(coker b, DegreeLimit =>0,LengthLimit =>4);
                     if rank fb_4==0 then isGoodModule=true;);
                i=i+1;);
           <<"     -- Trial n. " << i <<", k="<< rank fb_3 <<endl;
           b);

i30 : K=ZZ/13;

i31 : R=K[x_0..x_6];

i32 : time b=randomModule2ForDeg17CY(8,R);
     -- used 12.3878 seconds
     -- Trial n. 759, k=8

3      16
o32 : Matrix R  <-- R
```

---

## constructions / test.m2 — chunk 4

### Input

```macaulay2
betti res coker b
betti (skewSymMorphisms=skewSymMorphismsForDeg17CY b)
checkBasePtsForDeg17CY b
finalTest=checkMorphismsForDeg17CY(b,skewSymMorphisms);
finalTest#0
n=finalTest#1;
betti (nn=syz n)
n2t=transpose submatrix(nn,{0..15},{3});
```

### Output

```
i33 : betti res coker b

0  1  2  3   4  5  6 7
o33 = total: 3 16 36 78 112 84 32 5
          0: 3 16 28  8   .  .  . .
          1: .  .  8 70 112 84 32 5

o33 : BettiTally

i34 : betti (skewSymMorphisms=skewSymMorphismsForDeg17CY b)

0 1
o34 = total: 120 8
         -1: 120 8

o34 : BettiTally

i35 : checkBasePtsForDeg17CY b

o35 = true

i36 : finalTest=checkMorphismsForDeg17CY(b,skewSymMorphisms);

i37 : finalTest#0

o37 = true

i38 : n=finalTest#1;

16      16
o38 : Matrix R   <-- R

i39 : betti (nn=syz n)

0 1
o39 = total: 16 4
          1: 16 3
          2:  . .
          3:  . 1

o39 : BettiTally

i40 : n2t=transpose submatrix(nn,{0..15},{3});

1      16
o40 : Matrix R  <-- R
```

---

## constructions / test.m2 — chunk 5

### Input

```macaulay2
b2:=syz b;
j:=ideal mingens ideal flatten(n2t*b2);
degree j
codim j
betti res j
i46 :
```

### Output

```
i41 : b2:=syz b;

16      36
o41 : Matrix R   <-- R

i42 : j:=ideal mingens ideal flatten(n2t*b2);

o42 : Ideal of R

i43 : degree j

o43 = 17

i44 : codim j

o44 = 3

i45 : betti res j

0  1  2   3  4  5 6
o45 = total: 1 20 75 113 84 32 5
          0: 1  .  .   .  .  . .
          1: .  .  .   .  .  . .
          2: .  .  .   .  .  . .
          3: . 12  5   .  .  . .
          4: .  8 70 113 84 32 5

o45 : BettiTally

i46 :
```

---

## d-modules / chapter.m2 — chunk 0

### Input

```macaulay2
load "D-modules.m2"
D = QQ[x,y,z,Dx,Dy,Dz, WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz}]
Delta = ideal(Dx,Dy,Dz)
(Dx * x)^2
options D
DeltaBern = inw(Delta,{1,1,1,1,1,1}) 
dim DeltaBern 
D = QQ[x,y,z,w,Dx,Dy,Dz,Dw, 
            WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz, w=>Dw}];
```

### Output

```
i1 : load "D-modules.m2"

i2 : D = QQ[x,y,z,Dx,Dy,Dz, WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz}]

o2 = D

o2 : PolynomialRing

i3 : Delta = ideal(Dx,Dy,Dz)

o3 = ideal (Dx, Dy, Dz)

o3 : Ideal of D

i4 : (Dx * x)^2

2  2
o4 = x Dx  + 3x*Dx + 1

o4 : D

i5 : options D

o5 = OptionTable{Adjust => identity                        }
                 Degrees => {{1}, {1}, {1}, {1}, {1}, {1}}
                 Inverses => false
                 MonomialOrder => GRevLex
                 MonomialSize => 8
                 NewMonomialOrder => 
                 Repair => identity
                 SkewCommutative => false
                 VariableBaseName => 
                 VariableOrder => 
                 Variables => {x, y, z, Dx, Dy, Dz}
                 Weights => {}
                 WeylAlgebra => {x => Dx, y => Dy, z => Dz}

o5 : OptionTable

i6 : DeltaBern = inw(Delta,{1,1,1,1,1,1}) 

o6 = ideal (Dz, Dy, Dx)

o6 : Ideal of QQ [x, y, z, Dx, Dy, Dz]

i7 : dim DeltaBern 

o7 = 3

i8 : D = QQ[x,y,z,w,Dx,Dy,Dz,Dw, 
            WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz, w=>Dw}];
```

---

## d-modules / chapter.m2 — chunk 1

### Input

```macaulay2
f = x^2+y^2+z^2+w^2
AnnFs(f)
L=ideal(x,y,Dz,Dw)
AnnIFs(L,f)
f
globalBFunction(f)
g=x^3+y^3+z^3+w^3
factorBFunction globalBFunction(g)
```

### Output

```
i9 : f = x^2+y^2+z^2+w^2

2    2    2    2
o9 = x  + y  + z  + w

o9 : D

i10 : AnnFs(f)

1        1        1        1
o10 = ideal (w*Dz - z*Dw, w*Dy - y*Dw, z*Dy - y*Dz, w*Dx - x*Dw, z*Dx - x*Dz, y*Dx - x*Dy, -*x*Dx + -*y*Dy + -*z*Dz + -*w*Dw - $s)
                                                                                           2        2        2        2

o10 : Ideal of QQ [x, y, z, w, Dx, Dy, Dz, Dw, $s, WeylAlgebra => {x => Dx, y => Dy, z => Dz, w => Dw}]

i11 : L=ideal(x,y,Dz,Dw)

o11 = ideal (x, y, Dz, Dw)

o11 : Ideal of D

i12 : AnnIFs(L,f)

1        1
o12 = ideal (y, x, w*Dz - z*Dw, -*z*Dz + -*w*Dw - $s)
                                2        2

o12 : Ideal of QQ [x, y, z, w, Dx, Dy, Dz, Dw, $s, WeylAlgebra => {x => Dx, y => Dy, z => Dz, w => Dw}]

i13 : f

2    2    2    2
o13 = x  + y  + z  + w

o13 : D

i14 : globalBFunction(f)

2
o14 = $s  + 3$s + 2

o14 : QQ [$s]

i15 : g=x^3+y^3+z^3+w^3

3    3    3    3
o15 = x  + y  + z  + w

o15 : D

i16 : factorBFunction globalBFunction(g)

7       8               4       5
o16 = ($s + 1)($s + -)($s + -)($s + 2)($s + -)($s + -)
                    3       3               3       3

o16 : Product
```

---

## d-modules / chapter.m2 — chunk 2

### Input

```macaulay2
D1 = QQ[x,Dx,WeylAlgebra => {x=>Dx}];
I1 = ideal((x*Dx)^2+1)
f1 = x;
b=globalB(I1, f1)
use D
R = (D^1/ideal(Dx,Dy,Dz,Dw))
ann2 = relations Dlocalize(R,f)
F = matrix{{f}}
```

### Output

```
i17 : D1 = QQ[x,Dx,WeylAlgebra => {x=>Dx}];

i18 : I1 = ideal((x*Dx)^2+1)

2  2
o18 = ideal(x Dx  + x*Dx + 1)

o18 : Ideal of D1

i19 : f1 = x;

i20 : b=globalB(I1, f1)

2
o20 = HashTable{Boperator => - x*Dx  + 2Dx*$s + Dx}
                                 2
                Bpolynomial => $s  + 2$s + 2

o20 : HashTable

i21 : use D

o21 = D

o21 : PolynomialRing

i22 : R = (D^1/ideal(Dx,Dy,Dz,Dw))

o22 = cokernel | Dx Dy Dz Dw |

                             1
o22 : D-module, quotient of D

i23 : ann2 = relations Dlocalize(R,f)

o23 = | wDz-zDw wDy-yDw zDy-yDz wDx-xDw zDx-xDz yDx-xDy xDx+yDy+zDz+wDw+4 x2Dw+y2Dw+z2Dw+w2Dw+4w x2Dz+y2Dz+z2Dz+zwDw+4z x2Dy+y2Dy+yzDz+ywDw+4y |

              1       10
o23 : Matrix D  <--- D

i24 : F = matrix{{f}}

o24 = | x2+y2+z2+w2 |

              1       1
o24 : Matrix D  <--- D
```

---

## d-modules / chapter.m2 — chunk 3

### Input

```macaulay2
ann1 = gb modulo(F,ann2)
gb((ideal ann2) + (ideal F))
D = QQ[x,y,z,Dx,Dy,Dz, WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz}];
Delta = ideal(Dx,Dy,Dz);
f=x^3+y^3+z^3;
I1=DlocalizeAll(D^1/Delta,f,Strategy=>Oaku)
I2=DlocalizeAll(D^1/Delta,f)
I1.LocModule
```

### Output

```
i25 : ann1 = gb modulo(F,ann2)

o25 = {2} | wDz-zDw wDy-yDw zDy-yDz Dx^2+Dy^2+Dz^2+Dw^2 wDx-xDw zDx-xDz yDx-xDy xDx+yDy+zDz+wDw+2 x2Dw+y2Dw+z2Dw+w2Dw+2w x2Dz+y2Dz+z2Dz+zwDw+2z x2Dy+y2Dy+yzDz+ywDw+2y |

o25 : GroebnerBasis

i26 : gb((ideal ann2) + (ideal F))

o26 = | w z y x |

o26 : GroebnerBasis

i27 : D = QQ[x,y,z,Dx,Dy,Dz, WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz}];

i28 : Delta = ideal(Dx,Dy,Dz);

o28 : Ideal of D

i29 : f=x^3+y^3+z^3;

i30 : I1=DlocalizeAll(D^1/Delta,f,Strategy=>Oaku)

1        1        1             2      2     2      2     2      2
o30 = HashTable{annFS => ideal (-*x*Dx + -*y*Dy + -*z*Dz - $s, z Dy - y Dz, z Dx - x Dz, y Dx - x Dy)                                                                                                                                                                                                                                                                                           }
                                3        3        3
                                     2      5       4
                Bfunction => ($s + 1) ($s + -)($s + -)($s + 2)
                                            3       3
                              2       3         2       4      1   2  3  2    1   2  3  2    4  2  2  3    8           4    1   2  5    2     3         2     4      2     3         2     3         8        3      2     3      2     4    22     3      14     3      8        3    16     4    1   3  2   1   3  2    2   3  2    5   3     11   3     10   3      62   3    70   3   16   3
                Boperator => --*y*z*Dx Dy*Dz - --*y*z*Dy Dz + ---*z Dx Dz  - ---*z Dy Dz  - --*y Dy Dz  - ---*y*z*Dy*Dz  - ---*z Dz  + --*y*Dx Dy*$s - --*y*Dy $s + --*z*Dx Dz*$s + --*z*Dy Dz*$s + --*y*Dy*Dz $s + --*y*Dx Dy - --*y*Dy  + ---*z*Dx Dz + ---*z*Dy Dz - --*y*Dy*Dz  - ---*z*Dz  + --*Dx $s  + -*Dy $s  + --*Dz $s  + --*Dx $s + --*Dy $s + --*Dz $s + ---*Dx  + ---*Dy  + --*Dz
                             81                81             243            243            81            243              243         81              81           81              27              81              27           27         243           243           81            243         27          9          27          27         27         27         243       243       81
                GeneratorPower => -2
                LocMap => | x6+2x3y3+y6+2x3z3+2y3z3+z6 |
                LocModule => cokernel | 1/3xDx+1/3yDy+1/3zDz+2 z2Dy-y2Dz z2Dx-x2Dz y2Dx-x2Dy |

o30 : HashTable

i31 : I2=DlocalizeAll(D^1/Delta,f)

o31 = HashTable{GeneratorPower => -2                                                                                        }
                                          2        2      2       1
                IntegrateBfunction => ($s) ($s + 1) ($s + -)($s + -)
                                                          3       3
                LocMap => | x6+2x3y3+y6+2x3z3+2y3z3+z6 |
                LocModule => cokernel | xDx+yDy+zDz+6 z2Dy-y2Dz z2Dx-x2Dz y2Dx-x2Dy x3Dz+y3Dz+z3Dz+6z2 x3Dy+y3Dy+y2zDz+6y2 |

o31 : HashTable

i32 : I1.LocModule

o32 = cokernel | 1/3xDx+1/3yDy+1/3zDz+2 z2Dy-y2Dz z2Dx-x2Dz y2Dx-x2Dy |

                             1
o32 : D-module, quotient of D
```

---

## d-modules / chapter.m2 — chunk 4

### Input

```macaulay2
D= QQ[x,y,z,u,v,w,Dx,Dy,Dz,Du,Dv,Dw, WeylAlgebra =>
                {x=>Dx, y=>Dy, z=>Dz, u=>Du, v=>Dv, w=>Dw}];
Delta=ideal(Dx,Dy,Dz,Du,Dv,Dw);
R=D^1/Delta;
f=x*v-u*y;
g=x*w-u*z;
h=y*w-v*z;
Rf=DlocalizeAll(R,f,Strategy => Oaku)
Rfg=DlocalizeAll(Rf.LocModule,g, Strategy => Oaku)
```

### Output

```
i33 : D= QQ[x,y,z,u,v,w,Dx,Dy,Dz,Du,Dv,Dw, WeylAlgebra =>
                {x=>Dx, y=>Dy, z=>Dz, u=>Du, v=>Dv, w=>Dw}];

i34 : Delta=ideal(Dx,Dy,Dz,Du,Dv,Dw);

o34 : Ideal of D

i35 : R=D^1/Delta;

i36 : f=x*v-u*y;

i37 : g=x*w-u*z;

i38 : h=y*w-v*z;

i39 : Rf=DlocalizeAll(R,f,Strategy => Oaku)

o39 = HashTable{annFS => ideal (Dw, Dz, x*Du + y*Dv, y*Dy - u*Du, x*Dy + u*Dv, u*Dx + v*Dy, y*Dx + v*Du, x*Dx - v*Dv, u*Du + v*Dv - $s)}
                Bfunction => ($s + 1)($s + 2)
                Boperator => - Dy*Du + Dx*Dv
                GeneratorPower => -2
                LocMap => | y2u2-2xyuv+x2v2 |
                LocModule => cokernel | Dw Dz xDu+yDv yDy-uDu xDy+uDv uDx+vDy yDx+vDu xDx-vDv uDu+vDv+2 |

o39 : HashTable

i40 : Rfg=DlocalizeAll(Rf.LocModule,g, Strategy => Oaku)

2                                                                                                        2
o40 = HashTable{annFS => ideal (Dz*Dv - Dy*Dw, x*Du + y*Dv + z*Dw, z*Dz - u*Du - v*Dv - 2, x*Dz + u*Dw, y*Dy + z*Dz - u*Du, x*Dy + u*Dv, u*Dx + v*Dy + w*Dz, x*Dx - v*Dv - w*Dw, z*Dz + w*Dw - $s, u*Du*Dv + v*Dv  - z*Dy*Dw + 3Dv, y*Dx*Dv + v*Du*Dv + z*Dx*Dw + w*Du*Dw + Du, y*u*Dv - x*v*Dv - 2x, v*Dy*Du*Dv - v*Dx*Dv  + z*Dx*Dy*Dw + w*Dy*Du*Dw + Dy*Du - 2Dx*Dv)}
                Bfunction => ($s + 1)($s)
                Boperator => - Dz*Du + Dx*Dw
                GeneratorPower => -1
                LocMap => | -zu+xw |
                LocModule => cokernel | DzDv-DyDw xDu+yDv+zDw zDz-uDu-vDv-2 xDz+uDw yDy+zDz-uDu xDy+uDv uDx+vDy+wDz xDx-vDv-wDw zDz+wDw+1 uDuDv+vDv^2-zDyDw+3Dv yDxDv+vDuDv+zDxDw+wDuDw+Du yuDv-xvDv-2x vDyDuDv-vDxDv^2+zDxDyDw+wDyDuDw+DyDu-2DxDv |

o40 : HashTable
```

---

## d-modules / chapter.m2 — chunk 5

### Input

```macaulay2
Rfgh=DlocalizeAll(Rfg.LocModule,h, Strategy => Oaku)
Rf.GeneratorPower
Jfgh=ideal relations Rfgh.LocModule;
JH3=Jfgh+ideal(f^2,g,h);
JH3gb=gb JH3
testmTorsion = method();
testmTorsion Ideal := (L) -> (
           LL = ideal generators gb L;
           n = numgens (ring (LL)) // 2;
           LLL = ideal select(first entries gens LL, f->(
                     l = apply(listForm f, t->drop(t#0,n));
                     all(l, t->t==toList(n:0))       
                     ));
           if dim inw(LLL,toList(apply(1..2*n,t -> 1))) == n
           then true
           else false);
testmTorsion(JH3)
```

### Output

```
i41 : Rfgh=DlocalizeAll(Rfg.LocModule,h, Strategy => Oaku)

2                                               2                2          2       2         2                          2                                                           2    2  2                          2                          2                   2       2                   2                       2                                                             2    2                       2                     2        2  2      2                                      2                       2   2   2                       2          2              2 2        2                         2                       2        2
o41 = HashTable{annFS => ideal (x*Du + y*Dv + z*Dw, z*Dz - u*Du - v*Dv - 2, y*Dy - u*Du - w*Dw - 1, u*Dx + v*Dy + w*Dz, x*Dx + y*Dy - w*Dw + 2, y*Dy + v*Dv - $s + 2, u*Du  - y*Dx*Dv - z*Dx*Dw + 3Du, x*v*Dy + x*w*Dz - u Du - 3u, v*Dy*Du  + w*Dz*Du  + y*Dx Dv + z*Dx Dw - Dx*Du, x*y*w*Dz - y*u Du - y*u*v*Dv - z*u*v*Dw + x*v*w*Dw - 3y*u + x*v, y*w*Dz*Du  + y Dx Dv + y*v*Dx*Du*Dv + y*z*Dx Dw + z*v*Dx*Du*Dw + v*w*Du Dw - y*Dx*Du - v*Du , y*z*u Du + y*z*u*v*Dv + y u*w*Dv - x*y*v*w*Dv + z u*v*Dw + y*z*u*w*Dw - x*z*v*w*Dw + 3y*z*u - x*z*v - 2x*y*w, y z*Dx Dv + y*z*v*Dx*Du*Dv + y w*Dx*Du*Dv + y*v*w*Du Dv + y*z Dx Dw + z v*Dx*Du*Dw + y*z*w*Dx*Du*Dw + z*v*w*Du Dw - y*z*Dx*Du - z*v*Du , y z*u Dv - x*y*z*u*v*Dv - x*y u*w*Dv + x y*v*w*Dv + y*z u Dw - x*z u*v*Dw - x*y*z*u*w*Dw + x z*v*w*Dw - 3x*y*z*u + x z*v + 2x y*w)}
                Bfunction => ($s - 1)($s + 1)
                Boperator => - Dz*Dv + Dy*Dw
                GeneratorPower => -1
                LocMap => | -zv+yw |
                LocModule => cokernel | xDu+yDv+zDw zDz-uDu-vDv-2 yDy-uDu-wDw-1 uDx+vDy+wDz xDx+yDy-wDw+2 yDy+vDv+3 uDu^2-yDxDv-zDxDw+3Du xvDy+xwDz-u2Du-3u vDyDu^2+wDzDu^2+yDx^2Dv+zDx^2Dw-DxDu xywDz-yu2Du-yuvDv-zuvDw+xvwDw-3yu+xv ywDzDu^2+y2Dx^2Dv+yvDxDuDv+yzDx^2Dw+zvDxDuDw+vwDu^2Dw-yDxDu-vDu^2 yzu2Du+yzuvDv+y2uwDv-xyvwDv+z2uvDw+yzuwDw-xzvwDw+3yzu-xzv-2xyw y2zDx^2Dv+yzvDxDuDv+y2wDxDuDv+yvwDu^2Dv+yz2Dx^2Dw+z2vDxDuDw+yzwDxDuDw+zvwDu^2Dw-yzDxDu-zvDu^2 y2zu2Dv-xyzuvDv-xy2uwDv+x2yvwDv+yz2u2Dw-xz2uvDw-xyzuwDw+x2zvwDw-3xyzu+x2zv+2x2yw |

o41 : HashTable

i42 : Rf.GeneratorPower

o42 = -2

i43 : Jfgh=ideal relations Rfgh.LocModule;

o43 : Ideal of D

i44 : JH3=Jfgh+ideal(f^2,g,h);

o44 : Ideal of D

i45 : JH3gb=gb JH3

o45 = | w z uDu+vDv+wDw+4 xDu+yDv+zDw yDy-uDu-wDw-1 xDy+uDv uDx+vDy+wDz yDx+vDu xDx-vDv-wDw-1 v2 uv yv u2 yu+xv xu y2 xy x2 xvDv+2x vDyDu+wDzDu-vDxDv-wDxDw-3Dx |

o45 : GroebnerBasis

i46 : testmTorsion = method();

i47 : testmTorsion Ideal := (L) -> (
           LL = ideal generators gb L;
           n = numgens (ring (LL)) // 2;
           LLL = ideal select(first entries gens LL, f->(
                     l = apply(listForm f, t->drop(t#0,n));
                     all(l, t->t==toList(n:0))       
                     ));
           if dim inw(LLL,toList(apply(1..2*n,t -> 1))) == n
           then true
           else false);

i48 : testmTorsion(JH3)

o48 = true
```

---

## d-modules / chapter.m2 — chunk 6

### Input

```macaulay2
D=QQ[x,y,z,w,Dx,Dy,Dz,Dw,WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz,
      w=>Dw}];
f=y^2-x*z;
g=z^2-y*w;
h=x*w-y*z;
Delta=ideal(Dx,Dy,Dz,Dw);
R=D^1/Delta;
Rf=DlocalizeAll(R,f,Strategy => Oaku)  
Rfg=DlocalizeAll(Rf.LocModule,g, Strategy => Oaku);
```

### Output

```
i49 : D=QQ[x,y,z,w,Dx,Dy,Dz,Dw,WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz,
      w=>Dw}];

i50 : f=y^2-x*z;

i51 : g=z^2-y*w;

i52 : h=x*w-y*z;

i53 : Delta=ideal(Dx,Dy,Dz,Dw);

o53 : Ideal of D

i54 : R=D^1/Delta;

i55 : Rf=DlocalizeAll(R,f,Strategy => Oaku)  

1                    1
o55 = HashTable{annFS => ideal (Dw, x*Dy + 2y*Dz, y*Dx + -*z*Dy, x*Dx - z*Dz, -*y*Dy + z*Dz - $s)}
                                                         2                    2
                                   3
                Bfunction => ($s + -)($s + 1)
                                   2
                             1   2
                Boperator => -*Dy  - Dx*Dz
                             4
                GeneratorPower => -1
                LocMap => | y2-xz |
                LocModule => cokernel | Dw xDy+2yDz yDx+1/2zDy xDx-zDz 1/2yDy+zDz+1 |

o55 : HashTable

i56 : Rfg=DlocalizeAll(Rf.LocModule,g, Strategy => Oaku);
```

---

## d-modules / chapter.m2 — chunk 7

### Input

```macaulay2
Rfgh=DlocalizeAll(Rfg.LocModule,h, Strategy => Oaku);
Ifgh=ideal relations Rfgh.LocModule;
IH3=Ifgh+ideal(f,g,h);
IH3gb=gb IH3
findSocle = method();
findSocle(Ideal, RingElement):= (L,P) -> (
           createDpairs(ring(L));
           v=(ring L).dpairVars#0;
           myflag = true;
           while myflag do (
                w = apply(v,temp -> temp*P % L);
                if all(w,temp -> temp == 0) then myflag = false
                else (
                     p = position(w, temp -> temp != 0);
                     P = v#p * P;)
                );
           P);
D = ring JH3
findSocle(JH3,1_D)
```

### Output

```
i57 : Rfgh=DlocalizeAll(Rfg.LocModule,h, Strategy => Oaku);

i58 : Ifgh=ideal relations Rfgh.LocModule;

o58 : Ideal of D

i59 : IH3=Ifgh+ideal(f,g,h);

o59 : Ideal of D

i60 : IH3gb=gb IH3

o60 = | 1 |

o60 : GroebnerBasis

i61 : findSocle = method();

i62 : findSocle(Ideal, RingElement):= (L,P) -> (
           createDpairs(ring(L));
           v=(ring L).dpairVars#0;
           myflag = true;
           while myflag do (
                w = apply(v,temp -> temp*P % L);
                if all(w,temp -> temp == 0) then myflag = false
                else (
                     p = position(w, temp -> temp != 0);
                     P = v#p * P;)
                );
           P);

i63 : D = ring JH3

o63 = D

o63 : PolynomialRing

i64 : findSocle(JH3,1_D)

o64 = x*v

o64 : D
```

---

## d-modules / chapter.m2 — chunk 8

### Input

```macaulay2
findLength = method();
findLength Ideal := (I) -> (   
           l = 0;
           while I != ideal 1_(ring I) do (
                l = l + 1;
                s = findSocle(I,1_(ring I));
                I = I + ideal s;);
           l);
findLength JH3
erase symbol x; erase symbol Dx;
D = QQ[x_1..x_5, Dx_1..Dx_5, WeylAlgebra =>
           apply(toList(1..5), i -> x_i => Dx_i)];
f = x_1^2 + x_2^2 + x_3^2 + x_4^2 +x_5^2;
g = x_1;
R = D^1/ideal(Dx_1,Dx_2,Dx_3,Dx_4,Dx_5);
```

### Output

```
i65 : findLength = method();

i66 : findLength Ideal := (I) -> (   
           l = 0;
           while I != ideal 1_(ring I) do (
                l = l + 1;
                s = findSocle(I,1_(ring I));
                I = I + ideal s;);
           l);

i67 : findLength JH3

o67 = 1

i68 : erase symbol x; erase symbol Dx;

i70 : D = QQ[x_1..x_5, Dx_1..Dx_5, WeylAlgebra =>
           apply(toList(1..5), i -> x_i => Dx_i)];

i71 : f = x_1^2 + x_2^2 + x_3^2 + x_4^2 +x_5^2;

i72 : g = x_1;

i73 : R = D^1/ideal(Dx_1,Dx_2,Dx_3,Dx_4,Dx_5);
```

---

## d-modules / chapter.m2 — chunk 9

### Input

```macaulay2
Rf =DlocalizeAll(R,f,Strategy => Oaku);
Bf = Rf.Bfunction
Rfg = DlocalizeAll(Rf.LocModule,g,Strategy => Oaku);
Bfg = Rfg.Bfunction
Rg = DlocalizeAll(R,g,Strategy => Oaku);
Bg = Rg.Bfunction
Rgf = DlocalizeAll(Rg.LocModule,f,Strategy => Oaku);
Bgf = Rgf.Bfunction
```

### Output

```
i74 : Rf =DlocalizeAll(R,f,Strategy => Oaku);

i75 : Bf = Rf.Bfunction

5
o75 = ($s + -)($s + 1)
            2

o75 : Product

i76 : Rfg = DlocalizeAll(Rf.LocModule,g,Strategy => Oaku);

i77 : Bfg = Rfg.Bfunction

o77 = ($s + 1)($s + 3)

o77 : Product

i78 : Rg = DlocalizeAll(R,g,Strategy => Oaku);

i79 : Bg = Rg.Bfunction

o79 = ($s + 1)

o79 : Product

i80 : Rgf = DlocalizeAll(Rg.LocModule,f,Strategy => Oaku);

i81 : Bgf = Rgf.Bfunction

5
o81 = ($s + 2)($s + 1)($s + -)
                            2

o81 : Product
```

---

## d-modules / chapter.m2 — chunk 10

### Input

```macaulay2
erase symbol x;
R = QQ[x,y,z];
f=x^3+y^3+z^3;
H=deRhamAll(f);
H.CohomologyGroups
H.LocalizeMap
H.TransferCycles
I = gkz(matrix{{1,2}}, {5})
```

### Output

```
i82 : erase symbol x;

i83 : R = QQ[x,y,z];

i84 : f=x^3+y^3+z^3;

i85 : H=deRhamAll(f);

i86 : H.CohomologyGroups

1
o86 = HashTable{0 => QQ }
                       1
                1 => QQ
                       2
                2 => QQ
                       2
                3 => QQ

o86 : HashTable

i87 : H.LocalizeMap

o87 = | $x_1^6+2$x_1^3$x_2^3+$x_2^6+2$x_1^3$x_3^3+2$x_2^3$x_3^3+$x_3^6 |

o87 : Matrix

i88 : H.TransferCycles

o88 = HashTable{0 => | -1/12$x_1^4$x_2^3$D_1-1/3$x_1$x_2^6$D_1-1/12$x_1^4$x_3^3$D_1-2/3$x_1$x_2^3$x_3^3$D_1-1/3$x_1$x_3^6$D_1+1/12$x_1^6$x_2$D_2+1/3$x_1^3$x_2^4$D_2+1/3$x_1^3$x_2$x_3^3$D_2+1/12$x_1^6$x_3$D_3+1/3$x_1^3$x_2^3$x_3$D_3+1/3$x_1^3$x_3^4$D_3+1/3$x_1^6+2/3$x_1^3$x_2^3+1/3$x_2^6+2/3$x_1^3$x_3^3+2/3$x_2^3$x_3^3+1/3$x_3^6 |}
                1 => | 2/3$x_1^5+2/3$x_1^2$x_2^3+2/3$x_1^2$x_3^3  |
                     | -2/3$x_1^3$x_2^2-2/3$x_2^5-2/3$x_2^2$x_3^3 |
                     | 2/3$x_1^3$x_3^2+2/3$x_2^3$x_3^2+2/3$x_3^5  |
                2 => | 48$x_1$x_2$x_3^2 600$x_3^4     |
                     | 48$x_1$x_2^2$x_3 600$x_2$x_3^3 |
                     | 48$x_1^2$x_2$x_3 600$x_1$x_3^3 |
                3 => | -$x_1$x_2$x_3 -$x_3^3 |

o88 : HashTable

i89 : I = gkz(matrix{{1,2}}, {5})

2
o89 = ideal (D  - D , x D  + 2x D  - 5)
              1    2   1 1     2 2

o89 : Ideal of QQ [x , x , D , D , WeylAlgebra => {x  => D , x  => D }]
                    1   2   1   2                   1     1   2     2
```

---

## d-modules / chapter.m2 — chunk 11

### Input

```macaulay2
PolySols I
i91 :
```

### Output

```
i90 : PolySols I

5      3          2
o90 = {x  + 20x x  + 60x x }
        1      1 2      1 2

o90 : List

i91 :
```

---

## d-modules / test.m2 — chunk 0

### Input

```macaulay2
needsPackage "BernsteinSato";
D = QQ[x,y,z,Dx,Dy,Dz, WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz}]
Delta = ideal(Dx,Dy,Dz)
(Dx * x)^2
options D
DeltaBern = inw(Delta,{1,1,1,1,1,1}) 
dim DeltaBern 
D = QQ[x,y,z,w,Dx,Dy,Dz,Dw, 
            WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz, w=>Dw}];
```

### Output

```
i1 : needsPackage "BernsteinSato";

i2 : D = QQ[x,y,z,Dx,Dy,Dz, WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz}]

o2 = D

o2 : PolynomialRing, 3 differential variable(s)

i3 : Delta = ideal(Dx,Dy,Dz)

o3 = ideal (Dx, Dy, Dz)

o3 : Ideal of D

i4 : (Dx * x)^2

2  2
o4 = x Dx  + 3x*Dx + 1

o4 : D

i5 : options D

o5 = OptionTable{Constants => false                              }
                                  1
                 DegreeGroup => ZZ
                 DegreeLift => null
                 DegreeMap => null
                 DegreeRank => 1
                 Degrees => {{1}, {1}, {1}, {1}, {1}, {1}}
                 Global => true
                 Heft => {1}
                 Inverses => false
                 Join => null
                 Local => false
                 MonomialOrder => {MonomialSize => 32           }
                                  {GRevLex => {1, 1, 1, 1, 1, 1}}
                                  {Position => Up               }
                 SkewCommutative => {}
                 Variables => {x, y, z, Dx, Dy, Dz}
                 WeylAlgebra => {{x, Dx}, {y, Dy}, {z, Dz}}

o5 : OptionTable

i6 : DeltaBern = inw(Delta,{1,1,1,1,1,1}) 

o6 = ideal (Dz, Dy, Dx)

o6 : Ideal of QQ[x..z, Dx, Dy, Dz]

i7 : dim DeltaBern 

o7 = 3

i8 : D = QQ[x,y,z,w,Dx,Dy,Dz,Dw, 
            WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz, w=>Dw}];
```

---

## d-modules / test.m2 — chunk 1

### Input

```macaulay2
f = x^2+y^2+z^2+w^2
AnnFs(f)
L=ideal(x,y,Dz,Dw)
AnnIFs(L,f)
f
globalBFunction(f)
g=x^3+y^3+z^3+w^3
factorBFunction globalBFunction(g)
```

### Output

```
i9 : f = x^2+y^2+z^2+w^2

2    2    2    2
o9 = x  + y  + z  + w

o9 : D

i10 : AnnFs(f)

o10 = ideal (w*Dz - z*Dw, w*Dy - y*Dw, z*Dy - y*Dz, w*Dx - x*Dw, z*Dx - x*Dz, y*Dx - x*Dy, x*Dx + y*Dy + z*Dz + w*Dw - 2s)

o10 : Ideal of QQ[x..z, w, Dx, Dy, Dz, Dw, s]

i11 : L=ideal(x,y,Dz,Dw)

o11 = ideal (x, y, Dz, Dw)

o11 : Ideal of D

i12 : AnnIFs(L,f)

o12 = ideal (y, x, w*Dz - z*Dw, z*Dz + w*Dw - 2s)

o12 : Ideal of QQ[x..z, w, Dx, Dy, Dz, Dw, s]

i13 : f

2    2    2    2
o13 = x  + y  + z  + w

o13 : D

i14 : globalBFunction(f)

2
o14 = s  + 3s + 2

o14 : QQ[s]

i15 : g=x^3+y^3+z^3+w^3

3    3    3    3
o15 = x  + y  + z  + w

o15 : D

i16 : factorBFunction globalBFunction(g)

4      5      7      8
o16 = (s + 1)(s + 2)(s + -)(s + -)(s + -)(s + -)
                         3      3      3      3

o16 : Expression of class Product
```

---

## d-modules / test.m2 — chunk 2

### Input

```macaulay2
D1 = QQ[x,Dx,WeylAlgebra => {x=>Dx}];
I1 = ideal((x*Dx)^2+1)
f1 = x;
b=globalB(I1, f1)
use D
R = (D^1/ideal(Dx,Dy,Dz,Dw))
ann2 = relations Dlocalize(R,f)
F = matrix{{f}}
```

### Output

```
i17 : D1 = QQ[x,Dx,WeylAlgebra => {x=>Dx}];

i18 : I1 = ideal((x*Dx)^2+1)

2  2
o18 = ideal(x Dx  + x*Dx + 1)

o18 : Ideal of D1

i19 : f1 = x;

i20 : b=globalB(I1, f1)

2
o20 = HashTable{Boperator => - x*Dx  + 2Dx*s + Dx}
                                2
                Bpolynomial => s  + 2s + 2

o20 : HashTable

i21 : use D

o21 = D

o21 : PolynomialRing, 4 differential variable(s)

i22 : R = (D^1/ideal(Dx,Dy,Dz,Dw))

o22 = cokernel | Dx Dy Dz Dw |

                             1
o22 : D-module, quotient of D

i23 : ann2 = relations Dlocalize(R,f)

o23 = | wDz-zDw wDy-yDw zDy-yDz wDx-xDw zDx-xDz yDx-xDy -xDx-yDy-zDz-wDw-4 |

              1      7
o23 : Matrix D  <-- D

i24 : F = matrix{{f}}

o24 = | x2+y2+z2+w2 |

              1      1
o24 : Matrix D  <-- D
```

---

## d-modules / test.m2 — chunk 3

### Input

```macaulay2
ann1 = gens gb modulo(F,ann2)
gens gb((ideal ann2) + (ideal F))
D = QQ[x,y,z,Dx,Dy,Dz, WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz}];
Delta = ideal(Dx,Dy,Dz);
f=x^3+y^3+z^3;
I1=DlocalizeAll(D^1/Delta,f,Strategy=>Oaku)
I2=DlocalizeAll(D^1/Delta,f)
I1.LocModule
```

### Output

```
i25 : ann1 = gens gb modulo(F,ann2)

o25 = {2} | wDz-zDw wDy-yDw zDy-yDz Dx^2+Dy^2+Dz^2+Dw^2 wDx-xDw zDx-xDz yDx-xDy xDx+yDy+zDz+wDw+2 x2Dw+y2Dw+z2Dw+w2Dw+2w x2Dz+y2Dz+z2Dz+zwDw+2z x2Dy+y2Dy+yzDz+ywDw+2y |

              1      11
o25 : Matrix D  <-- D

i26 : gens gb((ideal ann2) + (ideal F))

o26 = | w z y x |

              1      4
o26 : Matrix D  <-- D

i27 : D = QQ[x,y,z,Dx,Dy,Dz, WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz}];

i28 : Delta = ideal(Dx,Dy,Dz);

o28 : Ideal of D

i29 : f=x^3+y^3+z^3;

i30 : I1=DlocalizeAll(D^1/Delta,f,Strategy=>Oaku)

2      2     2      2     2      2
o30 = HashTable{annFS => ideal (x*Dx + y*Dy + z*Dz - 3s, z Dy - y Dz, z Dx - x Dz, y Dx - x Dy)                                                                                                                                                                                    }
                                    2            4      5
                Bfunction => (s + 1) (s + 2)(s + -)(s + -)
                                                 3      3
                                    3               4      2  3  2     2  3  2    2  5        3            4         3            3            4         3          4        3          3          4      3 2      3 2       3 2       3        3        3        3       3       3
                Boperator => 2y*z*Dx Dy*Dz - 2y*z*Dy Dz - z Dx Dz  - 3z Dy Dz  + z Dz  + 2y*Dx Dy*s - 2y*Dy s + 2z*Dx Dz*s + 6z*Dy Dz*s - 8z*Dz s + 6y*Dx Dy - 6y*Dy  + 2z*Dx Dz - 6z*Dy Dz - 8z*Dz  + 3Dx s  + 9Dy s  + 18Dz s  + 15Dx s + 33Dy s + 42Dz s + 18Dx  + 18Dy  + 24Dz
                GeneratorPower => -2
                LocMap => | x6+2x3y3+y6+2x3z3+2y3z3+z6 |
                LocModule => cokernel | xDx+yDy+zDz+6 z2Dy-y2Dz z2Dx-x2Dz y2Dx-x2Dy |

o30 : HashTable

i31 : I2=DlocalizeAll(D^1/Delta,f)

o31 = HashTable{GeneratorPower => -2                                                     }
                                         2       2     1      2
                IntegrateBfunction => (s) (s + 1) (s + -)(s + -)
                                                       3      3
                LocMap => | x6+2x3y3+y6+2x3z3+2y3z3+z6 |
                LocModule => cokernel | -xDx-yDy-zDz-6 -z2Dy+y2Dz -z2Dx+x2Dz -y2Dx+x2Dy |

o31 : HashTable

i32 : I1.LocModule

o32 = cokernel | xDx+yDy+zDz+6 z2Dy-y2Dz z2Dx-x2Dz y2Dx-x2Dy |

                             1
o32 : D-module, quotient of D
```

---

## d-modules / test.m2 — chunk 4

### Input

```macaulay2
D= QQ[x,y,z,u,v,w,Dx,Dy,Dz,Du,Dv,Dw, WeylAlgebra =>
                {x=>Dx, y=>Dy, z=>Dz, u=>Du, v=>Dv, w=>Dw}];
Delta=ideal(Dx,Dy,Dz,Du,Dv,Dw);
R=D^1/Delta;
f=x*v-u*y;
g=x*w-u*z;
h=y*w-v*z;
Rf=DlocalizeAll(R,f,Strategy => Oaku)
Rfg=DlocalizeAll(Rf.LocModule,g, Strategy => Oaku)
```

### Output

```
i33 : D= QQ[x,y,z,u,v,w,Dx,Dy,Dz,Du,Dv,Dw, WeylAlgebra =>
                {x=>Dx, y=>Dy, z=>Dz, u=>Du, v=>Dv, w=>Dw}];

i34 : Delta=ideal(Dx,Dy,Dz,Du,Dv,Dw);

o34 : Ideal of D

i35 : R=D^1/Delta;

i36 : f=x*v-u*y;

i37 : g=x*w-u*z;

i38 : h=y*w-v*z;

i39 : Rf=DlocalizeAll(R,f,Strategy => Oaku)

o39 = HashTable{annFS => ideal (Dw, Dz, x*Du + y*Dv, y*Dy - u*Du, x*Dy + u*Dv, u*Dx + v*Dy, y*Dx + v*Du, x*Dx - v*Dv, u*Du + v*Dv - s)}
                Bfunction => (s + 1)(s + 2)
                Boperator => - Dy*Du + Dx*Dv
                GeneratorPower => -2
                LocMap => | y2u2-2xyuv+x2v2 |
                LocModule => cokernel | Dw Dz xDu+yDv yDy-uDu xDy+uDv uDx+vDy yDx+vDu xDx-vDv uDu+vDv+2 |

o39 : HashTable

i40 : Rfg=DlocalizeAll(Rf.LocModule,g, Strategy => Oaku)

2                                                                                                        2
o40 = HashTable{annFS => ideal (Dz*Dv - Dy*Dw, x*Du + y*Dv + z*Dw, z*Dz - u*Du - v*Dv - 2, x*Dz + u*Dw, y*Dy + v*Dv + 2, x*Dy + u*Dv, u*Dx + v*Dy + w*Dz, x*Dx - v*Dv - w*Dw, u*Du + v*Dv + w*Dw - s + 2, u*Du*Dv + v*Dv  - z*Dy*Dw + 3Dv, y*Dx*Dv + v*Du*Dv + z*Dx*Dw + w*Du*Dw + Du, y*u*Dv - x*v*Dv - 2x, v*Dy*Du*Dv - v*Dx*Dv  + z*Dx*Dy*Dw + w*Dy*Du*Dw + Dy*Du - 2Dx*Dv)}
                Bfunction => (s)(s + 1)
                Boperator => - Dz*Du + Dx*Dw
                GeneratorPower => -1
                LocMap => | -zu+xw |
                LocModule => cokernel | DzDv-DyDw xDu+yDv+zDw zDz-uDu-vDv-2 xDz+uDw yDy+vDv+2 xDy+uDv uDx+vDy+wDz xDx-vDv-wDw uDu+vDv+wDw+3 uDuDv+vDv^2-zDyDw+3Dv yDxDv+vDuDv+zDxDw+wDuDw+Du yuDv-xvDv-2x vDyDuDv-vDxDv^2+zDxDyDw+wDyDuDw+DyDu-2DxDv |

o40 : HashTable
```

---

## d-modules / test.m2 — chunk 5

### Input

```macaulay2
Rfgh=DlocalizeAll(Rfg.LocModule,h, Strategy => Oaku)
Rf.GeneratorPower
Jfgh=ideal relations Rfgh.LocModule;
JH3=Jfgh+ideal(f^2,g,h);
JH3gb=gens gb JH3
testmTorsion = method();
testmTorsion Ideal := (L) -> (
           LL = ideal generators gb L;
           n = numgens (ring (LL)) // 2;
           LLLL = ideal select(first entries gens LL, f->(
                     l = apply(listForm f, t->drop(t#0,n));
                     all(l, t->t==toList(n:0))       
                     ));
           if dim inw(LLLL,toList(apply(1..2*n,t -> 1))) == n
           then true
           else false);
testmTorsion(JH3)
```

### Output

```
i41 : Rfgh=DlocalizeAll(Rfg.LocModule,h, Strategy => Oaku)

2                                               2                2          2       2         2                          2                                                           2    2  2                          2                          2                   2       2                   2                       2                                                             2    2                       2                     2        2  2      2                                      2                       2   2   2                       2          2              2 2        2                         2                       2        2
o41 = HashTable{annFS => ideal (x*Du + y*Dv + z*Dw, z*Dz - u*Du - v*Dv - 2, y*Dy - u*Du - w*Dw - 1, u*Dx + v*Dy + w*Dz, x*Dx + u*Du + 3, u*Du + v*Dv + w*Dw - s + 3, u*Du  - y*Dx*Dv - z*Dx*Dw + 3Du, x*v*Dy + x*w*Dz - u Du - 3u, v*Dy*Du  + w*Dz*Du  + y*Dx Dv + z*Dx Dw - Dx*Du, x*y*w*Dz - y*u Du - y*u*v*Dv - z*u*v*Dw + x*v*w*Dw - 3y*u + x*v, y*w*Dz*Du  + y Dx Dv + y*v*Dx*Du*Dv + y*z*Dx Dw + z*v*Dx*Du*Dw + v*w*Du Dw - y*Dx*Du - v*Du , y*z*u Du + y*z*u*v*Dv + y u*w*Dv - x*y*v*w*Dv + z u*v*Dw + y*z*u*w*Dw - x*z*v*w*Dw + 3y*z*u - x*z*v - 2x*y*w, y z*Dx Dv + y*z*v*Dx*Du*Dv + y w*Dx*Du*Dv + y*v*w*Du Dv + y*z Dx Dw + z v*Dx*Du*Dw + y*z*w*Dx*Du*Dw + z*v*w*Du Dw - y*z*Dx*Du - z*v*Du , y z*u Dv - x*y*z*u*v*Dv - x*y u*w*Dv + x y*v*w*Dv + y*z u Dw - x*z u*v*Dw - x*y*z*u*w*Dw + x z*v*w*Dw - 3x*y*z*u + x z*v + 2x y*w)}
                Bfunction => (s - 1)(s + 1)
                Boperator => - Dz*Dv + Dy*Dw
                GeneratorPower => -1
                LocMap => | -zv+yw |
                LocModule => cokernel | xDu+yDv+zDw zDz-uDu-vDv-2 yDy-uDu-wDw-1 uDx+vDy+wDz xDx+uDu+3 uDu+vDv+wDw+4 uDu^2-yDxDv-zDxDw+3Du xvDy+xwDz-u2Du-3u vDyDu^2+wDzDu^2+yDx^2Dv+zDx^2Dw-DxDu xywDz-yu2Du-yuvDv-zuvDw+xvwDw-3yu+xv ywDzDu^2+y2Dx^2Dv+yvDxDuDv+yzDx^2Dw+zvDxDuDw+vwDu^2Dw-yDxDu-vDu^2 yzu2Du+yzuvDv+y2uwDv-xyvwDv+z2uvDw+yzuwDw-xzvwDw+3yzu-xzv-2xyw y2zDx^2Dv+yzvDxDuDv+y2wDxDuDv+yvwDu^2Dv+yz2Dx^2Dw+z2vDxDuDw+yzwDxDuDw+zvwDu^2Dw-yzDxDu-zvDu^2 y2zu2Dv-xyzuvDv-xy2uwDv+x2yvwDv+yz2u2Dw-xz2uvDw-xyzuwDw+x2zvwDw-3xyzu+x2zv+2x2yw |

o41 : HashTable

i42 : Rf.GeneratorPower

o42 = -2

i43 : Jfgh=ideal relations Rfgh.LocModule;

o43 : Ideal of D

i44 : JH3=Jfgh+ideal(f^2,g,h);

o44 : Ideal of D

i45 : JH3gb=gens gb JH3

o45 = | w z uDu+vDv+3 xDu+yDv yDy+vDv+3 xDy+uDv uDx+vDy yDx+vDu xDx-vDv v2 uv yv u2 yu+xv xu y2 xy x2 xvDv+2x vDyDu-vDxDv-2Dx |

              1      20
o45 : Matrix D  <-- D

i46 : testmTorsion = method();

i47 : testmTorsion Ideal := (L) -> (
           LL = ideal generators gb L;
           n = numgens (ring (LL)) // 2;
           LLLL = ideal select(first entries gens LL, f->(
                     l = apply(listForm f, t->drop(t#0,n));
                     all(l, t->t==toList(n:0))       
                     ));
           if dim inw(LLLL,toList(apply(1..2*n,t -> 1))) == n
           then true
           else false);

i48 : testmTorsion(JH3)

o48 = true
```

---

## d-modules / test.m2 — chunk 6

### Input

```macaulay2
D=QQ[x,y,z,w,Dx,Dy,Dz,Dw,WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz,
      w=>Dw}];
f=y^2-x*z;
g=z^2-y*w;
h=x*w-y*z;
Delta=ideal(Dx,Dy,Dz,Dw);
R=D^1/Delta;
Rf=DlocalizeAll(R,f,Strategy => Oaku)  
Rfg=DlocalizeAll(Rf.LocModule,g, Strategy => Oaku);
```

### Output

```
i49 : D=QQ[x,y,z,w,Dx,Dy,Dz,Dw,WeylAlgebra => {x=>Dx, y=>Dy, z=>Dz,
      w=>Dw}];

i50 : f=y^2-x*z;

i51 : g=z^2-y*w;

i52 : h=x*w-y*z;

i53 : Delta=ideal(Dx,Dy,Dz,Dw);

o53 : Ideal of D

i54 : R=D^1/Delta;

i55 : Rf=DlocalizeAll(R,f,Strategy => Oaku)  

o55 = HashTable{annFS => ideal (Dw, x*Dy + 2y*Dz, 2y*Dx + z*Dy, x*Dx - z*Dz, y*Dy + 2z*Dz - 2s)}
                                         3
                Bfunction => (s + 1)(s + -)
                                         2
                               2
                Boperator => Dy  - 4Dx*Dz
                GeneratorPower => -1
                LocMap => | y2-xz |
                LocModule => cokernel | Dw xDy+2yDz 2yDx+zDy xDx-zDz yDy+2zDz+2 |

o55 : HashTable

i56 : Rfg=DlocalizeAll(Rf.LocModule,g, Strategy => Oaku);
```

---

## d-modules / test.m2 — chunk 7

### Input

```macaulay2
Rfgh=DlocalizeAll(Rfg.LocModule,h, Strategy => Oaku);
Ifgh=ideal relations Rfgh.LocModule;
IH3=Ifgh+ideal(f,g,h);
IH3gb=gens gb IH3
findSocle = method();
findSocle(Ideal, RingElement):= (L,P) -> (
           createDpairs(ring(L));
           v=(ring L).dpairVars#0;
           myflag = true;
           while myflag do (
                w = apply(v,temp -> temp*P % L);
                if all(w,temp -> temp == 0) then myflag = false
                else (
                     p = position(w, temp -> temp != 0);
                     P = v#p * P;)
                );
           P);
D = ring JH3
findSocle(JH3,1_D)
```

### Output

```
i57 : Rfgh=DlocalizeAll(Rfg.LocModule,h, Strategy => Oaku);

i58 : Ifgh=ideal relations Rfgh.LocModule;

o58 : Ideal of D

i59 : IH3=Ifgh+ideal(f,g,h);

o59 : Ideal of D

i60 : IH3gb=gens gb IH3

o60 = | 1 |

              1      1
o60 : Matrix D  <-- D

i61 : findSocle = method();

i62 : findSocle(Ideal, RingElement):= (L,P) -> (
           createDpairs(ring(L));
           v=(ring L).dpairVars#0;
           myflag = true;
           while myflag do (
                w = apply(v,temp -> temp*P % L);
                if all(w,temp -> temp == 0) then myflag = false
                else (
                     p = position(w, temp -> temp != 0);
                     P = v#p * P;)
                );
           P);

i63 : D = ring JH3

o63 = D

o63 : PolynomialRing, 6 differential variable(s)

i64 : findSocle(JH3,1_D)

o64 = x*v

o64 : D
```

---

## d-modules / test.m2 — chunk 8

### Input

```macaulay2
findLength = method();
findLength Ideal := (I) -> (   
           l = 0;
           while I != ideal 1_(ring I) do (
                l = l + 1;
                s = findSocle(I,1_(ring I));
                I = I + ideal s;);
           l);
findLength JH3
x = symbol x; Dx = symbol Dx;
D = QQ[x_1..x_5, Dx_1..Dx_5, WeylAlgebra =>
           apply(toList(1..5), i -> x_i => Dx_i)];
f = x_1^2 + x_2^2 + x_3^2 + x_4^2 +x_5^2;
g = x_1;
R = D^1/ideal(Dx_1,Dx_2,Dx_3,Dx_4,Dx_5);
```

### Output

```
i65 : findLength = method();

i66 : findLength Ideal := (I) -> (   
           l = 0;
           while I != ideal 1_(ring I) do (
                l = l + 1;
                s = findSocle(I,1_(ring I));
                I = I + ideal s;);
           l);

i67 : findLength JH3

o67 = 1

i68 : x = symbol x; Dx = symbol Dx;

i70 : D = QQ[x_1..x_5, Dx_1..Dx_5, WeylAlgebra =>
           apply(toList(1..5), i -> x_i => Dx_i)];

i71 : f = x_1^2 + x_2^2 + x_3^2 + x_4^2 +x_5^2;

i72 : g = x_1;

i73 : R = D^1/ideal(Dx_1,Dx_2,Dx_3,Dx_4,Dx_5);
```

---

## d-modules / test.m2 — chunk 9

### Input

```macaulay2
Rf =DlocalizeAll(R,f,Strategy => Oaku);
Bf = Rf.Bfunction
Rfg = DlocalizeAll(Rf.LocModule,g,Strategy => Oaku);
Bfg = Rfg.Bfunction
Rg = DlocalizeAll(R,g,Strategy => Oaku);
Bg = Rg.Bfunction
Rgf = DlocalizeAll(Rg.LocModule,f,Strategy => Oaku);
Bgf = Rgf.Bfunction
```

### Output

```
i74 : Rf =DlocalizeAll(R,f,Strategy => Oaku);

i75 : Bf = Rf.Bfunction

5
o75 = (s + 1)(s + -)
                  2

o75 : Expression of class Product

i76 : Rfg = DlocalizeAll(Rf.LocModule,g,Strategy => Oaku);

i77 : Bfg = Rfg.Bfunction

o77 = (s + 1)(s + 3)

o77 : Expression of class Product

i78 : Rg = DlocalizeAll(R,g,Strategy => Oaku);

i79 : Bg = Rg.Bfunction

o79 = (s + 1)

o79 : Expression of class Product

i80 : Rgf = DlocalizeAll(Rg.LocModule,f,Strategy => Oaku);

i81 : Bgf = Rgf.Bfunction

5
o81 = (s + 1)(s + 2)(s + -)
                         2

o81 : Expression of class Product
```

---

## d-modules / test.m2 — chunk 10

### Input

```macaulay2
x = symbol x;
R = QQ[x,y,z];
f=x^3+y^3+z^3;
H=deRhamAll(f);
H.CohomologyGroups
H.LocalizeMap
H.TransferCycles
I = gkz(matrix{{1,2}}, {5})
```

### Output

```
i82 : x = symbol x;

i83 : R = QQ[x,y,z];

i84 : f=x^3+y^3+z^3;

i85 : H=deRhamAll(f);

i86 : H.CohomologyGroups

1
o86 = HashTable{0 => QQ }
                       1
                1 => QQ
                       2
                2 => QQ
                       2
                3 => QQ

o86 : HashTable

i87 : H.LocalizeMap

o87 = | x_1^6+2x_1^3x_2^3+x_2^6+2x_1^3x_3^3+2x_2^3x_3^3+x_3^6 |

o87 : Matrix

i88 : H.TransferCycles

o88 = HashTable{0 => | 4/3x_1^6+8/3x_1^3x_2^3+4/3x_2^6+8/3x_1^3x_3^3+8/3x_2^3x_3^3+4/3x_3^6 |}
                1 => | 20x_1^5+20x_1^2x_2^3+20x_1^2x_3^3  |
                     | -20x_1^3x_2^2-20x_2^5-20x_2^2x_3^3 |
                     | 20x_1^3x_3^2+20x_2^3x_3^2+20x_3^5  |
                2 => | 48x_1x_2x_3^2 600x_3^4    |
                     | 48x_1x_2^2x_3 600x_2x_3^3 |
                     | 48x_1^2x_2x_3 600x_1x_3^3 |
                3 => | -x_1x_2x_3 -x_3^3 |

o88 : HashTable

i89 : I = gkz(matrix{{1,2}}, {5})

2
o89 = ideal (x D  + 2x D  - 5, D  - D )
              1 1     2 2       1    2

o89 : Ideal of QQ[x ..x , D ..D ]
                   1   2   1   2
```

---

## d-modules / test.m2 — chunk 11

### Input

```macaulay2
PolySols I
i91 :
```

### Output

```
i90 : PolySols I

5      3          2
o90 = {x  + 20x x  + 60x x }
        1      1 2      1 2

o90 : List

i91 :
```

---

## exterior-algebra / chapter.m2 — chunk 0

### Input

```macaulay2
symExt = (m,E) ->(
          ev := map(E,ring m,vars E);
          mt := transpose jacobian m;
          jn := gens kernel mt;
          q  := vars(ring m)**id_(target m);
          ans:= transpose ev(q*jn);
          --now correct the degrees:
          map(E^{(rank target ans):1}, E^{(rank source ans):0}, 
              ans));
S=ZZ/32003[x_0..x_2];
E=ZZ/32003[e_0..e_2,SkewCommutative=>true];
M=coker matrix{{x_0^2, x_1^2}};
m=presentation truncate(regularity M,M);
symExt(m,E)
bgg = (i,M,E) ->(
          S :=ring(M);
          numvarsE := rank source vars E;
          ev:=map(E,S,vars E);
          f0:=basis(i,M);
          f1:=basis(i+1,M);
          g :=((vars S)**f0)//f1;
          b:=(ev g)*((transpose vars E)**(ev source f0));
          --correct the degrees (which are otherwise
          --wrong in the transpose)
          map(E^{(rank target b):i+1},E^{(rank source b):i}, b));
M=cokernel matrix{{x_0^2, x_1^2, x_2^2}};
```

### Output

```
i1 : symExt = (m,E) ->(
          ev := map(E,ring m,vars E);
          mt := transpose jacobian m;
          jn := gens kernel mt;
          q  := vars(ring m)**id_(target m);
          ans:= transpose ev(q*jn);
          --now correct the degrees:
          map(E^{(rank target ans):1}, E^{(rank source ans):0}, 
              ans));

i2 : S=ZZ/32003[x_0..x_2];

i3 : E=ZZ/32003[e_0..e_2,SkewCommutative=>true];

i4 : M=coker matrix{{x_0^2, x_1^2}};

i5 : m=presentation truncate(regularity M,M);

4       8
o5 : Matrix S  <--- S

i6 : symExt(m,E)

o6 = {-1} | e_2 e_1 e_0 0   |
     {-1} | 0   e_2 0   e_0 |
     {-1} | 0   0   e_2 e_1 |
     {-1} | 0   0   0   e_2 |

             4       4
o6 : Matrix E  <--- E

i7 : bgg = (i,M,E) ->(
          S :=ring(M);
          numvarsE := rank source vars E;
          ev:=map(E,S,vars E);
          f0:=basis(i,M);
          f1:=basis(i+1,M);
          g :=((vars S)**f0)//f1;
          b:=(ev g)*((transpose vars E)**(ev source f0));
          --correct the degrees (which are otherwise
          --wrong in the transpose)
          map(E^{(rank target b):i+1},E^{(rank source b):i}, b));

i8 : M=cokernel matrix{{x_0^2, x_1^2, x_2^2}};
```

---

## exterior-algebra / chapter.m2 — chunk 1

### Input

```macaulay2
bgg(1,M,E)
tateResolution = (m,E,loDeg,hiDeg)->(
           M := coker m;
           reg := regularity M;
           bnd := max(reg+1,hiDeg-1);
           mt  := presentation truncate(bnd,M);
           o   := symExt(mt,E);
           --adjust degrees, since symExt forgets them
           ofixed   :=  map(E^{(rank target o):bnd+1},
                      E^{(rank source o):bnd},
                      o);
           res(coker ofixed, LengthLimit=>max(1,bnd-loDeg+1)));
m = matrix{{x_0,x_1}};
regularity coker m
T = tateResolution(m,E,-2,4)
betti T
T.dd_1
sheafCohomology = (m,E,loDeg,hiDeg)->(
           T := tateResolution(m,E,loDeg,hiDeg);
           k := length T;
           d := k-hiDeg+loDeg;
           if d > 0 then 
              chainComplex apply(d+1 .. k, i->T.dd_(i))
           else T);
```

### Output

```
i9 : bgg(1,M,E)

o9 = {-2} | e_1 e_0 0   |
     {-2} | e_2 0   e_0 |
     {-2} | 0   e_2 e_1 |

             3       3
o9 : Matrix E  <--- E

i10 : tateResolution = (m,E,loDeg,hiDeg)->(
           M := coker m;
           reg := regularity M;
           bnd := max(reg+1,hiDeg-1);
           mt  := presentation truncate(bnd,M);
           o   := symExt(mt,E);
           --adjust degrees, since symExt forgets them
           ofixed   :=  map(E^{(rank target o):bnd+1},
                      E^{(rank source o):bnd},
                      o);
           res(coker ofixed, LengthLimit=>max(1,bnd-loDeg+1)));

i11 : m = matrix{{x_0,x_1}};

1       2
o11 : Matrix S  <--- S

i12 : regularity coker m

o12 = 0

i13 : T = tateResolution(m,E,-2,4)

1      1      1      1      1      1      1
o13 = E  <-- E  <-- E  <-- E  <-- E  <-- E  <-- E
                                                 
      0      1      2      3      4      5      6

o13 : ChainComplex

i14 : betti T

o14 = total: 1 1 1 1 1 1 1
         -4: 1 1 1 1 1 1 1

i15 : T.dd_1

o15 = {-4} | e_2 |

              1       1
o15 : Matrix E  <--- E

i16 : sheafCohomology = (m,E,loDeg,hiDeg)->(
           T := tateResolution(m,E,loDeg,hiDeg);
           k := length T;
           d := k-hiDeg+loDeg;
           if d > 0 then 
              chainComplex apply(d+1 .. k, i->T.dd_(i))
           else T);
```

---

## exterior-algebra / chapter.m2 — chunk 2

### Input

```macaulay2
S=ZZ/32003[x_0..x_3];
E=ZZ/32003[e_0..e_3,SkewCommutative=>true];
m=koszul(3,vars S);
regularity coker m
betti tateResolution(m,E,-6,2)
betti sheafCohomology(m,E,-6,2)
M=sheaf coker m;
HH^1(M(>=0))
```

### Output

```
i17 : S=ZZ/32003[x_0..x_3];

i18 : E=ZZ/32003[e_0..e_3,SkewCommutative=>true];

i19 : m=koszul(3,vars S);

6       4
o19 : Matrix S  <--- S

i20 : regularity coker m

o20 = 2

i21 : betti tateResolution(m,E,-6,2)

o21 = total: 45 20 6 1 4 15 36 70 120 189 280
         -4: 45 20 6 . .  .  .  .   .   .   .
         -3:  .  . . 1 .  .  .  .   .   .   .
         -2:  .  . . . .  .  .  .   .   .   .
         -1:  .  . . . 4 15 36 70 120 189 280

i22 : betti sheafCohomology(m,E,-6,2)

o22 = total: 6 1 4 15 36 70 120 189 280
         -2: 6 . .  .  .  .   .   .   .
         -1: . 1 .  .  .  .   .   .   .
          0: . . .  .  .  .   .   .   .
          1: . . 4 15 36 70 120 189 280

i23 : M=sheaf coker m;

i24 : HH^1(M(>=0))

o24 = cokernel | x_3 x_2 x_1 x_0 |

                             1
o24 : S-module, quotient of S
```

---

## exterior-algebra / chapter.m2 — chunk 3

### Input

```macaulay2
S = ZZ/32003[x_0..x_2];
U = coker koszul(3,vars S) ** S^{1};
k2 = koszul(2,vars S)
alpha = map(U ++ U, S^{-1}, transpose{{0,-1,0,1,0,0}});
alphad = map(S^1, U ++ U, matrix{{0,1,0,0,0,1}} * (k2 ++ k2));
F = prune homology(alphad, alpha);
betti  F
sortedBasis = (i,E) -> (
           m := basis(i,E);
           p := sortColumns(m,MonomialOrder=>Descending);
           m_p);
```

### Output

```
i25 : S = ZZ/32003[x_0..x_2];

i26 : U = coker koszul(3,vars S) ** S^{1};

i27 : k2 = koszul(2,vars S)

o27 = {1} | -x_1 -x_2 0    |
      {1} | x_0  0    -x_2 |
      {1} | 0    x_0  x_1  |

              3       3
o27 : Matrix S  <--- S

i28 : alpha = map(U ++ U, S^{-1}, transpose{{0,-1,0,1,0,0}});

o28 : Matrix

i29 : alphad = map(S^1, U ++ U, matrix{{0,1,0,0,0,1}} * (k2 ++ k2));

o29 : Matrix

i30 : F = prune homology(alphad, alpha);

i31 : betti  F

o31 = relations : total: 3 1
                      1: 2 .
                      2: 1 1

i32 : sortedBasis = (i,E) -> (
           m := basis(i,E);
           p := sortColumns(m,MonomialOrder=>Descending);
           m_p);
```

---

## exterior-algebra / chapter.m2 — chunk 4

### Input

```macaulay2
S=ZZ/32003[x_0..x_3];
E=ZZ/32003[e_0..e_3,SkewCommutative=>true];
koszul(2,vars S)
sortedBasis(2,E)
beilinson1=(e,dege,i,S)->(
           E := ring e;
           mi := if i < 0 or i >= numgens E then map(E^1, E^0, 0)
                 else if i === 0 then id_(E^1)
                 else sortedBasis(i+1,E);
           r := i - dege;
           mr := if r < 0 or r >= numgens E then map(E^1, E^0, 0)
                 else sortedBasis(r+1,E);
           s = numgens source mr;
           if i === 0 and r === 0 then
                substitute(map(E^1,E^1,{{e}}),S)
           else if i>0 and r === i then substitute(e*id_(E^s),S)
           else if i > 0 and r === 0 then
                (vars S) * substitute(contract(diff(e,mi),transpose mr),S)
           else substitute(contract(diff(e,mi), transpose mr),S));
beilinson1(e_1,1,3,S)
beilinson1(e_1,1,2,S)
beilinson1(e_1,1,1,S)
```

### Output

```
i33 : S=ZZ/32003[x_0..x_3];

i34 : E=ZZ/32003[e_0..e_3,SkewCommutative=>true];

i35 : koszul(2,vars S)

o35 = {1} | -x_1 -x_2 0    -x_3 0    0    |
      {1} | x_0  0    -x_2 0    -x_3 0    |
      {1} | 0    x_0  x_1  0    0    -x_3 |
      {1} | 0    0    0    x_0  x_1  x_2  |

              4       6
o35 : Matrix S  <--- S

i36 : sortedBasis(2,E)

o36 = | e_0e_1 e_0e_2 e_1e_2 e_0e_3 e_1e_3 e_2e_3 |

              1       6
o36 : Matrix E  <--- E

i37 : beilinson1=(e,dege,i,S)->(
           E := ring e;
           mi := if i < 0 or i >= numgens E then map(E^1, E^0, 0)
                 else if i === 0 then id_(E^1)
                 else sortedBasis(i+1,E);
           r := i - dege;
           mr := if r < 0 or r >= numgens E then map(E^1, E^0, 0)
                 else sortedBasis(r+1,E);
           s = numgens source mr;
           if i === 0 and r === 0 then
                substitute(map(E^1,E^1,{{e}}),S)
           else if i>0 and r === i then substitute(e*id_(E^s),S)
           else if i > 0 and r === 0 then
                (vars S) * substitute(contract(diff(e,mi),transpose mr),S)
           else substitute(contract(diff(e,mi), transpose mr),S));

i38 : beilinson1(e_1,1,3,S)

o38 = {-3} | 0 |
      {-3} | 0 |
      {-3} | 1 |
      {-3} | 0 |

              4       1
o38 : Matrix S  <--- S

i39 : beilinson1(e_1,1,2,S)

o39 = {-2} | 0  0  0 0 |
      {-2} | -1 0  0 0 |
      {-2} | 0  0  0 0 |
      {-2} | 0  -1 0 0 |
      {-2} | 0  0  0 0 |
      {-2} | 0  0  0 1 |

              6       4
o39 : Matrix S  <--- S

i40 : beilinson1(e_1,1,1,S)

o40 = | x_0 0 -x_2 0 -x_3 0 |

              1       6
o40 : Matrix S  <--- S
```

---

## exterior-algebra / chapter.m2 — chunk 5

### Input

```macaulay2
U = (i,S) -> (
           if i < 0 or i >= numgens S then S^0
           else if i === 0 then S^1
           else cokernel koszul(i+2,vars S) ** S^{i});
beilinson = (o,S) -> (
           coldegs := degrees source o;
           rowdegs := degrees target o;
           mats = table(numgens target o, numgens source o,
                    (r,c) -> (
                         rdeg = first rowdegs#r;
                         cdeg = first coldegs#c;
                         overS = beilinson1(o_(r,c),cdeg-rdeg,cdeg,S);
                         -- overS = substitute(overE,S);
                         map(U(rdeg,S),U(cdeg,S),overS)));
           if #mats === 0 then matrix(S,{{}})
           else matrix(mats));
S=ZZ/32003[x_0..x_2];
E = ZZ/32003[e_0..e_2,SkewCommutative=>true];
alphad = map(E^1,E^{-1,-1},{{e_1,e_2}})
alpha = map(E^{-1,-1},E^{-2},{{e_1},{e_2}})
alphad=beilinson(alphad,S);
alpha=beilinson(alpha,S);
```

### Output

```
i41 : U = (i,S) -> (
           if i < 0 or i >= numgens S then S^0
           else if i === 0 then S^1
           else cokernel koszul(i+2,vars S) ** S^{i});

i42 : beilinson = (o,S) -> (
           coldegs := degrees source o;
           rowdegs := degrees target o;
           mats = table(numgens target o, numgens source o,
                    (r,c) -> (
                         rdeg = first rowdegs#r;
                         cdeg = first coldegs#c;
                         overS = beilinson1(o_(r,c),cdeg-rdeg,cdeg,S);
                         -- overS = substitute(overE,S);
                         map(U(rdeg,S),U(cdeg,S),overS)));
           if #mats === 0 then matrix(S,{{}})
           else matrix(mats));

i43 : S=ZZ/32003[x_0..x_2];

i44 : E = ZZ/32003[e_0..e_2,SkewCommutative=>true];

i45 : alphad = map(E^1,E^{-1,-1},{{e_1,e_2}})

o45 = | e_1 e_2 |

              1       2
o45 : Matrix E  <--- E

i46 : alpha = map(E^{-1,-1},E^{-2},{{e_1},{e_2}})

o46 = {1} | e_1 |
      {1} | e_2 |

              2       1
o46 : Matrix E  <--- E

i47 : alphad=beilinson(alphad,S);

o47 : Matrix

i48 : alpha=beilinson(alpha,S);

o48 : Matrix
```

---

## exterior-algebra / chapter.m2 — chunk 6

### Input

```macaulay2
F = prune homology(alphad,alpha);
betti  F
S = ZZ/32003[x_0..x_4];
E = ZZ/32003[e_0..e_4,SkewCommutative=>true];
beta=map(E^1,E^{-2,-1},{{e_0*e_2+e_1*e_3,-e_4}})
alpha=map(E^{-2,-1},E^{-3},{{e_4},{e_0*e_2+e_1*e_3}})
beta=beilinson(beta,S);
alpha=beilinson(alpha,S);
```

### Output

```
i49 : F = prune homology(alphad,alpha);

i50 : betti  F

o50 = relations : total: 3 1
                      1: 2 .
                      2: 1 1

i51 : S = ZZ/32003[x_0..x_4];

i52 : E = ZZ/32003[e_0..e_4,SkewCommutative=>true];

i53 : beta=map(E^1,E^{-2,-1},{{e_0*e_2+e_1*e_3,-e_4}})

o53 = | e_0e_2+e_1e_3 -e_4 |

              1       2
o53 : Matrix E  <--- E

i54 : alpha=map(E^{-2,-1},E^{-3},{{e_4},{e_0*e_2+e_1*e_3}})

o54 = {2} | e_4           |
      {1} | e_0e_2+e_1e_3 |

              2       1
o54 : Matrix E  <--- E

i55 : beta=beilinson(beta,S);

o55 : Matrix

i56 : alpha=beilinson(alpha,S);

o56 : Matrix
```

---

## exterior-algebra / chapter.m2 — chunk 7

### Input

```macaulay2
G = prune homology(beta,alpha);
betti res G
foursect = random(S^4, S^10) * presentation G;
IX = trim minors(4,foursect);
codim IX
degree IX
codim singularLocus IX
alphad = matrix{{e_4*e_1, e_2*e_3},{e_0*e_2, e_3*e_4},
                      {e_1*e_3, e_4*e_0},{e_2*e_4, e_0*e_1},
                      {e_3*e_0, e_1*e_2}};
```

### Output

```
i57 : G = prune homology(beta,alpha);

i58 : betti res G

o58 = total: 10 9 5 1
          1: 10 4 1 .
          2:  . 5 4 1

i59 : foursect = random(S^4, S^10) * presentation G;

4       9
o59 : Matrix S  <--- S

i60 : IX = trim minors(4,foursect);

o60 : Ideal of S

i61 : codim IX

o61 = 2

i62 : degree IX

o62 = 8

i63 : codim singularLocus IX

o63 = 5

i64 : alphad = matrix{{e_4*e_1, e_2*e_3},{e_0*e_2, e_3*e_4},
                      {e_1*e_3, e_4*e_0},{e_2*e_4, e_0*e_1},
                      {e_3*e_0, e_1*e_2}};

5       2
o64 : Matrix E  <--- E
```

---

## exterior-algebra / chapter.m2 — chunk 8

### Input

```macaulay2
alphad=map(E^5,E^{-2,-2},alphad)
alpha=syz alphad
alphad=beilinson(alphad,S);
alpha=beilinson(alpha,S);
FHM = prune homology(alphad,alpha);
betti res FHM
regularity FHM
betti sheafCohomology(presentation FHM,E,-6,6)
```

### Output

```
i65 : alphad=map(E^5,E^{-2,-2},alphad)

o65 = | -e_1e_4 e_2e_3  |
      | e_0e_2  e_3e_4  |
      | e_1e_3  -e_0e_4 |
      | e_2e_4  e_0e_1  |
      | -e_0e_3 e_1e_2  |

              5       2
o65 : Matrix E  <--- E

i66 : alpha=syz alphad

o66 = {2} | e_2e_3 e_0e_4 e_1e_2 -e_3e_4 e_0e_1  |
      {2} | e_1e_4 e_1e_3 e_0e_3 e_0e_2  -e_2e_4 |

              2       5
o66 : Matrix E  <--- E

i67 : alphad=beilinson(alphad,S);

o67 : Matrix

i68 : alpha=beilinson(alpha,S);

o68 : Matrix

i69 : FHM = prune homology(alphad,alpha);

i70 : betti res FHM

o70 = total: 19 35 20 2
          3:  4  .  . .
          4: 15 35 20 .
          5:  .  .  . 2

i71 : regularity FHM

o71 = 5

i72 : betti sheafCohomology(presentation FHM,E,-6,6)

o72 = total: 210 100 37 14 10 5 2 5 10 14 37 100 210
         -6: 210 100 35  4  . . . .  .  .  .   .   .
         -5:   .   .  2 10 10 5 . .  .  .  .   .   .
         -4:   .   .  .  .  . . 2 .  .  .  .   .   .
         -3:   .   .  .  .  . . . 5 10 10  2   .   .
         -2:   .   .  .  .  . . . .  .  4 35 100 210
```

---

## exterior-algebra / chapter.m2 — chunk 9

### Input

```macaulay2
sect =  map(S^1,S^15,0) | random(S^1, S^4);
mapcone = sect || transpose presentation FHM;
fmapcone = res coker mapcone;
IX =  trim ideal fmapcone.dd_2;
codim IX
degree IX
codim singularLocus IX
i80 :
```

### Output

```
i73 : sect =  map(S^1,S^15,0) | random(S^1, S^4);

1       19
o73 : Matrix S  <--- S

i74 : mapcone = sect || transpose presentation FHM;

36       19
o74 : Matrix S   <--- S

i75 : fmapcone = res coker mapcone;

i76 : IX =  trim ideal fmapcone.dd_2;

o76 : Ideal of S

i77 : codim IX

o77 = 2

i78 : degree IX

o78 = 10

i79 : codim singularLocus IX

o79 = 5

i80 :
```

---

## exterior-algebra / test.m2 — chunk 0

### Input

```macaulay2
needsPackage "Truncations";
lineNumber = 0;
setRandomSeed();
 -- initializing random seed
symExt = (m,E) ->(
          ev := map(E,ring m,vars E);
          mt := transpose jacobian m;
          jn := gens kernel mt;
          q  := vars(ring m)**id_(target m);
          ans:= transpose ev(q*jn);
          --now correct the degrees:
          map(E^{(rank target ans):1}, E^{(rank source ans):0}, 
              ans));
S=ZZ/32003[x_0..x_2];
E=ZZ/32003[e_0..e_2,SkewCommutative=>true];
M=coker matrix{{x_0^2, x_1^2}};
m=presentation truncate(regularity M,M);
```

### Output

```
i1 : needsPackage "Truncations";

i2 : lineNumber = 0;

i1 : setRandomSeed();
 -- initializing random seed

i2 : symExt = (m,E) ->(
          ev := map(E,ring m,vars E);
          mt := transpose jacobian m;
          jn := gens kernel mt;
          q  := vars(ring m)**id_(target m);
          ans:= transpose ev(q*jn);
          --now correct the degrees:
          map(E^{(rank target ans):1}, E^{(rank source ans):0}, 
              ans));

i3 : S=ZZ/32003[x_0..x_2];

i4 : E=ZZ/32003[e_0..e_2,SkewCommutative=>true];

i5 : M=coker matrix{{x_0^2, x_1^2}};

i6 : m=presentation truncate(regularity M,M);

4      8
o6 : Matrix S  <-- S
```

---

## exterior-algebra / test.m2 — chunk 1

### Input

```macaulay2
symExt(m,E)
bgg = (i,M,E) ->(
          S :=ring(M);
          numvarsE := rank source vars E;
          ev:=map(E,S,vars E);
          f0:=basis(i,M);
          f1:=basis(i+1,M);
          g :=((vars S)**f0)//f1;
          b:=(ev g)*((transpose vars E)**(ev source f0));
          --correct the degrees (which are otherwise
          --wrong in the transpose)
          map(E^{(rank target b):i+1},E^{(rank source b):i}, b));
M=cokernel matrix{{x_0^2, x_1^2, x_2^2}};
bgg(1,M,E)
tateResolution = (m,E,loDeg,hiDeg)->(
           M := coker m;
           reg := regularity M;
           bnd := max(reg+1,hiDeg-1);
           mt  := presentation truncate(bnd,M);
           o   := symExt(mt,E);
           --adjust degrees, since symExt forgets them
           ofixed   :=  map(E^{(rank target o):bnd+1},
                      E^{(rank source o):bnd},
                      o);
           res(coker ofixed, LengthLimit=>max(1,bnd-loDeg+1)));
m = matrix{{x_0,x_1}};
regularity coker m
T = tateResolution(m,E,-2,4)
```

### Output

```
i7 : symExt(m,E)

o7 = {-1} | e_2 0   0   0   |
     {-1} | e_1 e_2 0   0   |
     {-1} | e_0 0   e_2 0   |
     {-1} | 0   e_0 e_1 e_2 |

             4      4
o7 : Matrix E  <-- E

i8 : bgg = (i,M,E) ->(
          S :=ring(M);
          numvarsE := rank source vars E;
          ev:=map(E,S,vars E);
          f0:=basis(i,M);
          f1:=basis(i+1,M);
          g :=((vars S)**f0)//f1;
          b:=(ev g)*((transpose vars E)**(ev source f0));
          --correct the degrees (which are otherwise
          --wrong in the transpose)
          map(E^{(rank target b):i+1},E^{(rank source b):i}, b));

i9 : M=cokernel matrix{{x_0^2, x_1^2, x_2^2}};

i10 : bgg(1,M,E)

o10 = {-2} | e_1 e_0 0   |
      {-2} | e_2 0   e_0 |
      {-2} | 0   e_2 e_1 |

              3      3
o10 : Matrix E  <-- E

i11 : tateResolution = (m,E,loDeg,hiDeg)->(
           M := coker m;
           reg := regularity M;
           bnd := max(reg+1,hiDeg-1);
           mt  := presentation truncate(bnd,M);
           o   := symExt(mt,E);
           --adjust degrees, since symExt forgets them
           ofixed   :=  map(E^{(rank target o):bnd+1},
                      E^{(rank source o):bnd},
                      o);
           res(coker ofixed, LengthLimit=>max(1,bnd-loDeg+1)));

i12 : m = matrix{{x_0,x_1}};

1      2
o12 : Matrix S  <-- S

i13 : regularity coker m

o13 = 0

i14 : T = tateResolution(m,E,-2,4)

1      1      1      1      1      1      1
o14 = E  <-- E  <-- E  <-- E  <-- E  <-- E  <-- E
                                                 
      0      1      2      3      4      5      6

o14 : ChainComplex
```

---

## exterior-algebra / test.m2 — chunk 2

### Input

```macaulay2
betti T
T.dd_1
sheafCohomology = (m,E,loDeg,hiDeg)->(
           T := tateResolution(m,E,loDeg,hiDeg);
           k := length T;
           d := k-hiDeg+loDeg;
           if d > 0 then 
              chainComplex apply(d+1 .. k, i->T.dd_(i))
           else T);
S=ZZ/32003[x_0..x_3];
E=ZZ/32003[e_0..e_3,SkewCommutative=>true];
m=koszul(3,vars S);
regularity coker m
betti tateResolution(m,E,-6,2)
```

### Output

```
i15 : betti T

0 1 2 3 4 5 6
o15 = total: 1 1 1 1 1 1 1
         -4: 1 1 1 1 1 1 1

o15 : BettiTally

i16 : T.dd_1

o16 = {-4} | e_2 |

              1      1
o16 : Matrix E  <-- E

i17 : sheafCohomology = (m,E,loDeg,hiDeg)->(
           T := tateResolution(m,E,loDeg,hiDeg);
           k := length T;
           d := k-hiDeg+loDeg;
           if d > 0 then 
              chainComplex apply(d+1 .. k, i->T.dd_(i))
           else T);

i18 : S=ZZ/32003[x_0..x_3];

i19 : E=ZZ/32003[e_0..e_3,SkewCommutative=>true];

i20 : m=koszul(3,vars S);

6      4
o20 : Matrix S  <-- S

i21 : regularity coker m

o21 = 2

i22 : betti tateResolution(m,E,-6,2)

0  1 2 3 4  5  6  7   8   9  10
o22 = total: 45 20 6 1 4 15 36 70 120 189 280
         -4: 45 20 6 . .  .  .  .   .   .   .
         -3:  .  . . 1 .  .  .  .   .   .   .
         -2:  .  . . . .  .  .  .   .   .   .
         -1:  .  . . . 4 15 36 70 120 189 280

o22 : BettiTally
```

---

## exterior-algebra / test.m2 — chunk 3

### Input

```macaulay2
betti sheafCohomology(m,E,-6,2)
M=sheaf coker m;
HH^1(M(>=0))
S = ZZ/32003[x_0..x_2];
U = coker koszul(3,vars S) ** S^{1};
k2 = koszul(2,vars S)
alpha = map(U ++ U, S^{-1}, transpose{{0,-1,0,1,0,0}});
alphad = map(S^1, U ++ U, matrix{{0,1,0,0,0,1}} * (k2 ++ k2));
```

### Output

```
i23 : betti sheafCohomology(m,E,-6,2)

0 1 2  3  4  5   6   7   8
o23 = total: 6 1 4 15 36 70 120 189 280
         -2: 6 . .  .  .  .   .   .   .
         -1: . 1 .  .  .  .   .   .   .
          0: . . .  .  .  .   .   .   .
          1: . . 4 15 36 70 120 189 280

o23 : BettiTally

i24 : M=sheaf coker m;

i25 : HH^1(M(>=0))

o25 = cokernel | x_3 x_2 x_1 x_0 |

                             1
o25 : S-module, quotient of S

i26 : S = ZZ/32003[x_0..x_2];

i27 : U = coker koszul(3,vars S) ** S^{1};

i28 : k2 = koszul(2,vars S)

o28 = {1} | -x_1 -x_2 0    |
      {1} | x_0  0    -x_2 |
      {1} | 0    x_0  x_1  |

              3      3
o28 : Matrix S  <-- S

i29 : alpha = map(U ++ U, S^{-1}, transpose{{0,-1,0,1,0,0}});

o29 : Matrix

i30 : alphad = map(S^1, U ++ U, matrix{{0,1,0,0,0,1}} * (k2 ++ k2));

o30 : Matrix
```

---

## exterior-algebra / test.m2 — chunk 4

### Input

```macaulay2
F = prune homology(alphad, alpha);
betti  F
sortedBasis = (i,E) -> (
           m := basis(i,E);
           p := sortColumns(m,MonomialOrder=>Descending);
           m_p);
S=ZZ/32003[x_0..x_3];
E=ZZ/32003[e_0..e_3,SkewCommutative=>true];
koszul(2,vars S)
sortedBasis(2,E)
beilinson1=(e,dege,i,S)->(
           E := ring e;
           mi := if i < 0 or i >= numgens E then map(E^1, E^0, 0)
                 else if i === 0 then id_(E^1)
                 else sortedBasis(i+1,E);
           r := i - dege;
           mr := if r < 0 or r >= numgens E then map(E^1, E^0, 0)
                 else sortedBasis(r+1,E);
           s = numgens source mr;
           if i === 0 and r === 0 then
                substitute(map(E^1,E^1,{{e}}),S)
           else if i>0 and r === i then substitute(e*id_(E^s),S)
           else if i > 0 and r === 0 then
                (vars S) * substitute(contract(diff(e,mi),transpose mr),S)
           else substitute(contract(diff(e,mi), transpose mr),S));
```

### Output

```
i31 : F = prune homology(alphad, alpha);

i32 : betti  F

0 1
o32 = total: 3 1
          1: 2 .
          2: 1 1

o32 : BettiTally

i33 : sortedBasis = (i,E) -> (
           m := basis(i,E);
           p := sortColumns(m,MonomialOrder=>Descending);
           m_p);

i34 : S=ZZ/32003[x_0..x_3];

i35 : E=ZZ/32003[e_0..e_3,SkewCommutative=>true];

i36 : koszul(2,vars S)

o36 = {1} | -x_1 -x_2 0    -x_3 0    0    |
      {1} | x_0  0    -x_2 0    -x_3 0    |
      {1} | 0    x_0  x_1  0    0    -x_3 |
      {1} | 0    0    0    x_0  x_1  x_2  |

              4      6
o36 : Matrix S  <-- S

i37 : sortedBasis(2,E)

o37 = | e_0e_1 e_0e_2 e_1e_2 e_0e_3 e_1e_3 e_2e_3 |

              1      6
o37 : Matrix E  <-- E

i38 : beilinson1=(e,dege,i,S)->(
           E := ring e;
           mi := if i < 0 or i >= numgens E then map(E^1, E^0, 0)
                 else if i === 0 then id_(E^1)
                 else sortedBasis(i+1,E);
           r := i - dege;
           mr := if r < 0 or r >= numgens E then map(E^1, E^0, 0)
                 else sortedBasis(r+1,E);
           s = numgens source mr;
           if i === 0 and r === 0 then
                substitute(map(E^1,E^1,{{e}}),S)
           else if i>0 and r === i then substitute(e*id_(E^s),S)
           else if i > 0 and r === 0 then
                (vars S) * substitute(contract(diff(e,mi),transpose mr),S)
           else substitute(contract(diff(e,mi), transpose mr),S));
```

---

## exterior-algebra / test.m2 — chunk 5

### Input

```macaulay2
beilinson1(e_1,1,3,S)
beilinson1(e_1,1,2,S)
beilinson1(e_1,1,1,S)
U = (i,S) -> (
           if i < 0 or i >= numgens S then S^0
           else if i === 0 then S^1
           else cokernel koszul(i+2,vars S) ** S^{i});
beilinson = (o,S) -> (
           coldegs := degrees source o;
           rowdegs := degrees target o;
           mats = table(numgens target o, numgens source o,
                    (r,c) -> (
                         rdeg = first rowdegs#r;
                         cdeg = first coldegs#c;
                         overS = beilinson1(o_(r,c),cdeg-rdeg,cdeg,S);
                         -- overS = substitute(overE,S);
                         map(U(rdeg,S),U(cdeg,S),overS)));
           if #mats === 0 then matrix(S,{{}})
           else matrix(mats));
S=ZZ/32003[x_0..x_2];
E = ZZ/32003[e_0..e_2,SkewCommutative=>true];
alphad = map(E^1,E^{-1,-1},{{e_1,e_2}})
```

### Output

```
i39 : beilinson1(e_1,1,3,S)

o39 = {-3} | 0  |
      {-3} | 0  |
      {-3} | -1 |
      {-3} | 0  |

              4      1
o39 : Matrix S  <-- S

i40 : beilinson1(e_1,1,2,S)

o40 = {-2} | 0 0 0 0  |
      {-2} | 1 0 0 0  |
      {-2} | 0 0 0 0  |
      {-2} | 0 1 0 0  |
      {-2} | 0 0 0 0  |
      {-2} | 0 0 0 -1 |

              6      4
o40 : Matrix S  <-- S

i41 : beilinson1(e_1,1,1,S)

o41 = | x_0 0 -x_2 0 -x_3 0 |

              1      6
o41 : Matrix S  <-- S

i42 : U = (i,S) -> (
           if i < 0 or i >= numgens S then S^0
           else if i === 0 then S^1
           else cokernel koszul(i+2,vars S) ** S^{i});

i43 : beilinson = (o,S) -> (
           coldegs := degrees source o;
           rowdegs := degrees target o;
           mats = table(numgens target o, numgens source o,
                    (r,c) -> (
                         rdeg = first rowdegs#r;
                         cdeg = first coldegs#c;
                         overS = beilinson1(o_(r,c),cdeg-rdeg,cdeg,S);
                         -- overS = substitute(overE,S);
                         map(U(rdeg,S),U(cdeg,S),overS)));
           if #mats === 0 then matrix(S,{{}})
           else matrix(mats));

i44 : S=ZZ/32003[x_0..x_2];

i45 : E = ZZ/32003[e_0..e_2,SkewCommutative=>true];

i46 : alphad = map(E^1,E^{-1,-1},{{e_1,e_2}})

o46 = | e_1 e_2 |

              1      2
o46 : Matrix E  <-- E
```

---

## exterior-algebra / test.m2 — chunk 6

### Input

```macaulay2
alpha = map(E^{-1,-1},E^{-2},{{e_1},{e_2}})
alphad=beilinson(alphad,S);
alpha=beilinson(alpha,S);
F = prune homology(alphad,alpha);
betti  F
S = ZZ/32003[x_0..x_4];
E = ZZ/32003[e_0..e_4,SkewCommutative=>true];
beta=map(E^1,E^{-2,-1},{{e_0*e_2+e_1*e_3,-e_4}})
```

### Output

```
i47 : alpha = map(E^{-1,-1},E^{-2},{{e_1},{e_2}})

o47 = {1} | e_1 |
      {1} | e_2 |

              2      1
o47 : Matrix E  <-- E

i48 : alphad=beilinson(alphad,S);

o48 : Matrix

i49 : alpha=beilinson(alpha,S);

o49 : Matrix

i50 : F = prune homology(alphad,alpha);

i51 : betti  F

0 1
o51 = total: 3 1
          1: 2 .
          2: 1 1

o51 : BettiTally

i52 : S = ZZ/32003[x_0..x_4];

i53 : E = ZZ/32003[e_0..e_4,SkewCommutative=>true];

i54 : beta=map(E^1,E^{-2,-1},{{e_0*e_2+e_1*e_3,-e_4}})

o54 = | e_0e_2+e_1e_3 -e_4 |

              1      2
o54 : Matrix E  <-- E
```

---

## exterior-algebra / test.m2 — chunk 7

### Input

```macaulay2
alpha=map(E^{-2,-1},E^{-3},{{e_4},{e_0*e_2+e_1*e_3}})
beta=beilinson(beta,S);
alpha=beilinson(alpha,S);
G = prune homology(beta,alpha);
betti res G
foursect = random(S^4, S^10) * presentation G;
IX = trim minors(4,foursect);
codim IX
```

### Output

```
i55 : alpha=map(E^{-2,-1},E^{-3},{{e_4},{e_0*e_2+e_1*e_3}})

o55 = {2} | e_4           |
      {1} | e_0e_2+e_1e_3 |

              2      1
o55 : Matrix E  <-- E

i56 : beta=beilinson(beta,S);

o56 : Matrix

i57 : alpha=beilinson(alpha,S);

o57 : Matrix

i58 : G = prune homology(beta,alpha);

i59 : betti res G

0 1 2 3
o59 = total: 10 9 5 1
          1: 10 4 1 .
          2:  . 5 4 1

o59 : BettiTally

i60 : foursect = random(S^4, S^10) * presentation G;

4      9
o60 : Matrix S  <-- S

i61 : IX = trim minors(4,foursect);

o61 : Ideal of S

i62 : codim IX

o62 = 2
```

---

## exterior-algebra / test.m2 — chunk 8

### Input

```macaulay2
degree IX
codim singularLocus IX
alphad = matrix{{e_4*e_1, e_2*e_3},{e_0*e_2, e_3*e_4},
                      {e_1*e_3, e_4*e_0},{e_2*e_4, e_0*e_1},
                      {e_3*e_0, e_1*e_2}};
alphad=map(E^5,E^{-2,-2},alphad)
alpha=syz alphad
alphad=beilinson(alphad,S);
alpha=beilinson(alpha,S);
FHM = prune homology(alphad,alpha);
```

### Output

```
i63 : degree IX

o63 = 8

i64 : codim singularLocus IX

o64 = 5

i65 : alphad = matrix{{e_4*e_1, e_2*e_3},{e_0*e_2, e_3*e_4},
                      {e_1*e_3, e_4*e_0},{e_2*e_4, e_0*e_1},
                      {e_3*e_0, e_1*e_2}};

5      2
o65 : Matrix E  <-- E

i66 : alphad=map(E^5,E^{-2,-2},alphad)

o66 = | -e_1e_4 e_2e_3  |
      | e_0e_2  e_3e_4  |
      | e_1e_3  -e_0e_4 |
      | e_2e_4  e_0e_1  |
      | -e_0e_3 e_1e_2  |

              5      2
o66 : Matrix E  <-- E

i67 : alpha=syz alphad

o67 = {2} | e_0e_1  e_2e_3 e_0e_4 e_1e_2 -e_3e_4 |
      {2} | -e_2e_4 e_1e_4 e_1e_3 e_0e_3 e_0e_2  |

              2      5
o67 : Matrix E  <-- E

i68 : alphad=beilinson(alphad,S);

o68 : Matrix

i69 : alpha=beilinson(alpha,S);

o69 : Matrix

i70 : FHM = prune homology(alphad,alpha);
```

---

## exterior-algebra / test.m2 — chunk 9

### Input

```macaulay2
betti res FHM
regularity FHM
betti sheafCohomology(presentation FHM,E,-6,6)
-- presentation FHM has the basis elements in the reverse order now
      -- sect =  map(S^1,S^15,0) | random(S^1, S^4);
      sect =  random(S^1, S^4) | map(S^1,S^15,0)
mapcone = sect || transpose presentation FHM;
fmapcone = res coker mapcone;
IX =  trim ideal fmapcone.dd_2;
codim IX
```

### Output

```
i71 : betti res FHM

0  1  2 3
o71 = total: 19 35 20 2
          3:  4  .  . .
          4: 15 35 20 .
          5:  .  .  . 2

o71 : BettiTally

i72 : regularity FHM

o72 = 5

i73 : betti sheafCohomology(presentation FHM,E,-6,6)

0   1  2  3  4 5 6 7  8  9 10  11  12
o73 = total: 210 100 37 14 10 5 2 5 10 14 37 100 210
         -6: 210 100 35  4  . . . .  .  .  .   .   .
         -5:   .   .  2 10 10 5 . .  .  .  .   .   .
         -4:   .   .  .  .  . . 2 .  .  .  .   .   .
         -3:   .   .  .  .  . . . 5 10 10  2   .   .
         -2:   .   .  .  .  . . . .  .  4 35 100 210

o73 : BettiTally

i74 : -- presentation FHM has the basis elements in the reverse order now
      -- sect =  map(S^1,S^15,0) | random(S^1, S^4);
      sect =  random(S^1, S^4) | map(S^1,S^15,0)

o74 = | 5576 4983 5586 -2697 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |

              1      19
o74 : Matrix S  <-- S

i75 : mapcone = sect || transpose presentation FHM;

36      19
o75 : Matrix S   <-- S

i76 : fmapcone = res coker mapcone;

i77 : IX =  trim ideal fmapcone.dd_2;

o77 : Ideal of S

i78 : codim IX

o78 = 2
```

---

## exterior-algebra / test.m2 — chunk 10

### Input

```macaulay2
degree IX
codim singularLocus IX
i81 :
```

### Output

```
i79 : degree IX

o79 = 10

i80 : codim singularLocus IX

o80 = 5

i81 :
```

---

## geometry / chapter.m2 — chunk 0

### Input

```macaulay2
kk = ZZ/32749
ringP3 = kk[x_0..x_3]
ringP1 = kk[s,t]
cubicMap = map(ringP1,ringP3,{s^3, s^2*t, s*t^2, t^3})
idealCubic = kernel cubicMap
idealCubic2 = monomialCurveIdeal(ringP3,{1,2,3})
M = matrix{{x_0,x_1,x_2},{x_1,x_2,x_3}}
idealCubic3 = minors(2, M)
```

### Output

```
i1 : kk = ZZ/32749

o1 = kk

o1 : QuotientRing

i2 : ringP3 = kk[x_0..x_3]

o2 = ringP3

o2 : PolynomialRing

i3 : ringP1 = kk[s,t]

o3 = ringP1

o3 : PolynomialRing

i4 : cubicMap = map(ringP1,ringP3,{s^3, s^2*t, s*t^2, t^3})

3   2      2   3
o4 = map(ringP1,ringP3,{s , s t, s*t , t })

o4 : RingMap ringP1 <--- ringP3

i5 : idealCubic = kernel cubicMap

2                       2
o5 = ideal (x  - x x , x x  - x x , x  - x x )
             2    1 3   1 2    0 3   1    0 2

o5 : Ideal of ringP3

i6 : idealCubic2 = monomialCurveIdeal(ringP3,{1,2,3})

2          2
o6 = ideal (x x  - x x , x  - x x , x  - x x )
             1 2    0 3   2    1 3   1    0 2

o6 : Ideal of ringP3

i7 : M = matrix{{x_0,x_1,x_2},{x_1,x_2,x_3}}

o7 = | x_0 x_1 x_2 |
     | x_1 x_2 x_3 |

                  2            3
o7 : Matrix ringP3  <--- ringP3

i8 : idealCubic3 = minors(2, M)

2                           2
o8 = ideal (- x  + x x , - x x  + x x , - x  + x x )
               1    0 2     1 2    0 3     2    1 3

o8 : Ideal of ringP3
```

---

## geometry / chapter.m2 — chunk 1

### Input

```macaulay2
codim idealCubic
degree idealCubic
dim idealCubic
gens idealCubic
0 == (gens idealCubic)%(gens idealCubic3)
idealCubic == idealCubic3
f = vars ringP3
OmegaP3 = kernel f
```

### Output

```
i9 : codim idealCubic

o9 = 2

i10 : degree idealCubic

o10 = 3

i11 : dim idealCubic

o11 = 2

i12 : gens idealCubic

o12 = | x_2^2-x_1x_3 x_1x_2-x_0x_3 x_1^2-x_0x_2 |

                   1            3
o12 : Matrix ringP3  <--- ringP3

i13 : 0 == (gens idealCubic)%(gens idealCubic3)

o13 = true

i14 : idealCubic == idealCubic3

o14 = true

i15 : f = vars ringP3

o15 = | x_0 x_1 x_2 x_3 |

                   1            4
o15 : Matrix ringP3  <--- ringP3

i16 : OmegaP3 = kernel f

o16 = image {1} | 0    0    0    -x_1 -x_2 -x_3 |
            {1} | 0    -x_2 -x_3 x_0  0    0    |
            {1} | -x_3 x_1  0    0    x_0  0    |
            {1} | x_2  0    x_1  0    0    x_0  |

                                        4
o16 : ringP3-module, submodule of ringP3
```

---

## geometry / chapter.m2 — chunk 2

### Input

```macaulay2
g=generators OmegaP3
OmegaP3=image g
presentation OmegaP3
G = res coker f
G.dd
G.dd_2
degrees source G.dd_2
degrees target G.dd_2
```

### Output

```
i17 : g=generators OmegaP3

o17 = {1} | 0    0    0    -x_1 -x_2 -x_3 |
      {1} | 0    -x_2 -x_3 x_0  0    0    |
      {1} | -x_3 x_1  0    0    x_0  0    |
      {1} | x_2  0    x_1  0    0    x_0  |

                   4            6
o17 : Matrix ringP3  <--- ringP3

i18 : OmegaP3=image g

o18 = image {1} | 0    0    0    -x_1 -x_2 -x_3 |
            {1} | 0    -x_2 -x_3 x_0  0    0    |
            {1} | -x_3 x_1  0    0    x_0  0    |
            {1} | x_2  0    x_1  0    0    x_0  |

                                        4
o18 : ringP3-module, submodule of ringP3

i19 : presentation OmegaP3

o19 = {2} | x_1  0    0    x_0  |
      {2} | x_3  x_0  0    0    |
      {2} | -x_2 0    x_0  0    |
      {2} | 0    x_2  x_3  0    |
      {2} | 0    -x_1 0    x_3  |
      {2} | 0    0    -x_1 -x_2 |

                   6            4
o19 : Matrix ringP3  <--- ringP3

i20 : G = res coker f

1           4           6           4           1
o20 = ringP3  <-- ringP3  <-- ringP3  <-- ringP3  <-- ringP3  <-- 0
                                                                   
      0           1           2           3           4           5

o20 : ChainComplex

i21 : G.dd

1                                4
o21 = 0 : ringP3  <----------------------- ringP3  : 1
                     | x_0 x_1 x_2 x_3 |

                4                                                  6
      1 : ringP3  <----------------------------------------- ringP3  : 2
                     {1} | -x_1 -x_2 0    -x_3 0    0    |
                     {1} | x_0  0    -x_2 0    -x_3 0    |
                     {1} | 0    x_0  x_1  0    0    -x_3 |
                     {1} | 0    0    0    x_0  x_1  x_2  |

                6                                        4
      2 : ringP3  <------------------------------- ringP3  : 3
                     {2} | x_2  x_3  0    0    |
                     {2} | -x_1 0    x_3  0    |
                     {2} | x_0  0    0    x_3  |
                     {2} | 0    -x_1 -x_2 0    |
                     {2} | 0    x_0  0    -x_2 |
                     {2} | 0    0    x_0  x_1  |

                4                         1
      3 : ringP3  <---------------- ringP3  : 4
                     {3} | -x_3 |
                     {3} | x_2  |
                     {3} | -x_1 |
                     {3} | x_0  |

                1
      4 : ringP3  <----- 0 : 5
                     0

o21 : ChainComplexMap

i22 : G.dd_2

o22 = {1} | -x_1 -x_2 0    -x_3 0    0    |
      {1} | x_0  0    -x_2 0    -x_3 0    |
      {1} | 0    x_0  x_1  0    0    -x_3 |
      {1} | 0    0    0    x_0  x_1  x_2  |

                   4            6
o22 : Matrix ringP3  <--- ringP3

i23 : degrees source G.dd_2

o23 = {{2}, {2}, {2}, {2}, {2}, {2}}

o23 : List

i24 : degrees target G.dd_2

o24 = {{1}, {1}, {1}, {1}}

o24 : List
```

---

## geometry / chapter.m2 — chunk 3

### Input

```macaulay2
betti G
m = matrix{{x_0^3, x_1^2, x_2,x_3},{x_1^3,x_2^2,x_3,0}}
I = minors(2,m)
F = res(ringP3^1/I)
betti F
betti G
OmegaP3res = kernel (f ** (ringP3^1/idealCubic))
delta1 = jacobian idealCubic
```

### Output

```
i25 : betti G

o25 = total: 1 4 6 4 1
          0: 1 4 6 4 1

i26 : m = matrix{{x_0^3, x_1^2, x_2,x_3},{x_1^3,x_2^2,x_3,0}}

o26 = | x_0^3 x_1^2 x_2 x_3 |
      | x_1^3 x_2^2 x_3 0   |

                   2            4
o26 : Matrix ringP3  <--- ringP3

i27 : I = minors(2,m)

5    3 2     3      3       3    2      3      2      2
o27 = ideal (- x  + x x , - x x  + x x , - x  + x x , -x x , -x x , -x )
                1    0 2     1 2    0 3     2    1 3    1 3    2 3    3

o27 : Ideal of ringP3

i28 : F = res(ringP3^1/I)

1           6           8           3
o28 = ringP3  <-- ringP3  <-- ringP3  <-- ringP3  <-- 0
                                                       
      0           1           2           3           4

o28 : ChainComplex

i29 : betti F

o29 = total: 1 6 8 3
          0: 1 . . .
          1: . 1 . .
          2: . 2 2 .
          3: . 2 2 .
          4: . 1 4 3

i30 : betti G

o30 = total: 1 4 6 4 1
          0: 1 4 6 4 1

i31 : OmegaP3res = kernel (f ** (ringP3^1/idealCubic))

o31 = subquotient ({1} | -x_3 0    0    -x_2 -x_3 0    -x_1 -x_2 -x_3 |, {1} | x_2^2-x_1x_3 x_1x_2-x_0x_3 x_1^2-x_0x_2 0            0             0            0            0             0            0            0             0            |)
                   {1} | x_2  -x_3 0    x_1  0    -x_3 x_0  0    0    |  {1} | 0            0             0            x_2^2-x_1x_3 x_1x_2-x_0x_3 x_1^2-x_0x_2 0            0             0            0            0             0            |
                   {1} | 0    x_2  -x_3 0    x_1  0    0    x_0  0    |  {1} | 0            0             0            0            0             0            x_2^2-x_1x_3 x_1x_2-x_0x_3 x_1^2-x_0x_2 0            0             0            |
                   {1} | 0    0    x_2  0    0    x_1  0    0    x_0  |  {1} | 0            0             0            0            0             0            0            0             0            x_2^2-x_1x_3 x_1x_2-x_0x_3 x_1^2-x_0x_2 |

                                          4
o31 : ringP3-module, subquotient of ringP3

i32 : delta1 = jacobian idealCubic

o32 = {1} | 0    -x_3 -x_2 |
      {1} | -x_3 x_2  2x_1 |
      {1} | 2x_2 x_1  -x_0 |
      {1} | -x_1 -x_0 0    |

                   4            3
o32 : Matrix ringP3  <--- ringP3
```

---

## geometry / chapter.m2 — chunk 4

### Input

```macaulay2
delta2 = delta1 // (gens OmegaP3res)
delta = map(OmegaP3res, module idealCubic, delta2)
OmegaCubic = prune coker delta
prune HH^0((sheaf OmegaCubic)(>=0))
Cubic = Proj(ringP3/idealCubic)
cotangentSheaf Cubic
ringP4 = kk[x_0..x_4]
idealX = ideal(x_1+x_3, x_2+x_4)
```

### Output

```
i33 : delta2 = delta1 // (gens OmegaP3res)

o33 = {2} | 0  1  0  |
      {2} | 2  0  0  |
      {2} | 0  0  0  |
      {2} | 0  0  2  |
      {2} | 0  1  0  |
      {2} | -1 0  0  |
      {2} | 0  0  0  |
      {2} | 0  0  -1 |
      {2} | 0  -1 0  |

                   9            3
o33 : Matrix ringP3  <--- ringP3

i34 : delta = map(OmegaP3res, module idealCubic, delta2)

o34 = {2} | 0  1  0  |
      {2} | 2  0  0  |
      {2} | 0  0  0  |
      {2} | 0  0  2  |
      {2} | 0  1  0  |
      {2} | -1 0  0  |
      {2} | 0  0  0  |
      {2} | 0  0  -1 |
      {2} | 0  -1 0  |

o34 : Matrix

i35 : OmegaCubic = prune coker delta

o35 = cokernel {2} | -10917x_3 0    -10917x_3 x_2      0        0     0     0     0    x_1   10916x_3 0     -x_0 0     x_0   0        |
               {2} | 0         0    x_2       0        16374x_3 0     0     0     x_1  0     0        0     0    x_0   0     0        |
               {2} | 0         -x_3 0         16373x_3 0        x_2   x_1   0     -x_3 0     0        x_0   0    0     0     16374x_3 |
               {2} | x_3       x_2  0         0        0        0     0     x_1   0    0     0        0     x_0  0     0     0        |
               {2} | 0         0    0         0        0        -2x_3 -2x_2 -2x_3 0    -3x_3 0        -2x_1 x_2  -2x_3 -3x_2 0        |
               {2} | 0         0    0         0        x_2      0     0     0     0    0     x_1      0     0    0     0     x_0      |

                                       6
o35 : ringP3-module, quotient of ringP3

i36 : prune HH^0((sheaf OmegaCubic)(>=0))

o36 = cokernel {1} | 16374x_3 16374x_2 16374x_1 |
               {1} | x_2      x_1      x_0      |

                                       2
o36 : ringP3-module, quotient of ringP3

i37 : Cubic = Proj(ringP3/idealCubic)

o37 = Cubic

o37 : ProjectiveVariety

i38 : cotangentSheaf Cubic

o38 = cokernel {1} | x_2  x_1  x_0  |
               {1} | -x_3 -x_2 -x_1 |

                                                  2
o38 : coherent sheaf on Cubic, quotient of OO      (-1)
                                             Cubic

i39 : ringP4 = kk[x_0..x_4]

o39 = ringP4

o39 : PolynomialRing

i40 : idealX = ideal(x_1+x_3, x_2+x_4)

o40 = ideal (x  + x , x  + x )
              1    3   2    4

o40 : Ideal of ringP4
```

---

## geometry / chapter.m2 — chunk 5

### Input

```macaulay2
idealL1 = ideal(x_1,x_2)
idealL2 = ideal(x_3,x_4)
idealY = intersect(idealL1,idealL2)
degree(idealX+idealY)
degree Tor_0(ringP4^1/idealX, ringP4^1/idealY)
degree Tor_1(ringP4^1/idealX, ringP4^1/idealY)
degree Tor_2(ringP4^1/idealX, ringP4^1/idealY)
res (ringP4^1/idealX)
```

### Output

```
i41 : idealL1 = ideal(x_1,x_2)

o41 = ideal (x , x )
              1   2

o41 : Ideal of ringP4

i42 : idealL2 = ideal(x_3,x_4)

o42 = ideal (x , x )
              3   4

o42 : Ideal of ringP4

i43 : idealY = intersect(idealL1,idealL2)

o43 = ideal (x x , x x , x x , x x )
              2 4   1 4   2 3   1 3

o43 : Ideal of ringP4

i44 : degree(idealX+idealY)

o44 = 3

i45 : degree Tor_0(ringP4^1/idealX, ringP4^1/idealY)

o45 = 3

i46 : degree Tor_1(ringP4^1/idealX, ringP4^1/idealY)

o46 = 1

i47 : degree Tor_2(ringP4^1/idealX, ringP4^1/idealY)

o47 = 0

i48 : res (ringP4^1/idealX)

1           2           1
o48 = ringP4  <-- ringP4  <-- ringP4  <-- 0
                                           
      0           1           2           3

o48 : ChainComplex
```

---

## geometry / chapter.m2 — chunk 6

### Input

```macaulay2
ringP3 = kk[x_0..x_3];
load "mystery.m2"
idealX = mystery ringP3
prettyPrint gens idealX
x_1^4-2*x_0*x_1^2*x_3-x_1^2*x_2*x_3+x_0^2*x_3^2,
x_0^2*x_1^2-10915*x_0*x_1^2*x_2-10917*x_0^3*x_3+10916*x_0^2*x_2*x_3-
   10916*x_0*x_2^2*x_3-10916*x_1*x_3^3,
x_0*x_1^2*x_2^2+11909*x_0^4*x_3+5954*x_0^3*x_2*x_3+2977*x_0^2*x_2^2*x_3+
   11910*x_0*x_2^3*x_3-2978*x_1^3*x_3^2+14887*x_0*x_1*x_3^3+
   11910*x_1*x_2*x_3^3,
x_0*x_1^3*x_2-13099*x_1^3*x_2^2-6550*x_0^3*x_1*x_3-
   13100*x_0^2*x_1*x_2*x_3-6550*x_0*x_1*x_2^2*x_3+13099*x_1*x_2^3*x_3+
   13100*x_1^2*x_3^3+13099*x_0*x_3^4,
x_0^5+5*x_0^2*x_2^3+5*x_0*x_2^4-3*x_0*x_1^3*x_3-4*x_1^3*x_2*x_3+
   4*x_0^2*x_1*x_3^2+10*x_0*x_1*x_2*x_3^2+5*x_1*x_2^2*x_3^2,
x_1^2*x_2^4-8932*x_0^4*x_2*x_3+11909*x_0^3*x_2^2*x_3+5954*x_0^2*x_2^3*x_3-
   8934*x_0*x_2^4*x_3-x_2^5*x_3+2*x_0*x_1^3*x_3^2-5952*x_1^3*x_2*x_3^2-
   x_0^2*x_1*x_3^3-2979*x_0*x_1*x_2*x_3^3-8934*x_1*x_2^2*x_3^3+x_3^6
X = variety idealX
idealX == saturate idealX
dim X
idealXtop = top idealX
```

### Output

```
i49 : ringP3 = kk[x_0..x_3];

i50 : load "mystery.m2"

i51 : idealX = mystery ringP3

4       2      2        2 2   2 2           2           3           2               2             3     2 2         4          3            2 2             3          3 2             3             3     3           3 2        3             2                  2             3           2 3           4   5     2 3       4       3       3         2   2            2       2 2   2 4        4             3 2          2 3            4      5         3 2        3   2    2   3              3          2 3    6
o51 = ideal (x  - 2x x x  - x x x  + x x , x x  - 10915x x x  - 10917x x  + 10916x x x  - 10916x x x  - 10916x x , x x x  + 11909x x  + 5954x x x  + 2977x x x  + 11910x x x  - 2978x x  + 14887x x x  + 11910x x x , x x x  - 13099x x  - 6550x x x  - 13100x x x x  - 6550x x x x  + 13099x x x  + 13100x x  + 13099x x , x  + 5x x  + 5x x  - 3x x x  - 4x x x  + 4x x x  + 10x x x x  + 5x x x , x x  - 8932x x x  + 11909x x x  + 5954x x x  - 8934x x x  - x x  + 2x x x  - 5952x x x  - x x x  - 2979x x x x  - 8934x x x  + x )
              1     0 1 3    1 2 3    0 3   0 1         0 1 2         0 3         0 2 3         0 2 3         1 3   0 1 2         0 3        0 2 3        0 2 3         0 2 3        1 3         0 1 3         1 2 3   0 1 2         1 2        0 1 3         0 1 2 3        0 1 2 3         1 2 3         1 3         0 3   0     0 2     0 2     0 1 3     1 2 3     0 1 3      0 1 2 3     1 2 3   1 2        0 2 3         0 2 3        0 2 3        0 2 3    2 3     0 1 3        1 2 3    0 1 3        0 1 2 3        1 2 3    3

o51 : Ideal of ringP3

i52 : prettyPrint gens idealX
x_1^4-2*x_0*x_1^2*x_3-x_1^2*x_2*x_3+x_0^2*x_3^2,
x_0^2*x_1^2-10915*x_0*x_1^2*x_2-10917*x_0^3*x_3+10916*x_0^2*x_2*x_3-
   10916*x_0*x_2^2*x_3-10916*x_1*x_3^3,
x_0*x_1^2*x_2^2+11909*x_0^4*x_3+5954*x_0^3*x_2*x_3+2977*x_0^2*x_2^2*x_3+
   11910*x_0*x_2^3*x_3-2978*x_1^3*x_3^2+14887*x_0*x_1*x_3^3+
   11910*x_1*x_2*x_3^3,
x_0*x_1^3*x_2-13099*x_1^3*x_2^2-6550*x_0^3*x_1*x_3-
   13100*x_0^2*x_1*x_2*x_3-6550*x_0*x_1*x_2^2*x_3+13099*x_1*x_2^3*x_3+
   13100*x_1^2*x_3^3+13099*x_0*x_3^4,
x_0^5+5*x_0^2*x_2^3+5*x_0*x_2^4-3*x_0*x_1^3*x_3-4*x_1^3*x_2*x_3+
   4*x_0^2*x_1*x_3^2+10*x_0*x_1*x_2*x_3^2+5*x_1*x_2^2*x_3^2,
x_1^2*x_2^4-8932*x_0^4*x_2*x_3+11909*x_0^3*x_2^2*x_3+5954*x_0^2*x_2^3*x_3-
   8934*x_0*x_2^4*x_3-x_2^5*x_3+2*x_0*x_1^3*x_3^2-5952*x_1^3*x_2*x_3^2-
   x_0^2*x_1*x_3^3-2979*x_0*x_1*x_2*x_3^3-8934*x_1*x_2^2*x_3^3+x_3^6

i53 : X = variety idealX

o53 = X

o53 : ProjectiveVariety

i54 : idealX == saturate idealX

o54 = true

i55 : dim X

o55 = 1

i56 : idealXtop = top idealX

4       2      2        2 2   2 2           2           3           2               2             3     2 2         4          3            2 2             3          3 2             3             3     3           3 2        3             2                  2             3           2 3           4   5     2 3       4       3       3         2   2            2       2 2   2 4        4             3 2          2 3            4      5         3 2        3   2    2   3              3          2 3    6
o56 = ideal (x  - 2x x x  - x x x  + x x , x x  - 10915x x x  - 10917x x  + 10916x x x  - 10916x x x  - 10916x x , x x x  + 11909x x  + 5954x x x  + 2977x x x  + 11910x x x  - 2978x x  + 14887x x x  + 11910x x x , x x x  - 13099x x  - 6550x x x  - 13100x x x x  - 6550x x x x  + 13099x x x  + 13100x x  + 13099x x , x  + 5x x  + 5x x  - 3x x x  - 4x x x  + 4x x x  + 10x x x x  + 5x x x , x x  - 8932x x x  + 11909x x x  + 5954x x x  - 8934x x x  - x x  + 2x x x  - 5952x x x  - x x x  - 2979x x x x  - 8934x x x  + x )
              1     0 1 3    1 2 3    0 3   0 1         0 1 2         0 3         0 2 3         0 2 3         1 3   0 1 2         0 3        0 2 3        0 2 3         0 2 3        1 3         0 1 3         1 2 3   0 1 2         1 2        0 1 3         0 1 2 3        0 1 2 3         1 2 3         1 3         0 3   0     0 2     0 2     0 1 3     1 2 3     0 1 3      0 1 2 3     1 2 3   1 2        0 2 3         0 2 3        0 2 3        0 2 3    2 3     0 1 3        1 2 3    0 1 3        0 1 2 3        1 2 3    3

o56 : Ideal of ringP3
```

---

## geometry / chapter.m2 — chunk 7

### Input

```macaulay2
(gens idealXtop)%(gens idealX) == 0
codim singularLocus idealX
# decompose idealX
HH^0 OO_X
rank oo
HH^1 OO_X
degree idealX
P3 = Proj ringP3
```

### Output

```
i57 : (gens idealXtop)%(gens idealX) == 0

o57 = true

i58 : codim singularLocus idealX

o58 = 4

i59 : # decompose idealX

o59 = 1

i60 : HH^0 OO_X

1
o60 = kk

o60 : kk-module, free

i61 : rank oo

o61 = 1

i62 : HH^1 OO_X

6
o62 = kk

o62 : kk-module, free

i63 : degree idealX

o63 = 10

i64 : P3 = Proj ringP3

o64 = P3

o64 : ProjectiveVariety
```

---

## geometry / chapter.m2 — chunk 8

### Input

```macaulay2
HH^1((OO_P3(1)/idealX)(>=0))
degrees oo
omegaX = Ext^(codim idealX)(ringP3^1/idealX, ringP3^{-4})
dualModule = Hom(omegaX, ringP3^1/idealX)
betti prune dualModule
f = homomorphism dualModule_{0}
canGens = f*basis(0,omegaX)
ringX = ringP3/idealX
```

### Output

```
i65 : HH^1((OO_P3(1)/idealX)(>=0))

o65 = cokernel | x_3 x_2 x_1 x_0 |

                                       1
o65 : ringP3-module, quotient of ringP3

i66 : degrees oo

o66 = {{0}}

o66 : List

i67 : omegaX = Ext^(codim idealX)(ringP3^1/idealX, ringP3^{-4})

o67 = cokernel {0}  | 9359x_3           -4677x_3         -10105x_1         -13636x_1x_2                    5460x_0^2+10920x_0x_2+2184x_2^2            -15942x_0^2+1388x_0x_2-6063x_2^2              |
               {0}  | 12014x_1          2552x_1          2626x_0           13438x_0^2-8515x_0x_2-6719x_2^2 -1364x_3^2                                 11524x_3^2                                    |
               {-1} | x_0x_3-2553x_2x_3 x_1^2-1702x_2x_3 x_0x_1-8086x_1x_2 x_1x_2^2-11925x_3^3             x_0^3+14737x_0^2x_2-8626x_0x_2^2-9388x_2^3 x_0^2x_2-15006x_0x_2^2+8248x_2^3+3876x_1x_3^2 |

                                       3
o67 : ringP3-module, quotient of ringP3

i68 : dualModule = Hom(omegaX, ringP3^1/idealX)

o68 = subquotient ({0} | x_0^3x_2^2+10915x_0^2x_2^3+807x_0x_2^4+4043x_2^5+7655x_0x_1x_2x_3^2-15561x_1x_2^2x_3^2-14150x_3^5                x_1^2x_2^2+10887x_0^2x_2x_3-16279x_0x_2^2x_3-10556x_2^3x_3-7591x_1x_3^3 -1488x_1^2x_3^2+5359x_0x_3^3-14291x_2x_3^3                                                     x_0^4+10915x_0^3x_2+807x_0^2x_2^2+4043x_0x_2^3+4850x_0x_1x_3^2+4043x_1x_2x_3^2 x_0^3x_1+13548x_0x_1x_2^2+4124x_1x_2^3-6356x_1^2x_3^2+12615x_0x_3^3-13828x_2x_3^3 2732x_0^3x_2+5356x_0^2x_2^2+2224x_0x_2^3-13255x_0x_1x_3^2+2224x_1x_2x_3^2 x_0^2x_1x_2-15006x_0x_1x_2^2+8248x_1x_2^3+3876x_1^2x_3^2-7519x_0x_3^3+5093x_2x_3^3 x_0x_1^2-8086x_1^2x_2-9301x_0^2x_3+2428x_0x_2x_3 x_1^3-8565x_0x_1x_3-11589x_1x_2x_3 -8169x_1^2x_2+6498x_0^2x_3+3416x_0x_2x_3 |, {0} | 0                                         x_1^4-2x_0x_1^2x_3-x_1^2x_2x_3+x_0^2x_3^2 0                                                                                         x_0^2x_1^2-10915x_0x_1^2x_2-10917x_0^3x_3+10916x_0^2x_2x_3-10916x_0x_2^2x_3-10916x_1x_3^3 0                                         0                                                                                         0                                                                                                                               x_0x_1^2x_2^2+11909x_0^4x_3+5954x_0^3x_2x_3+2977x_0^2x_2^2x_3+11910x_0x_2^3x_3-2978x_1^3x_3^2+14887x_0x_1x_3^3+11910x_1x_2x_3^3 0                                                                                                                                 x_0x_1^3x_2-13099x_1^3x_2^2-6550x_0^3x_1x_3-13100x_0^2x_1x_2x_3-6550x_0x_1x_2^2x_3+13099x_1x_2^3x_3+13100x_1^2x_3^3+13099x_0x_3^4 0                                                                                                    x_0^5+5x_0^2x_2^3+5x_0x_2^4-3x_0x_1^3x_3-4x_1^3x_2x_3+4x_0^2x_1x_3^2+10x_0x_1x_2x_3^2+5x_1x_2^2x_3^2 0                                                                                                                               0                                                                                                                                 0                                                                                                    0                                                                                                                                                                                  x_1^2x_2^4-8932x_0^4x_2x_3+11909x_0^3x_2^2x_3+5954x_0^2x_2^3x_3-8934x_0x_2^4x_3-x_2^5x_3+2x_0x_1^3x_3^2-5952x_1^3x_2x_3^2-x_0^2x_1x_3^3-2979x_0x_1x_2x_3^3-8934x_1x_2^2x_3^3+x_3^6 0                                                                                                                                                                                  |)
                   {0} | 10105x_0x_1x_2^3+6063x_1x_2^4+11820x_0x_1^2x_3^2+1305x_1^2x_2x_3^2-2394x_0^2x_3^3-1037x_0x_2x_3^3+4042x_2^2x_3^3 15208x_0^2x_1x_3+9361x_0x_1x_2x_3-11900x_1x_2^2x_3+16016x_3^4           x_0^2x_1^2+6549x_1^2x_2^2-13100x_0^3x_3+6550x_0^2x_2x_3-13099x_0x_2^2x_3-6549x_2^3x_3+x_1x_3^3 10105x_0^2x_1x_2+6063x_0x_1x_2^2+6063x_1^2x_3^2                                11887x_0^3x_3+5058x_0^2x_2x_3+13757x_0x_2^2x_3+2912x_2^3x_3+6238x_1x_3^3          x_0^3x_1+13748x_0^2x_1x_2-4856x_0x_1x_2^2-4848x_1^2x_3^2                  -8975x_0^3x_3+762x_0^2x_2x_3+8802x_0x_2^2x_3+5824x_2^3x_3-6236x_1x_3^3             2021x_0x_1x_3-12126x_1x_2x_3                     6048x_1^2x_3-4032x_0x_3^2          x_1^3+9299x_0x_1x_3+9700x_1x_2x_3        |  {0} | x_1^4-2x_0x_1^2x_3-x_1^2x_2x_3+x_0^2x_3^2 0                                         x_0^2x_1^2-10915x_0x_1^2x_2-10917x_0^3x_3+10916x_0^2x_2x_3-10916x_0x_2^2x_3-10916x_1x_3^3 0                                                                                         0                                         0                                                                                         x_0x_1^2x_2^2+11909x_0^4x_3+5954x_0^3x_2x_3+2977x_0^2x_2^2x_3+11910x_0x_2^3x_3-2978x_1^3x_3^2+14887x_0x_1x_3^3+11910x_1x_2x_3^3 0                                                                                                                               x_0x_1^3x_2-13099x_1^3x_2^2-6550x_0^3x_1x_3-13100x_0^2x_1x_2x_3-6550x_0x_1x_2^2x_3+13099x_1x_2^3x_3+13100x_1^2x_3^3+13099x_0x_3^4 0                                                                                                                                 x_0^5+5x_0^2x_2^3+5x_0x_2^4-3x_0x_1^3x_3-4x_1^3x_2x_3+4x_0^2x_1x_3^2+10x_0x_1x_2x_3^2+5x_1x_2^2x_3^2 0                                                                                                    0                                                                                                                               0                                                                                                                                 0                                                                                                    x_1^2x_2^4-8932x_0^4x_2x_3+11909x_0^3x_2^2x_3+5954x_0^2x_2^3x_3-8934x_0x_2^4x_3-x_2^5x_3+2x_0x_1^3x_3^2-5952x_1^3x_2x_3^2-x_0^2x_1x_3^3-2979x_0x_1x_2x_3^3-8934x_1x_2^2x_3^3+x_3^6 0                                                                                                                                                                                  0                                                                                                                                                                                  |
                   {1} | 10105x_0^2x_2^2-11322x_0x_2^3+11322x_2^4+8396x_1^3x_3+788x_0x_1x_3^2+6891x_1x_2x_3^2                             10542x_0x_1^2+8104x_1^2x_2-8522x_0^2x_3+7864x_0x_2x_3+12729x_2^2x_3     -x_3^3                                                                                         10105x_0^3-11322x_0^2x_2+11322x_0x_2^2+11322x_1x_3^2                           -1388x_0^2x_1+8660x_0x_1x_2-13343x_1x_2^2-3640x_3^3                               -2626x_0^3+6868x_0^2x_2-6878x_0x_2^2-6878x_1x_3^2                         15942x_0^2x_1-1388x_0x_1x_2+6063x_1x_2^2-7280x_3^3                                 10105x_1^2+1217x_0x_3                            -5040x_1x_3                        -2626x_1^2+12125x_0x_3                   |  {1} | 0                                         0                                         0                                                                                         0                                                                                         x_1^4-2x_0x_1^2x_3-x_1^2x_2x_3+x_0^2x_3^2 x_0^2x_1^2-10915x_0x_1^2x_2-10917x_0^3x_3+10916x_0^2x_2x_3-10916x_0x_2^2x_3-10916x_1x_3^3 0                                                                                                                               0                                                                                                                               0                                                                                                                                 0                                                                                                                                 0                                                                                                    0                                                                                                    x_0x_1^2x_2^2+11909x_0^4x_3+5954x_0^3x_2x_3+2977x_0^2x_2^2x_3+11910x_0x_2^3x_3-2978x_1^3x_3^2+14887x_0x_1x_3^3+11910x_1x_2x_3^3 x_0x_1^3x_2-13099x_1^3x_2^2-6550x_0^3x_1x_3-13100x_0^2x_1x_2x_3-6550x_0x_1x_2^2x_3+13099x_1x_2^3x_3+13100x_1^2x_3^3+13099x_0x_3^4 x_0^5+5x_0^2x_2^3+5x_0x_2^4-3x_0x_1^3x_3-4x_1^3x_2x_3+4x_0^2x_1x_3^2+10x_0x_1x_2x_3^2+5x_1x_2^2x_3^2 0                                                                                                                                                                                  0                                                                                                                                                                                  x_1^2x_2^4-8932x_0^4x_2x_3+11909x_0^3x_2^2x_3+5954x_0^2x_2^3x_3-8934x_0x_2^4x_3-x_2^5x_3+2x_0x_1^3x_3^2-5952x_1^3x_2x_3^2-x_0^2x_1x_3^3-2979x_0x_1x_2x_3^3-8934x_1x_2^2x_3^3+x_3^6 |

                                          3
o68 : ringP3-module, subquotient of ringP3

i69 : betti prune dualModule

o69 = relations : total: 10 26
                      3:  3  2
                      4:  6 14
                      5:  1  9
                      6:  .  1

i70 : f = homomorphism dualModule_{0}

o70 = | x_0^3x_2^2+10915x_0^2x_2^3+807x_0x_2^4+4043x_2^5+7655x_0x_1x_2x_3^2-15561x_1x_2^2x_3^2-14150x_3^5 10105x_0x_1x_2^3+6063x_1x_2^4+11820x_0x_1^2x_3^2+1305x_1^2x_2x_3^2-2394x_0^2x_3^3-1037x_0x_2x_3^3+4042x_2^2x_3^3 10105x_0^2x_2^2-11322x_0x_2^3+11322x_2^4+8396x_1^3x_3+788x_0x_1x_3^2+6891x_1x_2x_3^2 |

o70 : Matrix

i71 : canGens = f*basis(0,omegaX)

o71 = | x_0^3x_2^2+10915x_0^2x_2^3+807x_0x_2^4+4043x_2^5+7655x_0x_1x_2x_3^2-15561x_1x_2^2x_3^2-14150x_3^5 10105x_0x_1x_2^3+6063x_1x_2^4+11820x_0x_1^2x_3^2+1305x_1^2x_2x_3^2-2394x_0^2x_3^3-1037x_0x_2x_3^3+4042x_2^2x_3^3 10105x_0^3x_2^2-11322x_0^2x_2^3+11322x_0x_2^4+8396x_0x_1^3x_3+788x_0^2x_1x_3^2+6891x_0x_1x_2x_3^2 10105x_0^2x_1x_2^2-11322x_0x_1x_2^3+11322x_1x_2^4-15169x_0x_1^2x_3^2+15287x_1^2x_2x_3^2-8396x_0^2x_3^3 10105x_0^2x_2^3-11322x_0x_2^4+11322x_2^5+8396x_1^3x_2x_3+788x_0x_1x_2x_3^2+6891x_1x_2^2x_3^2 10105x_0^2x_2^2x_3-11322x_0x_2^3x_3+11322x_2^4x_3+8396x_1^3x_3^2+788x_0x_1x_3^3+6891x_1x_2x_3^3 |

o71 : Matrix

i72 : ringX = ringP3/idealX

o72 = ringX

o72 : QuotientRing
```

---

## geometry / chapter.m2 — chunk 9

### Input

```macaulay2
ringP5 = kk[x_0..x_5]
idealXcan = trim kernel map(ringX, ringP5, 
                                     substitute(matrix canGens,ringX),
                                     DegreeMap => i -> 5*i)
betti res idealXcan
deg2places = positions(degrees idealXcan, i->i=={2})
idealS= ideal (gens idealXcan)_deg2places
codim singularLocus idealS
omegaS = Ext^(codim idealS)(ringP5^1/idealS, ringP5^{-6})
OS = ringP5^1/idealS
```

### Output

```
i73 : ringP5 = kk[x_0..x_5]

o73 = ringP5

o73 : PolynomialRing

i74 : idealXcan = trim kernel map(ringX, ringP5, 
                                     substitute(matrix canGens,ringX),
                                     DegreeMap => i -> 5*i)

2                                                                                                                     2                                                                                       2                    2                               2                2                                      2          2       3   3                      2             2           2        3          2           2     2                      2            2          2        3          2          2
o74 = ideal (x  + 5040x x  - 8565x x  - 11589x x , x x  - 6048x x  - 15922x x  + 7357x x , x x  - 4032x x  - 6248x x  - 10379x x , x  + 4032x x  + 14108x x  - 4032x x , x x  - 301x x  - 855x x  - 14291x x  - 10440x x , x  + 7742x x  - 14401x  + 2679x x  + 1764x x  - 11925x , x x x  + 4615x x  - 16374x x x  + 4763x x x  + 930x x  + 9601x x  + 744x , x  - 7549x x x  - 10074x x  + 15120x x  + 14608x x  - 2015x  + 8191x x  - 16372x x , x x  + 10074x x x  - 7307x x  - 7056x x  + 5190x x  - 9976x  - 8189x x  + 5953x x )
              3        0 5        2 5         4 5   1 3        0 5         2 5        4 5   1 2        0 3        2 3         3 4   1        0 5         2 5        4 5   0 1       0 3       2 3         1 4         3 4   0        0 2         2        0 4        2 4         4   0 2 3        2 3         0 3 4        2 3 4       1 4        3 4       5   2        0 2 4         2 4         0 4         2 4        4        1 5         3 5   0 2         0 2 4        2 4        0 4        2 4        4        1 5        3 5

o74 : Ideal of ringP5

i75 : betti res idealXcan

o75 = total: 1 9 16 9 1
          0: 1 .  . . .
          1: . 6  8 3 .
          2: . 3  8 6 .
          3: . .  . . 1

i76 : deg2places = positions(degrees idealXcan, i->i=={2})

o76 = {0, 1, 2, 3, 4, 5}

o76 : List

i77 : idealS= ideal (gens idealXcan)_deg2places

2                                                                                                                     2                                                                                       2                    2                               2
o77 = ideal (x  + 5040x x  - 8565x x  - 11589x x , x x  - 6048x x  - 15922x x  + 7357x x , x x  - 4032x x  - 6248x x  - 10379x x , x  + 4032x x  + 14108x x  - 4032x x , x x  - 301x x  - 855x x  - 14291x x  - 10440x x , x  + 7742x x  - 14401x  + 2679x x  + 1764x x  - 11925x )
              3        0 5        2 5         4 5   1 3        0 5         2 5        4 5   1 2        0 3        2 3         3 4   1        0 5         2 5        4 5   0 1       0 3       2 3         1 4         3 4   0        0 2         2        0 4        2 4         4

o77 : Ideal of ringP5

i78 : codim singularLocus idealS

o78 = 6

i79 : omegaS = Ext^(codim idealS)(ringP5^1/idealS, ringP5^{-6})

o79 = cokernel {2} | 4032x_5  0       14811x_5 -4032x_3    6549x_3      -x_2         x_1-301x_3 x_0+7742x_2-15779x_4 |
               {2} | x_3      x_2     x_1      -x_4        x_0-14291x_4 0            5359x_4    0                    |
               {2} | -6852x_5 6549x_3 362x_5   x_1-6248x_3 0            x_0-14291x_4 -855x_3    -14401x_2-16185x_4   |

                                       3
o79 : ringP5-module, quotient of ringP5

i80 : OS = ringP5^1/idealS

o80 = cokernel | x_3^2+5040x_0x_5-8565x_2x_5-11589x_4x_5 x_1x_3-6048x_0x_5-15922x_2x_5+7357x_4x_5 x_1x_2-4032x_0x_3-6248x_2x_3-10379x_3x_4 x_1^2+4032x_0x_5+14108x_2x_5-4032x_4x_5 x_0x_1-301x_0x_3-855x_2x_3-14291x_1x_4-10440x_3x_4 x_0^2+7742x_0x_2-14401x_2^2+2679x_0x_4+1764x_2x_4-11925x_4^2 |

                                       1
o80 : ringP5-module, quotient of ringP5
```

---

## geometry / chapter.m2 — chunk 10

### Input

```macaulay2
omegaS**omegaS
omega2S = Hom(Hom(omegaS**omegaS, OS),OS)
L = Hom(omegaS, OS**(ringP5^{-1}))
dualModule = Hom(L, OS)
betti generators dualModule
g = homomorphism dualModule_{0}
toP2 = g*basis(0,L)
ringXcan = ringP5/idealXcan
```

### Output

```
i81 : omegaS**omegaS

o81 = cokernel {4} | 4032x_5  0       14811x_5 -4032x_3    6549x_3      -x_2         x_1-301x_3 x_0+7742x_2-15779x_4 0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    4032x_5  0       14811x_5 -4032x_3    6549x_3      -x_2         x_1-301x_3 x_0+7742x_2-15779x_4 0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    |
               {4} | x_3      x_2     x_1      -x_4        x_0-14291x_4 0            5359x_4    0                    0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    4032x_5  0       14811x_5 -4032x_3    6549x_3      -x_2         x_1-301x_3 x_0+7742x_2-15779x_4 0        0       0        0           0            0            0          0                    |
               {4} | -6852x_5 6549x_3 362x_5   x_1-6248x_3 0            x_0-14291x_4 -855x_3    -14401x_2-16185x_4   0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    4032x_5  0       14811x_5 -4032x_3    6549x_3      -x_2         x_1-301x_3 x_0+7742x_2-15779x_4 |
               {4} | 0        0       0        0           0            0            0          0                    4032x_5  0       14811x_5 -4032x_3    6549x_3      -x_2         x_1-301x_3 x_0+7742x_2-15779x_4 0        0       0        0           0            0            0          0                    x_3      x_2     x_1      -x_4        x_0-14291x_4 0            5359x_4    0                    0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    |
               {4} | 0        0       0        0           0            0            0          0                    x_3      x_2     x_1      -x_4        x_0-14291x_4 0            5359x_4    0                    0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    x_3      x_2     x_1      -x_4        x_0-14291x_4 0            5359x_4    0                    0        0       0        0           0            0            0          0                    |
               {4} | 0        0       0        0           0            0            0          0                    -6852x_5 6549x_3 362x_5   x_1-6248x_3 0            x_0-14291x_4 -855x_3    -14401x_2-16185x_4   0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    x_3      x_2     x_1      -x_4        x_0-14291x_4 0            5359x_4    0                    |
               {4} | 0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    4032x_5  0       14811x_5 -4032x_3    6549x_3      -x_2         x_1-301x_3 x_0+7742x_2-15779x_4 -6852x_5 6549x_3 362x_5   x_1-6248x_3 0            x_0-14291x_4 -855x_3    -14401x_2-16185x_4   0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    |
               {4} | 0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    x_3      x_2     x_1      -x_4        x_0-14291x_4 0            5359x_4    0                    0        0       0        0           0            0            0          0                    -6852x_5 6549x_3 362x_5   x_1-6248x_3 0            x_0-14291x_4 -855x_3    -14401x_2-16185x_4   0        0       0        0           0            0            0          0                    |
               {4} | 0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    -6852x_5 6549x_3 362x_5   x_1-6248x_3 0            x_0-14291x_4 -855x_3    -14401x_2-16185x_4   0        0       0        0           0            0            0          0                    0        0       0        0           0            0            0          0                    -6852x_5 6549x_3 362x_5   x_1-6248x_3 0            x_0-14291x_4 -855x_3    -14401x_2-16185x_4   |

                                       9
o81 : ringP5-module, quotient of ringP5

i82 : omega2S = Hom(Hom(omegaS**omegaS, OS),OS)

o82 = cokernel {3} | x_3^2+5040x_0x_5-8565x_2x_5-11589x_4x_5 x_1x_3-6048x_0x_5-15922x_2x_5+7357x_4x_5 x_1x_2-4032x_0x_3-6248x_2x_3-10379x_3x_4 x_1^2+4032x_0x_5+14108x_2x_5-4032x_4x_5 x_0x_1-301x_0x_3-855x_2x_3-14291x_1x_4-10440x_3x_4 x_0^2+7742x_0x_2-14401x_2^2+2679x_0x_4+1764x_2x_4-11925x_4^2 |

                                       1
o82 : ringP5-module, quotient of ringP5

i83 : L = Hom(omegaS, OS**(ringP5^{-1}))

o83 = subquotient ({-1} | 14401x_2+16185x_4    x_0-14291x_4 -5359x_1+14409x_3 |, {-1} | 0                                       0                                       x_3^2+5040x_0x_5-8565x_2x_5-11589x_4x_5 0                                        0                                        x_1x_3-6048x_0x_5-15922x_2x_5+7357x_4x_5 0                                        0                                        x_1x_2-4032x_0x_3-6248x_2x_3-10379x_3x_4 0                                       0                                       x_1^2+4032x_0x_5+14108x_2x_5-4032x_4x_5 0                                                  0                                                  x_0x_1-301x_0x_3-855x_2x_3-14291x_1x_4-10440x_3x_4 0                                                            0                                                            x_0^2+7742x_0x_2-14401x_2^2+2679x_0x_4+1764x_2x_4-11925x_4^2 |)
                   {-1} | -1488x_1-10598x_3    -6549x_3     -11789x_5         |  {-1} | 0                                       x_3^2+5040x_0x_5-8565x_2x_5-11589x_4x_5 0                                       0                                        x_1x_3-6048x_0x_5-15922x_2x_5+7357x_4x_5 0                                        0                                        x_1x_2-4032x_0x_3-6248x_2x_3-10379x_3x_4 0                                        0                                       x_1^2+4032x_0x_5+14108x_2x_5-4032x_4x_5 0                                       0                                                  x_0x_1-301x_0x_3-855x_2x_3-14291x_1x_4-10440x_3x_4 0                                                  0                                                            x_0^2+7742x_0x_2-14401x_2^2+2679x_0x_4+1764x_2x_4-11925x_4^2 0                                                            |
                   {-1} | x_0+7742x_2-15779x_4 x_2          x_1+6551x_3       |  {-1} | x_3^2+5040x_0x_5-8565x_2x_5-11589x_4x_5 0                                       0                                       x_1x_3-6048x_0x_5-15922x_2x_5+7357x_4x_5 0                                        0                                        x_1x_2-4032x_0x_3-6248x_2x_3-10379x_3x_4 0                                        0                                        x_1^2+4032x_0x_5+14108x_2x_5-4032x_4x_5 0                                       0                                       x_0x_1-301x_0x_3-855x_2x_3-14291x_1x_4-10440x_3x_4 0                                                  0                                                  x_0^2+7742x_0x_2-14401x_2^2+2679x_0x_4+1764x_2x_4-11925x_4^2 0                                                            0                                                            |

                                          3
o83 : ringP5-module, subquotient of ringP5

i84 : dualModule = Hom(L, OS)

o84 = subquotient (| x_0+7742x_2-15779x_4 14401x_2+16185x_4 x_1-301x_3 |, | 0                                       0                                       x_3^2+5040x_0x_5-8565x_2x_5-11589x_4x_5 0                                        0                                        x_1x_3-6048x_0x_5-15922x_2x_5+7357x_4x_5 0                                        0                                        x_1x_2-4032x_0x_3-6248x_2x_3-10379x_3x_4 0                                       0                                       x_1^2+4032x_0x_5+14108x_2x_5-4032x_4x_5 0                                                  0                                                  x_0x_1-301x_0x_3-855x_2x_3-14291x_1x_4-10440x_3x_4 0                                                            0                                                            x_0^2+7742x_0x_2-14401x_2^2+2679x_0x_4+1764x_2x_4-11925x_4^2 |)
                   | x_2                  x_0-14291x_4      4032x_3    |  | 0                                       x_3^2+5040x_0x_5-8565x_2x_5-11589x_4x_5 0                                       0                                        x_1x_3-6048x_0x_5-15922x_2x_5+7357x_4x_5 0                                        0                                        x_1x_2-4032x_0x_3-6248x_2x_3-10379x_3x_4 0                                        0                                       x_1^2+4032x_0x_5+14108x_2x_5-4032x_4x_5 0                                       0                                                  x_0x_1-301x_0x_3-855x_2x_3-14291x_1x_4-10440x_3x_4 0                                                  0                                                            x_0^2+7742x_0x_2-14401x_2^2+2679x_0x_4+1764x_2x_4-11925x_4^2 0                                                            |
                   | x_1+6551x_3          -5359x_1+14409x_3 -9874x_5   |  | x_3^2+5040x_0x_5-8565x_2x_5-11589x_4x_5 0                                       0                                       x_1x_3-6048x_0x_5-15922x_2x_5+7357x_4x_5 0                                        0                                        x_1x_2-4032x_0x_3-6248x_2x_3-10379x_3x_4 0                                        0                                        x_1^2+4032x_0x_5+14108x_2x_5-4032x_4x_5 0                                       0                                       x_0x_1-301x_0x_3-855x_2x_3-14291x_1x_4-10440x_3x_4 0                                                  0                                                  x_0^2+7742x_0x_2-14401x_2^2+2679x_0x_4+1764x_2x_4-11925x_4^2 0                                                            0                                                            |

                                          3
o84 : ringP5-module, subquotient of ringP5

i85 : betti generators dualModule

o85 = total: 3 3
          0: 3 3

i86 : g = homomorphism dualModule_{0}

o86 = | x_0+7742x_2-15779x_4 x_2 x_1+6551x_3 |

o86 : Matrix

i87 : toP2 = g*basis(0,L)

o87 = | x_0+7742x_2-15779x_4 x_2 x_1+6551x_3 |

o87 : Matrix

i88 : ringXcan = ringP5/idealXcan

o88 = ringXcan

o88 : QuotientRing
```

---

## geometry / chapter.m2 — chunk 11

### Input

```macaulay2
ringP2 = kk[x_0..x_2]
idealXplane = trim kernel map(ringXcan, ringP2, 
                                        substitute(matrix toP2,ringXcan))
ringP2 = kk[x_0..x_2]
idealC2 = ideal(x_0^5+x_1^5+x_2^5)
ringC2 = ringP2/idealC2
ringP5 = kk[x_0..x_5]
idealC5 = trim kernel map(ringC2, ringP5, 
              gens (ideal vars ringC2)^2)
ringC5 = ringP5/idealC5
```

### Output

```
i89 : ringP2 = kk[x_0..x_2]

o89 = ringP2

o89 : PolynomialRing

i90 : idealXplane = trim kernel map(ringXcan, ringP2, 
                                        substitute(matrix toP2,ringXcan))

5         4           3 2        2 3           4        5        5
o90 = ideal(x  + 13394x x  - 13014x x  + 9232x x  + 12418x x  - 2746x  + 2107x )
             0         0 1         0 1        0 1         0 1        1        2

o90 : Ideal of ringP2

i91 : ringP2 = kk[x_0..x_2]

o91 = ringP2

o91 : PolynomialRing

i92 : idealC2 = ideal(x_0^5+x_1^5+x_2^5)

5    5    5
o92 = ideal(x  + x  + x )
             0    1    2

o92 : Ideal of ringP2

i93 : ringC2 = ringP2/idealC2

o93 = ringC2

o93 : QuotientRing

i94 : ringP5 = kk[x_0..x_5]

o94 = ringP5

o94 : PolynomialRing

i95 : idealC5 = trim kernel map(ringC2, ringP5, 
              gens (ideal vars ringC2)^2)

2                                    2                       2          2      2      3   2      3      2   3      2      2
o95 = ideal (x  - x x , x x  - x x , x x  - x x , x  - x x , x x  - x x , x  - x x , x x  + x x  + x , x x  + x  + x x , x  + x x  + x x )
              4    3 5   2 4    1 5   2 3    1 4   2    0 5   1 2    0 4   1    0 3   0 2    3 4    5   0 1    3    4 5   0    1 3    2 5

o95 : Ideal of ringP5

i96 : ringC5 = ringP5/idealC5

o96 = ringC5

o96 : QuotientRing
```

---

## geometry / chapter.m2 — chunk 12

### Input

```macaulay2
use ringC5
idealC = trim kernel map(ringC5, ringP3,
              matrix{{x_0+x_1,x_2,x_3,x_5}})
idealC == idealX
code mystery
code prettyPrint
i102 :
```

### Output

```
i97 : use ringC5

o97 = ringC5

o97 : QuotientRing

i98 : idealC = trim kernel map(ringC5, ringP3,
              matrix{{x_0+x_1,x_2,x_3,x_5}})

4       2      2        2 2   2 2           2           3           2               2             3     2 2         4          3            2 2             3          3 2             3             3     3           3 2        3             2                  2             3           2 3           4   5     2 3       4       3       3         2   2            2       2 2   2 4        4             3 2          2 3            4      5         3 2        3   2    2   3              3          2 3    6
o98 = ideal (x  - 2x x x  - x x x  + x x , x x  - 10915x x x  - 10917x x  + 10916x x x  - 10916x x x  - 10916x x , x x x  + 11909x x  + 5954x x x  + 2977x x x  + 11910x x x  - 2978x x  + 14887x x x  + 11910x x x , x x x  - 13099x x  - 6550x x x  - 13100x x x x  - 6550x x x x  + 13099x x x  + 13100x x  + 13099x x , x  + 5x x  + 5x x  - 3x x x  - 4x x x  + 4x x x  + 10x x x x  + 5x x x , x x  - 8932x x x  + 11909x x x  + 5954x x x  - 8934x x x  - x x  + 2x x x  - 5952x x x  - x x x  - 2979x x x x  - 8934x x x  + x )
              1     0 1 3    1 2 3    0 3   0 1         0 1 2         0 3         0 2 3         0 2 3         1 3   0 1 2         0 3        0 2 3        0 2 3         0 2 3        1 3         0 1 3         1 2 3   0 1 2         1 2        0 1 3         0 1 2 3        0 1 2 3         1 2 3         1 3         0 3   0     0 2     0 2     0 1 3     1 2 3     0 1 3      0 1 2 3     1 2 3   1 2        0 2 3         0 2 3        0 2 3        0 2 3    2 3     0 1 3        1 2 3    0 1 3        0 1 2 3        1 2 3    3

o98 : Ideal of ringP3

i99 : idealC == idealX

o99 = true

i100 : code mystery

o100 = -- mystery.m2:1-13
       mystery = ringP3 -> (
          kk := coefficientRing ringP3;
          x := local x;
          ringP2 := kk[x_0..x_2];
          idealC2 := ideal(x_0^5+x_1^5+x_2^5);
          ringC2 := ringP2/idealC2;
          ringP5 := kk[x_0..x_5];
          idealC5 := trim kernel map(ringC2, ringP5, 
               gens (ideal vars ringC2)^2);
          ringC5 := ringP5/idealC5;
          use ringC5;
          trim kernel map(ringC5, ringP3,
             matrix{{x_0+x_1,x_2,x_3,x_5}}))

i101 : code prettyPrint

o101 = -- mystery.m2:15-51
       prettyPrint = f -> (
          -- accept a matrix f and print its entries prettily,
          -- separated by commas
          wid := 74;
          -- page width
          post := (c,s) -> (
             -- This function concatenates string c to end of each
             -- string in list s except the last one
             concatenate \ pack_2 between_c s);
          strings := post_"," (toString \ flatten entries f);
          -- list of strings, one for each polynomial, with commas
          istate := ("",0);
          -- initial state = (out : output string, col : column number)
          strings = apply(
             strings,
             poly -> first fold(
                -- break each poly into lines
                (state,term) -> (
                   (out,col) -> (
                      if col + #term > wid -- too wide?
                      then (
                         out = out | "\n   "; 
                         col = 3;
                         -- insert line break
                         );
                      (out | term, col + #term) -- new state
                      )
                   ) state,
                istate,
                fold( -- separate poly into terms 
                   {"+","-"},
                   {poly},
                   (delimiter,poly) -> flatten( 
                      post_delimiter \ separate_delimiter \ poly
                      ))));
          print stack strings;  -- stack them vertically, then print
          )

i102 :
```

---

## geometry / test.m2 — chunk 0

### Input

```macaulay2
kk = ZZ/32749
ringP3 = kk[x_0..x_3]
ringP1 = kk[s,t]
cubicMap = map(ringP1,ringP3,{s^3, s^2*t, s*t^2, t^3})
idealCubic = kernel cubicMap
idealCubic2 = monomialCurveIdeal(ringP3,{1,2,3})
M = matrix{{x_0,x_1,x_2},{x_1,x_2,x_3}}
idealCubic3 = minors(2, M)
```

### Output

```
i1 : kk = ZZ/32749

o1 = kk

o1 : QuotientRing

i2 : ringP3 = kk[x_0..x_3]

o2 = ringP3

o2 : PolynomialRing

i3 : ringP1 = kk[s,t]

o3 = ringP1

o3 : PolynomialRing

i4 : cubicMap = map(ringP1,ringP3,{s^3, s^2*t, s*t^2, t^3})

3   2      2   3
o4 = map (ringP1, ringP3, {s , s t, s*t , t })

o4 : RingMap ringP1 <-- ringP3

i5 : idealCubic = kernel cubicMap

2                       2
o5 = ideal (x  - x x , x x  - x x , x  - x x )
             2    1 3   1 2    0 3   1    0 2

o5 : Ideal of ringP3

i6 : idealCubic2 = monomialCurveIdeal(ringP3,{1,2,3})

2                       2
o6 = ideal (x  - x x , x x  - x x , x  - x x )
             2    1 3   1 2    0 3   1    0 2

o6 : Ideal of ringP3

i7 : M = matrix{{x_0,x_1,x_2},{x_1,x_2,x_3}}

o7 = | x_0 x_1 x_2 |
     | x_1 x_2 x_3 |

                  2           3
o7 : Matrix ringP3  <-- ringP3

i8 : idealCubic3 = minors(2, M)

2                           2
o8 = ideal (- x  + x x , - x x  + x x , - x  + x x )
               1    0 2     1 2    0 3     2    1 3

o8 : Ideal of ringP3
```

---

## geometry / test.m2 — chunk 1

### Input

```macaulay2
codim idealCubic
degree idealCubic
dim idealCubic
gens idealCubic
0 == (gens idealCubic)%(gens idealCubic3)
idealCubic == idealCubic3
f = vars ringP3
OmegaP3 = kernel f
```

### Output

```
i9 : codim idealCubic

o9 = 2

i10 : degree idealCubic

o10 = 3

i11 : dim idealCubic

o11 = 2

i12 : gens idealCubic

o12 = | x_2^2-x_1x_3 x_1x_2-x_0x_3 x_1^2-x_0x_2 |

                   1           3
o12 : Matrix ringP3  <-- ringP3

i13 : 0 == (gens idealCubic)%(gens idealCubic3)

o13 = true

i14 : idealCubic == idealCubic3

o14 = true

i15 : f = vars ringP3

o15 = | x_0 x_1 x_2 x_3 |

                   1           4
o15 : Matrix ringP3  <-- ringP3

i16 : OmegaP3 = kernel f

o16 = image {1} | -x_1 0    -x_2 0    0    -x_3 |
            {1} | x_0  -x_2 0    0    -x_3 0    |
            {1} | 0    x_1  x_0  -x_3 0    0    |
            {1} | 0    0    0    x_2  x_1  x_0  |

                                        4
o16 : ringP3-module, submodule of ringP3
```

---

## geometry / test.m2 — chunk 2

### Input

```macaulay2
g=generators OmegaP3
OmegaP3=image g
presentation OmegaP3
G = res coker f
G.dd
G.dd_2
degrees source G.dd_2
degrees target G.dd_2
```

### Output

```
i17 : g=generators OmegaP3

o17 = {1} | -x_1 0    -x_2 0    0    -x_3 |
      {1} | x_0  -x_2 0    0    -x_3 0    |
      {1} | 0    x_1  x_0  -x_3 0    0    |
      {1} | 0    0    0    x_2  x_1  x_0  |

                   4           6
o17 : Matrix ringP3  <-- ringP3

i18 : OmegaP3=image g

o18 = image {1} | -x_1 0    -x_2 0    0    -x_3 |
            {1} | x_0  -x_2 0    0    -x_3 0    |
            {1} | 0    x_1  x_0  -x_3 0    0    |
            {1} | 0    0    0    x_2  x_1  x_0  |

                                        4
o18 : ringP3-module, submodule of ringP3

i19 : presentation OmegaP3

o19 = {2} | x_2  0    0    x_3  |
      {2} | x_0  x_3  0    0    |
      {2} | -x_1 0    x_3  0    |
      {2} | 0    x_1  x_0  0    |
      {2} | 0    -x_2 0    x_0  |
      {2} | 0    0    -x_2 -x_1 |

                   6           4
o19 : Matrix ringP3  <-- ringP3

i20 : G = res coker f

1           4           6           4           1
o20 = ringP3  <-- ringP3  <-- ringP3  <-- ringP3  <-- ringP3  <-- 0
                                                                   
      0           1           2           3           4           5

o20 : ChainComplex

i21 : G.dd

1                                4
o21 = 0 : ringP3  <----------------------- ringP3  : 1
                     | x_0 x_1 x_2 x_3 |

                4                                                  6
      1 : ringP3  <----------------------------------------- ringP3  : 2
                     {1} | -x_1 -x_2 0    -x_3 0    0    |
                     {1} | x_0  0    -x_2 0    -x_3 0    |
                     {1} | 0    x_0  x_1  0    0    -x_3 |
                     {1} | 0    0    0    x_0  x_1  x_2  |

                6                                        4
      2 : ringP3  <------------------------------- ringP3  : 3
                     {2} | x_2  x_3  0    0    |
                     {2} | -x_1 0    x_3  0    |
                     {2} | x_0  0    0    x_3  |
                     {2} | 0    -x_1 -x_2 0    |
                     {2} | 0    x_0  0    -x_2 |
                     {2} | 0    0    x_0  x_1  |

                4                         1
      3 : ringP3  <---------------- ringP3  : 4
                     {3} | -x_3 |
                     {3} | x_2  |
                     {3} | -x_1 |
                     {3} | x_0  |

                1
      4 : ringP3  <----- 0 : 5
                     0

o21 : ChainComplexMap

i22 : G.dd_2

o22 = {1} | -x_1 -x_2 0    -x_3 0    0    |
      {1} | x_0  0    -x_2 0    -x_3 0    |
      {1} | 0    x_0  x_1  0    0    -x_3 |
      {1} | 0    0    0    x_0  x_1  x_2  |

                   4           6
o22 : Matrix ringP3  <-- ringP3

i23 : degrees source G.dd_2

o23 = {{2}, {2}, {2}, {2}, {2}, {2}}

o23 : List

i24 : degrees target G.dd_2

o24 = {{1}, {1}, {1}, {1}}

o24 : List
```

---

## geometry / test.m2 — chunk 3

### Input

```macaulay2
betti G
m = matrix{{x_0^3, x_1^2, x_2,x_3},{x_1^3,x_2^2,x_3,0}}
I = minors(2,m)
F = res(ringP3^1/I)
betti F
betti G
OmegaP3res = kernel (f ** (ringP3^1/idealCubic))
delta1 = jacobian idealCubic
```

### Output

```
i25 : betti G

0 1 2 3 4
o25 = total: 1 4 6 4 1
          0: 1 4 6 4 1

o25 : BettiTally

i26 : m = matrix{{x_0^3, x_1^2, x_2,x_3},{x_1^3,x_2^2,x_3,0}}

o26 = | x_0^3 x_1^2 x_2 x_3 |
      | x_1^3 x_2^2 x_3 0   |

                   2           4
o26 : Matrix ringP3  <-- ringP3

i27 : I = minors(2,m)

5    3 2     3      3       3    2      3      2      2
o27 = ideal (- x  + x x , - x x  + x x , - x  + x x , -x x , -x x , -x )
                1    0 2     1 2    0 3     2    1 3    1 3    2 3    3

o27 : Ideal of ringP3

i28 : F = res(ringP3^1/I)

1           6           8           3
o28 = ringP3  <-- ringP3  <-- ringP3  <-- ringP3  <-- 0
                                                       
      0           1           2           3           4

o28 : ChainComplex

i29 : betti F

0 1 2 3
o29 = total: 1 6 8 3
          0: 1 . . .
          1: . 1 . .
          2: . 2 2 .
          3: . 2 2 .
          4: . 1 4 3

o29 : BettiTally

i30 : betti G

0 1 2 3 4
o30 = total: 1 4 6 4 1
          0: 1 4 6 4 1

o30 : BettiTally

i31 : OmegaP3res = kernel (f ** (ringP3^1/idealCubic))

o31 = subquotient ({1} | -x_3 -x_2 -x_1 0    -x_3 -x_2 0    0    -x_3 |, {1} | x_2^2-x_1x_3 x_1x_2-x_0x_3 x_1^2-x_0x_2 0            0             0            0            0             0            0            0             0            |)
                   {1} | x_2  x_1  x_0  -x_3 0    0    0    -x_3 0    |  {1} | 0            0             0            x_2^2-x_1x_3 x_1x_2-x_0x_3 x_1^2-x_0x_2 0            0             0            0            0             0            |
                   {1} | 0    0    0    x_2  x_1  x_0  -x_3 0    0    |  {1} | 0            0             0            0            0             0            x_2^2-x_1x_3 x_1x_2-x_0x_3 x_1^2-x_0x_2 0            0             0            |
                   {1} | 0    0    0    0    0    0    x_2  x_1  x_0  |  {1} | 0            0             0            0            0             0            0            0             0            x_2^2-x_1x_3 x_1x_2-x_0x_3 x_1^2-x_0x_2 |

                                          4
o31 : ringP3-module, subquotient of ringP3

i32 : delta1 = jacobian idealCubic

o32 = {1} | 0    -x_3 -x_2 |
      {1} | -x_3 x_2  2x_1 |
      {1} | 2x_2 x_1  -x_0 |
      {1} | -x_1 -x_0 0    |

                   4           3
o32 : Matrix ringP3  <-- ringP3
```

---

## geometry / test.m2 — chunk 4

### Input

```macaulay2
delta2 = delta1 // (gens OmegaP3res)
delta = map(OmegaP3res, module idealCubic, delta2)
OmegaCubic = prune coker delta
prune HH^0((sheaf OmegaCubic)(>=0))
Cubic = Proj(ringP3/idealCubic)
cotangentSheaf Cubic
ringP4 = kk[x_0..x_4]
idealX = ideal(x_1+x_3, x_2+x_4)
```

### Output

```
i33 : delta2 = delta1 // (gens OmegaP3res)

o33 = {2} | 0  1  0  |
      {2} | 0  0  2  |
      {2} | 0  0  0  |
      {2} | 2  0  0  |
      {2} | 0  1  0  |
      {2} | 0  0  -1 |
      {2} | 0  0  0  |
      {2} | -1 0  0  |
      {2} | 0  -1 0  |

                   9           3
o33 : Matrix ringP3  <-- ringP3

i34 : delta = map(OmegaP3res, module idealCubic, delta2)

o34 = {2} | 0  1  0  |
      {2} | 0  0  2  |
      {2} | 0  0  0  |
      {2} | 2  0  0  |
      {2} | 0  1  0  |
      {2} | 0  0  -1 |
      {2} | 0  0  0  |
      {2} | -1 0  0  |
      {2} | 0  -1 0  |

o34 : Matrix

i35 : OmegaCubic = prune coker delta

o35 = cokernel {2} | -2x_3 -2x_2 0    -2x_3 -2x_2 -2x_1 0        0        0        0    0    -2x_3 0        0        -3x_3 -3x_2 |
               {2} | x_1   x_0   x_2  0     0     0     16374x_3 0        0        -x_3 0    0     16373x_3 0        0     0     |
               {2} | 0     0     -x_3 x_2   x_1   x_0   0        16374x_3 0        0    -x_3 0     0        16373x_3 0     0     |
               {2} | 0     0     0    0     0     0     x_1      x_0      x_2      0    0    0     0        0        0     0     |
               {2} | 0     0     0    0     0     0     0        0        16374x_3 x_2  x_1  x_0   0        0        0     0     |
               {2} | 0     0     0    0     0     0     0        0        0        0    0    0     x_3      x_2      x_1   x_0   |

                                       6
o35 : ringP3-module, quotient of ringP3

i36 : prune HH^0((sheaf OmegaCubic)(>=0))

o36 = cokernel {1} | x_2      x_1      x_0      |
               {1} | 16374x_3 16374x_2 16374x_1 |

                                       2
o36 : ringP3-module, quotient of ringP3

i37 : Cubic = Proj(ringP3/idealCubic)

o37 = Cubic

o37 : ProjectiveVariety

i38 : cotangentSheaf Cubic

o38 = cokernel {1} | -2x_3 -2x_2 -2x_1 |
               {1} | x_2   x_1   x_0   |

                                                  2
o38 : coherent sheaf on Cubic, quotient of OO      (-1)
                                             Cubic

i39 : ringP4 = kk[x_0..x_4]

o39 = ringP4

o39 : PolynomialRing

i40 : idealX = ideal(x_1+x_3, x_2+x_4)

o40 = ideal (x  + x , x  + x )
              1    3   2    4

o40 : Ideal of ringP4
```

---

## geometry / test.m2 — chunk 5

### Input

```macaulay2
idealL1 = ideal(x_1,x_2)
idealL2 = ideal(x_3,x_4)
idealY = intersect(idealL1,idealL2)
degree(idealX+idealY)
degree Tor_0(ringP4^1/idealX, ringP4^1/idealY)
degree Tor_1(ringP4^1/idealX, ringP4^1/idealY)
degree Tor_2(ringP4^1/idealX, ringP4^1/idealY)
res (ringP4^1/idealX)
```

### Output

```
i41 : idealL1 = ideal(x_1,x_2)

o41 = ideal (x , x )
              1   2

o41 : Ideal of ringP4

i42 : idealL2 = ideal(x_3,x_4)

o42 = ideal (x , x )
              3   4

o42 : Ideal of ringP4

i43 : idealY = intersect(idealL1,idealL2)

o43 = ideal (x x , x x , x x , x x )
              2 4   1 4   2 3   1 3

o43 : Ideal of ringP4

i44 : degree(idealX+idealY)

o44 = 3

i45 : degree Tor_0(ringP4^1/idealX, ringP4^1/idealY)

o45 = 3

i46 : degree Tor_1(ringP4^1/idealX, ringP4^1/idealY)

o46 = 1

i47 : degree Tor_2(ringP4^1/idealX, ringP4^1/idealY)

o47 = 0

i48 : res (ringP4^1/idealX)

1           2           1
o48 = ringP4  <-- ringP4  <-- ringP4  <-- 0
                                           
      0           1           2           3

o48 : ChainComplex
```

---

## geometry / test.m2 — chunk 6

### Input

```macaulay2
ringP3 = kk[x_0..x_3];
load "mystery.m2"
idealX = mystery ringP3
prettyPrint gens idealX
x_1^4-2*x_0*x_1^2*x_3-x_1^2*x_2*x_3+x_0^2*x_3^2,
x_0^2*x_1^2-10915*x_0*x_1^2*x_2-10917*x_0^3*x_3+10916*x_0^2*x_2*x_3-
   10916*x_0*x_2^2*x_3-10916*x_1*x_3^3,
x_0*x_1^2*x_2^2+11909*x_0^4*x_3+5954*x_0^3*x_2*x_3+2977*x_0^2*x_2^2*x_3+
   11910*x_0*x_2^3*x_3-2978*x_1^3*x_3^2+14887*x_0*x_1*x_3^3+
   11910*x_1*x_2*x_3^3,
x_0*x_1^3*x_2-13099*x_1^3*x_2^2-6550*x_0^3*x_1*x_3-
   13100*x_0^2*x_1*x_2*x_3-6550*x_0*x_1*x_2^2*x_3+13099*x_1*x_2^3*x_3+
   13100*x_1^2*x_3^3+13099*x_0*x_3^4,
x_0^5+5*x_0^2*x_2^3+5*x_0*x_2^4-3*x_0*x_1^3*x_3-4*x_1^3*x_2*x_3+
   4*x_0^2*x_1*x_3^2+10*x_0*x_1*x_2*x_3^2+5*x_1*x_2^2*x_3^2,
x_1^2*x_2^4-8932*x_0^4*x_2*x_3+11909*x_0^3*x_2^2*x_3+5954*x_0^2*x_2^3*x_3-
   8934*x_0*x_2^4*x_3-x_2^5*x_3+2*x_0*x_1^3*x_3^2-5952*x_1^3*x_2*x_3^2-
   x_0^2*x_1*x_3^3-2979*x_0*x_1*x_2*x_3^3-8934*x_1*x_2^2*x_3^3+x_3^6
X = variety idealX
idealX == saturate idealX
dim X
idealXtop = topComponents idealX
```

### Output

```
i49 : ringP3 = kk[x_0..x_3];

i50 : load "mystery.m2"

i51 : idealX = mystery ringP3

4       2      2        2 2   2 2           2           3           2               2             3     2 2         4          3            2 2             3          3 2             3             3     3           3 2        3             2                  2             3           2 3           4   5     2 3       4       3       3         2   2            2       2 2   2 4        4             3 2          2 3            4      5         3 2        3   2    2   3              3          2 3    6
o51 = ideal (x  - 2x x x  - x x x  + x x , x x  - 10915x x x  - 10917x x  + 10916x x x  - 10916x x x  - 10916x x , x x x  + 11909x x  + 5954x x x  + 2977x x x  + 11910x x x  - 2978x x  + 14887x x x  + 11910x x x , x x x  - 13099x x  - 6550x x x  - 13100x x x x  - 6550x x x x  + 13099x x x  + 13100x x  + 13099x x , x  + 5x x  + 5x x  - 3x x x  - 4x x x  + 4x x x  + 10x x x x  + 5x x x , x x  - 8932x x x  + 11909x x x  + 5954x x x  - 8934x x x  - x x  + 2x x x  - 5952x x x  - x x x  - 2979x x x x  - 8934x x x  + x )
              1     0 1 3    1 2 3    0 3   0 1         0 1 2         0 3         0 2 3         0 2 3         1 3   0 1 2         0 3        0 2 3        0 2 3         0 2 3        1 3         0 1 3         1 2 3   0 1 2         1 2        0 1 3         0 1 2 3        0 1 2 3         1 2 3         1 3         0 3   0     0 2     0 2     0 1 3     1 2 3     0 1 3      0 1 2 3     1 2 3   1 2        0 2 3         0 2 3        0 2 3        0 2 3    2 3     0 1 3        1 2 3    0 1 3        0 1 2 3        1 2 3    3

o51 : Ideal of ringP3

i52 : prettyPrint gens idealX
x_1^4-2*x_0*x_1^2*x_3-x_1^2*x_2*x_3+x_0^2*x_3^2,
x_0^2*x_1^2-10915*x_0*x_1^2*x_2-10917*x_0^3*x_3+10916*x_0^2*x_2*x_3-
   10916*x_0*x_2^2*x_3-10916*x_1*x_3^3,
x_0*x_1^2*x_2^2+11909*x_0^4*x_3+5954*x_0^3*x_2*x_3+2977*x_0^2*x_2^2*x_3+
   11910*x_0*x_2^3*x_3-2978*x_1^3*x_3^2+14887*x_0*x_1*x_3^3+
   11910*x_1*x_2*x_3^3,
x_0*x_1^3*x_2-13099*x_1^3*x_2^2-6550*x_0^3*x_1*x_3-
   13100*x_0^2*x_1*x_2*x_3-6550*x_0*x_1*x_2^2*x_3+13099*x_1*x_2^3*x_3+
   13100*x_1^2*x_3^3+13099*x_0*x_3^4,
x_0^5+5*x_0^2*x_2^3+5*x_0*x_2^4-3*x_0*x_1^3*x_3-4*x_1^3*x_2*x_3+
   4*x_0^2*x_1*x_3^2+10*x_0*x_1*x_2*x_3^2+5*x_1*x_2^2*x_3^2,
x_1^2*x_2^4-8932*x_0^4*x_2*x_3+11909*x_0^3*x_2^2*x_3+5954*x_0^2*x_2^3*x_3-
   8934*x_0*x_2^4*x_3-x_2^5*x_3+2*x_0*x_1^3*x_3^2-5952*x_1^3*x_2*x_3^2-
   x_0^2*x_1*x_3^3-2979*x_0*x_1*x_2*x_3^3-8934*x_1*x_2^2*x_3^3+x_3^6

i53 : X = variety idealX

o53 = X

o53 : ProjectiveVariety

i54 : idealX == saturate idealX

o54 = true

i55 : dim X

o55 = 1

i56 : idealXtop = topComponents idealX

4       2      2        2 2   2 2           2           3           2               2             3     2 2         4          3            2 2             3          3 2             3             3     3           3 2        3             2                  2             3           2 3           4   5     2 3       4       3       3         2   2            2       2 2   2 4        4             3 2          2 3            4      5         3 2        3   2    2   3              3          2 3    6
o56 = ideal (x  - 2x x x  - x x x  + x x , x x  - 10915x x x  - 10917x x  + 10916x x x  - 10916x x x  - 10916x x , x x x  + 11909x x  + 5954x x x  + 2977x x x  + 11910x x x  - 2978x x  + 14887x x x  + 11910x x x , x x x  - 13099x x  - 6550x x x  - 13100x x x x  - 6550x x x x  + 13099x x x  + 13100x x  + 13099x x , x  + 5x x  + 5x x  - 3x x x  - 4x x x  + 4x x x  + 10x x x x  + 5x x x , x x  - 8932x x x  + 11909x x x  + 5954x x x  - 8934x x x  - x x  + 2x x x  - 5952x x x  - x x x  - 2979x x x x  - 8934x x x  + x )
              1     0 1 3    1 2 3    0 3   0 1         0 1 2         0 3         0 2 3         0 2 3         1 3   0 1 2         0 3        0 2 3        0 2 3         0 2 3        1 3         0 1 3         1 2 3   0 1 2         1 2        0 1 3         0 1 2 3        0 1 2 3         1 2 3         1 3         0 3   0     0 2     0 2     0 1 3     1 2 3     0 1 3      0 1 2 3     1 2 3   1 2        0 2 3         0 2 3        0 2 3        0 2 3    2 3     0 1 3        1 2 3    0 1 3        0 1 2 3        1 2 3    3

o56 : Ideal of ringP3
```

---

## geometry / test.m2 — chunk 7

### Input

```macaulay2
(gens idealXtop)%(gens idealX) == 0
codim singularLocus idealX
# decompose idealX
HH^0 OO_X
rank oo
HH^1 OO_X
degree idealX
P3 = Proj ringP3
```

### Output

```
i57 : (gens idealXtop)%(gens idealX) == 0

o57 = true

i58 : codim singularLocus idealX

o58 = 4

i59 : # decompose idealX

o59 = 1

i60 : HH^0 OO_X

1
o60 = kk

o60 : kk-module, free

i61 : rank oo

o61 = 1

i62 : HH^1 OO_X

6
o62 = kk

o62 : kk-module, free

i63 : degree idealX

o63 = 10

i64 : P3 = Proj ringP3

o64 = P3

o64 : ProjectiveVariety
```

---

## geometry / test.m2 — chunk 8

### Input

```macaulay2
HH^1((OO_P3(1)/idealX)(>=0))
degrees oo
omegaX = prune Ext^(codim idealX)(ringP3^1/idealX, ringP3^{-4})
dualModule = Hom(omegaX, ringP3^1/idealX, MinimalGenerators => true)
betti prune dualModule
f = homomorphism dualModule_{0}
canGens = f*basis(0,omegaX)
ringX = ringP3/idealX
```

### Output

```
i65 : HH^1((OO_P3(1)/idealX)(>=0))

o65 = cokernel | x_3 x_2 x_1 x_0 |

                                       1
o65 : ringP3-module, quotient of ringP3

i66 : degrees oo

o66 = {{0}}

o66 : List

i67 : omegaX = prune Ext^(codim idealX)(ringP3^1/idealX, ringP3^{-4})

o67 = cokernel {-1} | x_1^2-1702x_2x_3 x_0x_3-2553x_2x_3 x_0x_1-8086x_1x_2 x_1x_2^2-11925x_3^3             x_0^2x_2-15006x_0x_2^2+8248x_2^3+3876x_1x_3^2 x_0^3+13548x_0x_2^2+4124x_2^3-6356x_1x_3^2 |
               {0}  | 2552x_1          12014x_1          2626x_0           13438x_0^2-8515x_0x_2-6719x_2^2 11524x_3^2                                    5762x_3^2                                  |
               {0}  | -4880x_3         -7320x_3          1234x_1           11498x_1x_2                     -3715x_0^2+7197x_0x_2+13840x_2^2              7197x_0^2+10213x_0x_2+6920x_2^2            |

                                       3
o67 : ringP3-module, quotient of ringP3

i68 : dualModule = Hom(omegaX, ringP3^1/idealX, MinimalGenerators => true)

o68 = subquotient ({1} | -2626x_1^2+12125x_0x_3                -9334x_1x_3                        -1234x_1^2+1851x_0x_3                            8188x_3^3                                                                                             -13469x_0x_1^2-6054x_1^2x_2+14617x_0^2x_3+14475x_0x_2x_3-5394x_2^2x_3 3715x_0^2x_1-7197x_0x_1x_2-13840x_1x_2^2+11989x_3^3                                -2626x_0^3+6868x_0^2x_2-6878x_0x_2^2-6878x_1x_3^2                        -7197x_0^2x_1-10213x_0x_1x_2-6920x_1x_2^2-10380x_3^3                              -1234x_0^3-617x_0^2x_2+617x_0x_2^2+617x_1x_3^2                                 -13438x_0^4+1514x_0^3x_2-8548x_0^2x_2^2+10542x_0x_2^3+447x_2^4-11923x_1^3x_3-6949x_0x_1x_3^2+9432x_1x_2x_3^2                       |, {1} | 0                                         0                                                                                         0                                         0                                                                                         x_1^4-2x_0x_1^2x_3-x_1^2x_2x_3+x_0^2x_3^2 x_0^2x_1^2-10915x_0x_1^2x_2-10917x_0^3x_3+10916x_0^2x_2x_3-10916x_0x_2^2x_3-10916x_1x_3^3 0                                                                                                                               0                                                                                                                                 0                                                                                                    0                                                                                                                               0                                                                                                                                 0                                                                                                    x_0x_1^2x_2^2+11909x_0^4x_3+5954x_0^3x_2x_3+2977x_0^2x_2^2x_3+11910x_0x_2^3x_3-2978x_1^3x_3^2+14887x_0x_1x_3^3+11910x_1x_2x_3^3 x_0x_1^3x_2-13099x_1^3x_2^2-6550x_0^3x_1x_3-13100x_0^2x_1x_2x_3-6550x_0x_1x_2^2x_3+13099x_1x_2^3x_3+13100x_1^2x_3^3+13099x_0x_3^4 x_0^5+5x_0^2x_2^3+5x_0x_2^4-3x_0x_1^3x_3-4x_1^3x_2x_3+4x_0^2x_1x_3^2+10x_0x_1x_2x_3^2+5x_1x_2^2x_3^2 0                                                                                                                                                                                  0                                                                                                                                                                                  x_1^2x_2^4-8932x_0^4x_2x_3+11909x_0^3x_2^2x_3+5954x_0^2x_2^3x_3-8934x_0x_2^4x_3-x_2^5x_3+2x_0x_1^3x_3^2-5952x_1^3x_2x_3^2-x_0^2x_1x_3^3-2979x_0x_1x_2x_3^3-8934x_1x_2^2x_3^3+x_3^6 |)
                   {0} | x_1^3+9299x_0x_1x_3+9700x_1x_2x_3     4651x_1^2x_3-14017x_0x_3^2         6303x_0x_1x_3-5069x_1x_2x_3                      x_0x_1^2x_2-13099x_1^2x_2^2-6550x_0^3x_3-13100x_0^2x_2x_3-6550x_0x_2^2x_3+13099x_2^3x_3+16374x_1x_3^3 3856x_0^2x_1x_3-7009x_0x_1x_2x_3+638x_1x_2^2x_3+10865x_3^4            5536x_0^3x_3-15821x_0^2x_2x_3-4050x_0x_2^2x_3-16141x_2^3x_3+15326x_1x_3^3          x_0^3x_1+13748x_0^2x_1x_2-4856x_0x_1x_2^2-4848x_1^2x_3^2                 2768x_0^3x_3+13344x_0^2x_2x_3+903x_0x_2^2x_3+8304x_2^3x_3+10591x_1x_3^3           -1234x_0^2x_1x_2-13840x_0x_1x_2^2-13840x_1^2x_3^2                              x_0^2x_1x_2^2-10915x_0x_1x_2^3-13636x_1x_2^4+14316x_0x_1^2x_3^2+15412x_1^2x_2x_3^2+7507x_0^2x_3^3+11854x_0x_2x_3^3+12742x_2^2x_3^3 |  {0} | x_1^4-2x_0x_1^2x_3-x_1^2x_2x_3+x_0^2x_3^2 x_0^2x_1^2-10915x_0x_1^2x_2-10917x_0^3x_3+10916x_0^2x_2x_3-10916x_0x_2^2x_3-10916x_1x_3^3 0                                         0                                                                                         0                                         0                                                                                         x_0x_1^2x_2^2+11909x_0^4x_3+5954x_0^3x_2x_3+2977x_0^2x_2^2x_3+11910x_0x_2^3x_3-2978x_1^3x_3^2+14887x_0x_1x_3^3+11910x_1x_2x_3^3 x_0x_1^3x_2-13099x_1^3x_2^2-6550x_0^3x_1x_3-13100x_0^2x_1x_2x_3-6550x_0x_1x_2^2x_3+13099x_1x_2^3x_3+13100x_1^2x_3^3+13099x_0x_3^4 x_0^5+5x_0^2x_2^3+5x_0x_2^4-3x_0x_1^3x_3-4x_1^3x_2x_3+4x_0^2x_1x_3^2+10x_0x_1x_2x_3^2+5x_1x_2^2x_3^2 0                                                                                                                               0                                                                                                                                 0                                                                                                    0                                                                                                                               0                                                                                                                                 0                                                                                                    x_1^2x_2^4-8932x_0^4x_2x_3+11909x_0^3x_2^2x_3+5954x_0^2x_2^3x_3-8934x_0x_2^4x_3-x_2^5x_3+2x_0x_1^3x_3^2-5952x_1^3x_2x_3^2-x_0^2x_1x_3^3-2979x_0x_1x_2x_3^3-8934x_1x_2^2x_3^3+x_3^6 0                                                                                                                                                                                  0                                                                                                                                                                                  |
                   {0} | -16305x_1^2x_2+8147x_0^2x_3-x_0x_2x_3 x_1^3-8565x_0x_1x_3-11589x_1x_2x_3 x_0x_1^2-8086x_1^2x_2-9301x_0^2x_3+2428x_0x_2x_3 15914x_1^2x_3^2-2072x_0x_3^3+15022x_2x_3^3                                                            x_0^3x_3-6168x_0^2x_2x_3-152x_0x_2^2x_3+727x_2^3x_3+1116x_1x_3^3      x_0^2x_1x_2-15006x_0x_1x_2^2+8248x_1x_2^3+3876x_1^2x_3^2-7519x_0x_3^3+5093x_2x_3^3 -12924x_0^3x_2-2034x_0^2x_2^2+843x_0x_2^3-8308x_0x_1x_3^2+843x_1x_2x_3^2 x_0^3x_1+13548x_0x_1x_2^2+4124x_1x_2^3-6356x_1^2x_3^2+12615x_0x_3^3-13828x_2x_3^3 x_0^4+10915x_0^3x_2+807x_0^2x_2^2+4043x_0x_2^3+4850x_0x_1x_3^2+4043x_1x_2x_3^2 -13262x_0^2x_2^3-6973x_0x_2^4+169x_2^5-14463x_0x_1x_2x_3^2-12512x_1x_2^2x_3^2+12466x_3^5                                           |  {0} | 0                                         0                                                                                         x_1^4-2x_0x_1^2x_3-x_1^2x_2x_3+x_0^2x_3^2 x_0^2x_1^2-10915x_0x_1^2x_2-10917x_0^3x_3+10916x_0^2x_2x_3-10916x_0x_2^2x_3-10916x_1x_3^3 0                                         0                                                                                         0                                                                                                                               0                                                                                                                                 0                                                                                                    x_0x_1^2x_2^2+11909x_0^4x_3+5954x_0^3x_2x_3+2977x_0^2x_2^2x_3+11910x_0x_2^3x_3-2978x_1^3x_3^2+14887x_0x_1x_3^3+11910x_1x_2x_3^3 x_0x_1^3x_2-13099x_1^3x_2^2-6550x_0^3x_1x_3-13100x_0^2x_1x_2x_3-6550x_0x_1x_2^2x_3+13099x_1x_2^3x_3+13100x_1^2x_3^3+13099x_0x_3^4 x_0^5+5x_0^2x_2^3+5x_0x_2^4-3x_0x_1^3x_3-4x_1^3x_2x_3+4x_0^2x_1x_3^2+10x_0x_1x_2x_3^2+5x_1x_2^2x_3^2 0                                                                                                                               0                                                                                                                                 0                                                                                                    0                                                                                                                                                                                  x_1^2x_2^4-8932x_0^4x_2x_3+11909x_0^3x_2^2x_3+5954x_0^2x_2^3x_3-8934x_0x_2^4x_3-x_2^5x_3+2x_0x_1^3x_3^2-5952x_1^3x_2x_3^2-x_0^2x_1x_3^3-2979x_0x_1x_2x_3^3-8934x_1x_2^2x_3^3+x_3^6 0                                                                                                                                                                                  |

                                          3
o68 : ringP3-module, subquotient of ringP3

i69 : betti prune dualModule

0  1
o69 = total: 10 26
          3:  3  2
          4:  6 14
          5:  1  9
          6:  .  1

o69 : BettiTally

i70 : f = homomorphism dualModule_{0}

o70 = | -2626x_1^2+12125x_0x_3 x_1^3+9299x_0x_1x_3+9700x_1x_2x_3 -16305x_1^2x_2+8147x_0^2x_3-x_0x_2x_3 |

o70 : Matrix

i71 : canGens = f*basis(0,omegaX)

o71 = | -2626x_0x_1^2+12125x_0^2x_3 -2626x_1^3+12125x_0x_1x_3 -2626x_1^2x_2+12125x_0x_2x_3 -2626x_1^2x_3+12125x_0x_3^2 x_1^3+9299x_0x_1x_3+9700x_1x_2x_3 -16305x_1^2x_2+8147x_0^2x_3-x_0x_2x_3 |

o71 : Matrix

i72 : ringX = ringP3/idealX

o72 = ringX

o72 : QuotientRing
```

---

## geometry / test.m2 — chunk 9

### Input

```macaulay2
ringP5 = kk[x_0..x_5]
idealXcan = trim kernel map(ringX, ringP5, 
                                     substitute(matrix canGens,ringX),
                                     DegreeMap => i -> 5*i)
betti res idealXcan
deg2places = positions(degrees idealXcan, i->i=={2})
idealS= ideal (gens idealXcan)_deg2places
codim singularLocus idealS
omegaS = prune Ext^(codim idealS)(ringP5^1/idealS, ringP5^{-6})
OS = ringP5^1/idealS
```

### Output

```
i73 : ringP5 = kk[x_0..x_5]

o73 = ringP5

o73 : PolynomialRing

i74 : idealXcan = trim kernel map(ringX, ringP5, 
                                     substitute(matrix canGens,ringX),
                                     DegreeMap => i -> 5*i)

2                                    2                                                                 2               2                                                                   2                     2                              2   3                     2                                       2         2   3           2        2                        2             2          2         3     2          2        2                       2            2          2        3
o74 = ideal (x x  + 16373x x  - 5733x  - 2813x x , x x  - 8190x x  + 2454x  + 15871x x , x x  - 5836x x  - 4040x x  - 2813x x  + 7504x x , x  - x x  + 1636x  - 11252x x , x x  + 4039x x  + 16062x x  + 15871x x  - 6553x x , x  - 14179x x  + 13145x  + 472x x  + 12845x x  - 9802x , x  + 4144x x x  + 6956x x  + 9223x x x  - 1704x x x  + 10100x x  - 549x x , x  + 13726x x  + 2361x x  + 4733x x x  - 13702x x  + 13978x x  + 6659x x  + 11450x , x x  + 7184x x  - 8490x x  - 9167x x x  + 1176x x  + 4091x x  - 1273x x  - 7651x )
              2 3         1 4        4        3 5   0 3        1 4        4         3 5   1 2        0 4        2 4        1 5        4 5   1    1 4        4         3 5   0 1        0 4         2 4         1 5        4 5   0         0 2         2       0 5         2 5        5   3        0 2 4        2 4        0 4 5        2 4 5         1 5       4 5   2         1 3        3 4        0 2 5         2 5         0 5        2 5         5   0 2        1 3        3 4        0 2 5        2 5        0 5        2 5        5

o74 : Ideal of ringP5

i75 : betti res idealXcan

0 1  2 3 4
o75 = total: 1 9 16 9 1
          0: 1 .  . . .
          1: . 6  8 3 .
          2: . 3  8 6 .
          3: . .  . . 1

o75 : BettiTally

i76 : deg2places = positions(degrees idealXcan, i->i=={2})

o76 = {0, 1, 2, 3, 4, 5}

o76 : List

i77 : idealS= ideal (gens idealXcan)_deg2places

2                                    2                                                                 2               2                                                                   2                     2                              2
o77 = ideal (x x  + 16373x x  - 5733x  - 2813x x , x x  - 8190x x  + 2454x  + 15871x x , x x  - 5836x x  - 4040x x  - 2813x x  + 7504x x , x  - x x  + 1636x  - 11252x x , x x  + 4039x x  + 16062x x  + 15871x x  - 6553x x , x  - 14179x x  + 13145x  + 472x x  + 12845x x  - 9802x )
              2 3         1 4        4        3 5   0 3        1 4        4         3 5   1 2        0 4        2 4        1 5        4 5   1    1 4        4         3 5   0 1        0 4         2 4         1 5        4 5   0         0 2         2       0 5         2 5        5

o77 : Ideal of ringP5

i78 : codim singularLocus idealS

o78 = 6

i79 : omegaS = prune Ext^(codim idealS)(ringP5^1/idealS, ringP5^{-6})

o79 = cokernel {2} | -5836x_4 0           x_0+15871x_5 x_2-2813x_5 x_1+4039x_4 0                     -11252x_5   0               |
               {2} | x_3      x_1+4039x_4 5287x_4      -8190x_4    0           x_0-14179x_2-15399x_5 16062x_4    13145x_2-110x_5 |
               {2} | 0        -5836x_4    -8190x_4     16373x_4    -x_3        -x_2+2813x_5          x_1-4040x_4 x_0+15871x_5    |

                                       3
o79 : ringP5-module, quotient of ringP5

i80 : OS = ringP5^1/idealS

o80 = cokernel | x_2x_3+16373x_1x_4-5733x_4^2-2813x_3x_5 x_0x_3-8190x_1x_4+2454x_4^2+15871x_3x_5 x_1x_2-5836x_0x_4-4040x_2x_4-2813x_1x_5+7504x_4x_5 x_1^2-x_1x_4+1636x_4^2-11252x_3x_5 x_0x_1+4039x_0x_4+16062x_2x_4+15871x_1x_5-6553x_4x_5 x_0^2-14179x_0x_2+13145x_2^2+472x_0x_5+12845x_2x_5-9802x_5^2 |

                                       1
o80 : ringP5-module, quotient of ringP5
```

---

## geometry / test.m2 — chunk 10

### Input

```macaulay2
omegaS**omegaS
omega2S = Hom(Hom(omegaS**omegaS, OS, MinimalGenerators => true), OS, MinimalGenerators => true)
L = Hom(omegaS, OS**(ringP5^{-1}), MinimalGenerators => true)
dualModule = Hom(L, OS, MinimalGenerators => true)
betti generators dualModule
g = homomorphism dualModule_{0}
toP2 = g*basis(0,L)
ringXcan = ringP5/idealXcan
```

### Output

```
i81 : omegaS**omegaS

o81 = cokernel {4} | -5836x_4 0           x_0+15871x_5 x_2-2813x_5 x_1+4039x_4 0                     -11252x_5   0               0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               -5836x_4 0           x_0+15871x_5 x_2-2813x_5 x_1+4039x_4 0                     -11252x_5   0               0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               |
               {4} | x_3      x_1+4039x_4 5287x_4      -8190x_4    0           x_0-14179x_2-15399x_5 16062x_4    13145x_2-110x_5 0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               -5836x_4 0           x_0+15871x_5 x_2-2813x_5 x_1+4039x_4 0                     -11252x_5   0               0        0           0            0           0           0                     0           0               |
               {4} | 0        -5836x_4    -8190x_4     16373x_4    -x_3        -x_2+2813x_5          x_1-4040x_4 x_0+15871x_5    0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               -5836x_4 0           x_0+15871x_5 x_2-2813x_5 x_1+4039x_4 0                     -11252x_5   0               |
               {4} | 0        0           0            0           0           0                     0           0               -5836x_4 0           x_0+15871x_5 x_2-2813x_5 x_1+4039x_4 0                     -11252x_5   0               0        0           0            0           0           0                     0           0               x_3      x_1+4039x_4 5287x_4      -8190x_4    0           x_0-14179x_2-15399x_5 16062x_4    13145x_2-110x_5 0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               |
               {4} | 0        0           0            0           0           0                     0           0               x_3      x_1+4039x_4 5287x_4      -8190x_4    0           x_0-14179x_2-15399x_5 16062x_4    13145x_2-110x_5 0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               x_3      x_1+4039x_4 5287x_4      -8190x_4    0           x_0-14179x_2-15399x_5 16062x_4    13145x_2-110x_5 0        0           0            0           0           0                     0           0               |
               {4} | 0        0           0            0           0           0                     0           0               0        -5836x_4    -8190x_4     16373x_4    -x_3        -x_2+2813x_5          x_1-4040x_4 x_0+15871x_5    0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               x_3      x_1+4039x_4 5287x_4      -8190x_4    0           x_0-14179x_2-15399x_5 16062x_4    13145x_2-110x_5 |
               {4} | 0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               -5836x_4 0           x_0+15871x_5 x_2-2813x_5 x_1+4039x_4 0                     -11252x_5   0               0        -5836x_4    -8190x_4     16373x_4    -x_3        -x_2+2813x_5          x_1-4040x_4 x_0+15871x_5    0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               |
               {4} | 0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               x_3      x_1+4039x_4 5287x_4      -8190x_4    0           x_0-14179x_2-15399x_5 16062x_4    13145x_2-110x_5 0        0           0            0           0           0                     0           0               0        -5836x_4    -8190x_4     16373x_4    -x_3        -x_2+2813x_5          x_1-4040x_4 x_0+15871x_5    0        0           0            0           0           0                     0           0               |
               {4} | 0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               0        -5836x_4    -8190x_4     16373x_4    -x_3        -x_2+2813x_5          x_1-4040x_4 x_0+15871x_5    0        0           0            0           0           0                     0           0               0        0           0            0           0           0                     0           0               0        -5836x_4    -8190x_4     16373x_4    -x_3        -x_2+2813x_5          x_1-4040x_4 x_0+15871x_5    |

                                       9
o81 : ringP5-module, quotient of ringP5

i82 : omega2S = Hom(Hom(omegaS**omegaS, OS, MinimalGenerators => true), OS, MinimalGenerators => true)

o82 = cokernel {3} | x_2x_3+16373x_1x_4-5733x_4^2-2813x_3x_5 x_0x_3-8190x_1x_4+2454x_4^2+15871x_3x_5 x_1x_2-5836x_0x_4-4040x_2x_4-2813x_1x_5+7504x_4x_5 x_1^2-x_1x_4+1636x_4^2-11252x_3x_5 x_0x_1+4039x_0x_4+16062x_2x_4+15871x_1x_5-6553x_4x_5 x_0^2-14179x_0x_2+13145x_2^2+472x_0x_5+12845x_2x_5-9802x_5^2 |

                                       1
o82 : ringP5-module, quotient of ringP5

i83 : L = Hom(omegaS, OS**(ringP5^{-1}), MinimalGenerators => true)

o83 = subquotient ({-1} | 10495x_1+6812x_4 x_3         -3207x_1-9028x_4      |, {-1} | x_2x_3+16373x_1x_4-5733x_4^2-2813x_3x_5 x_0x_3-8190x_1x_4+2454x_4^2+15871x_3x_5 x_1x_2-5836x_0x_4-4040x_2x_4-2813x_1x_5+7504x_4x_5 x_1^2-x_1x_4+1636x_4^2-11252x_3x_5 x_0x_1+4039x_0x_4+16062x_2x_4+15871x_1x_5-6553x_4x_5 x_0^2-14179x_0x_2+13145x_2^2+472x_0x_5+12845x_2x_5-9802x_5^2 0                                       0                                       0                                                  0                                  0                                                    0                                                            0                                       0                                       0                                                  0                                  0                                                    0                                                            |)
                   {-1} | x_0+15871x_5     5836x_4     x_2-2813x_5           |  {-1} | 0                                       0                                       0                                                  0                                  0                                                    0                                                            x_2x_3+16373x_1x_4-5733x_4^2-2813x_3x_5 x_0x_3-8190x_1x_4+2454x_4^2+15871x_3x_5 x_1x_2-5836x_0x_4-4040x_2x_4-2813x_1x_5+7504x_4x_5 x_1^2-x_1x_4+1636x_4^2-11252x_3x_5 x_0x_1+4039x_0x_4+16062x_2x_4+15871x_1x_5-6553x_4x_5 x_0^2-14179x_0x_2+13145x_2^2+472x_0x_5+12845x_2x_5-9802x_5^2 0                                       0                                       0                                                  0                                  0                                                    0                                                            |
                   {-1} | -13145x_2+110x_5 x_1+4039x_4 x_0-14179x_2-15399x_5 |  {-1} | 0                                       0                                       0                                                  0                                  0                                                    0                                                            0                                       0                                       0                                                  0                                  0                                                    0                                                            x_2x_3+16373x_1x_4-5733x_4^2-2813x_3x_5 x_0x_3-8190x_1x_4+2454x_4^2+15871x_3x_5 x_1x_2-5836x_0x_4-4040x_2x_4-2813x_1x_5+7504x_4x_5 x_1^2-x_1x_4+1636x_4^2-11252x_3x_5 x_0x_1+4039x_0x_4+16062x_2x_4+15871x_1x_5-6553x_4x_5 x_0^2-14179x_0x_2+13145x_2^2+472x_0x_5+12845x_2x_5-9802x_5^2 |

                                          3
o83 : ringP5-module, subquotient of ringP5

i84 : dualModule = Hom(L, OS, MinimalGenerators => true)

o84 = subquotient (| x_0+15871x_5 5460x_1-1636x_4 -13145x_2+110x_5      |, | x_2x_3+16373x_1x_4-5733x_4^2-2813x_3x_5 x_0x_3-8190x_1x_4+2454x_4^2+15871x_3x_5 x_1x_2-5836x_0x_4-4040x_2x_4-2813x_1x_5+7504x_4x_5 x_1^2-x_1x_4+1636x_4^2-11252x_3x_5 x_0x_1+4039x_0x_4+16062x_2x_4+15871x_1x_5-6553x_4x_5 x_0^2-14179x_0x_2+13145x_2^2+472x_0x_5+12845x_2x_5-9802x_5^2 0                                       0                                       0                                                  0                                  0                                                    0                                                            0                                       0                                       0                                                  0                                  0                                                    0                                                            |)
                   | 5836x_4      14807x_3        x_1+4039x_4           |  | 0                                       0                                       0                                                  0                                  0                                                    0                                                            x_2x_3+16373x_1x_4-5733x_4^2-2813x_3x_5 x_0x_3-8190x_1x_4+2454x_4^2+15871x_3x_5 x_1x_2-5836x_0x_4-4040x_2x_4-2813x_1x_5+7504x_4x_5 x_1^2-x_1x_4+1636x_4^2-11252x_3x_5 x_0x_1+4039x_0x_4+16062x_2x_4+15871x_1x_5-6553x_4x_5 x_0^2-14179x_0x_2+13145x_2^2+472x_0x_5+12845x_2x_5-9802x_5^2 0                                       0                                       0                                                  0                                  0                                                    0                                                            |
                   | x_2-2813x_5  x_1+3822x_4     x_0-14179x_2-15399x_5 |  | 0                                       0                                       0                                                  0                                  0                                                    0                                                            0                                       0                                       0                                                  0                                  0                                                    0                                                            x_2x_3+16373x_1x_4-5733x_4^2-2813x_3x_5 x_0x_3-8190x_1x_4+2454x_4^2+15871x_3x_5 x_1x_2-5836x_0x_4-4040x_2x_4-2813x_1x_5+7504x_4x_5 x_1^2-x_1x_4+1636x_4^2-11252x_3x_5 x_0x_1+4039x_0x_4+16062x_2x_4+15871x_1x_5-6553x_4x_5 x_0^2-14179x_0x_2+13145x_2^2+472x_0x_5+12845x_2x_5-9802x_5^2 |

                                          3
o84 : ringP5-module, subquotient of ringP5

i85 : betti generators dualModule

0 1
o85 = total: 3 3
          0: 3 3

o85 : BettiTally

i86 : g = homomorphism dualModule_{0}

o86 = | x_0+15871x_5 5836x_4 x_2-2813x_5 |

o86 : Matrix OS <-- L

i87 : toP2 = g*basis(0,L)

o87 = | x_0+15871x_5 5836x_4 x_2-2813x_5 |

                          3
o87 : Matrix OS <-- ringP5

i88 : ringXcan = ringP5/idealXcan

o88 = ringXcan

o88 : QuotientRing
```

---

## geometry / test.m2 — chunk 11

### Input

```macaulay2
ringP2 = kk[x_0..x_2]
idealXplane = trim kernel map(ringXcan, ringP2, 
                                        substitute(matrix toP2,ringXcan))
ringP2 = kk[x_0..x_2]
idealC2 = ideal(x_0^5+x_1^5+x_2^5)
ringC2 = ringP2/idealC2
ringP5 = kk[x_0..x_5]
idealC5 = trim kernel map(ringC2, ringP5, 
              gens (ideal vars ringC2)^2)
ringC5 = ringP5/idealC5
```

### Output

```
i89 : ringP2 = kk[x_0..x_2]

o89 = ringP2

o89 : PolynomialRing

i90 : idealXplane = trim kernel map(ringXcan, ringP2, 
                                        substitute(matrix toP2,ringXcan))

5        5         4         3 2        2 3          4         5
o90 = ideal(x  + 9034x  + 11794x x  + 775x x  - 5707x x  + 6069x x  + 15158x )
             0        1         0 2       0 2        0 2        0 2         2

o90 : Ideal of ringP2

i91 : ringP2 = kk[x_0..x_2]

o91 = ringP2

o91 : PolynomialRing

i92 : idealC2 = ideal(x_0^5+x_1^5+x_2^5)

5    5    5
o92 = ideal(x  + x  + x )
             0    1    2

o92 : Ideal of ringP2

i93 : ringC2 = ringP2/idealC2

o93 = ringC2

o93 : QuotientRing

i94 : ringP5 = kk[x_0..x_5]

o94 = ringP5

o94 : PolynomialRing

i95 : idealC5 = trim kernel map(ringC2, ringP5, 
              gens (ideal vars ringC2)^2)

2                                    2                       2          2      2      3   2      3      2   3      2      2
o95 = ideal (x  - x x , x x  - x x , x x  - x x , x  - x x , x x  - x x , x  - x x , x x  + x x  + x , x x  + x  + x x , x  + x x  + x x )
              4    3 5   2 4    1 5   2 3    1 4   2    0 5   1 2    0 4   1    0 3   0 2    3 4    5   0 1    3    4 5   0    1 3    2 5

o95 : Ideal of ringP5

i96 : ringC5 = ringP5/idealC5

o96 = ringC5

o96 : QuotientRing
```

---

## geometry / test.m2 — chunk 12

### Input

```macaulay2
use ringC5
idealC = trim kernel map(ringC5, ringP3,
              matrix{{x_0+x_1,x_2,x_3,x_5}})
idealC == idealX
code mystery
code prettyPrint
i102 :
```

### Output

```
i97 : use ringC5

o97 = ringC5

o97 : QuotientRing

i98 : idealC = trim kernel map(ringC5, ringP3,
              matrix{{x_0+x_1,x_2,x_3,x_5}})

4       2      2        2 2   2 2           2           3           2               2             3     2 2         4          3            2 2             3          3 2             3             3     3           3 2        3             2                  2             3           2 3           4   5     2 3       4       3       3         2   2            2       2 2   2 4        4             3 2          2 3            4      5         3 2        3   2    2   3              3          2 3    6
o98 = ideal (x  - 2x x x  - x x x  + x x , x x  - 10915x x x  - 10917x x  + 10916x x x  - 10916x x x  - 10916x x , x x x  + 11909x x  + 5954x x x  + 2977x x x  + 11910x x x  - 2978x x  + 14887x x x  + 11910x x x , x x x  - 13099x x  - 6550x x x  - 13100x x x x  - 6550x x x x  + 13099x x x  + 13100x x  + 13099x x , x  + 5x x  + 5x x  - 3x x x  - 4x x x  + 4x x x  + 10x x x x  + 5x x x , x x  - 8932x x x  + 11909x x x  + 5954x x x  - 8934x x x  - x x  + 2x x x  - 5952x x x  - x x x  - 2979x x x x  - 8934x x x  + x )
              1     0 1 3    1 2 3    0 3   0 1         0 1 2         0 3         0 2 3         0 2 3         1 3   0 1 2         0 3        0 2 3        0 2 3         0 2 3        1 3         0 1 3         1 2 3   0 1 2         1 2        0 1 3         0 1 2 3        0 1 2 3         1 2 3         1 3         0 3   0     0 2     0 2     0 1 3     1 2 3     0 1 3      0 1 2 3     1 2 3   1 2        0 2 3         0 2 3        0 2 3        0 2 3    2 3     0 1 3        1 2 3    0 1 3        0 1 2 3        1 2 3    3

o98 : Ideal of ringP3

i99 : idealC == idealX

o99 = true

i100 : code mystery

o100 = -- ../../../../../../Macaulay2/packages/ComputationsBook/geometry/mystery.m2:1-13
       mystery = ringP3 -> (
          kk := coefficientRing ringP3;
          x := local x;
          ringP2 := kk[x_0..x_2];
          idealC2 := ideal(x_0^5+x_1^5+x_2^5);
          ringC2 := ringP2/idealC2;
          ringP5 := kk[x_0..x_5];
          idealC5 := trim kernel map(ringC2, ringP5, 
               gens (ideal vars ringC2)^2);
          ringC5 := ringP5/idealC5;
          use ringC5;
          trim kernel map(ringC5, ringP3,
             matrix{{x_0+x_1,x_2,x_3,x_5}}))

i101 : code prettyPrint

o101 = -- ../../../../../../Macaulay2/packages/ComputationsBook/geometry/mystery.m2:15-51
       prettyPrint = f -> (
          -- accept a matrix f and print its entries prettily,
          -- separated by commas
          wid := 74;
          -- page width
          post := (c,s) -> (
             -- This function concatenates string c to end of each
             -- string in list s except the last one
             concatenate \ pack_2 between_c s);
          strings := post_"," (toString \ flatten entries f);
          -- list of strings, one for each polynomial, with commas
          istate := ("",0);
          -- initial state = (out : output string, col : column number)
          strings = apply(
             strings,
             poly -> first fold(
                -- break each poly into lines
                (state,term) -> (
                   (out,col) -> (
                      if col + #term > wid -- too wide?
                      then (
                         out = out | "\n   "; 
                         col = 3;
                         -- insert line break
                         );
                      (out | term, col + #term) -- new state
                      )
                   ) state,
                istate,
                fold( -- separate poly into terms 
                   {"+","-"},
                   {poly},
                   (delimiter,poly) -> (
                        delimiterEscaped := if delimiter === "+" then "\\+" else delimiter;
                        flatten(post_delimiter \ separate_delimiterEscaped \ poly)
                      ))));
          print stack strings;  -- stack them vertically, then print
          )

i102 :
```

---

## monomialIdeals / chapter.m2 — chunk 0

### Input

```macaulay2
S = QQ[a, b, c, d];
I = monomialIdeal(a^2, a*b, b^3, a*c)
J = monomialIdeal{a^2, a*b, b^2}
monomialIdeal(a^2+a*b, a*b+3, b^2+d)
K = ideal(a^2, b^2, a*b+b*c)
monomialIdeal K
monomialIdeal gens K
isMonomialIdeal K
```

### Output

```
i1 : S = QQ[a, b, c, d];

i2 : I = monomialIdeal(a^2, a*b, b^3, a*c)

2        3
o2 = monomialIdeal (a , a*b, b , a*c)

o2 : MonomialIdeal of S

i3 : J = monomialIdeal{a^2, a*b, b^2}

2        2
o3 = monomialIdeal (a , a*b, b )

o3 : MonomialIdeal of S

i4 : monomialIdeal(a^2+a*b, a*b+3, b^2+d)

2        2
o4 = monomialIdeal (a , a*b, b )

o4 : MonomialIdeal of S

i5 : K = ideal(a^2, b^2, a*b+b*c)

2   2
o5 = ideal (a , b , a*b + b*c)

o5 : Ideal of S

i6 : monomialIdeal K

2        2     2
o6 = monomialIdeal (a , a*b, b , b*c )

o6 : MonomialIdeal of S

i7 : monomialIdeal gens K

2        2
o7 = monomialIdeal (a , a*b, b )

o7 : MonomialIdeal of S

i8 : isMonomialIdeal K

o8 = false
```

---

## monomialIdeals / chapter.m2 — chunk 1

### Input

```macaulay2
isMonomialIdeal ideal(a^5, b^2*c, d^11)
I+J
fvector = I -> (
           R := (ring I)/I;
           d := dim R;
           N := poincare R;
           t := first gens ring N;
           while 0 == substitute(N, t => 1) do N = N // (1-t);
           h := apply(reverse toList(0..d), i -> N_(t^i));
           f := j -> sum(0..j+1, i -> binomial(d-i, j+1-i)*h#(d-i));
           apply(toList(0..d-1), j -> f(j)));
S = QQ[x_1 .. x_6];
octahedron = monomialIdeal(x_1*x_2, x_3*x_4, x_5*x_6)
fvector octahedron
simplicial2sphere = v -> ( 
           S := QQ[x_1..x_v]; 
           if v === 4 then monomialIdeal product gens S 
           else ( 
                L := {};
                scan(1..v-4, i -> L = L | apply(v-i-3, 
                          j -> x_i*x_(i+j+4))); 
                scan(2..v-3, i -> L = L | {x_i*x_(i+1)*x_(i+2)}); 
                monomialIdeal L));
apply({4,5,6,7,8}, j -> fvector simplicial2sphere(j))
```

### Output

```
i9 : isMonomialIdeal ideal(a^5, b^2*c, d^11)

o9 = true

i10 : I+J

2        2
o10 = monomialIdeal (a , a*b, b , a*c)

o10 : MonomialIdeal of S

i11 : fvector = I -> (
           R := (ring I)/I;
           d := dim R;
           N := poincare R;
           t := first gens ring N;
           while 0 == substitute(N, t => 1) do N = N // (1-t);
           h := apply(reverse toList(0..d), i -> N_(t^i));
           f := j -> sum(0..j+1, i -> binomial(d-i, j+1-i)*h#(d-i));
           apply(toList(0..d-1), j -> f(j)));

i12 : S = QQ[x_1 .. x_6];

i13 : octahedron = monomialIdeal(x_1*x_2, x_3*x_4, x_5*x_6)

o13 = monomialIdeal (x x , x x , x x )
                      1 2   3 4   5 6

o13 : MonomialIdeal of S

i14 : fvector octahedron

o14 = {6, 12, 8}

o14 : List

i15 : simplicial2sphere = v -> ( 
           S := QQ[x_1..x_v]; 
           if v === 4 then monomialIdeal product gens S 
           else ( 
                L := {};
                scan(1..v-4, i -> L = L | apply(v-i-3, 
                          j -> x_i*x_(i+j+4))); 
                scan(2..v-3, i -> L = L | {x_i*x_(i+1)*x_(i+2)}); 
                monomialIdeal L));

i16 : apply({4,5,6,7,8}, j -> fvector simplicial2sphere(j))

o16 = {{4, 6, 4}, {5, 9, 6}, {6, 12, 8}, {7, 15, 10}, {8, 18, 12}}

o16 : List
```

---

## monomialIdeals / chapter.m2 — chunk 2

### Input

```macaulay2
supp = r -> select(gens ring r, e -> r % e == 0);
monomialDecompose = method();
monomialDecompose List := L -> (
           P := select(L, I -> all(first entries gens I, 
                     r -> #supp(r) < 2) === false);
           if #P > 0 then (
                I := first P;
                m := first select(first entries gens I, 
                     r -> #supp(r) > 1);
                E := first exponents m;
                i := position(E, e -> e =!= 0);
                r1 := product apply(E_{0..i}, (gens ring I)_{0..i}, 
                     (j, r) -> r^j);
                r2 := m // r1;
                monomialDecompose(delete(I, L) | {I+monomialIdeal(r1),
                          I+monomialIdeal(r2)}))
           else L);
monomialDecompose MonomialIdeal := I -> monomialDecompose {I};
S = QQ[a,b,c,d];
I = monomialIdeal(a^3*b, a^3*c, a*b^3, b^3*c, a*c^3, b*c^3)
P = monomialDecompose I;
scan(P, J -> << endl << J << endl);
```

### Output

```
i17 : supp = r -> select(gens ring r, e -> r % e == 0);

i18 : monomialDecompose = method();

i19 : monomialDecompose List := L -> (
           P := select(L, I -> all(first entries gens I, 
                     r -> #supp(r) < 2) === false);
           if #P > 0 then (
                I := first P;
                m := first select(first entries gens I, 
                     r -> #supp(r) > 1);
                E := first exponents m;
                i := position(E, e -> e =!= 0);
                r1 := product apply(E_{0..i}, (gens ring I)_{0..i}, 
                     (j, r) -> r^j);
                r2 := m // r1;
                monomialDecompose(delete(I, L) | {I+monomialIdeal(r1),
                          I+monomialIdeal(r2)}))
           else L);

i20 : monomialDecompose MonomialIdeal := I -> monomialDecompose {I};

i21 : S = QQ[a,b,c,d];

i22 : I = monomialIdeal(a^3*b, a^3*c, a*b^3, b^3*c, a*c^3, b*c^3)

3      3   3    3      3     3
o22 = monomialIdeal (a b, a*b , a c, b c, a*c , b*c )

o22 : MonomialIdeal of S

i23 : P = monomialDecompose I;

i24 : scan(P, J -> << endl << J << endl);

monomialIdeal (b, c)

monomialIdeal (a, c)

                3   3   3
monomialIdeal (a , b , c )

monomialIdeal (a, b)

                3      3
monomialIdeal (a , b, c )

monomialIdeal (a, b)

                   3   3
monomialIdeal (a, b , c )
```

---

## monomialIdeals / chapter.m2 — chunk 3

### Input

```macaulay2
I == intersect(P)
code(dual, MonomialIdeal, List)
code(primaryDecomposition, MonomialIdeal)
L = primaryDecomposition I;
scan(L, J -> << endl << J << endl);
I == intersect L
treeIdeal = n -> (
           S = QQ[vars(0..n-1)];
           L := delete({}, subsets gens S);
           monomialIdeal apply(L, F -> (product F)^(n - #F +1)));
apply(2..6, i -> #primaryDecomposition treeIdeal i)
```

### Output

```
i25 : I == intersect(P)

o25 = true

i26 : code(dual, MonomialIdeal, List)

o26 = -- ../../../m2/monideal.m2:260-278
      dual(MonomialIdeal, List) := (I,a) -> ( -- Alexander dual
           R := ring I;
           X := gens R;
           aI := lcmOfGens I;
           if aI =!= a then (
                if #aI =!= #a 
                then error (
                     "expected list of length ",
                     toString (#aI));
                scan(a, aI, 
                     (b,c) -> (
                          if b<c then
                          error "exponent vector not large enough"
                          ));
                ); 
           S := R/(I + monomialIdeal apply(#X, i -> X#i^(a#i+1)));
           monomialIdeal contract(
                lift(syz transpose vars S, R), 
                product(#X, i -> X#i^(a#i))))

i27 : code(primaryDecomposition, MonomialIdeal)

o27 = -- ../../../m2/monideal.m2:286-295
      primaryDecomposition MonomialIdeal := (I) -> (
           R := ring I;
           aI := lcmOfGens I;
           M := first entries gens dual I;
           L := unique apply(#M, i -> first exponents M_i);
           apply(L, i -> monomialIdeal apply(#i, j -> ( 
                          if i#j === 0 then 0_R 
                          else R_j^(aI#j+1-i#j)
                          )))
           )

i28 : L = primaryDecomposition I;

i29 : scan(L, J -> << endl << J << endl);

3   3   3
monomialIdeal (a , b , c )

monomialIdeal (b, c)

monomialIdeal (a, b)

monomialIdeal (a, c)

i30 : I == intersect L

o30 = true

i31 : treeIdeal = n -> (
           S = QQ[vars(0..n-1)];
           L := delete({}, subsets gens S);
           monomialIdeal apply(L, F -> (product F)^(n - #F +1)));

i32 : apply(2..6, i -> #primaryDecomposition treeIdeal i)

o32 = (2, 6, 24, 120, 720)

o32 : Sequence
```

---

## monomialIdeals / chapter.m2 — chunk 4

### Input

```macaulay2
minorsIdeal = (m,n,k) -> (
           S := QQ[x_1..x_(m*n), MonomialOrder => Lex];
           I := minors(k, matrix table(m, n, (i,j) -> x_(i*n+n-j)));
           forceGB gens I;
           I);
apply(2..8, i -> time codim monomialIdeal minorsIdeal(i,2*i,2))
     -- used 0.02 seconds
     -- used 0.05 seconds
     -- used 0.1 seconds
     -- used 0.36 seconds
     -- used 1.41 seconds
     -- used 5.94 seconds
     -- used 25.51 seconds
erase symbol x;
stdPairs = I -> (
           S := ring I;
           X := gens S;
           std := {};
           J := I;
           while J != S do (
                w1 := 1_S;
                F := X;
                K := J;
                while K != 0 do (
                     g1 := (ideal mingens ideal K)_0;
                     x := first supp g1;
                     w1 = w1 * g1 // x;
                     F = delete(x, F);
                     K = K : monomialIdeal(g1 // x);
                     L := select(first entries gens K, 
                          r -> not member(x, supp r));
                     if #L > 0 then K = monomialIdeal L
                     else K = monomialIdeal 0_S;);
                w2 := w1;
                scan(X, r -> if not member(r, supp w1) or member(r, F)
                     then w2 = substitute(w2, {r => 1}));
                P := monomialIdeal select(X, r -> not member(r, F));
                if (I:(I:P) == P) and (all(std, p -> 
                          (w2 % (first p) != 0) or not
                          isSubset(supp(w2 // first p) | F, last p)))
                then std = std | {{w2, F}};
                J = J + monomialIdeal(w1););
           std);
S = QQ[x,y,z];
I = monomialIdeal(x*y^3*z, x*y^2*z^2, y^3*z^2, y^2*z^3);
scan(time stdPairs I, P -> << endl << P << endl);
     -- used 0.66 seconds
code(standardPairs, MonomialIdeal, List)
```

### Output

```
i33 : minorsIdeal = (m,n,k) -> (
           S := QQ[x_1..x_(m*n), MonomialOrder => Lex];
           I := minors(k, matrix table(m, n, (i,j) -> x_(i*n+n-j)));
           forceGB gens I;
           I);

i34 : apply(2..8, i -> time codim monomialIdeal minorsIdeal(i,2*i,2))
     -- used 0.02 seconds
     -- used 0.05 seconds
     -- used 0.1 seconds
     -- used 0.36 seconds
     -- used 1.41 seconds
     -- used 5.94 seconds
     -- used 25.51 seconds

o34 = (3, 10, 21, 36, 55, 78, 105)

o34 : Sequence

i35 : erase symbol x;

i36 : stdPairs = I -> (
           S := ring I;
           X := gens S;
           std := {};
           J := I;
           while J != S do (
                w1 := 1_S;
                F := X;
                K := J;
                while K != 0 do (
                     g1 := (ideal mingens ideal K)_0;
                     x := first supp g1;
                     w1 = w1 * g1 // x;
                     F = delete(x, F);
                     K = K : monomialIdeal(g1 // x);
                     L := select(first entries gens K, 
                          r -> not member(x, supp r));
                     if #L > 0 then K = monomialIdeal L
                     else K = monomialIdeal 0_S;);
                w2 := w1;
                scan(X, r -> if not member(r, supp w1) or member(r, F)
                     then w2 = substitute(w2, {r => 1}));
                P := monomialIdeal select(X, r -> not member(r, F));
                if (I:(I:P) == P) and (all(std, p -> 
                          (w2 % (first p) != 0) or not
                          isSubset(supp(w2 // first p) | F, last p)))
                then std = std | {{w2, F}};
                J = J + monomialIdeal(w1););
           std);

i37 : S = QQ[x,y,z];

i38 : I = monomialIdeal(x*y^3*z, x*y^2*z^2, y^3*z^2, y^2*z^3);

o38 : MonomialIdeal of S

i39 : scan(time stdPairs I, P -> << endl << P << endl);
     -- used 0.66 seconds

{y, {x, z}}

{1, {x, z}}

  2 2
{y z , {}}

{z, {y}}

  2
{y z, {x}}

{1, {x, y}}

i40 : code(standardPairs, MonomialIdeal, List)

o40 = -- ../../../m2/monideal.m2:318-341
      standardPairs(MonomialIdeal, List) := (I,D) -> (
           R := ring I;
           X := gens R;
           S := {};
           k := coefficientRing R;
           scan(D, L -> ( 
                     Y := X;
                     m := vars R;
                     Lset := set L;
                     Y = select(Y, r -> not Lset#?r);
                     m = substitute(m, apply(L, r -> r => 1));
                     -- using monoid to create ring to avoid 
                     -- changing global ring.
                     A := k (monoid [Y]);
                     phi := map(A, R, substitute(m, A));
                     J := ideal mingens ideal phi gens I;
                     Jsat := saturate(J, ideal vars A);
                     if Jsat != J then (
                          B := flatten entries super basis (
                               trim (Jsat / J));
                          psi := map(R, A, matrix{Y});
                          S = join(S, apply(B, b -> {psi(b), L}));
                          )));
           S)
```

---

## monomialIdeals / chapter.m2 — chunk 5

### Input

```macaulay2
time standardPairs I;
     -- used 0.83 seconds
permutohedronIdeal = n -> (
           S := QQ[X_1..X_n];
           monomialIdeal terms det matrix table(n ,gens S, 
                (i,r) -> r^(i+1)));
L = apply({2,3,4,5}, j -> standardPairs(permutohedronIdeal(j)));
apply(L, i -> #i)
erase symbol x; erase symbol z;
toBinomial = (b, S) -> (
           pos := 1_S;
           neg := 1_S;
           scan(#b, i -> if b_i > 0 then pos = pos*S_i^(b_i)
                         else if b_i < 0 then neg = neg*S_i^(-b_i));
           pos - neg);
toricIdeal = (A, omega) -> (
           n := rank source A;
           S = QQ[x_1..x_n, Weights => omega, MonomialSize => 16];
           B := transpose matrix syz A;
           J := ideal apply(entries B, b -> toBinomial(b, S));
           scan(gens S, r -> J = saturate(J, r));
           J);
IP = (A, omega, beta) -> (
           std := standardPairs monomialIdeal toricIdeal(A, omega);
           n := rank source A;
           alpha := {};
           Q := first select(1, std, P -> (
                F := apply(last P, r -> index r);
                gamma := transpose matrix exponents first P;
                K := transpose syz (submatrix(A,F) | (A*gamma-beta));
                X := select(entries K, k -> abs last(k) === 1);
                scan(X, k -> if all(k, j -> j>=0) or all(k, j -> j<=0)
                     then alpha = apply(n, j -> if member(j, F) 
                          then last(k)*k_(position(F, i -> i === j))
                          else 0));
                #alpha > 0));
           if #Q > 0 then (matrix {alpha})+(matrix exponents first Q)
           else 0);
```

### Output

```
i41 : time standardPairs I;
     -- used 0.83 seconds

i42 : permutohedronIdeal = n -> (
           S := QQ[X_1..X_n];
           monomialIdeal terms det matrix table(n ,gens S, 
                (i,r) -> r^(i+1)));

i43 : L = apply({2,3,4,5}, j -> standardPairs(permutohedronIdeal(j)));

i44 : apply(L, i -> #i)

o44 = {3, 10, 53, 446}

o44 : List

i45 : erase symbol x; erase symbol z;

i47 : toBinomial = (b, S) -> (
           pos := 1_S;
           neg := 1_S;
           scan(#b, i -> if b_i > 0 then pos = pos*S_i^(b_i)
                         else if b_i < 0 then neg = neg*S_i^(-b_i));
           pos - neg);

i48 : toricIdeal = (A, omega) -> (
           n := rank source A;
           S = QQ[x_1..x_n, Weights => omega, MonomialSize => 16];
           B := transpose matrix syz A;
           J := ideal apply(entries B, b -> toBinomial(b, S));
           scan(gens S, r -> J = saturate(J, r));
           J);

i49 : IP = (A, omega, beta) -> (
           std := standardPairs monomialIdeal toricIdeal(A, omega);
           n := rank source A;
           alpha := {};
           Q := first select(1, std, P -> (
                F := apply(last P, r -> index r);
                gamma := transpose matrix exponents first P;
                K := transpose syz (submatrix(A,F) | (A*gamma-beta));
                X := select(entries K, k -> abs last(k) === 1);
                scan(X, k -> if all(k, j -> j>=0) or all(k, j -> j<=0)
                     then alpha = apply(n, j -> if member(j, F) 
                          then last(k)*k_(position(F, i -> i === j))
                          else 0));
                #alpha > 0));
           if #Q > 0 then (matrix {alpha})+(matrix exponents first Q)
           else 0);
```

---

## monomialIdeals / chapter.m2 — chunk 6

### Input

```macaulay2
A = matrix{{1,1,1,1,1},{1,2,4,5,6}}
w1 = {1,1,1,1,1};
w2 = {2,3,5,7,11};
b1 = transpose matrix{{3,9}}
b2 = transpose matrix{{5,16}}
IP(A, w1, b1)
IP(A, w2, b1)
IP(A, w1, b2)
```

### Output

```
i50 : A = matrix{{1,1,1,1,1},{1,2,4,5,6}}

o50 = | 1 1 1 1 1 |
      | 1 2 4 5 6 |

               2        5
o50 : Matrix ZZ  <--- ZZ

i51 : w1 = {1,1,1,1,1};

i52 : w2 = {2,3,5,7,11};

i53 : b1 = transpose matrix{{3,9}}

o53 = | 3 |
      | 9 |

               2        1
o53 : Matrix ZZ  <--- ZZ

i54 : b2 = transpose matrix{{5,16}}

o54 = | 5  |
      | 16 |

               2        1
o54 : Matrix ZZ  <--- ZZ

i55 : IP(A, w1, b1)

o55 = | 1 1 0 0 1 |

               1        5
o55 : Matrix ZZ  <--- ZZ

i56 : IP(A, w2, b1)

o56 = | 1 0 2 0 0 |

               1        5
o56 : Matrix ZZ  <--- ZZ

i57 : IP(A, w1, b2)

o57 = | 2 1 0 0 2 |

               1        5
o57 : Matrix ZZ  <--- ZZ
```

---

## monomialIdeals / chapter.m2 — chunk 7

### Input

```macaulay2
IP(A, w2, b2)
S = QQ[a,b,c,d];
isBorel monomialIdeal(a^2, a*b, b^2)
isBorel monomialIdeal(a^2, b^2)
borel monomialIdeal(b*c)
borel monomialIdeal(a,c^3)
gin = method();
gin Ideal := I -> (
           S := ring I;
           StoS := map(S, S, random(S^{0}, S^{numgens S:-1}));
           monomialIdeal StoS I);
```

### Output

```
i58 : IP(A, w2, b2)

o58 = | 2 0 1 2 0 |

               1        5
o58 : Matrix ZZ  <--- ZZ

i59 : S = QQ[a,b,c,d];

i60 : isBorel monomialIdeal(a^2, a*b, b^2)

o60 = true

i61 : isBorel monomialIdeal(a^2, b^2)

o61 = false

i62 : borel monomialIdeal(b*c)

2        2
o62 = monomialIdeal (a , a*b, b , a*c, b*c)

o62 : MonomialIdeal of S

i63 : borel monomialIdeal(a,c^3)

3   2      2   3
o63 = monomialIdeal (a, b , b c, b*c , c )

o63 : MonomialIdeal of S

i64 : gin = method();

i65 : gin Ideal := I -> (
           S := ring I;
           StoS := map(S, S, random(S^{0}, S^{numgens S:-1}));
           monomialIdeal StoS I);
```

---

## monomialIdeals / chapter.m2 — chunk 8

### Input

```macaulay2
gin MonomialIdeal := I -> gin ideal I;
genericForms = (p,q) -> ideal(random(p,S), random(q,S));
gin genericForms(2,2)
gin genericForms(2,3)
J = ideal(a^2, a*b+b^2, a*c)
ginJ = gin J
inJ = monomialIdeal J
isBorel inJ and isBorel ginJ
```

### Output

```
i66 : gin MonomialIdeal := I -> gin ideal I;

i67 : genericForms = (p,q) -> ideal(random(p,S), random(q,S));

i68 : gin genericForms(2,2)

2        3
o68 = monomialIdeal (a , a*b, b )

o68 : MonomialIdeal of S

i69 : gin genericForms(2,3)

2     2   4
o69 = monomialIdeal (a , a*b , b )

o69 : MonomialIdeal of S

i70 : J = ideal(a^2, a*b+b^2, a*c)

2         2
o70 = ideal (a , a*b + b , a*c)

o70 : Ideal of S

i71 : ginJ = gin J

2        2     2
o71 = monomialIdeal (a , a*b, b , a*c )

o71 : MonomialIdeal of S

i72 : inJ = monomialIdeal J

2        3        2
o72 = monomialIdeal (a , a*b, b , a*c, b c)

o72 : MonomialIdeal of S

i73 : isBorel inJ and isBorel ginJ

o73 = true
```

---

## monomialIdeals / chapter.m2 — chunk 9

### Input

```macaulay2
S = QQ[a,b,c,d, MonomialOrder => Lex];
gin genericForms(2,2)
gin genericForms(2,3)
projection = I -> (
           S := ring I;
           n := numgens S;
           X := gens S;
           monomialIdeal mingens substitute(ideal I, 
                {X#(n-2) => 1, X#(n-1) => 1}));
polarization = I -> (
           n := numgens ring I;
           u := apply(numgens I, i -> first exponents I_i);
           I.lcm = max \ transpose u;
           Z := flatten apply(n, i -> apply(I.lcm#i, j -> z_{i,j}));
           R := QQ(monoid[Z]);
           Z = gens R;
           p := apply(n, i -> sum((I.lcm)_{0..i-1}));
           monomialIdeal apply(u, e -> product apply(n, i -> 
                     product(toList(0..e#i-1), j -> Z#(p#i+j)))));
distraction = I -> (
           S := ring I;
           n := numgens S;
           X := gens S;
           J := polarization I;
           W := flatten apply(n, i -> flatten apply(I.lcm#i, 
                     j -> X#i));
           section := map(S, ring J, apply(W, r -> r - 
                     random(500)*X#(n-2) - random(500)*X#(n-1)));     
           section ideal J);
S = QQ[x_0 .. x_4, MonomialOrder => GLex];
I = monomialIdeal(x_0^2, x_0*x_1^2*x_3, x_1^3*x_4)
```

### Output

```
i74 : S = QQ[a,b,c,d, MonomialOrder => Lex];

i75 : gin genericForms(2,2)

2        4     2
o75 = monomialIdeal (a , a*b, b , a*c )

o75 : MonomialIdeal of S

i76 : gin genericForms(2,3)

2     2   6       2     6         2       4
o76 = monomialIdeal (a , a*b , b , a*b*c , a*c , a*b*c*d , a*b*d )

o76 : MonomialIdeal of S

i77 : projection = I -> (
           S := ring I;
           n := numgens S;
           X := gens S;
           monomialIdeal mingens substitute(ideal I, 
                {X#(n-2) => 1, X#(n-1) => 1}));

i78 : polarization = I -> (
           n := numgens ring I;
           u := apply(numgens I, i -> first exponents I_i);
           I.lcm = max \ transpose u;
           Z := flatten apply(n, i -> apply(I.lcm#i, j -> z_{i,j}));
           R := QQ(monoid[Z]);
           Z = gens R;
           p := apply(n, i -> sum((I.lcm)_{0..i-1}));
           monomialIdeal apply(u, e -> product apply(n, i -> 
                     product(toList(0..e#i-1), j -> Z#(p#i+j)))));

i79 : distraction = I -> (
           S := ring I;
           n := numgens S;
           X := gens S;
           J := polarization I;
           W := flatten apply(n, i -> flatten apply(I.lcm#i, 
                     j -> X#i));
           section := map(S, ring J, apply(W, r -> r - 
                     random(500)*X#(n-2) - random(500)*X#(n-1)));     
           section ideal J);

i80 : S = QQ[x_0 .. x_4, MonomialOrder => GLex];

i81 : I = monomialIdeal(x_0^2, x_0*x_1^2*x_3, x_1^3*x_4)

2     2     3
o81 = monomialIdeal (x , x x x , x x )
                      0   0 1 3   1 4

o81 : MonomialIdeal of S
```

---

## monomialIdeals / chapter.m2 — chunk 10

### Input

```macaulay2
projection I
polarization I
distraction I
m =  matrix table({0,1,2}, {0,1,2}, (i,j) -> (gens S)#(i+j))
rationalQuartic = minors(2, m);
H = hilbertPolynomial(S/rationalQuartic);
hilbertPolynomial(S/rationalQuartic, Projective => false)
L = {monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_1^2, x_1*x_2, x_2^2), monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_0*x_3, x_1^2, x_1*x_2, x_2^3), monomialIdeal(x_0, x_1^2, x_1*x_2^2, x_1*x_2*x_3, x_2^3), monomialIdeal(x_0, x_1^2, x_1*x_2, x_2^4, x_2^3*x_3), monomialIdeal(x_0, x_1, x_2^5, x_2^4*x_3^3), monomialIdeal(x_0, x_1^2, x_1*x_2, x_1*x_3, x_2^5, x_2^4*x_3^2), monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_0*x_3, x_1^2, x_1*x_2, x_1*x_3, x_2^5, x_2^4*x_3), monomialIdeal(x_0, x_1^2, x_1*x_2, x_1*x_3^2, x_2^5, x_2^4*x_3), monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_0*x_3, x_1^2, x_1*x_2, x_1*x_3^2, x_2^4), monomialIdeal(x_0, x_1^2, x_1*x_2^2, x_1*x_2*x_3, x_1*x_3^2, x_2^4), monomialIdeal(x_0, x_1^2, x_1*x_2, x_1*x_3^3, x_2^4), monomialIdeal(x_0, x_1, x_2^6, x_2^5*x_3, x_2^4*x_3^2)};
```

### Output

```
i82 : projection I

2     2   3
o82 = monomialIdeal (x , x x , x )
                      0   0 1   1

o82 : MonomialIdeal of S

i83 : polarization I

o83 = monomialIdeal (z      z      , z      z      z      z      , z      z      z      z      )
                      {0, 0} {0, 1}   {0, 0} {1, 0} {1, 1} {3, 0}   {1, 0} {1, 1} {1, 2} {4, 0}

o83 : MonomialIdeal of QQ [z      , z      , z      , z      , z      , z      , z      ]
                            {0, 0}   {0, 1}   {1, 0}   {1, 1}   {1, 2}   {3, 0}   {4, 0}

i84 : distraction I

2                             2                     2          2          2                2                              2             3              2                  2              3         2 2          2             2 2              3               2                   2              3             4               3                 2 2                 3              4       3         3           2 2          2              2 2              3              2                   2              3             4              3                 2 2                 3              4
o84 = ideal (x  - 398x x  - 584x x  + 36001x  + 92816x x  + 47239x , - 322x x x  - 83x x x  + 152950x x x  + 335987x x x x  + 76443x x x  - 1789032x x  - 67481906x x x  - 85381113x x x  - 17555164x x  + 83398x x  + 178311x x x  + 40421x x  - 39614050x x  - 161507283x x x  - 183424406x x x  - 37227741x x  + 463359288x  + 18349072238x x  + 54977396489x x  + 46127389507x x  + 8549364868x , - 85x x  - 109x x  + 82790x x  + 193801x x x  + 112379x x  - 20619385x x  - 87638609x x x  - 105066042x x x  - 34097162x x  + 235657740x  + 9182360681x x  + 22304716259x x  + 15977318038x x  + 2535980920x )
              0       0 3       0 4         3         3 4         4        0 1 3      0 1 4          0 1 3          0 1 3 4         0 1 4           0 3            0 3 4            0 3 4            0 4         1 3          1 3 4         1 4            1 3             1 3 4             1 3 4            1 4             3               3 4               3 4               3 4              4       1 3       1 4         1 3          1 3 4          1 4            1 3            1 3 4             1 3 4            1 4             3              3 4               3 4               3 4              4

o84 : Ideal of S

i85 : m =  matrix table({0,1,2}, {0,1,2}, (i,j) -> (gens S)#(i+j))

o85 = | x_0 x_1 x_2 |
      | x_1 x_2 x_3 |
      | x_2 x_3 x_4 |

              3       3
o85 : Matrix S  <--- S

i86 : rationalQuartic = minors(2, m);

o86 : Ideal of S

i87 : H = hilbertPolynomial(S/rationalQuartic);

i88 : hilbertPolynomial(S/rationalQuartic, Projective => false)

o88 = 4$i + 1

o88 : QQ [$i]

i89 : L = {monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_1^2, x_1*x_2, x_2^2), monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_0*x_3, x_1^2, x_1*x_2, x_2^3), monomialIdeal(x_0, x_1^2, x_1*x_2^2, x_1*x_2*x_3, x_2^3), monomialIdeal(x_0, x_1^2, x_1*x_2, x_2^4, x_2^3*x_3), monomialIdeal(x_0, x_1, x_2^5, x_2^4*x_3^3), monomialIdeal(x_0, x_1^2, x_1*x_2, x_1*x_3, x_2^5, x_2^4*x_3^2), monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_0*x_3, x_1^2, x_1*x_2, x_1*x_3, x_2^5, x_2^4*x_3), monomialIdeal(x_0, x_1^2, x_1*x_2, x_1*x_3^2, x_2^5, x_2^4*x_3), monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_0*x_3, x_1^2, x_1*x_2, x_1*x_3^2, x_2^4), monomialIdeal(x_0, x_1^2, x_1*x_2^2, x_1*x_2*x_3, x_1*x_3^2, x_2^4), monomialIdeal(x_0, x_1^2, x_1*x_2, x_1*x_3^3, x_2^4), monomialIdeal(x_0, x_1, x_2^6, x_2^5*x_3, x_2^4*x_3^2)};
```

---

## monomialIdeals / chapter.m2 — chunk 11

### Input

```macaulay2
scan(#L, i -> << endl << i+1 << " : " << L#i << endl);
all(L, I -> isBorel I and hilbertPolynomial(S/I) == H)
class1 = projection L#0
class2 = projection L#1
class3 = projection L#4
all(1..3, i -> projection L#i == class2)
all(4..11, i -> projection L#i == class3)
all(L, I -> I == monomialIdeal distraction I)
```

### Output

```
i90 : scan(#L, i -> << endl << i+1 << " : " << L#i << endl);

2         2               2
1 : monomialIdeal (x , x x , x , x x , x x , x )
                    0   0 1   1   0 2   1 2   2

                    2         2               3
2 : monomialIdeal (x , x x , x , x x , x x , x , x x )
                    0   0 1   1   0 2   1 2   2   0 3

                        2     2   3
3 : monomialIdeal (x , x , x x , x , x x x )
                    0   1   1 2   2   1 2 3

                        2         4   3
4 : monomialIdeal (x , x , x x , x , x x )
                    0   1   1 2   2   2 3

                            5   4 3
5 : monomialIdeal (x , x , x , x x )
                    0   1   2   2 3

                        2         5         4 2
6 : monomialIdeal (x , x , x x , x , x x , x x )
                    0   1   1 2   2   1 3   2 3

                    2         2               5               4
7 : monomialIdeal (x , x x , x , x x , x x , x , x x , x x , x x )
                    0   0 1   1   0 2   1 2   2   0 3   1 3   2 3

                        2         5   4       2
8 : monomialIdeal (x , x , x x , x , x x , x x )
                    0   1   1 2   2   2 3   1 3

                    2         2               4           2
9 : monomialIdeal (x , x x , x , x x , x x , x , x x , x x )
                    0   0 1   1   0 2   1 2   2   0 3   1 3

                         2     2   4             2
10 : monomialIdeal (x , x , x x , x , x x x , x x )
                     0   1   1 2   2   1 2 3   1 3

                         2         4     3
11 : monomialIdeal (x , x , x x , x , x x )
                     0   1   1 2   2   1 3

                             6   5     4 2
12 : monomialIdeal (x , x , x , x x , x x )
                     0   1   2   2 3   2 3

i91 : all(L, I -> isBorel I and hilbertPolynomial(S/I) == H)

o91 = true

i92 : class1 = projection L#0

2         2               2
o92 = monomialIdeal (x , x x , x , x x , x x , x )
                      0   0 1   1   0 2   1 2   2

o92 : MonomialIdeal of S

i93 : class2 = projection L#1

2         3
o93 = monomialIdeal (x , x , x x , x )
                      0   1   1 2   2

o93 : MonomialIdeal of S

i94 : class3 = projection L#4

4
o94 = monomialIdeal (x , x , x )
                      0   1   2

o94 : MonomialIdeal of S

i95 : all(1..3, i -> projection L#i == class2)

o95 = true

i96 : all(4..11, i -> projection L#i == class3)

o96 = true

i97 : all(L, I -> I == monomialIdeal distraction I)

o97 = true
```

---

## monomialIdeals / chapter.m2 — chunk 12

### Input

```macaulay2
all(0..3, i -> projection gin distraction L#i == class3)
hasChainProperty = I -> (
           L := ass I;
           radI := radical I;
           all(L, P -> radI : (radI : P) == P or (
                     gensP := first entries gens P;
                     all(gensP, r -> (
                               Q := monomialIdeal delete(r, gensP);
                               I : (I : Q) == Q)))));
A = matrix{{1,1,1,1,1,1,1}, {2,0,0,0,1,0,0}, {0,2,0,0,0,1,0}, {2,2,0,2,1,1,1}}
IA = toricIdeal(A, {1,1,1,1,1,1,1})
inIA = monomialIdeal IA
hasChainProperty inIA
StoS = map(S, S, {x_1, x_2, x_3, x_3 - x_4, x_5, x_6, x_7});
J = StoS IA
```

### Output

```
i98 : all(0..3, i -> projection gin distraction L#i == class3)

o98 = true

i99 : hasChainProperty = I -> (
           L := ass I;
           radI := radical I;
           all(L, P -> radI : (radI : P) == P or (
                     gensP := first entries gens P;
                     all(gensP, r -> (
                               Q := monomialIdeal delete(r, gensP);
                               I : (I : Q) == Q)))));

i100 : A = matrix{{1,1,1,1,1,1,1}, {2,0,0,0,1,0,0}, {0,2,0,0,0,1,0}, {2,2,0,2,1,1,1}}

o100 = | 1 1 1 1 1 1 1 |
       | 2 0 0 0 1 0 0 |
       | 0 2 0 0 0 1 0 |
       | 2 2 0 2 1 1 1 |

                4        7
o100 : Matrix ZZ  <--- ZZ

i101 : IA = toricIdeal(A, {1,1,1,1,1,1,1})

2          2          2
o101 = ideal (x x  - x , x x  - x , x x  - x )
               3 4    7   2 3    6   1 3    5

o101 : Ideal of S

i102 : inIA = monomialIdeal IA

2     2     2
o102 = monomialIdeal (x x , x x , x x , x x , x x , x x )
                       1 3   2 3   3 4   2 5   4 5   4 6

o102 : MonomialIdeal of S

i103 : hasChainProperty inIA

o103 = true

i104 : StoS = map(S, S, {x_1, x_2, x_3, x_3 - x_4, x_5, x_6, x_7});

o104 : RingMap S <--- S

i105 : J = StoS IA

2           2          2          2
o105 = ideal (x  - x x  - x , x x  - x , x x  - x )
               3    3 4    7   2 3    6   1 3    5

o105 : Ideal of S
```

---

## monomialIdeals / chapter.m2 — chunk 13

### Input

```macaulay2
inJ = monomialIdeal J
hasChainProperty inJ
A = matrix{{2,0,0,1,0,0,2,1,1,3,2,2,2,3,3,3},
                  {0,2,0,0,1,0,1,2,1,2,3,2,3,2,3,3},
                  {0,0,2,0,0,1,1,1,2,2,2,3,3,3,2,3}};
D = A^{0}+A^{1}+A^{2} || A
D = entries transpose D;
S = QQ[vars(0..15), Degrees => D, MonomialSize => 16];
I = monomialIdeal(d*j, d*k, d*l, d*m, d*n, d*o, d*p, e*j, e*k,
           e*l, e*m, e*n, e*o, e*p, f*j, f*k, f*l, f*m, f*n, f*o, f*p,
           g*j, g*k, g*l, g*m, g*n, g*o, g*p, h*j, h*k, h*l, h*m, h*n,
           h*o, h*p, i*j, i*k, i*l, i*m, i*n, i*o, i*p, g^2, g*h, g*i,
           h^2, h*i, i^2, j^2, j*k, j*l, j*m, j*n, j*o, j*p, k^2, k*l,
           k*m, k*n, k*o, k*p, l^2, l*m, l*n, l*o, l*p, m^2, m*n, m*o,
           m*p, n^2, n*o, n*p, o^2, o*p, p^2, d^2, e^2, f^2, d*h, e*i,
           f*g, f*d*i, d*e*g, e*f*h, c*d*g, a*e*h, b*f*i, c*e*g, 
           a*f*h, b*d*i, c*d*e, a*e*f, b*f*d, c*b*d, a*c*e, b*a*f, 
           c*b*g, a*c*h, b*a*i);
apply(D, d -> rank source basis(d, (S^1)/ ideal I))
```

### Output

```
i106 : inJ = monomialIdeal J

2     2     2       2     2       2       2
o106 = monomialIdeal (x x , x x , x , x x , x x , x x x , x x , x x x , x x x )
                       1 3   2 3   3   2 5   3 5   1 4 5   3 6   1 4 6   2 4 6

o106 : MonomialIdeal of S

i107 : hasChainProperty inJ

o107 = false

i108 : A = matrix{{2,0,0,1,0,0,2,1,1,3,2,2,2,3,3,3},
                  {0,2,0,0,1,0,1,2,1,2,3,2,3,2,3,3},
                  {0,0,2,0,0,1,1,1,2,2,2,3,3,3,2,3}};

3        16
o108 : Matrix ZZ  <--- ZZ

i109 : D = A^{0}+A^{1}+A^{2} || A

o109 = | 2 2 2 1 1 1 4 4 4 7 7 7 8 8 8 9 |
       | 2 0 0 1 0 0 2 1 1 3 2 2 2 3 3 3 |
       | 0 2 0 0 1 0 1 2 1 2 3 2 3 2 3 3 |
       | 0 0 2 0 0 1 1 1 2 2 2 3 3 3 2 3 |

                4        16
o109 : Matrix ZZ  <--- ZZ

i110 : D = entries transpose D;

i111 : S = QQ[vars(0..15), Degrees => D, MonomialSize => 16];

i112 : I = monomialIdeal(d*j, d*k, d*l, d*m, d*n, d*o, d*p, e*j, e*k,
           e*l, e*m, e*n, e*o, e*p, f*j, f*k, f*l, f*m, f*n, f*o, f*p,
           g*j, g*k, g*l, g*m, g*n, g*o, g*p, h*j, h*k, h*l, h*m, h*n,
           h*o, h*p, i*j, i*k, i*l, i*m, i*n, i*o, i*p, g^2, g*h, g*i,
           h^2, h*i, i^2, j^2, j*k, j*l, j*m, j*n, j*o, j*p, k^2, k*l,
           k*m, k*n, k*o, k*p, l^2, l*m, l*n, l*o, l*p, m^2, m*n, m*o,
           m*p, n^2, n*o, n*p, o^2, o*p, p^2, d^2, e^2, f^2, d*h, e*i,
           f*g, f*d*i, d*e*g, e*f*h, c*d*g, a*e*h, b*f*i, c*e*g, 
           a*f*h, b*d*i, c*d*e, a*e*f, b*f*d, c*b*d, a*c*e, b*a*f, 
           c*b*g, a*c*h, b*a*i);

o112 : MonomialIdeal of S

i113 : apply(D, d -> rank source basis(d, (S^1)/ ideal I))

o113 = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}

o113 : List
```

---

## monomialIdeals / chapter.m2 — chunk 14

### Input

```macaulay2
hasChainProperty I
i115 :
```

### Output

```
i114 : hasChainProperty I

o114 = false

i115 :
```

---

## monomialIdeals / test.m2 — chunk 0

### Input

```macaulay2
setRandomSeed();
 -- initializing random seed
S = QQ[a, b, c, d];
I = monomialIdeal(a^2, a*b, b^3, a*c)
J = monomialIdeal{a^2, a*b, b^2}
monomialIdeal(a^2+a*b, a*b+3, b^2+d)
K = ideal(a^2, b^2, a*b+b*c)
monomialIdeal K
monomialIdeal gens K
```

### Output

```
i1 : setRandomSeed();
 -- initializing random seed

i2 : S = QQ[a, b, c, d];

i3 : I = monomialIdeal(a^2, a*b, b^3, a*c)

2        3
o3 = monomialIdeal (a , a*b, b , a*c)

o3 : MonomialIdeal of S

i4 : J = monomialIdeal{a^2, a*b, b^2}

2        2
o4 = monomialIdeal (a , a*b, b )

o4 : MonomialIdeal of S

i5 : monomialIdeal(a^2+a*b, a*b+3, b^2+d)

2        2
o5 = monomialIdeal (a , a*b, b )

o5 : MonomialIdeal of S

i6 : K = ideal(a^2, b^2, a*b+b*c)

2   2
o6 = ideal (a , b , a*b + b*c)

o6 : Ideal of S

i7 : monomialIdeal K

2        2     2
o7 = monomialIdeal (a , a*b, b , b*c )

o7 : MonomialIdeal of S

i8 : monomialIdeal gens K

2        2
o8 = monomialIdeal (a , a*b, b )

o8 : MonomialIdeal of S
```

---

## monomialIdeals / test.m2 — chunk 1

### Input

```macaulay2
isMonomialIdeal K
isMonomialIdeal ideal(a^5, b^2*c, d^11)
I+J
fvector = I -> (
           R := (ring I)/I;
           d := dim R;
           N := poincare R;
           t := first gens ring N;
           while 0 == substitute(N, t => 1) do N = N // (1-t);
           h := apply(reverse toList(0..d), i -> N_(t^i));
           f := j -> sum(0..j+1, i -> binomial(d-i, j+1-i)*h#(d-i));
           apply(toList(0..d-1), j -> f(j)));
S = QQ[x_1 .. x_6];
octahedron = monomialIdeal(x_1*x_2, x_3*x_4, x_5*x_6)
fvector octahedron
simplicial2sphere = v -> ( 
           S := QQ[x_1..x_v]; 
           if v === 4 then monomialIdeal product gens S 
           else ( 
                L := {};
                scan(1..v-4, i -> L = L | apply(v-i-3, 
                          j -> x_i*x_(i+j+4))); 
                scan(2..v-3, i -> L = L | {x_i*x_(i+1)*x_(i+2)}); 
                monomialIdeal L));
```

### Output

```
i9 : isMonomialIdeal K

o9 = false

i10 : isMonomialIdeal ideal(a^5, b^2*c, d^11)

o10 = true

i11 : I+J

2        2
o11 = monomialIdeal (a , a*b, b , a*c)

o11 : MonomialIdeal of S

i12 : fvector = I -> (
           R := (ring I)/I;
           d := dim R;
           N := poincare R;
           t := first gens ring N;
           while 0 == substitute(N, t => 1) do N = N // (1-t);
           h := apply(reverse toList(0..d), i -> N_(t^i));
           f := j -> sum(0..j+1, i -> binomial(d-i, j+1-i)*h#(d-i));
           apply(toList(0..d-1), j -> f(j)));

i13 : S = QQ[x_1 .. x_6];

i14 : octahedron = monomialIdeal(x_1*x_2, x_3*x_4, x_5*x_6)

o14 = monomialIdeal (x x , x x , x x )
                      1 2   3 4   5 6

o14 : MonomialIdeal of S

i15 : fvector octahedron

o15 = {6, 12, 8}

o15 : List

i16 : simplicial2sphere = v -> ( 
           S := QQ[x_1..x_v]; 
           if v === 4 then monomialIdeal product gens S 
           else ( 
                L := {};
                scan(1..v-4, i -> L = L | apply(v-i-3, 
                          j -> x_i*x_(i+j+4))); 
                scan(2..v-3, i -> L = L | {x_i*x_(i+1)*x_(i+2)}); 
                monomialIdeal L));
```

---

## monomialIdeals / test.m2 — chunk 2

### Input

```macaulay2
apply({4,5,6,7,8}, j -> fvector simplicial2sphere(j))
supp = r -> select(gens ring r, e -> r % e == 0);
monomialDecompose = method();
monomialDecompose List := L -> (
           P := select(L, I -> all(first entries gens I, 
                     r -> #supp(r) < 2) === false);
           if #P > 0 then (
                I := first P;
                m := first select(first entries gens I, 
                     r -> #supp(r) > 1);
                E := first exponents m;
                i := position(E, e -> e =!= 0);
                r1 := product apply(E_{0..i}, (gens ring I)_{0..i}, 
                     (j, r) -> r^j);
                r2 := m // r1;
                monomialDecompose(delete(I, L) | {I+monomialIdeal(r1),
                          I+monomialIdeal(r2)}))
           else L);
monomialDecompose MonomialIdeal := I -> monomialDecompose {I};
S = QQ[a,b,c,d];
I = monomialIdeal(a^3*b, a^3*c, a*b^3, b^3*c, a*c^3, b*c^3)
P = monomialDecompose I;
```

### Output

```
i17 : apply({4,5,6,7,8}, j -> fvector simplicial2sphere(j))

o17 = {{4, 6, 4}, {5, 9, 6}, {6, 12, 8}, {7, 15, 10}, {8, 18, 12}}

o17 : List

i18 : supp = r -> select(gens ring r, e -> r % e == 0);

i19 : monomialDecompose = method();

i20 : monomialDecompose List := L -> (
           P := select(L, I -> all(first entries gens I, 
                     r -> #supp(r) < 2) === false);
           if #P > 0 then (
                I := first P;
                m := first select(first entries gens I, 
                     r -> #supp(r) > 1);
                E := first exponents m;
                i := position(E, e -> e =!= 0);
                r1 := product apply(E_{0..i}, (gens ring I)_{0..i}, 
                     (j, r) -> r^j);
                r2 := m // r1;
                monomialDecompose(delete(I, L) | {I+monomialIdeal(r1),
                          I+monomialIdeal(r2)}))
           else L);

i21 : monomialDecompose MonomialIdeal := I -> monomialDecompose {I};

i22 : S = QQ[a,b,c,d];

i23 : I = monomialIdeal(a^3*b, a^3*c, a*b^3, b^3*c, a*c^3, b*c^3)

3      3   3    3      3     3
o23 = monomialIdeal (a b, a*b , a c, b c, a*c , b*c )

o23 : MonomialIdeal of S

i24 : P = monomialDecompose I;
```

---

## monomialIdeals / test.m2 — chunk 3

### Input

```macaulay2
scan(P, J -> << endl << J << endl);
I == intersect(P)
code(dual, MonomialIdeal, List)
code(primaryDecomposition, MonomialIdeal)
L = primaryDecomposition I;
scan(L, J -> << endl << J << endl);
I == intersect L
treeIdeal = n -> (
           S = QQ[vars(0..n-1)];
           L := delete({}, subsets gens S);
           monomialIdeal apply(L, F -> (product F)^(n - #F +1)));
```

### Output

```
i25 : scan(P, J -> << endl << J << endl);

monomialIdeal (b, c)

monomialIdeal (a, c)

                3   3   3
monomialIdeal (a , b , c )

monomialIdeal (a, b)

                3      3
monomialIdeal (a , b, c )

monomialIdeal (a, b)

                   3   3
monomialIdeal (a, b , c )

i26 : I == intersect(P)

o26 = true

i27 : code(dual, MonomialIdeal, List)

o27 = -- code for method: dual(MonomialIdeal,List)
      /Users/dan/src/M2/Macaulay2/m2/option.m2:6:20-10:34: --source code:
        (opts,f) -> args -> (
             -- Common code for functions created with >> to process options and arguments.
             uncurry(f, override (opts,args))
             )
      | symbol   class              value                                                   location of symbol
      | ------   -----              -----                                                   ------------------                              
      | opts   : OptionTable     -- OptionTable{Strategy => 0}                              /Users/dan/src/M2/Macaulay2/m2/option.m2:6:4-6:7
      | f      : FunctionClosure -- {*Function[/Users/dan/src/M2/Macaulay2/m2/monideal.m2:. /Users/dan/src/M2/Macaulay2/m2/option.m2:6:9-6:9
      | -- function f:
      | /Users/dan/src/M2/Macaulay2/m2/monideal.m2:243:44-250:60: --source code:
      | dual(MonomialIdeal, List) := alexopts >> o -> (I, a) -> I.cache#(AlexanderDual, a) ??= (
      |      aI := first exponents lcm I;
      |      if aI =!= a then (
      |         if #aI =!= #a            then error("expected list of length ", #aI);
      |         if any(a-aI, i -> i < 0) then error "exponent vector not large enough");
      |      newMonomialIdeal(ring I, rawAlexanderDual(raw I, a, o.Strategy)) -- 0 is the default algorithm
      |      )
      | -- option table opts:
      | OptionTable{Strategy => 0}

i28 : code(primaryDecomposition, MonomialIdeal)

o28 = -- code for method: primaryDecomposition(MonomialIdeal)
      primaryDecomposition Ideal  := List => opts -> I -> primarydecompHelper(I, (primaryDecomposition, Ideal), opts)

i29 : L = primaryDecomposition I;

i30 : scan(L, J -> << endl << J << endl);

monomialIdeal (a, b)

monomialIdeal (a, c)

monomialIdeal (b, c)

                3   3   3
monomialIdeal (a , b , c )

i31 : I == intersect L

o31 = true

i32 : treeIdeal = n -> (
           S = QQ[vars(0..n-1)];
           L := delete({}, subsets gens S);
           monomialIdeal apply(L, F -> (product F)^(n - #F +1)));
```

---

## monomialIdeals / test.m2 — chunk 4

### Input

```macaulay2
apply(2..6, i -> #primaryDecomposition treeIdeal i)
minorsIdeal = (m,n,k) -> (
           S := QQ[x_1..x_(m*n), MonomialOrder => Lex];
           I := minors(k, matrix table(m, n, (i,j) -> x_(i*n+n-j)));
           forceGB gens I;
           I);
apply(2..8, i -> time codim monomialIdeal minorsIdeal(i,2*i,2))
     -- used 0.001977 seconds
     -- used 0.004674 seconds
     -- used 0.010817 seconds
     -- used 0.150144 seconds
     -- used 0.077651 seconds
     -- used 0.565484 seconds
     -- used 2.11014 seconds
x = symbol x;
stdPairs = I -> (
           S := ring I;
           X := gens S;
           std := {};
           J := I;
           while J != S do (
                w1 := 1_S;
                F := X;
                K := J;
                while K != 0 do (
                     g1 := (ideal mingens ideal K)_0;
                     x := first supp g1;
                     w1 = w1 * g1 // x;
                     F = delete(x, F);
                     K = K : monomialIdeal(g1 // x);
                     L := select(first entries gens K, 
                          r -> not member(x, supp r));
                     if #L > 0 then K = monomialIdeal L
                     else K = monomialIdeal 0_S;);
                w2 := w1;
                scan(X, r -> if not member(r, supp w1) or member(r, F)
                     then w2 = substitute(w2, {r => 1}));
                P := monomialIdeal select(X, r -> not member(r, F));
                if (I:(I:P) == P) and (all(std, p -> 
                          (w2 % (first p) != 0) or not
                          isSubset(supp(w2 // first p) | F, last p)))
                then std = std | {{w2, F}};
                J = J + monomialIdeal(w1););
           std);
S = QQ[x,y,z];
I = monomialIdeal(x*y^3*z, x*y^2*z^2, y^3*z^2, y^2*z^3);
scan(time stdPairs I, P -> << endl << P << endl);
     -- used 0.039405 seconds
```

### Output

```
i33 : apply(2..6, i -> #primaryDecomposition treeIdeal i)

o33 = (1, 1, 1, 1, 1)

o33 : Sequence

i34 : minorsIdeal = (m,n,k) -> (
           S := QQ[x_1..x_(m*n), MonomialOrder => Lex];
           I := minors(k, matrix table(m, n, (i,j) -> x_(i*n+n-j)));
           forceGB gens I;
           I);

i35 : apply(2..8, i -> time codim monomialIdeal minorsIdeal(i,2*i,2))
     -- used 0.001977 seconds
     -- used 0.004674 seconds
     -- used 0.010817 seconds
     -- used 0.150144 seconds
     -- used 0.077651 seconds
     -- used 0.565484 seconds
     -- used 2.11014 seconds

o35 = (3, 10, 21, 36, 55, 78, 105)

o35 : Sequence

i36 : x = symbol x;

i37 : stdPairs = I -> (
           S := ring I;
           X := gens S;
           std := {};
           J := I;
           while J != S do (
                w1 := 1_S;
                F := X;
                K := J;
                while K != 0 do (
                     g1 := (ideal mingens ideal K)_0;
                     x := first supp g1;
                     w1 = w1 * g1 // x;
                     F = delete(x, F);
                     K = K : monomialIdeal(g1 // x);
                     L := select(first entries gens K, 
                          r -> not member(x, supp r));
                     if #L > 0 then K = monomialIdeal L
                     else K = monomialIdeal 0_S;);
                w2 := w1;
                scan(X, r -> if not member(r, supp w1) or member(r, F)
                     then w2 = substitute(w2, {r => 1}));
                P := monomialIdeal select(X, r -> not member(r, F));
                if (I:(I:P) == P) and (all(std, p -> 
                          (w2 % (first p) != 0) or not
                          isSubset(supp(w2 // first p) | F, last p)))
                then std = std | {{w2, F}};
                J = J + monomialIdeal(w1););
           std);

i38 : S = QQ[x,y,z];

i39 : I = monomialIdeal(x*y^3*z, x*y^2*z^2, y^3*z^2, y^2*z^3);

o39 : MonomialIdeal of S

i40 : scan(time stdPairs I, P -> << endl << P << endl);
     -- used 0.039405 seconds

{y, {x, z}}

{1, {x, z}}

  2 2
{y z , {}}

{z, {y}}

  2
{y z, {x}}

{1, {x, y}}
```

---

## monomialIdeals / test.m2 — chunk 5

### Input

```macaulay2
code(standardPairs, MonomialIdeal, List)
time standardPairs I;
     -- used 0.078395 seconds
permutohedronIdeal = n -> (
           S := QQ[X_1..X_n];
           monomialIdeal terms det matrix table(n ,gens S, 
                (i,r) -> r^(i+1)));
L = apply({2,3,4,5}, j -> standardPairs(permutohedronIdeal(j)));
apply(L, i -> #i)
x = symbol x; z = symbol z;
toBinomial = (b, S) -> (
           pos := 1_S;
           neg := 1_S;
           scan(#b, i -> if b_i > 0 then pos = pos*S_i^(b_i)
                         else if b_i < 0 then neg = neg*S_i^(-b_i));
           pos - neg);
toricIdeal = (A, omega) -> (
           n := rank source A;
           S = QQ[x_1..x_n, Weights => omega, MonomialSize => 16];
           B := transpose matrix syz A;
           J := ideal apply(entries B, b -> toBinomial(b, S));
           scan(gens S, r -> J = saturate(J, r));
           J);
```

### Output

```
i41 : code(standardPairs, MonomialIdeal, List)

o41 = -- code for method: standardPairs(MonomialIdeal,List)
      /Users/dan/src/M2/Macaulay2/m2/monideal.m2:269:45-292:6: --source code:
      standardPairs(MonomialIdeal, List) := (I,D) -> (
           R := ring I;
           X := generators R;
           S := {};
           k := coefficientRing R;
           scan(D, L -> ( 
                     Y := X;
                     m := vars R;
                     Lset := set L;
                     Y = select(Y, r -> not Lset#?r);
                     m = substitute(m, apply(L, r -> r => 1));
                     -- using monoid to create ring to avoid 
                     -- changing global ring.
                     A := k (monoid [Y]);
                     phi := map(A, R, substitute(m, A));
                     J := ideal mingens ideal phi generators I;
                     Jsat := saturate(J, ideal vars A);
                     if Jsat != J then (
                          B := flatten entries super basis (
                               trim (Jsat / J));
                          psi := map(R, A, matrix{Y});
                          S = join(S, apply(B, b -> {psi(b), L}));
                          )));
           S)

i42 : time standardPairs I;
     -- used 0.078395 seconds

i43 : permutohedronIdeal = n -> (
           S := QQ[X_1..X_n];
           monomialIdeal terms det matrix table(n ,gens S, 
                (i,r) -> r^(i+1)));

i44 : L = apply({2,3,4,5}, j -> standardPairs(permutohedronIdeal(j)));

i45 : apply(L, i -> #i)

o45 = {3, 10, 53, 446}

o45 : List

i46 : x = symbol x; z = symbol z;

i48 : toBinomial = (b, S) -> (
           pos := 1_S;
           neg := 1_S;
           scan(#b, i -> if b_i > 0 then pos = pos*S_i^(b_i)
                         else if b_i < 0 then neg = neg*S_i^(-b_i));
           pos - neg);

i49 : toricIdeal = (A, omega) -> (
           n := rank source A;
           S = QQ[x_1..x_n, Weights => omega, MonomialSize => 16];
           B := transpose matrix syz A;
           J := ideal apply(entries B, b -> toBinomial(b, S));
           scan(gens S, r -> J = saturate(J, r));
           J);
```

---

## monomialIdeals / test.m2 — chunk 6

### Input

```macaulay2
IP = (A, omega, beta) -> (
           std := standardPairs monomialIdeal toricIdeal(A, omega);
           n := rank source A;
           alpha := {};
           Q := first select(1, std, P -> (
                F := apply(last P, r -> index r);
                gamma := transpose matrix exponents first P;
                K := transpose syz (submatrix(A,F) | (A*gamma-beta));
                X := select(entries K, k -> abs last(k) === 1);
                scan(X, k -> if all(k, j -> j>=0) or all(k, j -> j<=0)
                     then alpha = apply(n, j -> if member(j, F) 
                          then last(k)*k_(position(F, i -> i === j))
                          else 0));
                #alpha > 0));
           if #Q > 0 then (matrix {alpha})+(matrix exponents first Q)
           else 0);
A = matrix{{1,1,1,1,1},{1,2,4,5,6}}
w1 = {1,1,1,1,1};
w2 = {2,3,5,7,11};
b1 = transpose matrix{{3,9}}
b2 = transpose matrix{{5,16}}
IP(A, w1, b1)
IP(A, w2, b1)
```

### Output

```
i50 : IP = (A, omega, beta) -> (
           std := standardPairs monomialIdeal toricIdeal(A, omega);
           n := rank source A;
           alpha := {};
           Q := first select(1, std, P -> (
                F := apply(last P, r -> index r);
                gamma := transpose matrix exponents first P;
                K := transpose syz (submatrix(A,F) | (A*gamma-beta));
                X := select(entries K, k -> abs last(k) === 1);
                scan(X, k -> if all(k, j -> j>=0) or all(k, j -> j<=0)
                     then alpha = apply(n, j -> if member(j, F) 
                          then last(k)*k_(position(F, i -> i === j))
                          else 0));
                #alpha > 0));
           if #Q > 0 then (matrix {alpha})+(matrix exponents first Q)
           else 0);

i51 : A = matrix{{1,1,1,1,1},{1,2,4,5,6}}

o51 = | 1 1 1 1 1 |
      | 1 2 4 5 6 |

               2       5
o51 : Matrix ZZ  <-- ZZ

i52 : w1 = {1,1,1,1,1};

i53 : w2 = {2,3,5,7,11};

i54 : b1 = transpose matrix{{3,9}}

o54 = | 3 |
      | 9 |

               2       1
o54 : Matrix ZZ  <-- ZZ

i55 : b2 = transpose matrix{{5,16}}

o55 = | 5  |
      | 16 |

               2       1
o55 : Matrix ZZ  <-- ZZ

i56 : IP(A, w1, b1)

o56 = | 1 1 0 0 1 |

               1       5
o56 : Matrix ZZ  <-- ZZ

i57 : IP(A, w2, b1)

o57 = | 1 0 2 0 0 |

               1       5
o57 : Matrix ZZ  <-- ZZ
```

---

## monomialIdeals / test.m2 — chunk 7

### Input

```macaulay2
IP(A, w1, b2)
IP(A, w2, b2)
S = QQ[a,b,c,d];
isBorel monomialIdeal(a^2, a*b, b^2)
isBorel monomialIdeal(a^2, b^2)
borel monomialIdeal(b*c)
borel monomialIdeal(a,c^3)
gin = method();
```

### Output

```
i58 : IP(A, w1, b2)

o58 = | 2 1 0 0 2 |

               1       5
o58 : Matrix ZZ  <-- ZZ

i59 : IP(A, w2, b2)

o59 = | 0 2 3 0 0 |

               1       5
o59 : Matrix ZZ  <-- ZZ

i60 : S = QQ[a,b,c,d];

i61 : isBorel monomialIdeal(a^2, a*b, b^2)

o61 = true

i62 : isBorel monomialIdeal(a^2, b^2)

o62 = false

i63 : borel monomialIdeal(b*c)

2        2
o63 = monomialIdeal (a , a*b, b , a*c, b*c)

o63 : MonomialIdeal of S

i64 : borel monomialIdeal(a,c^3)

3   2      2   3
o64 = monomialIdeal (a, b , b c, b*c , c )

o64 : MonomialIdeal of S

i65 : gin = method();
```

---

## monomialIdeals / test.m2 — chunk 8

### Input

```macaulay2
gin Ideal := I -> (
           S := ring I;
           StoS := map(S, S, random(S^{0}, S^{numgens S:-1}));
           monomialIdeal StoS I);
gin MonomialIdeal := I -> gin ideal I;
genericForms = (p,q) -> ideal(random(p,S), random(q,S));
gin genericForms(2,2)
gin genericForms(2,3)
J = ideal(a^2, a*b+b^2, a*c)
ginJ = gin J
inJ = monomialIdeal J
```

### Output

```
i66 : gin Ideal := I -> (
           S := ring I;
           StoS := map(S, S, random(S^{0}, S^{numgens S:-1}));
           monomialIdeal StoS I);

i67 : gin MonomialIdeal := I -> gin ideal I;

i68 : genericForms = (p,q) -> ideal(random(p,S), random(q,S));

i69 : gin genericForms(2,2)

2        3
o69 = monomialIdeal (a , a*b, b )

o69 : MonomialIdeal of S

i70 : gin genericForms(2,3)

2     2   4
o70 = monomialIdeal (a , a*b , b )

o70 : MonomialIdeal of S

i71 : J = ideal(a^2, a*b+b^2, a*c)

2         2
o71 = ideal (a , a*b + b , a*c)

o71 : Ideal of S

i72 : ginJ = gin J

2        2     2
o72 = monomialIdeal (a , a*b, b , a*c )

o72 : MonomialIdeal of S

i73 : inJ = monomialIdeal J

2        3        2
o73 = monomialIdeal (a , a*b, b , a*c, b c)

o73 : MonomialIdeal of S
```

---

## monomialIdeals / test.m2 — chunk 9

### Input

```macaulay2
isBorel inJ and isBorel ginJ
S = QQ[a,b,c,d, MonomialOrder => Lex];
gin genericForms(2,2)
gin genericForms(2,3)
projection = I -> (
           S := ring I;
           n := numgens S;
           X := gens S;
           monomialIdeal mingens substitute(ideal I, 
                {X#(n-2) => 1, X#(n-1) => 1}));
polarization = I -> (
           n := numgens ring I;
           u := apply(numgens I, i -> first exponents I_i);
           I.cache.lcm = max \ transpose u;
           Z := flatten apply(n, i -> apply(I.cache.lcm#i, j -> z_{i,j}));
           R := QQ(monoid[Z]);
           Z = gens R;
           p := apply(n, i -> sum((I.cache.lcm)_{0..i-1}));
           monomialIdeal apply(u, e -> product apply(n, i -> 
                     product(toList(0..e#i-1), j -> Z#(p#i+j)))));
distraction = I -> (
           S := ring I;
           n := numgens S;
           X := gens S;
           J := polarization I;
           W := flatten apply(n, i -> flatten apply(I.cache.lcm#i, 
                     j -> X#i));
           section := map(S, ring J, apply(W, r -> r - 
                     random(500)*X#(n-2) - random(500)*X#(n-1)));     
           section ideal J);
S = QQ[x_0 .. x_4, MonomialOrder => GLex];
```

### Output

```
i74 : isBorel inJ and isBorel ginJ

o74 = true

i75 : S = QQ[a,b,c,d, MonomialOrder => Lex];

i76 : gin genericForms(2,2)

2        4     2
o76 = monomialIdeal (a , a*b, b , a*c )

o76 : MonomialIdeal of S

i77 : gin genericForms(2,3)

2     2   6       2     6         2       4
o77 = monomialIdeal (a , a*b , b , a*b*c , a*c , a*b*c*d , a*b*d )

o77 : MonomialIdeal of S

i78 : projection = I -> (
           S := ring I;
           n := numgens S;
           X := gens S;
           monomialIdeal mingens substitute(ideal I, 
                {X#(n-2) => 1, X#(n-1) => 1}));

i79 : polarization = I -> (
           n := numgens ring I;
           u := apply(numgens I, i -> first exponents I_i);
           I.cache.lcm = max \ transpose u;
           Z := flatten apply(n, i -> apply(I.cache.lcm#i, j -> z_{i,j}));
           R := QQ(monoid[Z]);
           Z = gens R;
           p := apply(n, i -> sum((I.cache.lcm)_{0..i-1}));
           monomialIdeal apply(u, e -> product apply(n, i -> 
                     product(toList(0..e#i-1), j -> Z#(p#i+j)))));

i80 : distraction = I -> (
           S := ring I;
           n := numgens S;
           X := gens S;
           J := polarization I;
           W := flatten apply(n, i -> flatten apply(I.cache.lcm#i, 
                     j -> X#i));
           section := map(S, ring J, apply(W, r -> r - 
                     random(500)*X#(n-2) - random(500)*X#(n-1)));     
           section ideal J);

i81 : S = QQ[x_0 .. x_4, MonomialOrder => GLex];
```

---

## monomialIdeals / test.m2 — chunk 10

### Input

```macaulay2
I = monomialIdeal(x_0^2, x_0*x_1^2*x_3, x_1^3*x_4)
projection I
polarization I
distraction I
m =  matrix table({0,1,2}, {0,1,2}, (i,j) -> (gens S)#(i+j))
rationalQuartic = minors(2, m);
H = hilbertPolynomial(S/rationalQuartic);
hilbertPolynomial(S/rationalQuartic, Projective => false)
```

### Output

```
i82 : I = monomialIdeal(x_0^2, x_0*x_1^2*x_3, x_1^3*x_4)

2     2     3
o82 = monomialIdeal (x , x x x , x x )
                      0   0 1 3   1 4

o82 : MonomialIdeal of S

i83 : projection I

2     2   3
o83 = monomialIdeal (x , x x , x )
                      0   0 1   1

o83 : MonomialIdeal of S

i84 : polarization I

o84 = monomialIdeal (z      z      , z      z      z      z      , z      z      z      z      )
                      {0, 0} {0, 1}   {0, 0} {1, 0} {1, 1} {3, 0}   {1, 0} {1, 1} {1, 2} {4, 0}

o84 : MonomialIdeal of QQ[z      , z      , z      , z      , z      , z      , z      ]
                           {0, 0}   {0, 1}   {1, 0}   {1, 1}   {1, 2}   {3, 0}   {4, 0}

i85 : distraction I

2                             2                    2         2           2               2                               2             3              2                  2              3         2 2          2             2 2              3              2                  2             3              4               3                 2 2                3             4       3         3           2 2          2              2 2              3               2                   2              3              4              3                 2 2                 3              4
o85 = ideal (x  - 632x x  - 160x x  + 93927x  + 56258x x  + 5031x , - 84x x x  - 381x x x  + 42924x x x  + 223335x x x x  + 129921x x x  - 5371632x x  - 31832964x x x  - 36267714x x x  - 10847070x x  + 33012x x  + 153345x x x  + 16383x x  - 16869132x x  - 89616387x x x  - 60662358x x x  - 5586603x x  + 2111051376x  + 12741335028x x  + 15622029054x x  + 5822410212x x  + 466424010x , - 90x x  - 462x x  + 62730x x  + 395634x x x  + 377916x x  - 14309460x x  - 109103058x x x  - 200193624x x x  - 88300674x x  + 1070489520x  + 9728887536x x  + 26026700220x x  + 23263034976x x  + 6274047780x )
              0       0 3       0 4         3         3 4        4       0 1 3       0 1 4         0 1 3          0 1 3 4          0 1 4           0 3            0 3 4            0 3 4            0 4         1 3          1 3 4         1 4            1 3            1 3 4            1 3 4           1 4              3               3 4               3 4              3 4             4       1 3       1 4         1 3          1 3 4          1 4            1 3             1 3 4             1 3 4            1 4              3              3 4               3 4               3 4              4

o85 : Ideal of S

i86 : m =  matrix table({0,1,2}, {0,1,2}, (i,j) -> (gens S)#(i+j))

o86 = | x_0 x_1 x_2 |
      | x_1 x_2 x_3 |
      | x_2 x_3 x_4 |

              3      3
o86 : Matrix S  <-- S

i87 : rationalQuartic = minors(2, m);

o87 : Ideal of S

i88 : H = hilbertPolynomial(S/rationalQuartic);

i89 : hilbertPolynomial(S/rationalQuartic, Projective => false)

o89 = 4i + 1

o89 : QQ[i]
```

---

## monomialIdeals / test.m2 — chunk 11

### Input

```macaulay2
L = {monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_1^2, x_1*x_2, x_2^2), monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_0*x_3, x_1^2, x_1*x_2, x_2^3), monomialIdeal(x_0, x_1^2, x_1*x_2^2, x_1*x_2*x_3, x_2^3), monomialIdeal(x_0, x_1^2, x_1*x_2, x_2^4, x_2^3*x_3), monomialIdeal(x_0, x_1, x_2^5, x_2^4*x_3^3), monomialIdeal(x_0, x_1^2, x_1*x_2, x_1*x_3, x_2^5, x_2^4*x_3^2), monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_0*x_3, x_1^2, x_1*x_2, x_1*x_3, x_2^5, x_2^4*x_3), monomialIdeal(x_0, x_1^2, x_1*x_2, x_1*x_3^2, x_2^5, x_2^4*x_3), monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_0*x_3, x_1^2, x_1*x_2, x_1*x_3^2, x_2^4), monomialIdeal(x_0, x_1^2, x_1*x_2^2, x_1*x_2*x_3, x_1*x_3^2, x_2^4), monomialIdeal(x_0, x_1^2, x_1*x_2, x_1*x_3^3, x_2^4), monomialIdeal(x_0, x_1, x_2^6, x_2^5*x_3, x_2^4*x_3^2)};
scan(#L, i -> << endl << i+1 << " : " << L#i << endl);
all(L, I -> isBorel I and hilbertPolynomial(S/I) == H)
class1 = projection L#0
class2 = projection L#1
class3 = projection L#4
all(1..3, i -> projection L#i == class2)
all(4..11, i -> projection L#i == class3)
```

### Output

```
i90 : L = {monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_1^2, x_1*x_2, x_2^2), monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_0*x_3, x_1^2, x_1*x_2, x_2^3), monomialIdeal(x_0, x_1^2, x_1*x_2^2, x_1*x_2*x_3, x_2^3), monomialIdeal(x_0, x_1^2, x_1*x_2, x_2^4, x_2^3*x_3), monomialIdeal(x_0, x_1, x_2^5, x_2^4*x_3^3), monomialIdeal(x_0, x_1^2, x_1*x_2, x_1*x_3, x_2^5, x_2^4*x_3^2), monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_0*x_3, x_1^2, x_1*x_2, x_1*x_3, x_2^5, x_2^4*x_3), monomialIdeal(x_0, x_1^2, x_1*x_2, x_1*x_3^2, x_2^5, x_2^4*x_3), monomialIdeal(x_0^2, x_0*x_1, x_0*x_2, x_0*x_3, x_1^2, x_1*x_2, x_1*x_3^2, x_2^4), monomialIdeal(x_0, x_1^2, x_1*x_2^2, x_1*x_2*x_3, x_1*x_3^2, x_2^4), monomialIdeal(x_0, x_1^2, x_1*x_2, x_1*x_3^3, x_2^4), monomialIdeal(x_0, x_1, x_2^6, x_2^5*x_3, x_2^4*x_3^2)};

i91 : scan(#L, i -> << endl << i+1 << " : " << L#i << endl);

2         2               2
1 : monomialIdeal (x , x x , x , x x , x x , x )
                    0   0 1   1   0 2   1 2   2

                    2         2               3
2 : monomialIdeal (x , x x , x , x x , x x , x , x x )
                    0   0 1   1   0 2   1 2   2   0 3

                        2     2   3
3 : monomialIdeal (x , x , x x , x , x x x )
                    0   1   1 2   2   1 2 3

                        2         4   3
4 : monomialIdeal (x , x , x x , x , x x )
                    0   1   1 2   2   2 3

                            5   4 3
5 : monomialIdeal (x , x , x , x x )
                    0   1   2   2 3

                        2         5         4 2
6 : monomialIdeal (x , x , x x , x , x x , x x )
                    0   1   1 2   2   1 3   2 3

                    2         2               5               4
7 : monomialIdeal (x , x x , x , x x , x x , x , x x , x x , x x )
                    0   0 1   1   0 2   1 2   2   0 3   1 3   2 3

                        2         5   4       2
8 : monomialIdeal (x , x , x x , x , x x , x x )
                    0   1   1 2   2   2 3   1 3

                    2         2               4           2
9 : monomialIdeal (x , x x , x , x x , x x , x , x x , x x )
                    0   0 1   1   0 2   1 2   2   0 3   1 3

                         2     2   4             2
10 : monomialIdeal (x , x , x x , x , x x x , x x )
                     0   1   1 2   2   1 2 3   1 3

                         2         4     3
11 : monomialIdeal (x , x , x x , x , x x )
                     0   1   1 2   2   1 3

                             6   5     4 2
12 : monomialIdeal (x , x , x , x x , x x )
                     0   1   2   2 3   2 3

i92 : all(L, I -> isBorel I and hilbertPolynomial(S/I) == H)

o92 = true

i93 : class1 = projection L#0

2         2               2
o93 = monomialIdeal (x , x x , x , x x , x x , x )
                      0   0 1   1   0 2   1 2   2

o93 : MonomialIdeal of S

i94 : class2 = projection L#1

2         3
o94 = monomialIdeal (x , x , x x , x )
                      0   1   1 2   2

o94 : MonomialIdeal of S

i95 : class3 = projection L#4

4
o95 = monomialIdeal (x , x , x )
                      0   1   2

o95 : MonomialIdeal of S

i96 : all(1..3, i -> projection L#i == class2)

o96 = true

i97 : all(4..11, i -> projection L#i == class3)

o97 = true
```

---

## monomialIdeals / test.m2 — chunk 12

### Input

```macaulay2
all(L, I -> I == monomialIdeal distraction I)
all(0..3, i -> projection gin distraction L#i == class3)
hasChainProperty = I -> (
            L := ass I;
            radI := radical I;
            all(L, P -> radI : (radI : P) == P or (
                      gensP := first entries gens P;
                      all(gensP, r -> (
                                Q := monomialIdeal delete(r, gensP);
                                I : (I : Q) == Q)))));
A = matrix{{1,1,1,1,1,1,1}, {2,0,0,0,1,0,0}, {0,2,0,0,0,1,0}, {2,2,0,2,1,1,1}}
IA = toricIdeal(A, {1,1,1,1,1,1,1})
inIA = monomialIdeal IA
hasChainProperty inIA
StoS = map(S, S, {x_1, x_2, x_3, x_3 - x_4, x_5, x_6, x_7});
```

### Output

```
i98 : all(L, I -> I == monomialIdeal distraction I)

o98 = true

i99 : all(0..3, i -> projection gin distraction L#i == class3)

o99 = true

i100 : hasChainProperty = I -> (
            L := ass I;
            radI := radical I;
            all(L, P -> radI : (radI : P) == P or (
                      gensP := first entries gens P;
                      all(gensP, r -> (
                                Q := monomialIdeal delete(r, gensP);
                                I : (I : Q) == Q)))));

i101 : A = matrix{{1,1,1,1,1,1,1}, {2,0,0,0,1,0,0}, {0,2,0,0,0,1,0}, {2,2,0,2,1,1,1}}

o101 = | 1 1 1 1 1 1 1 |
       | 2 0 0 0 1 0 0 |
       | 0 2 0 0 0 1 0 |
       | 2 2 0 2 1 1 1 |

                4       7
o101 : Matrix ZZ  <-- ZZ

i102 : IA = toricIdeal(A, {1,1,1,1,1,1,1})

2          2          2
o102 = ideal (x x  - x , x x  - x , x x  - x )
               3 4    7   2 3    6   1 3    5

o102 : Ideal of S

i103 : inIA = monomialIdeal IA

2     2     2
o103 = monomialIdeal (x x , x x , x x , x x , x x , x x )
                       1 3   2 3   3 4   2 5   4 5   4 6

o103 : MonomialIdeal of S

i104 : hasChainProperty inIA

o104 = true

i105 : StoS = map(S, S, {x_1, x_2, x_3, x_3 - x_4, x_5, x_6, x_7});

o105 : RingMap S <-- S
```

---

## monomialIdeals / test.m2 — chunk 13

### Input

```macaulay2
J = StoS IA
inJ = monomialIdeal J
hasChainProperty inJ
A = matrix{{2,0,0,1,0,0,2,1,1,3,2,2,2,3,3,3},
                  {0,2,0,0,1,0,1,2,1,2,3,2,3,2,3,3},
                  {0,0,2,0,0,1,1,1,2,2,2,3,3,3,2,3}};
D = A^{0}+A^{1}+A^{2} || A
D = entries transpose D;
S = QQ[vars(0..15), Degrees => D, MonomialSize => 16];
I = monomialIdeal(d*j, d*k, d*l, d*m, d*n, d*o, d*p, e*j, e*k,
           e*l, e*m, e*n, e*o, e*p, f*j, f*k, f*l, f*m, f*n, f*o, f*p,
           g*j, g*k, g*l, g*m, g*n, g*o, g*p, h*j, h*k, h*l, h*m, h*n,
           h*o, h*p, i*j, i*k, i*l, i*m, i*n, i*o, i*p, g^2, g*h, g*i,
           h^2, h*i, i^2, j^2, j*k, j*l, j*m, j*n, j*o, j*p, k^2, k*l,
           k*m, k*n, k*o, k*p, l^2, l*m, l*n, l*o, l*p, m^2, m*n, m*o,
           m*p, n^2, n*o, n*p, o^2, o*p, p^2, d^2, e^2, f^2, d*h, e*i,
           f*g, f*d*i, d*e*g, e*f*h, c*d*g, a*e*h, b*f*i, c*e*g, 
           a*f*h, b*d*i, c*d*e, a*e*f, b*f*d, c*b*d, a*c*e, b*a*f, 
           c*b*g, a*c*h, b*a*i);
```

### Output

```
i106 : J = StoS IA

2           2          2          2
o106 = ideal (x  - x x  - x , x x  - x , x x  - x )
               3    3 4    7   2 3    6   1 3    5

o106 : Ideal of S

i107 : inJ = monomialIdeal J

2     2     2       2     2       2       2
o107 = monomialIdeal (x x , x x , x , x x , x x , x x x , x x , x x x , x x x )
                       1 3   2 3   3   2 5   3 5   1 4 5   3 6   1 4 6   2 4 6

o107 : MonomialIdeal of S

i108 : hasChainProperty inJ

o108 = false

i109 : A = matrix{{2,0,0,1,0,0,2,1,1,3,2,2,2,3,3,3},
                  {0,2,0,0,1,0,1,2,1,2,3,2,3,2,3,3},
                  {0,0,2,0,0,1,1,1,2,2,2,3,3,3,2,3}};

3       16
o109 : Matrix ZZ  <-- ZZ

i110 : D = A^{0}+A^{1}+A^{2} || A

o110 = | 2 2 2 1 1 1 4 4 4 7 7 7 8 8 8 9 |
       | 2 0 0 1 0 0 2 1 1 3 2 2 2 3 3 3 |
       | 0 2 0 0 1 0 1 2 1 2 3 2 3 2 3 3 |
       | 0 0 2 0 0 1 1 1 2 2 2 3 3 3 2 3 |

                4       16
o110 : Matrix ZZ  <-- ZZ

i111 : D = entries transpose D;

i112 : S = QQ[vars(0..15), Degrees => D, MonomialSize => 16];

i113 : I = monomialIdeal(d*j, d*k, d*l, d*m, d*n, d*o, d*p, e*j, e*k,
           e*l, e*m, e*n, e*o, e*p, f*j, f*k, f*l, f*m, f*n, f*o, f*p,
           g*j, g*k, g*l, g*m, g*n, g*o, g*p, h*j, h*k, h*l, h*m, h*n,
           h*o, h*p, i*j, i*k, i*l, i*m, i*n, i*o, i*p, g^2, g*h, g*i,
           h^2, h*i, i^2, j^2, j*k, j*l, j*m, j*n, j*o, j*p, k^2, k*l,
           k*m, k*n, k*o, k*p, l^2, l*m, l*n, l*o, l*p, m^2, m*n, m*o,
           m*p, n^2, n*o, n*p, o^2, o*p, p^2, d^2, e^2, f^2, d*h, e*i,
           f*g, f*d*i, d*e*g, e*f*h, c*d*g, a*e*h, b*f*i, c*e*g, 
           a*f*h, b*d*i, c*d*e, a*e*f, b*f*d, c*b*d, a*c*e, b*a*f, 
           c*b*g, a*c*h, b*a*i);

o113 : MonomialIdeal of S
```

---

## monomialIdeals / test.m2 — chunk 14

### Input

```macaulay2
apply(D, d -> rank source basis(d, (S^1)/ ideal I))
hasChainProperty I
i116 :
```

### Output

```
i114 : apply(D, d -> rank source basis(d, (S^1)/ ideal I))

o114 = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}

o114 : List

i115 : hasChainProperty I

o115 = false

i116 :
```

---

## preface / chapter.m2 — chunk 0

### Input

```macaulay2
3/5 + 7/11
100!
R = QQ[x,y,z]/(x^3-y^3-z^3)
(x+y+z)^3
b = vars R
c = matrix {{x^2,y^2,z^2}}
M = coker b
N = ker c
```

### Output

```
i1 : 3/5 + 7/11

68
o1 = --
     55

o1 : QQ

i2 : 100!

o2 = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

i3 : R = QQ[x,y,z]/(x^3-y^3-z^3)

o3 = R

o3 : QuotientRing

i4 : (x+y+z)^3

2        2     3     2               2        2       2     3
o4 = 3x y + 3x*y  + 2y  + 3x z + 6x*y*z + 3y z + 3x*z  + 3y*z  + 2z

o4 : R

i5 : b = vars R

o5 = | x y z |

             1       3
o5 : Matrix R  <--- R

i6 : c = matrix {{x^2,y^2,z^2}}

o6 = | x2 y2 z2 |

             1       3
o6 : Matrix R  <--- R

i7 : M = coker b

o7 = cokernel | x y z |

                            1
o7 : R-module, quotient of R

i8 : N = ker c

o8 = image {2} | x  0   -y2 -z2 |
           {2} | -y -z2 x2  0   |
           {2} | -z y2  0   x2  |

                             3
o8 : R-module, submodule of R
```

---

## preface / chapter.m2 — chunk 1

### Input

```macaulay2
res M
X = Proj R
HH^1 cotangentSheaf X 
i12 :
```

### Output

```
i9 : res M

1      3      4      4      4
o9 = R  <-- R  <-- R  <-- R  <-- R
                                  
     0      1      2      3      4

o9 : ChainComplex

i10 : X = Proj R

o10 = X

o10 : ProjectiveVariety

i11 : HH^1 cotangentSheaf X 

1
o11 = QQ

o11 : QQ-module, free

i12 :
```

---

## preface / test.m2 — chunk 0

### Input

```macaulay2
3/5 + 7/11
100!
R = QQ[x,y,z]/(x^3-y^3-z^3)
(x+y+z)^3
b = vars R
c = matrix {{x^2,y^2,z^2}}
M = coker b
N = ker c
```

### Output

```
i1 : 3/5 + 7/11

68
o1 = --
     55

o1 : QQ

i2 : 100!

o2 = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

i3 : R = QQ[x,y,z]/(x^3-y^3-z^3)

o3 = R

o3 : QuotientRing

i4 : (x+y+z)^3

2        2     3     2               2        2       2     3
o4 = 3x y + 3x*y  + 2y  + 3x z + 6x*y*z + 3y z + 3x*z  + 3y*z  + 2z

o4 : R

i5 : b = vars R

o5 = | x y z |

             1      3
o5 : Matrix R  <-- R

i6 : c = matrix {{x^2,y^2,z^2}}

o6 = | x2 y2 z2 |

             1      3
o6 : Matrix R  <-- R

i7 : M = coker b

o7 = cokernel | x y z |

                            1
o7 : R-module, quotient of R

i8 : N = ker c

o8 = image {2} | x  -y2 0   -z2 |
           {2} | -y x2  -z2 0   |
           {2} | -z 0   y2  x2  |

                             3
o8 : R-module, submodule of R
```

---

## preface / test.m2 — chunk 1

### Input

```macaulay2
res M
X = Proj R
HH^1 cotangentSheaf X 
i12 :
```

### Output

```
i9 : res M

1      3      4      4      4
o9 = R  <-- R  <-- R  <-- R  <-- R
                                  
     0      1      2      3      4

o9 : ChainComplex

i10 : X = Proj R

o10 = X

o10 : ProjectiveVariety

i11 : HH^1 cotangentSheaf X 

1
o11 = QQ

o11 : QQ-module, free

i12 :
```

---

## programming / chapter.m2 — chunk 0

### Input

```macaulay2
w
w = 2^100
w
(w,w') = (33,44)
w
w'
(w,w') = (33,   -- this is a comment
               44)
w = "abcdefghij"
```

### Output

```
i1 : w

o1 = w

o1 : Symbol

i2 : w = 2^100

o2 = 1267650600228229401496703205376

i3 : w

o3 = 1267650600228229401496703205376

i4 : (w,w') = (33,44)

o4 = (33, 44)

o4 : Sequence

i5 : w

o5 = 33

i6 : w'

o6 = 44

i7 : (w,w') = (33,   -- this is a comment
               44)

o7 = (33, 44)

o7 : Sequence

i8 : w = "abcdefghij"

o8 = abcdefghij
```

---

## programming / chapter.m2 — chunk 1

### Input

```macaulay2
w | w
w || w
2^100
2.^100
(36 + 1/8)^6
x1 = {1,a}
x2 = (2,b)
x3 = [3,c,d,e]
```

### Output

```
i9 : w | w

o9 = abcdefghijabcdefghij

i10 : w || w

o10 = abcdefghij
      abcdefghij

i11 : 2^100

o11 = 1267650600228229401496703205376

i12 : 2.^100

o12 = 1.26765 10^30

o12 : RR

i13 : (36 + 1/8)^6

582622237229761
o13 = ---------------
           262144

o13 : QQ

i14 : x1 = {1,a}

o14 = {1, a}

o14 : List

i15 : x2 = (2,b)

o15 = (2, b)

o15 : Sequence

i16 : x3 = [3,c,d,e]

o16 = [3, c, d, e]

o16 : Array
```

---

## programming / chapter.m2 — chunk 2

### Input

```macaulay2
1 .. 6
a .. f
xx = {x1,x2,x3}
#xx
xx#0
xx#0#1
join(x1,x2,x3)
append(x3,f)
```

### Output

```
i17 : 1 .. 6

o17 = (1, 2, 3, 4, 5, 6)

o17 : Sequence

i18 : a .. f

o18 = (a, b, c, d, e, f)

o18 : Sequence

i19 : xx = {x1,x2,x3}

o19 = {{1, a}, (2, b), [3, c, d, e]}

o19 : List

i20 : #xx

o20 = 3

i21 : xx#0

o21 = {1, a}

o21 : List

i22 : xx#0#1

o22 = a

o22 : Symbol

i23 : join(x1,x2,x3)

o23 = {1, a, 2, b, 3, c, d, e}

o23 : List

i24 : append(x3,f)

o24 = [3, c, d, e, f]

o24 : Array
```

---

## programming / chapter.m2 — chunk 3

### Input

```macaulay2
prepend(f,x3)
sum {1,2,3,4}
product {1,2,3,4}
f = (x,y) -> 1000 * x + y
f = (x,y) -> (z := 1000 * x; z + y)
f(3,7)
s = (3,7)
f s
```

### Output

```
i25 : prepend(f,x3)

o25 = [f, 3, c, d, e]

o25 : Array

i26 : sum {1,2,3,4}

o26 = 10

i27 : product {1,2,3,4}

o27 = 24

i28 : f = (x,y) -> 1000 * x + y

o28 = f

o28 : Function

i29 : f = (x,y) -> (z := 1000 * x; z + y)

o29 = f

o29 : Function

i30 : f(3,7)

o30 = 3007

i31 : s = (3,7)

o31 = (3, 7)

o31 : Sequence

i32 : f s

o32 = 3007
```

---

## programming / chapter.m2 — chunk 4

### Input

```macaulay2
sin 2.1
apply(1 .. 10, i -> i^3)
scan(1 .. 5, print)
1
2
3
4
5
apply(1 .. 10, i -> if even i then 1000*i else i)
apply(1 .. 10, i -> (if even i then return 1000*i; -i))
i = 1; while i < 50 do (print i; i = 2*i)
1
2
4
8
16
32
for i from 1 to 10 list i^3
for i from 1 to 4 do print i
1
2
3
4
```

### Output

```
i33 : sin 2.1

o33 = 0.863209

o33 : RR

i34 : apply(1 .. 10, i -> i^3)

o34 = (1, 8, 27, 64, 125, 216, 343, 512, 729, 1000)

o34 : Sequence

i35 : scan(1 .. 5, print)
1
2
3
4
5

i36 : apply(1 .. 10, i -> if even i then 1000*i else i)

o36 = (1, 2000, 3, 4000, 5, 6000, 7, 8000, 9, 10000)

o36 : Sequence

i37 : apply(1 .. 10, i -> (if even i then return 1000*i; -i))

o37 = (-1, 2000, -3, 4000, -5, 6000, -7, 8000, -9, 10000)

o37 : Sequence

i38 : i = 1; while i < 50 do (print i; i = 2*i)
1
2
4
8
16
32

i40 : for i from 1 to 10 list i^3

o40 = {1, 8, 27, 64, 125, 216, 343, 512, 729, 1000}

o40 : List

i41 : for i from 1 to 4 do print i
1
2
3
4
```

---

## programming / chapter.m2 — chunk 5

### Input

```macaulay2
for i from 2 to 100 do if not isPrime i then break i
for i from 2 to 100 when isPrime i do print i
2
3
print 2^100
1267650600228229401496703205376
(1 .. 5) / print;
1
2
3
4
5
<< 2^100
1267650600228229401496703205376
<< "the value is : " << 2^100
the value is : 1267650600228229401496703205376
<< "A = " << 2^100 << endl << "B = " << 2^200 << endl;
A = 1267650600228229401496703205376
B = 1606938044258990275541962092341162602522202993782792835301376
"foo" << "A = " << 2^100 << endl << close
```

### Output

```
i42 : for i from 2 to 100 do if not isPrime i then break i

o42 = 4

i43 : for i from 2 to 100 when isPrime i do print i
2
3

i44 : print 2^100
1267650600228229401496703205376

i45 : (1 .. 5) / print;
1
2
3
4
5

i46 : << 2^100
1267650600228229401496703205376

o46 = stdio

o46 : File

  --  the standard input output file

i47 : << "the value is : " << 2^100
the value is : 1267650600228229401496703205376

o47 = stdio

o47 : File

  --  the standard input output file

i48 : << "A = " << 2^100 << endl << "B = " << 2^200 << endl;
A = 1267650600228229401496703205376
B = 1606938044258990275541962092341162602522202993782792835301376

i49 : "foo" << "A = " << 2^100 << endl << close

o49 = foo

o49 : File
```

---

## programming / chapter.m2 — chunk 6

### Input

```macaulay2
get "foo"
load "foo"
A
input "foo"
A = 1267650600228229401496703205376
i55 :
R = QQ[x,y,z]
f = (x+y)^3
```

### Output

```
i50 : get "foo"

o50 = A = 1267650600228229401496703205376

i51 : load "foo"

i52 : A

o52 = 1267650600228229401496703205376

i53 : input "foo"

i54 : A = 1267650600228229401496703205376

o54 = 1267650600228229401496703205376

i55 :

i56 : R = QQ[x,y,z]

o56 = R

o56 : PolynomialRing

i57 : f = (x+y)^3

3     2        2    3
o57 = x  + 3x y + 3x*y  + y

o57 : R
```

---

## programming / chapter.m2 — chunk 7

### Input

```macaulay2
"foo" << f << close;
get "foo"
toString f
"foo" << toString f << close;
get "foo"
value oo
vars R
toString vars R
```

### Output

```
i58 : "foo" << f << close;

i59 : get "foo"

o59 =  3     2        2    3
      x  + 3x y + 3x*y  + y

i60 : toString f

o60 = x^3+3*x^2*y+3*x*y^2+y^3

i61 : "foo" << toString f << close;

i62 : get "foo"

o62 = x^3+3*x^2*y+3*x*y^2+y^3

i63 : value oo

3     2        2    3
o63 = x  + 3x y + 3x*y  + y

o63 : R

i64 : vars R

o64 = | x y z |

              1       3
o64 : Matrix R  <--- R

i65 : toString vars R

o65 = matrix {{x, y, z}}
```

---

## programming / chapter.m2 — chunk 8

### Input

```macaulay2
toExternalString vars R
R = QQ[x,y,z]/(x^3-y)
(x+y)^4
f = new HashTable from { a=>444, Daniel=>555, {c,d}=>{1,2,3,4}}
f#Daniel
f#{c,d}
Daniel = a
f.Daniel
```

### Output

```
i66 : toExternalString vars R

o66 = map(R^{{0}}, R^{{-1}, {-1}, {-1}}, {{x, y, z}})

i67 : R = QQ[x,y,z]/(x^3-y)

o67 = R

o67 : QuotientRing

i68 : (x+y)^4

2 2       3    4           2
o68 = 6x y  + 4x*y  + y  + x*y + 4y

o68 : R

i69 : f = new HashTable from { a=>444, Daniel=>555, {c,d}=>{1,2,3,4}}

o69 = HashTable{{c, d} => {1, 2, 3, 4}}
                a => 444
                Daniel => 555

o69 : HashTable

i70 : f#Daniel

o70 = 555

i71 : f#{c,d}

o71 = {1, 2, 3, 4}

o71 : List

i72 : Daniel = a

o72 = a

o72 : Symbol

i73 : f.Daniel

o73 = 555
```

---

## programming / chapter.m2 — chunk 9

### Input

```macaulay2
f#?a
f#?c
x = set{1,a,{4,5},a}
x#?a
peek x
y = tally{1,a,{4,5},a}
y#a
factor 60
```

### Output

```
i74 : f#?a

o74 = true

i75 : f#?c

o75 = false

i76 : x = set{1,a,{4,5},a}

o76 = Set {{4, 5}, 1, a}

o76 : Set

i77 : x#?a

o77 = true

i78 : peek x

o78 = Set{{4, 5} => 1}
          1 => 1
          a => 1

i79 : y = tally{1,a,{4,5},a}

o79 = Tally{{4, 5} => 1}
            1 => 1
            a => 2

o79 : Tally

i80 : y#a

o80 = 2

i81 : factor 60

2
o81 = 2 3*5

o81 : Product
```

---

## programming / chapter.m2 — chunk 10

### Input

```macaulay2
# factor 60
apply(2 .. 1000, i -> # factor i)
tally oo
R.ideal
ideal R
code demark
code(symbol **, RingMap, Module)
code(ideal, QuotientRing)
```

### Output

```
i82 : # factor 60

o82 = 3

i83 : apply(2 .. 1000, i -> # factor i)

o83 = (1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 3, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 3, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 3, 1, 2, 2, 1, 2, 3, 1, 2, 2, 3, 1, 2, 1, 2, 2, 2, 2, 3, 1, 2, 1, 2, 1, 3, 2, 2, 2, 2, 1, 3, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 3, 1, 2, 3, 2, 1, 2, 1, 3, 2, 2, 1, 3, 2, 2, 2, 2, 2, 3, 1, 2, 2, 2, 1, 3, 1, 1, 2, 3, 1, 3, 2, 2, 2, 2, 1, 3, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 3, 1, 2, 2, 3, 2, 3, 1, 2, 2, 2, 2, 2, 1, 2, 3, 2, 1, 3, 1, 3, 2, 2, 1, 3, 2, 2, 2, 2, 1, 3, 1, 3, 2, 2, 2, 3, 2, 2, 2, 3, 1, 2, 1, 2, 3, 2, 1, 3, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 4, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 1, 2, 2, 2, 1, 3, 1, 3, 3, 2, 1, 3, 2, 2, 2, 3, 1, 3, 1, 2, 1, 2, 2, 3, 2, 2, 2, 2, 1, 3, 2, 2, 3, 1, 1, 3, 2, 3, 2, 2, 1, 3, 2, 3, 2, 2, 1, 3, 1, 2, 3, 2, 2, 3, 1, 2, 2, 3, 1, 3, 1, 2, 3, 3, 2, 2, 1, 3, 2, 2, 1, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 3, 1, 3, 2, 3, 1, 3, 1, 2, 3, 2, 1, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 4, 1, 2, 2, 2, 2, 3, 1, 2, 2, 3, 2, 3, 1, 2, 3, 2, 1, 3, 1, 3, 2, 2, 1, 3, 2, 2, 3, 2, 1, 3, 1, 2, 2, 3, 2, 3, 1, 2, 2, 3, 2, 3, 1, 3, 2, 2, 2, 3, 1, 3, 2, 2, 1, 2, 3, 2, 2, 2, 1, 4, 2, 2, 2, 2, 2, 3, 1, 2, 3, 2, 1, 3, 2, 2, 2, 3, 2, 3, 1, 3, 2, 2, 2, 3, 2, 2, 2, 3, 1, 4, 1, 2, 2, 2, 2, 3, 2, 2, 3, 3, 1, 2, 1, 3, 3, 2, 2, 3, 1, 3, 2, 3, 1, 3, 2, 2, 2, 2, 1, 3, 2, 2, 2, 2, 3, 3, 1, 2, 2, 3, 1, 4, 1, 2, 3, 2, 1, 3, 2, 3, 2, 2, 2, 3, 2, 3, 2, 2, 1, 3, 2, 2, 3, 2, 2, 2, 1, 2, 2, 3, 1, 3, 2, 3, 3, 2, 2, 3, 1, 2, 2, 2, 1, 3, 2, 3, 2, 2, 1, 4, 2, 1, 2, 2, 2, 3, 2, 3, 2, 3, 1, 3, 1, 2, 3, 2, 2, 3, 1, 3, 2, 3, 2, 3, 2, 2, 2, 2, 2, 3, 1, 2, 2, 2, 2, 4, 1, 2, 2, 3, 2, 3, 2, 2, 3, 2, 1, 3, 2, 3, 3, 2, 1, 3, 2, 2, 2, 2, 1, 4, 1, 3, 2, 3, 2, 2, 1, 2, 2, 3, 2, 3, 2, 2, 3, 2, 1, 3, 2, 3, 2, 2, 1, 3, 3, 2, 2, 3, 1, 3, 1, 3, 2, 2, 2, 3, 1, 2, 3, 3, 2, 3, 1, 2, 3, 3, 1, 3, 1, 3, 2, 2, 2, 3, 1, 2, 3, 2, 2, 4, 1, 2, 2, 2, 2, 3, 2, 3, 2, 2, 1, 3, 1, 3, 3, 3, 1, 2, 2, 3, 3, 2, 1, 3, 2, 2, 2, 3, 1, 4, 1, 2, 3, 2, 3, 3, 2, 2, 2, 3, 2, 3, 1, 2, 2, 2, 1, 3, 2, 3, 2, 3, 1, 3, 2, 2, 2, 2, 2, 4, 1, 2, 3, 2, 2, 3, 2, 2, 2, 3, 1, 3, 2, 2, 3, 2, 2, 3, 1, 3, 2, 2, 2, 4, 3, 2, 2, 2, 1, 3, 2, 2, 2, 2, 2, 3, 1, 3, 1, 3, 2, 3, 1, 2, 3, 2, 2, 3, 1, 3, 3, 3, 1, 3, 2, 2, 2, 3, 2, 3, 1, 2, 2, 3, 2, 3, 1, 2, 3, 3, 1, 3, 2, 2, 3, 2, 2, 2, 1, 4, 2, 2, 1, 3, 2, 2, 3, 2, 2, 4, 2, 3, 2, 2, 2, 3, 1, 2, 2, 3, 2, 3, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 1, 3, 1, 3, 2, 3, 2, 3, 2, 2, 3, 3, 1, 3, 1, 2, 3, 3, 1, 3, 1, 3, 2, 2, 2, 3, 2, 3, 2, 2, 1, 4, 1, 2, 2, 2, 2, 3, 2, 2, 2, 3, 2, 3, 1, 3, 3, 2, 1, 4, 1, 3, 3, 2, 1, 2, 2, 2, 2, 3, 2, 4, 2, 2, 2, 3, 2, 3, 1, 2, 2, 3, 1, 3, 1, 3, 3, 2, 1, 3, 2, 3, 2, 2, 2, 3, 2, 2, 3, 2, 2, 3, 2, 3, 3, 2, 2, 3, 1, 2, 2, 4, 1, 3, 2, 2, 3, 2, 2, 3, 1, 3, 2, 2, 2, 4, 2, 2, 2, 2, 1, 4, 2, 2, 2, 2, 3, 3, 1, 3, 2, 3, 1, 3, 2, 2, 3, 3, 1, 3, 2, 3, 2, 3, 1, 3, 2, 2, 3, 2, 2, 3, 1, 3, 2, 2, 2, 4, 1, 2, 3, 3, 1, 2, 2, 2, 3, 2, 1, 3, 2, 3, 2, 2, 1, 3, 2, 3, 3, 3, 2, 4, 1, 2, 2, 3, 2, 3, 1, 2, 2, 2)

o83 : Sequence

i84 : tally oo

o84 = Tally{1 => 193}
            2 => 508
            3 => 275
            4 => 23

o84 : Tally

i85 : R.ideal

3
o85 = ideal(x  - y)

o85 : Ideal of QQ [x, y, z]

i86 : ideal R

3
o86 = ideal(x  - y)

o86 : Ideal of QQ [x, y, z]

i87 : code demark

o87 = -- ../../../m2/fold.m2:23
      demark = (s,v) -> concatenate between(s,v)

i88 : code(symbol **, RingMap, Module)

o88 = -- ../../../m2/ringmap.m2:294-298
      RingMap ** Module := Module => (f,M) -> (
           R := source f;
           S := target f;
           if R =!= ring M then error "expected module over source ring";
           cokernel f(presentation M));

i89 : code(ideal, QuotientRing)

o89 = -- ../../../m2/quotring.m2:7
      ideal QuotientRing := R -> R.ideal
```

---

## programming / chapter.m2 — chunk 11

### Input

```macaulay2
denom = method();
denom QQ := x -> denominator x;
denom ZZ := x -> 1;
denom(5/3)
denom 5
i95 :
```

### Output

```
i90 : denom = method();

i91 : denom QQ := x -> denominator x;

i92 : denom ZZ := x -> 1;

i93 : denom(5/3)

o93 = 3

i94 : denom 5

o94 = 1

i95 :
```

---

## programming / test.m2 — chunk 0

### Input

```macaulay2
w
w = 2^100
w
(w,w') = (33,44)
w
w'
(w,w') = (33,   -- this is a comment
               44)
w = "abcdefghij"
```

### Output

```
i1 : w

o1 = w

o1 : Symbol

i2 : w = 2^100

o2 = 1267650600228229401496703205376

i3 : w

o3 = 1267650600228229401496703205376

i4 : (w,w') = (33,44)

o4 = (33, 44)

o4 : Sequence

i5 : w

o5 = 33

i6 : w'

o6 = 44

i7 : (w,w') = (33,   -- this is a comment
               44)

o7 = (33, 44)

o7 : Sequence

i8 : w = "abcdefghij"

o8 = abcdefghij
```

---

## programming / test.m2 — chunk 1

### Input

```macaulay2
w | w
w || w
2^100
2.^100
(36 + 1/8)^6
x1 = {1,a}
x2 = (2,b)
x3 = [3,c,d,e]
```

### Output

```
i9 : w | w

o9 = abcdefghijabcdefghij

i10 : w || w

o10 = abcdefghij
      abcdefghij

i11 : 2^100

o11 = 1267650600228229401496703205376

i12 : 2.^100

o12 = 1.267650600228229e30

o12 : RR (of precision 53)

i13 : (36 + 1/8)^6

582622237229761
o13 = ---------------
           262144

o13 : QQ

i14 : x1 = {1,a}

o14 = {1, a}

o14 : List

i15 : x2 = (2,b)

o15 = (2, b)

o15 : Sequence

i16 : x3 = [3,c,d,e]

o16 = [3, c, d, e]

o16 : Array
```

---

## programming / test.m2 — chunk 2

### Input

```macaulay2
1 .. 6
a .. f
xx = {x1,x2,x3}
#xx
xx#0
xx#0#1
join(x1,x2,x3)
append(x3,f)
```

### Output

```
i17 : 1 .. 6

o17 = (1, 2, 3, 4, 5, 6)

o17 : Sequence

i18 : a .. f

o18 = (a, b, c, d, e, f)

o18 : Sequence

i19 : xx = {x1,x2,x3}

o19 = {{1, a}, (2, b), [3, c, d, e]}

o19 : List

i20 : #xx

o20 = 3

i21 : xx#0

o21 = {1, a}

o21 : List

i22 : xx#0#1

o22 = a

o22 : Symbol

i23 : join(x1,x2,x3)

o23 = {1, a, 2, b, 3, c, d, e}

o23 : List

i24 : append(x3,f)

o24 = [3, c, d, e, f]

o24 : Array
```

---

## programming / test.m2 — chunk 3

### Input

```macaulay2
prepend(f,x3)
sum {1,2,3,4}
product {1,2,3,4}
f = (x,y) -> 1000 * x + y
f = (x,y) -> (z := 1000 * x; z + y)
f(3,7)
s = (3,7)
f s
```

### Output

```
i25 : prepend(f,x3)

o25 = [f, 3, c, d, e]

o25 : Array

i26 : sum {1,2,3,4}

o26 = 10

i27 : product {1,2,3,4}

o27 = 24

i28 : f = (x,y) -> 1000 * x + y

o28 = f

o28 : FunctionClosure

i29 : f = (x,y) -> (z := 1000 * x; z + y)

o29 = f

o29 : FunctionClosure

i30 : f(3,7)

o30 = 3007

i31 : s = (3,7)

o31 = (3, 7)

o31 : Sequence

i32 : f s

o32 = 3007
```

---

## programming / test.m2 — chunk 4

### Input

```macaulay2
sin 2.1
apply(1 .. 10, i -> i^3)
scan(1 .. 5, print)
1
2
3
4
5
apply(1 .. 10, i -> if even i then 1000*i else i)
apply(1 .. 10, i -> (if even i then return 1000*i; -i))
i = 1; while i < 50 do (print i; i = 2*i)
1
2
4
8
16
32
for i from 1 to 10 list i^3
for i from 1 to 4 do print i
1
2
3
4
```

### Output

```
i33 : sin 2.1

o33 = .8632093666488737

o33 : RR (of precision 53)

i34 : apply(1 .. 10, i -> i^3)

o34 = (1, 8, 27, 64, 125, 216, 343, 512, 729, 1000)

o34 : Sequence

i35 : scan(1 .. 5, print)
1
2
3
4
5

i36 : apply(1 .. 10, i -> if even i then 1000*i else i)

o36 = (1, 2000, 3, 4000, 5, 6000, 7, 8000, 9, 10000)

o36 : Sequence

i37 : apply(1 .. 10, i -> (if even i then return 1000*i; -i))

o37 = (-1, 2000, -3, 4000, -5, 6000, -7, 8000, -9, 10000)

o37 : Sequence

i38 : i = 1; while i < 50 do (print i; i = 2*i)
1
2
4
8
16
32

i40 : for i from 1 to 10 list i^3

o40 = {1, 8, 27, 64, 125, 216, 343, 512, 729, 1000}

o40 : List

i41 : for i from 1 to 4 do print i
1
2
3
4
```

---

## programming / test.m2 — chunk 5

### Input

```macaulay2
for i from 2 to 100 do if not isPrime i then break i
for i from 2 to 100 when isPrime i do print i
2
3
print 2^100
1267650600228229401496703205376
(1 .. 5) / print;
1
2
3
4
5
<< 2^100
1267650600228229401496703205376
<< "the value is : " << 2^100
the value is : 1267650600228229401496703205376
<< "A = " << 2^100 << endl << "B = " << 2^200 << endl;
A = 1267650600228229401496703205376
B = 1606938044258990275541962092341162602522202993782792835301376
"foo" << "A = " << 2^100 << endl << close
```

### Output

```
i42 : for i from 2 to 100 do if not isPrime i then break i

o42 = 4

i43 : for i from 2 to 100 when isPrime i do print i
2
3

i44 : print 2^100
1267650600228229401496703205376

i45 : (1 .. 5) / print;
1
2
3
4
5

i46 : << 2^100
1267650600228229401496703205376

o46 = stdio

o46 : File

i47 : << "the value is : " << 2^100
the value is : 1267650600228229401496703205376

o47 = stdio

o47 : File

i48 : << "A = " << 2^100 << endl << "B = " << 2^200 << endl;
A = 1267650600228229401496703205376
B = 1606938044258990275541962092341162602522202993782792835301376

i49 : "foo" << "A = " << 2^100 << endl << close

o49 = foo

o49 : File
```

---

## programming / test.m2 — chunk 6

### Input

```macaulay2
get "foo"
load "foo"
A
input "foo"
R = QQ[x,y,z]
f = (x+y)^3
"foo" << f << close;
get "foo"
```

### Output

```
i50 : get "foo"

o50 = A = 1267650600228229401496703205376

i51 : load "foo"

i52 : A

o52 = 1267650600228229401496703205376

i53 : input "foo"

ii54 : A = 1267650600228229401496703205376

oo54 = 1267650600228229401496703205376

ii55 :

i56 : R = QQ[x,y,z]

o56 = R

o56 : PolynomialRing

i57 : f = (x+y)^3

3     2        2    3
o57 = x  + 3x y + 3x*y  + y

o57 : R

i58 : "foo" << f << close;

i59 : get "foo"

o59 =  3     2        2    3
      x  + 3x y + 3x*y  + y
```

---

## programming / test.m2 — chunk 7

### Input

```macaulay2
toString f
"foo" << toString f << close;
get "foo"
value oo
vars R
toString vars R
toExternalString vars R
R = QQ[x,y,z]/(x^3-y)
```

### Output

```
i60 : toString f

o60 = x^3+3*x^2*y+3*x*y^2+y^3

i61 : "foo" << toString f << close;

i62 : get "foo"

o62 = x^3+3*x^2*y+3*x*y^2+y^3

i63 : value oo

3     2        2    3
o63 = x  + 3x y + 3x*y  + y

o63 : R

i64 : vars R

o64 = | x y z |

              1      3
o64 : Matrix R  <-- R

i65 : toString vars R

o65 = matrix {{x, y, z}}

i66 : toExternalString vars R

o66 = map(R^1,R^{3:{-1}},{{x, y, z}})

i67 : R = QQ[x,y,z]/(x^3-y)

o67 = R

o67 : QuotientRing
```

---

## programming / test.m2 — chunk 8

### Input

```macaulay2
(x+y)^4
f = new HashTable from { a=>444, Daniel=>555, {c,d}=>{1,2,3,4}}
f#Daniel
f#{c,d}
Daniel = a
f.Daniel
f#?a
f#?c
```

### Output

```
i68 : (x+y)^4

2 2       3    4           2
o68 = 6x y  + 4x*y  + y  + x*y + 4y

o68 : R

i69 : f = new HashTable from { a=>444, Daniel=>555, {c,d}=>{1,2,3,4}}

o69 = HashTable{{c, d} => {1, 2, 3, 4}}
                a => 444
                Daniel => 555

o69 : HashTable

i70 : f#Daniel

o70 = 555

i71 : f#{c,d}

o71 = {1, 2, 3, 4}

o71 : List

i72 : Daniel = a

o72 = a

o72 : Symbol

i73 : f.Daniel

o73 = 555

i74 : f#?a

o74 = true

i75 : f#?c

o75 = false
```

---

## programming / test.m2 — chunk 9

### Input

```macaulay2
x = set{1,a,{4,5},a}
x#?a
peek x
y = tally{1,a,{4,5},a}
y#a
factor 60
# factor 60
apply(2 .. 1000, i -> # factor i)
```

### Output

```
i76 : x = set{1,a,{4,5},a}

o76 = set {{4, 5}, 1, a}

o76 : Set

i77 : x#?a

o77 = true

i78 : peek x

o78 = Set{{4, 5} => 1}
          1 => 1
          a => 1

i79 : y = tally{1,a,{4,5},a}

o79 = Tally{{4, 5} => 1}
            1 => 1
            a => 2

o79 : Tally

i80 : y#a

o80 = 2

i81 : factor 60

2
o81 = 2 3*5

o81 : Expression of class Product

i82 : # factor 60

o82 = 3

i83 : apply(2 .. 1000, i -> # factor i)

o83 = (1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 3, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 3, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 3, 1, 2, 2, 1, 2, 3, 1, 2, 2, 3, 1, 2, 1, 2, 2, 2, 2, 3, 1, 2, 1, 2, 1, 3, 2, 2, 2, 2, 1, 3, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 3, 1, 2, 3, 2, 1, 2, 1, 3, 2, 2, 1, 3, 2, 2, 2, 2, 2, 3, 1, 2, 2, 2, 1, 3, 1, 1, 2, 3, 1, 3, 2, 2, 2, 2, 1, 3, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 3, 1, 2, 2, 3, 2, 3, 1, 2, 2, 2, 2, 2, 1, 2, 3, 2, 1, 3, 1, 3, 2, 2, 1, 3, 2, 2, 2, 2, 1, 3, 1, 3, 2, 2, 2, 3, 2, 2, 2, 3, 1, 2, 1, 2, 3, 2, 1, 3, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 4, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 1, 2, 2, 2, 1, 3, 1, 3, 3, 2, 1, 3, 2, 2, 2, 3, 1, 3, 1, 2, 1, 2, 2, 3, 2, 2, 2, 2, 1, 3, 2, 2, 3, 1, 1, 3, 2, 3, 2, 2, 1, 3, 2, 3, 2, 2, 1, 3, 1, 2, 3, 2, 2, 3, 1, 2, 2, 3, 1, 3, 1, 2, 3, 3, 2, 2, 1, 3, 2, 2, 1, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 3, 1, 3, 2, 3, 1, 3, 1, 2, 3, 2, 1, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 4, 1, 2, 2, 2, 2, 3, 1, 2, 2, 3, 2, 3, 1, 2, 3, 2, 1, 3, 1, 3, 2, 2, 1, 3, 2, 2, 3, 2, 1, 3, 1, 2, 2, 3, 2, 3, 1, 2, 2, 3, 2, 3, 1, 3, 2, 2, 2, 3, 1, 3, 2, 2, 1, 2, 3, 2, 2, 2, 1, 4, 2, 2, 2, 2, 2, 3, 1, 2, 3, 2, 1, 3, 2, 2, 2, 3, 2, 3, 1, 3, 2, 2, 2, 3, 2, 2, 2, 3, 1, 4, 1, 2, 2, 2, 2, 3, 2, 2, 3, 3, 1, 2, 1, 3, 3, 2, 2, 3, 1, 3, 2, 3, 1, 3, 2, 2, 2, 2, 1, 3, 2, 2, 2, 2, 3, 3, 1, 2, 2, 3, 1, 4, 1, 2, 3, 2, 1, 3, 2, 3, 2, 2, 2, 3, 2, 3, 2, 2, 1, 3, 2, 2, 3, 2, 2, 2, 1, 2, 2, 3, 1, 3, 2, 3, 3, 2, 2, 3, 1, 2, 2, 2, 1, 3, 2, 3, 2, 2, 1, 4, 2, 1, 2, 2, 2, 3, 2, 3, 2, 3, 1, 3, 1, 2, 3, 2, 2, 3, 1, 3, 2, 3, 2, 3, 2, 2, 2, 2, 2, 3, 1, 2, 2, 2, 2, 4, 1, 2, 2, 3, 2, 3, 2, 2, 3, 2, 1, 3, 2, 3, 3, 2, 1, 3, 2, 2, 2, 2, 1, 4, 1, 3, 2, 3, 2, 2, 1, 2, 2, 3, 2, 3, 2, 2, 3, 2, 1, 3, 2, 3, 2, 2, 1, 3, 3, 2, 2, 3, 1, 3, 1, 3, 2, 2, 2, 3, 1, 2, 3, 3, 2, 3, 1, 2, 3, 3, 1, 3, 1, 3, 2, 2, 2, 3, 1, 2, 3, 2, 2, 4, 1, 2, 2, 2, 2, 3, 2, 3, 2, 2, 1, 3, 1, 3, 3, 3, 1, 2, 2, 3, 3, 2, 1, 3, 2, 2, 2, 3, 1, 4, 1, 2, 3, 2, 3, 3, 2, 2, 2, 3, 2, 3, 1, 2, 2, 2, 1, 3, 2, 3, 2, 3, 1, 3, 2, 2, 2, 2, 2, 4, 1, 2, 3, 2, 2, 3, 2, 2, 2, 3, 1, 3, 2, 2, 3, 2, 2, 3, 1, 3, 2, 2, 2, 4, 3, 2, 2, 2, 1, 3, 2, 2, 2, 2, 2, 3, 1, 3, 1, 3, 2, 3, 1, 2, 3, 2, 2, 3, 1, 3, 3, 3, 1, 3, 2, 2, 2, 3, 2, 3, 1, 2, 2, 3, 2, 3, 1, 2, 3, 3, 1, 3, 2, 2, 3, 2, 2, 2, 1, 4, 2, 2, 1, 3, 2, 2, 3, 2, 2, 4, 2, 3, 2, 2, 2, 3, 1, 2, 2, 3, 2, 3, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 1, 3, 1, 3, 2, 3, 2, 3, 2, 2, 3, 3, 1, 3, 1, 2, 3, 3, 1, 3, 1, 3, 2, 2, 2, 3, 2, 3, 2, 2, 1, 4, 1, 2, 2, 2, 2, 3, 2, 2, 2, 3, 2, 3, 1, 3, 3, 2, 1, 4, 1, 3, 3, 2, 1, 2, 2, 2, 2, 3, 2, 4, 2, 2, 2, 3, 2, 3, 1, 2, 2, 3, 1, 3, 1, 3, 3, 2, 1, 3, 2, 3, 2, 2, 2, 3, 2, 2, 3, 2, 2, 3, 2, 3, 3, 2, 2, 3, 1, 2, 2, 4, 1, 3, 2, 2, 3, 2, 2, 3, 1, 3, 2, 2, 2, 4, 2, 2, 2, 2, 1, 4, 2, 2, 2, 2, 3, 3, 1, 3, 2, 3, 1, 3, 2, 2, 3, 3, 1, 3, 2, 3, 2, 3, 1, 3, 2, 2, 3, 2, 2, 3, 1, 3, 2, 2, 2, 4, 1, 2, 3, 3, 1, 2, 2, 2, 3, 2, 1, 3, 2, 3, 2, 2, 1, 3, 2, 3, 3, 3, 2, 4, 1, 2, 2, 3, 2, 3, 1, 2, 2, 2)

o83 : Sequence
```

---

## programming / test.m2 — chunk 10

### Input

```macaulay2
tally oo
R.ideal
ideal R
code demark
code(symbol **, RingMap, Module)
code(ideal, QuotientRing)
denom = method();
denom QQ := x -> denominator x;
```

### Output

```
i84 : tally oo

o84 = Tally{1 => 193}
            2 => 508
            3 => 275
            4 => 23

o84 : Tally

i85 : R.ideal

3
o85 = ideal(x  - y)

o85 : Ideal of QQ[x..z]

i86 : ideal R

3
o86 = ideal(x  - y)

o86 : Ideal of QQ[x..z]

i87 : code demark

o87 = /home/dan/src/M2/1.2/Macaulay2/m2/fold.m2:23:16-23:41: --source code:
      demark = (s,v) -> concatenate between(s,v)

i88 : code(symbol **, RingMap, Module)

o88 = -- code for method: RingMap ** Module
      /home/dan/src/M2/1.2/Macaulay2/m2/ringmap.m2:384:38-388:30: --source code:
      RingMap ** Module := Module => (f, M) -> tensor(f, M)

i89 : code(ideal, QuotientRing)

o89 = -- code for method: ideal(QuotientRing)
      /home/dan/src/M2/1.2/Macaulay2/m2/quotring.m2:5:25-5:30: --source code:
      ideal QuotientRing := R -> R.ideal

i90 : denom = method();

i91 : denom QQ := x -> denominator x;
```

---

## programming / test.m2 — chunk 11

### Input

```macaulay2
denom ZZ := x -> 1;
denom(5/3)
denom 5
i95 :
```

### Output

```
i92 : denom ZZ := x -> 1;

i93 : denom(5/3)

o93 = 3

i94 : denom 5

o94 = 1

i95 :
```

---

## schemes / chapter.m2 — chunk 0

### Input

```macaulay2
S = ZZ[x, y, z];
elementaryBasis = ideal(x+y+z, x*y+x*z+y*z, x*y*z);
saturate(elementaryBasis, x)
powerSumBasis = ideal(x+y+z, x^2+y^2+z^2, x^3+y^3+z^3);
saturate(powerSumBasis, x)
clearAll
S = QQ[t, y_0 .. y_8, a..i, MonomialOrder => Eliminate 10];
N3 = (matrix {{0,1,0},{0,0,1},{0,0,0}}) ** S
```

### Output

```
i1 : S = ZZ[x, y, z];

i2 : elementaryBasis = ideal(x+y+z, x*y+x*z+y*z, x*y*z);

o2 : Ideal of S

i3 : saturate(elementaryBasis, x)

o3 = ideal 1

o3 : Ideal of S

i4 : powerSumBasis = ideal(x+y+z, x^2+y^2+z^2, x^3+y^3+z^3);

o4 : Ideal of S

i5 : saturate(powerSumBasis, x)

2            2
o5 = ideal (6, x + y + z, 2y  + 2y*z + 2z , 3y*z)

o5 : Ideal of S

i6 : clearAll

i7 : S = QQ[t, y_0 .. y_8, a..i, MonomialOrder => Eliminate 10];

i8 : N3 = (matrix {{0,1,0},{0,0,1},{0,0,0}}) ** S

o8 = | 0 1 0 |
     | 0 0 1 |
     | 0 0 0 |

             3       3
o8 : Matrix S  <--- S
```

---

## schemes / chapter.m2 — chunk 1

### Input

```macaulay2
G = genericMatrix(S, y_0, 3, 3)
classicalAdjoint = (G) -> (
           n := degree target G;
           m := degree source G;
           matrix table(n, n, (i, j) -> (-1)^(i+j) * det(
                     submatrix(G, {0..j-1, j+1..n-1}, 
                          {0..i-1, i+1..m-1}))));
num = G * N3 * classicalAdjoint(G);
D = det(G);
M = genericMatrix(S, a, 3, 3);
elimIdeal = minors(1, (D*id_(S^3))*M - num) + ideal(1-D*t);
closureOfOrbit = ideal selectInSubring(1, gens gb elimIdeal);
X = ideal substitute(
              contract(matrix{{t^2,t,1}}, det(t-M)),
              {t => 0_S})
```

### Output

```
i9 : G = genericMatrix(S, y_0, 3, 3)

o9 = | y_0 y_3 y_6 |
     | y_1 y_4 y_7 |
     | y_2 y_5 y_8 |

             3       3
o9 : Matrix S  <--- S

i10 : classicalAdjoint = (G) -> (
           n := degree target G;
           m := degree source G;
           matrix table(n, n, (i, j) -> (-1)^(i+j) * det(
                     submatrix(G, {0..j-1, j+1..n-1}, 
                          {0..i-1, i+1..m-1}))));

i11 : num = G * N3 * classicalAdjoint(G);

3       3
o11 : Matrix S  <--- S

i12 : D = det(G);

i13 : M = genericMatrix(S, a, 3, 3);

3       3
o13 : Matrix S  <--- S

i14 : elimIdeal = minors(1, (D*id_(S^3))*M - num) + ideal(1-D*t);

o14 : Ideal of S

i15 : closureOfOrbit = ideal selectInSubring(1, gens gb elimIdeal);

o15 : Ideal of S

i16 : X = ideal substitute(
              contract(matrix{{t^2,t,1}}, det(t-M)),
              {t => 0_S})

o16 = ideal (- a - e - i, - b*d + a*e - c*g - f*h + a*i + e*i, c*e*g - b*f*g - c*d*h + a*f*h + b*d*i - a*e*i)

o16 : Ideal of S
```

---

## schemes / chapter.m2 — chunk 2

### Input

```macaulay2
closureOfOrbit == X
clearAll
S = QQ[x, y, z, a..j, MonomialOrder => Eliminate 2];
F = a*x^3+b*x^2*y+c*x^2*z+d*x*y^2+e*x*y*z+f*x*z^2+g*y^3+h*y^2*z+
                   i*y*z^2+j*z^3;
partials = submatrix(jacobian matrix{{F}}, {0..2}, {0})
singularities = ideal(partials) + ideal(F);
elimDiscr = time ideal selectInSubring(1,gens gb singularities);
     -- used 64.27 seconds
elimDiscr = substitute(elimDiscr, {z => 1});
```

### Output

```
i17 : closureOfOrbit == X

o17 = true

i18 : clearAll

i19 : S = QQ[x, y, z, a..j, MonomialOrder => Eliminate 2];

i20 : F = a*x^3+b*x^2*y+c*x^2*z+d*x*y^2+e*x*y*z+f*x*z^2+g*y^3+h*y^2*z+
                   i*y*z^2+j*z^3;

i21 : partials = submatrix(jacobian matrix{{F}}, {0..2}, {0})

o21 = {1} | 3x2a+2xyb+y2d+2xzc+yze+z2f |
      {1} | x2b+2xyd+3y2g+xze+2yzh+z2i |
      {1} | x2c+xye+y2h+2xzf+2yzi+3z2j |

              3       1
o21 : Matrix S  <--- S

i22 : singularities = ideal(partials) + ideal(F);

o22 : Ideal of S

i23 : elimDiscr = time ideal selectInSubring(1,gens gb singularities);
     -- used 64.27 seconds

o23 : Ideal of S

i24 : elimDiscr = substitute(elimDiscr, {z => 1});

o24 : Ideal of S
```

---

## schemes / chapter.m2 — chunk 3

### Input

```macaulay2
A = contract(matrix{{x^2,x*y,y^2,x*z,y*z,z^2}},
              diff(transpose matrix{{x,y,z}},F))
hess = det submatrix(jacobian ideal partials, {0..2}, {0..2});
B = contract(matrix{{x^2,x*y,y^2,x*z,y*z,z^2}},
              diff(transpose matrix{{x,y,z}},hess))
detDiscr = ideal det (A || B);
detDiscr == elimDiscr
detDiscr_0
numgens detDiscr
# terms detDiscr_0
```

### Output

```
i25 : A = contract(matrix{{x^2,x*y,y^2,x*z,y*z,z^2}},
              diff(transpose matrix{{x,y,z}},F))

o25 = {1} | 3a 2b d  2c e  f  |
      {1} | b  2d 3g e  2h i  |
      {1} | c  e  h  2f 2i 3j |

              3       6
o25 : Matrix S  <--- S

i26 : hess = det submatrix(jacobian ideal partials, {0..2}, {0..2});

i27 : B = contract(matrix{{x^2,x*y,y^2,x*z,y*z,z^2}},
              diff(transpose matrix{{x,y,z}},hess))

o27 = {1} | -24c2d+24bce-18ae2-24b2f+72adf               4be2-16bdf-48c2g+144afg+32bch-48aeh-16b2i+48adi         2de2-8d2f-24ceg+24bfg+16cdh-24ah2-8bdi+72agi  4ce2-16cdf-16c2h+48afh+32bci-48aei-48b2j+144adj         2e3-8def-24cfg-8ceh+24bfh+24cdi-8bei-24ahi-24bdj+216agj 2e2f-8df2-8cfh+16bfi-24ai2+24cdj-24bej+72ahj  |
      {1} | 2be2-8bdf-24c2g+72afg+16bch-24aeh-8b2i+24adi 4de2-16d2f-48ceg+48bfg+32cdh-48ah2-16bdi+144agi         -18e2g+24deh-24bh2-24d2i+72bgi                2e3-8def-24cfg-8ceh+24bfh+24cdi-8bei-24ahi-24bdj+216agj -48efg+4e2h+32dfh-16ch2+48cgi-16bhi-48d2j+144bgj        -24f2g+2e2i+16dfi-8chi-8bi2-24dej+72cgj+24bhj |
      {1} | 2ce2-8cdf-8c2h+24afh+16bci-24aei-24b2j+72adj 2e3-8def-24cfg-8ceh+24bfh+24cdi-8bei-24ahi-24bdj+216agj -24efg+2e2h+16dfh-8ch2+24cgi-8bhi-24d2j+72bgj 4e2f-16df2-16cfh+32bfi-48ai2+48cdj-48bej+144ahj         -48f2g+4e2i+32dfi-16chi-16bi2-48dej+144cgj+48bhj        -24f2h+24efi-24ci2-18e2j+72chj                |

              3       6
o27 : Matrix S  <--- S

i28 : detDiscr = ideal det (A || B);

o28 : Ideal of S

i29 : detDiscr == elimDiscr

o29 = true

i30 : detDiscr_0

2   4 3 2             5 3 2           6 3 2          2 2 2 4 2                3 4 2         2 4 4 2              4 4 2          2 3 5 2              2   5 2          2   2 5 2            2 2 5 2          2 2 6 2            3 6 2         3 3 3 3          3     4 3            2 2 4 3              3 4 3            2   5 3           2     5 3                   5 3              2 5 3          3 6 3                 6 3          4 4 4             2 5 4           2 6 4         2   5 2                6 2              7 2             2 2 3 3                   4 3            2 5 3                 5 3             2 3   4                 2 2 4             2   3 4               2 3 4             2 2   5               3   5            3 4 2 2           3   2 3 2             2 3 3 2               4 3 2           3 2 4 2              2     4 2            2   2 4 2                  2 4 2                3 4 2           2     5 2                2 5 2            3   5 2                    5 2           4   3 3             3 4 3              2   4 3                  5 3             2   5 3          2 2 4 2 2               5 2 2             6 2 2          2 3 2 3 2              2 3 3 2         2   4 3 2            2 4 3 2          2 4 4 2              3   4 2          2 2 2 4 2            3 2 4 2          2 3 5 2            4 5 2          3   3 2   2            2 4 2   2              5 2   2          3 2   3   2             2   2 3   2          2   3 3   2                3 3   2              4 3   2             2 2 4   2           2       4   2               2   4   2          3 2 4   2                2 4   2          3   5   2               2 5   2          4 2 2 2 2          4   3 2 2            3   3 2 2             2 2 3 2 2         2 2 4 2 2             2   4 2 2                   4 2 2           2 2 4 2 2            2 5 2 2           2   5 2 2          3 2 2 2 3            2   3 2 3         2   4 2 3                4 2 3             5 2 3          3 3 3 3            2 2   3 3          2     2 3 3              2 2 3 3         3 3 3 3                3 3 3          2   2 4 3               3 4 3          3     4 3               2   4 3          4     2   3            3 2 2   3            2 3 2   3             3   3   3          2 2   3   3             2     3   3               2 3   3          2 3 3   3          3   4   3                   4   3            2   4   3           2     4   3          5 2 2 3             3 3 2 3           2   4 2 3          4 2 2 4            3     2 4          2 2 2 2 4            2   2 2 4                3 2 4         2 4 2 4          2 2   3 4            2 2 3 4          3     3 4                    3 4            2 2 3 4           2   2 3 4          4 4 4             2   4 4           2 2 4 4            4 2   4            3   2   4               2 3   4           2     3   4           2   4   4          2 3 2 5            3   2 5              2   2 5          2   2 2 5            2   3 5           2     3 5           2     3 5          2 2 2 6          3 3 6         2   6                  7                8               2 2 4 2                   5 2            2 6 2                 6 2             2 3 2 3                 2 3 3             2   4 3               2 4 3             2 4 4                 3   4             2 2 2 4                3 2 4             2 3 5                4 5            3 5   2           3   3 2 2             2 4 2 2               5 2 2           3 2   3 2             2   2 3 2            2   3 3 2                  3 3 2                4 3 2              2 2 4 2            2       4 2                2   4 2            3 2 4 2                  2 4 2            3   5 2                2 5 2           4 2 2 3           4   3 3             3   3 3              2 2 3 3           2 2 4 3              2   4 3                    4 3            2 2 4 3             2   5 3          2 2 5                    6                  7               2 3 3 2                 2 4 2            2   5 2               2 5 2             2 4   3                 3 2 3             2 2 3 3               3 3 3             2 3   4               4   4             3   4                   2 5                     6                  3 2 2 2                  2   3 2               2   4 2                     4 2                   5 2                3 3 3                 2 2   3                2     2 3                    2 2 3               3 3 3                      3 3               2   2 4                    3 4               3     4                   2   4               4 3   2              4     2 2               3 2 2 2               2 3 2 2                3   3 2              2 2   3 2                2     3 2                    2 3 2              2 3 3 2              3   4 2                       4 2               2   4 2              2     4 2             5 2 3                3 3 3               2   4 3             3 2 3   2             2   4   2          2   5   2                 5   2              6   2           3 3   2 2              2 2 2 2 2           2     3 2 2               2 3 2 2          3 4 2 2                 4 2 2             2 3 3 2            2   2   3 2                3   3 2           3   2 3 2                2 2 3 2           3 2 4 2                3 4 2           4   2     2             3 3     2             2 4     2            4 2 2   2             3     2   2            2 2 2 2   2             2   2 2   2                3 2   2            2 4 2   2            2 2   3   2              2 2 3   2            3     3   2                      3   2              2 2 3   2             2   2 3   2            4 4   2              2   4   2            2 2 4   2           5     2 2              4 2 2 2              3   2 2 2                 2 3 2 2            2     3 2 2             2   4 2 2           4 2     3             3   2   3           2 2 3   3             2   3   3                 4   3          2 5   3             3 2 2 3            2 2     2 3             2 2   2 3           3   2 2 3                    2 2 3             2 3 2 3            2   3 2 3           3     3 3                 2 3 3           4   3 3              2     3 3            2 2   3 3             4       3             3 2     3           2 3 2   3              3   2   3                2   2   3            2   2 2   3              2   3   3             2     3   3            2     3   3           2 3     4             3       4               2 2   4           2   3   4           3 2 2 4               2   2 4              2     2 4            2       2 4            2   2 2 4             3 3 4            2     3 4            2 2 2   4            3 3   4           2 2     5           2     2 5            3   2 5          2 3 4   2             2 5   2           2 6   2          2 4 2 2 2              3 3 2 2         2 2 4 2 2            3 4 2 2          2 5 3 2              4   3 2          2 3 2 3 2            4 2 3 2          2 4 4 2            5 4 2         3   5   2           2 6   2             7   2          3 2 3     2            2   4     2          2   5     2                5     2              6     2          3 3   2   2             2 2 2 2   2          2     3 2   2               2 3 2   2          3 4 2   2                4 2   2            2 3 3   2          2   2   3   2               3   3   2          3   2 3   2               2 2 3   2          3 2 4   2               3 4   2         4 4 2 2           4   2   2 2             3 3   2 2             2 4   2 2         4 2 2 2 2             3     2 2 2           2 2 2 2 2 2             2   2 2 2 2                 3 2 2 2           2 4 2 2 2          2 2   3 2 2             2 2 3 2 2           3     3 2 2                      3 2 2             2 2 3 2 2           2   2 3 2 2           4 4 2 2             2   4 2 2           2 2 4 2 2           5     3 2            4 2 3 2              3   2 3 2               2 3 3 2            2     3 3 2            2   4 3 2         3 2 4   2           2   5   2               6   2          3 3 2     2            2 2 3     2          2     4     2              2 4     2                5     2          3 4 2   2             2 3   2   2           2   2 2 2   2               3 2 2   2          3   3 2   2              2 3 2   2          2   3 3   2               4 3   2          3 2   3   2               3   3   2          4   3     2            3 4     2            2 5     2           4 2         2             3   2       2          2 2 3       2           2   3       2                4       2          2 5       2             3 2 2     2           2 2     2     2             2 2   2     2           3   2 2     2                   2 2     2             2 3 2     2           2   3 2     2          3     3     2                 2 3     2           4   3     2              2     3     2          2 2   3     2          5 2 2   2          5     2   2             4     2   2             3 2   2   2          2 3 2 2   2             3   2 2   2                2   2 2   2            2   2 2 2   2             2   3 2   2           2     3 2   2           2     3 2   2          4 2 2 2 2            3   3 2 2         2 2 4 2 2            2   4 2 2               5 2 2          4 3   2 2             3 2     2 2           2 2   2   2 2             2 2 2   2 2          3   3   2 2                   3   2 2            2 4   2 2          2   4   2 2          2 2 2 2 2 2             2 3 2 2 2           3       2 2 2                 2   2 2 2          4 2 2 2 2             2   2 2 2 2           2 2 2 2 2 2          4   3 2 2             2 2 3 2 2           2 3 3 2 2          5       2 2            4 2   2 2            3 3   2 2            4       2 2          2 3       2 2             3         2 2              2 2     2 2          2   3     2 2           3 2 2   2 2               2   2   2 2             2     2   2 2            2       2   2 2           2   2 2   2 2             3 3   2 2           2     3   2 2          6 2 2 2             4   2 2 2           2 2 2 2 2 2            3 3 2 2 2          5 2 3 2            4     3 2          2 3 2 3 2            3   2 3 2              2 3 3 2         2   4 3 2          2 3     3 2            3 2   3 2          3 2     3 2              2       3 2             2   2   3 2          2     2   3 2          2   3   3 2          4   2 3 2             2     2 3 2          2   2 2 3 2            3   2 3 2           2       2 3 2            5   3 2            4     3 2               3     3 2           2 2       3 2           2     2   3 2            3   2   3 2          2 4 4 2            4   4 2              3   4 2          2 2 2 4 2             2 2   4 2           2 2     4 2           2         4 2          3 2   4 2         2 2 2 4 2          3   2 4 2          2 3 5 2          3     5 2         3 3 3 3           2 2 4 3             2 5 3          3 4     3            2 3 2   3          2   2 3   3              3 3   3              2 4   3            2 4 2 3          2   3   2 3               4   2 3          3 2 2 2 3              3 2 2 3          3 3 3 3               4 3 3          4 2 2   3            3   3   3          2 2 4   3            2   4   3                5   3         2 6   3          4 3     3             3 2       3           2 2   2     3             2 2 2     3          3   3     3                   3     3            2 4     3           2   4     3           2 2 2 2   3             2 3 2   3           3       2   3                  2   2   3          4 2 2   3             2   2 2   3           2 2 2 2   3           4   3   3             2 2 3   3           2 3 3   3           5     2 3             4 2 2 3            3 3 2 3             4     2 3           2 3     2 3             3       2 3                2 2   2 3           2   3   2 3           3 2 2 2 3               2   2 2 3            2     2 2 3           2       2 2 3           2   2 2 2 3             3 3 2 3           2     3 2 3          6 3 3             4   3 3            2 2 2 3 3            3 3 3 3          4 3     3            3 2 2   3          2 2   3   3            2 2 3   3                  4   3         2   5   3            3 3     3           2 2 2       3             2 3       3          3     2     3                 2 2     3            2   3     3           2 2 3     3          3   2 2   3                3 2   3          4     2   3            2 2   2   3           2 3   2   3          5 2     3            4         3          2 3 2     3           3   2     3              2 3     3          2   4     3          2 3         3             3 2       3           3 2         3               2           3             2   2       3           2     2       3           2   3       3           4   2     3             2     2     3           2   2 2     3             3   2     3            2       2     3             5 2   3             4   2   3                3   2   3           2 2     2   3           2     2 2   3            3   2 2   3            4 2 2 3          2 3     2 3            3 2   2 3          3 2 2 2 3               2   2 2 3            2   3 2 3          2     3 2 3         2   4 2 3          3 2     2 3               2 2   2 3          4       2 3            2         2 3           2   2     2 3            3 2   2 3          2     2   2 3          5 2 2 3            3   2 2 3          2   2 2 2 3          2 4   2 3             4     2 3               3     2 3           2 2 2   2 3             2 2     2 3            2 2       2 3           2           2 3           3 2     2 3           2 2 2   2 3           3   2   2 3          3 3 3 3               3   3 3            2 2   3 3          2 2     3 3          2     2 3 3         3 3 3 3             3     3 3           2         3 3          2 2     3 3          3       3 3           2 3   3 3           3       3 3          2   2 4 3          3     4 3          3     4 3          4 4 4            3 3   4          2 2 2 2 4            2 3 2 4                2 3 4         2 2 4 4          2 2 3   4             2 4   4          3   2     4                3     4            2 2 2   4           2 3 2   4          4 2 2 4            2 3 2 4           2 4 2 4             4 2   4           2 3       4            3 2     4          3 2 2   4              2   2   4            2   3   4           2     3   4          2   4   4           3 2       4               2 2     4          4         4            2           4          2   2       4             3 2     4           2     2     4          5 2   4             3   2   4           2   2 2   4           2 4 2 4             4   2 4               3   2 4           2 2 2 2 4             2 2   2 4            2 2     2 4           2         2 4           3 2   2 4           2 2 2 2 4            3   2 2 4          2 3 2   4            3 3   4          3 2       4               2 2     4            2     2   4           2   2 2   4          2     3   4            2   2     4           2   3     4            3         4           2   2       4           3 3     4               3       4             2 2       4           2 2         4           2     2     4          3 3     4             3         4            2             4           2 2         4           3           4           2 3 2   4            3     2   4          4 2 2 4             2 2   2 4         2 2 2 2 4            3     2 4           2         2 4          2 2 2 2 4          3   2 2 4            4   2 4           2 2     2 4          3 2   2 4           2   2   2 4           3       2 4           3       2 4          2 2   3 4          3     3 4          3     3 4          4 4 4          3 2 2 5              2 3 5            2   2   5           2   3   5          2   2 2 5            3 2   5           2   3   5          4 2   5             2 2     5          2 2 2   5            3       5           2           5          2 2 2   5          3   2   5             4     5           2 2       5           2   2 2 5            3     2 5            3     2 5          2     2   5          2 2       5           3 2     5           2 2       5           3         5           3         5          2 3 2 5          3     2 5           4   2 5          2 2 2 6          3 3 6          2 3   6           3       6           4 2 6         2   7                8              9             2 2 5                     6              2 7                   7               2 3 3 2                 2 4 2             2   5 2                2 5 2             2 4   3                 3 2 3             2 2 3 3                3 3 3             2 3   4                4   4            3 6 2           3   4   2             2 5   2               6   2            3 2 2 2 2             2   3 2 2            2   4 2 2                  4 2 2                5 2 2            3 3 3 2              2 2   3 2            2     2 3 2                 2 2 3 2           3 3 3 2                  3 3 2            2   2 4 2                3 4 2            3     4 2                 2   4 2           4 3   3            4     2 3              3 2 2 3              2 3 2 3              3   3 3             2 2   3 3               2     3 3                  2 3 3            2 3 3 3            3   4 3                     4 3             2     4 3            5 2 4               3 3 4             2   4 4          2 2 6                  7                8             2 3 4                   2 5              2   6                 2 6               2 4 2 2                 3 3 2             2 2 4 2               3 4 2             2 5 3                 4   3             2 3 2 3                4 2 3             2 4 4                5 4             3   5                 2 6                   7               3 2 3                   2   4                 2   5                       5                     6                  3 3   2                 2 2 2 2              2     3 2                    2 3 2               3 4 2                      4 2                  2 3 3                2   2   3                    3   3              3   2 3                    2 2 3                3 2 4                     3 4               4 4 2              4   2   2                3 3   2                2 4   2              4 2 2 2                3     2 2              2 2 2 2 2                 2   2 2 2                    3 2 2              2 4 2 2              2 2   3 2                 2 2 3 2              3     3 2                         3 2                2 2 3 2              2   2 3 2              4 4 2                 2   4 2               2 2 4 2              5     3                4 2 3                 3   2 3                   2 3 3               2     3 3               2   4 3             3 2 4 2             2   5 2          2   6 2                 6 2              7 2           3 3 2   2             2 2 3   2           2     4   2               2 4   2          3 5   2                 5   2           3 4 2 2             2 3   2 2            2   2 2 2 2                3 2 2 2           3   3 2 2                2 3 2 2           2   3 3 2                4 3 2           3 2   3 2                3   3 2           4   3   2             3 4   2              2 5   2            4 2       2              3   2     2            2 2 3     2              2   3     2                  4     2            2 5     2              3 2 2   2            2 2     2   2               2 2   2   2            3   2 2   2                    2 2   2              2 3 2   2            2   3 2   2            3     3   2                   2 3   2           4   3   2              2     3   2             2 2   3   2           5 2 2 2            5     2 2              4     2 2               3 2   2 2            2 3 2 2 2               3   2 2 2                 2   2 2 2             2   2 2 2 2              2   3 2 2             2     3 2 2            2     3 2 2           4 2 2 3             3   3 3           2 2 4 3             2   4 3                 5 3          2 6 3            4 3   3              3 2     3            2 2   2   3              2 2 2   3           3   3   3                    3   3             2 4   3            2   4   3            2 2 2 2 3              2 3 2 3            3       2 3                   2   2 3           4 2 2 3              2   2 2 3            2 2 2 2 3           4   3 3              2 2 3 3            2 3 3 3           5       3              4 2   3              3 3   3              4       3            2 3       3              3         3                2 2     3            2   3     3            3 2 2   3                 2   2   3              2     2   3             2       2   3            2   2 2   3             3 3   3            2     3   3           6 2 3              4   2 3             2 2 2 2 3             3 3 2 3           5 2 4             4     4           2 3 2 4              3   2 4               2 3 4           2   4 4            2 3     4              3 2   4            3 2     4               2       4             2   2   4            2     2   4            2   3   4            4   2 4              2     2 4            2   2 2 4             3   2 4           2       2 4              5   4              4     4                 3     4             2 2       4             2     2   4           2 4 5              4   5               3   5           2 2 2 5              2 2   5            2 2     5            2         5           3 2   5           2 2 2 5           2 3 6            3     6          2 3 5                2 6              2 7             2 4 3                   3 4              2 2 5                 3 5               2 5   2                 4 2 2             2 3 3 2               4 3 2             2 4   3               5   3             3 2 4                 2   5               2   6                     6                   7              3 3 2                  2 2 3                 2     4                      2 4                 3 5                       5                  3 4 2                  2 3   2               2   2 2 2                    3 2 2               3   3 2                    2 3 2                2   3 3                     4 3                3 2   3                    3   3                4   3 2                3 4 2                2 5 2              4 2     2                3   2   2              2 2 3   2                2   3   2                    4   2              2 5   2                 3 2 2 2               2 2     2 2                 2 2   2 2               3   2 2 2                       2 2 2                2 3 2 2              2   3 2 2               3     3 2                     2 3 2              4   3 2                 2     3 2              2 2   3 2             5 2 3              5     3                4     3                3 2   3              2 3 2 3                 3   2 3                   2   2 3              2   2 2 3               2     3 3               2     3 3             3 3 3                 2 2 4               2     5                   2 5                     6               3 4                      2 3 2                  2   2 3                      3 3                 3   4                     2 4                   2 4 2               2   3   2                   4   2                3 2 2 2                    3 2 2                3 3 3                    4 3               4 2 2                    3   3                 2 2 4                    2   4                       5                 2 6                  4 3                      3 2                      2 2   2                      2 2 2                    3   3                             3                      2 4                    2   4                    2 2 2 2                     2 3 2                  3       2                         2   2                 4 2 2                    2   2 2                  2 2 2 2                  4   3                     2 2 3                  2 3 3                  5     2                  4 2 2                  3 3 2                   4     2                 2 3     2                   3       2                     2 2   2               2   3   2                3 2 2 2                     2   2 2                   2     2 2                 2       2 2                 2   2 2 2                  3 3 2                 2     3 2                6 3                   4   3                 2 2 2 3                 3 3 3                4 3   2                3 2 2 2             2 2   3 2                2 2 3 2             3   4 2                     4 2               2 5 2             2   5 2               3 3   2              2 2 2     2                 2 3     2              3     2   2                    2 2   2             4 3   2              2   3   2              2 2 3   2              3   2 2 2                    3 2 2              4     2 2                2 2   2 2             2 3   2 2              5 2   2               4       2              2 3 2   2                3   2   2                  2 3   2              2   4   2              2 3       2                 3 2     2               3 2       2                   2         2                2   2     2               2     2     2              2   3     2              4   2   2                 2     2   2               2   2 2   2                3   2   2               2       2   2                5 2 2                 4   2 2                   3   2 2               2 2     2 2               2     2 2 2               3   2 2 2                4 2 3              2 3     3                3 2   3             3 2 2 3                  2   2 3               2   3 3              2     3 3             2   4 3             3 2     3                  2 2   3             4       3                2         3               2   2     3              3 2   3              2     2   3             5 2 3                3   2 3              2   2 2 3              2 4   3                 4     3                  3     3               2 2 2   3                 2 2     3               2 2       3               2           3              3 2     3              2 2 2   3              3 3 4                  3   4                2 2   4              2 2     4              2     2 4             3 3 4                3     4               2         4              2 2     4              3       4              2 3   4               3       4              2   2 5              3     5              3     5             3 4 2 2             2 3 3 2           2   2 4 2               3 4 2               2 5 2           3 5   2              2 4     2            2   3 2   2               4 2   2           3 2 3   2               3 3   2            2   4 2 2                5 2 2           3 3   2 2                4   2 2           4 3     2              3 2 2   2            2 2   3   2              2 2 3   2           3   4   2                    4   2              2 5   2            2   5   2              3 3     2            2 2 2       2              2 3       2            3     2     2                  2 2     2           4 3     2              2   3     2            2 2 3     2            3   2 2   2                   3 2   2            4     2   2               2 2   2   2             2 3   2   2           5 2 2 2             4     2 2            2 3 2 2 2              3   2 2 2                2 3 2 2            2   4 2 2            2 3     2 2              3 2   2 2           3 2     2 2                 2       2 2              2   2   2 2             2     2   2 2            2   3   2 2            4   2 2 2               2     2 2 2             2   2 2 2 2               3   2 2 2             2       2 2 2             2 2     3 2             2     2 3 2              3   2 3 2            4 4   2              3 3     2            2 2 2 2   2              2 3 2   2           3     3   2                2 3   2             2   4   2            2 2 4   2            2 2 3     2              2 4     2           3   2       2                  3       2           4   2     2             2 2 2     2             2 3 2     2            4 2 2   2              2 3 2   2            2 4 2   2              4 2     2             2 3         2              3 2       2            3 2 2     2                2   2     2              2   3     2            2     3     2            2   4     2            3 2         2                 2 2       2           4           2               2             2             2   2         2              3 2       2             2     2       2            5 2     2               3   2     2             2   2 2     2            2 4 2   2               4   2   2                 3   2   2             2 2 2 2   2               2 2   2   2             2 2     2   2             2         2   2            3 2   2   2             2 2 2 2   2             3   2 2   2            2 3 2 2 2              3 3 2 2           3 2     2 2                2 2   2 2           4   2 2 2             2     2 2 2            2   2 2 2 2             3 3 2 2           2     3 2 2           4       2 2              2   2   2 2            2   3   2 2           5     2 2              3       2 2             2   2     2 2            3 3   2 2                 3     2 2               2 2     2 2             2 2       2 2             2     2   2 2            3 3   2 2               3       2 2             2           2 2             2 2       2 2             3         2 2             2 3 2 2 2             3     2 2 2           4 2 3 2              2 2   3 2            2 2 2 3 2              3     3 2            2         3 2            2 2 2 3 2            3   2 3 2              4   3 2             2 2     3 2            3 2   3 2             2   2   3 2             3       3 2             3       3 2            2 2   4 2            3     4 2            3     4 2            4 5 2             3 4 3           2 2 3   3             2 4   3           3   2 2 3                3 2 3             2 2 3 3           2 3 3 3            3   3   3                  4   3           4 2     3              2 3     3            2 4     3            2 3 2   3             3 3   3            3 2       3                2 2     3            4   2   3              2     2   3            2   2 2   3              3 3   3            2     3   3            4         3               2   2     3            2   3     3           5       3              3         3             2   2       3            3 3 2 3                3   2 3               2 2   2 3            2 2     2 3            2     2 2 3            3 3 2 3              3     2 3             2         2 3            2 2     2 3             3       2 3             2 3 3 3             3     3 3           3 2 2   3                2 3   3           4         3              2   2     3            2   3     3             3   2   3            2   2 2   3              3 2     3             2   3     3            4 2     3               2 2       3            2 2 2     3              3         3             2             3             2 2 2     3            3   2     3               4       3             2 2         3             2   2 2   3             3     2   3             3     2   3           5   2 3              3     2 3            2     2 2 3             4   2 3            2 2     2 3             3 2   2 3             2 2     2 3             3       2 3             3       2 3            2 3 3 3            3     3 3             4   3 3           4   2 4              2   3 4            2   4 4             3 2   4            2   3   4            5     4               3       4             2     2   4              4     4             2 2       4             2 2   2 4             3     2 4             3     2 4            2 2 2   4            3 3   4            2 3     4             3         4             4 2   4          2 4 4 2             3 5 2           3 6 2          2 5 2   2              4 3   2         2 3 4   2            4 4   2          2 6 2 2              5   2 2          2 4 2 2 2            5 2 2 2          2 5 3 2            6 3 2          3 3 3   2             2 2 4   2          2     5   2               2 5   2         3 6   2                6   2           3 4       2             2 3 2     2          2   2 3     2               3 3     2          3   4     2               2 4     2             2 4 2   2           2   3   2   2                4   2   2           3 2 2 2   2                3 2 2   2           3 3 3   2               4 3   2           4 2 2 2 2             3   3 2 2           2 2 4 2 2             2   4 2 2                 5 2 2           2 6 2 2           4 3   2 2             3 2     2 2            2 2   2   2 2              2 2 2   2 2           3   3   2 2                  3   2 2             2 4   2 2           2   4   2 2           2 2 2 2 2 2              2 3 2 2 2           3       2 2 2                  2   2 2 2           4 2 2 2 2              2   2 2 2 2           2 2 2 2 2 2           4   3 2 2              2 2 3 2 2            2 3 3 2 2            5     3 2             4 2 3 2             3 3 3 2              4     3 2            2 3     3 2              3       3 2               2 2   3 2           2   3   3 2            3 2 2 3 2                2   2 3 2              2     2 3 2            2       2 3 2            2   2 2 3 2              3 3 3 2            2     3 3 2           6 4 2              4   4 2             2 2 2 4 2            3 3 4 2           3 4 2   2             2 3 3   2          2   2 4   2               3 4   2         3   5   2              2 5   2           3 5     2             2 4       2          2   3 2     2               4 2     2          3 2 3     2               3 3     2           2   4 2   2               5 2   2          3 3   2   2               4   2   2           4 3       2              3 2 2     2           2 2   3     2             2 2 3     2           3   4     2                   4     2             2 5     2           2   5     2              3 3       2            2 2 2         2              2 3         2           3     2       2                  2 2       2           4 3       2             2   3       2           2 2 3       2            3   2 2     2                  3 2     2           4     2     2              2 2   2     2           2 3   2     2           5 2 2   2             4     2   2           2 3 2 2   2             3   2 2   2               2 3 2   2           2   4 2   2           2 3     2   2              3 2   2   2           3 2     2   2                2       2   2              2   2   2   2            2     2   2   2            2   3   2   2            4   2 2   2              2     2 2   2            2   2 2 2   2             3   2 2   2            2       2 2   2              5 3   2              4   3   2                3   3   2            2 2     3   2            2     2 3   2            3   2 3   2           4 4 2 2             3 3   2 2           2 2 2 2 2 2             2 3 2 2 2           3     3 2 2                 2 3 2 2         4 4 2 2             2   4 2 2           2 2 4 2 2          2 2 3   2 2             2 4   2 2           3   2     2 2                  3     2 2           4   2   2 2             2 2 2   2 2           2 3 2   2 2         4 2 2 2 2             2 3 2 2 2           2 4 2 2 2             4 2   2 2          2 3       2 2              3 2     2 2           3 2 2   2 2               2   2   2 2             2   3   2 2           2     3   2 2           2   4   2 2           3 2       2 2                2 2     2 2          4         2 2              2           2 2            2   2       2 2             3 2     2 2            2     2     2 2          5 2   2 2             3   2   2 2            2   2 2   2 2           2 4 2 2 2              4   2 2 2               3   2 2 2           2 2 2 2 2 2              2 2   2 2 2            2 2     2 2 2            2         2 2 2            3 2   2 2 2           2 2 2 2 2 2            3   2 2 2 2           2 3 2 3 2             3 3 3 2           3 2     3 2              2 2   3 2           4   2 3 2              2     2 3 2           2   2 2 3 2            3 3 3 2           2     3 3 2           4       3 2             2   2   3 2           2   3   3 2           5     3 2             3       3 2           2   2     3 2           3 3   3 2               3     3 2              2 2     3 2           2 2       3 2           2     2   3 2           3 3   3 2             3       3 2            2           3 2           2 2       3 2            3         3 2            2 3 2 3 2            3     2 3 2           4 2 4 2             2 2   4 2           2 2 2 4 2             3     4 2           2         4 2           2 2 2 4 2           3   2 4 2             4   4 2            2 2     4 2            3 2   4 2            2   2   4 2            3       4 2            3       4 2           2 2   5 2            3     5 2            3     5 2           4 6 2           3 5     2             2 4 2   2          2   3 3   2               4 3   2         3 2 4   2              3 4   2            2 5     2           2   4       2               5       2          3 3 2     2               4 2     2          3 4 2   2               5 2   2           4 4     2             3 3       2           2 2 2 2     2             2 3 2     2           3     3     2                 2 3     2          4 4     2             2   4     2           2 2 4     2           2 2 3       2              2 4       2           3   2         2                  3         2           4   2       2              2 2 2       2           2 3 2       2           4 2 2     2              2 3 2     2            2 4 2     2              4 2 2   2           2 3     2   2             3 2   2   2           3 2 2 2   2                2   2 2   2             2   3 2   2            2     3 2   2           2   4 2   2           3 2     2   2                2 2   2   2           4       2   2              2         2   2            2   2     2   2             3 2   2   2            2     2   2   2           5 2 2   2              3   2 2   2            2   2 2 2   2            2 4 3   2              4   3   2                3   3   2            2 2 2 3   2              2 2   3   2            2 2     3   2            2         3   2             3 2   3   2            2 2 2 3   2            3   2 3   2             3 4     2           2 2 3       2            2 4       2          3   2 2     2                 3 2     2          4   3     2            2 2 3     2           2 3 3     2           3   3       2                  4       2           4 2         2             2 3         2           2 4         2           2 3 2       2             3 3       2            3 2           2                2 2         2           4   2       2              2     2       2            2   2 2       2             3 3       2          2     3       2            4             2              2   2         2            2   3         2           5           2              3             2            2   2           2           3 3 2     2                3   2     2              2 2   2     2            2 2     2     2            2     2 2     2           3 3 2     2              3     2     2             2         2     2            2 2     2     2            3       2     2            2 3 3     2             3     3     2          3 2 2 2   2               2 3 2   2           4       2   2              2   2   2   2           2   3   2   2          5 2 2   2             3   2 2   2            2   2 2 2   2          5     2   2             3 2   2   2           2   3   2   2           4 2   2   2              2 2     2   2            2 2 2   2   2              3       2   2            2           2   2            2 2 2   2   2           3   2   2   2              4     2   2            2 2       2   2            3 2     2   2            2   2 2 2   2            3     2 2   2            3     2 2   2           5   3   2              3     3   2           2     2 3   2             4   3   2           2 2     3   2            3 2   3   2            2 2     3   2            3       3   2            3       3   2           2 3 4   2            3     4   2            4   4   2         2 2 4 2 2            2 5 2 2          3   3   2 2                 4   2 2          4 2 2 2 2             2 3 2 2 2           2 4 2 2 2          4 3   2 2             2 4   2 2           2 5   2 2           3 2 2   2 2               2 3   2 2           4         2 2              2   2     2 2           2   3     2 2          5 2   2 2              3   2   2 2            2   2 2   2 2           5       2 2              3 2     2 2            2   3     2 2           4 2 2 2 2              2 2   2 2 2           2 2 2 2 2 2             3     2 2 2            2         2 2 2           2 2 2 2 2 2            3   2 2 2 2              4   2 2 2            2 2     2 2 2            3 2   2 2 2            2   2 3 2 2            3     3 2 2            3     3 2 2           4   2   2 2              2   3   2 2            2   4   2 2          5       2 2             3 2     2 2           2   3     2 2           5       2 2              3         2 2            2     2     2 2              4       2 2            2 2         2 2            3 2       2 2            2 2   2   2 2            3     2   2 2            3     2   2 2          6 2 2 2             4   2 2 2           2 2 2 2 2 2            3 3 2 2 2            2 3   2 2 2            3       2 2 2             4 2 2 2 2          5 2 3 2             3 3 3 2           2   4 3 2          6   3 2             4     3 2            2 2 2   3 2            3 3   3 2            2 3 2 3 2            3     2 3 2            4 3 3 2          3 6 3             2 5   3          2   4 2 3              5 2 3         3 3 3 3              4 3 3          2   5   3               6   3          3 4     3               5     3             3 4   3            2 2 3     3           3   2 2   3                 3 2   3          4   3   3             2 2 3   3           2 3 3   3           3   3     3                  4     3           4 2       3              2 3       3            2 4       3            2 3 2 2 3              3 3 2 3            3 2     2 3                2 2   2 3           4   2 2 3             2     2 2 3            2   2 2 2 3             3 3 2 3           2     3 2 3            4       2 3              2   2   2 3            2   3   2 3            5     2 3              3       2 3            2   2     2 3            3 3 3 3                3   3 3               2 2   3 3            2 2     3 3             2     2 3 3            3 3 3 3              3     3 3             2         3 3            2 2     3 3             3       3 3            2 3 4 3             3     4 3          2 2 4   3          3   3     3                 4     3          4 2 2   3             2 3 2   3           2 4 2   3          4 3     3             2 4     3            2 5     3           3 2 2     3           4           3              2   2       3            2   3       3          5 2     3             3   2     3           2   2 2     3           5         3              3 2       3            2   3       3            4 2 2   3              2 2   2   3            2 2 2 2   3              3     2   3            2         2   3            2 2 2 2   3             3   2 2   3              4   2   3            2 2     2   3            3 2   2   3            2   2 3   3             3     3   3             3     3   3          4   2 2 3             2   3 2 3            2   4 2 3           5     2 3              3 2   2 3            2   3   2 3            2     2   2 3            2 2       2 3             3 2     2 3            2 2   2 2 3            3     2 2 3            3     2 2 3          6 3 3             4   3 3            2 2 2 3 3            3 3 3 3            2 3   3 3            3       3 3            4 2 3 3          3   4   3                 5   3          4 3     3             2 4     3            2 5     3           4   2     3              2   3     3            2   4     3           5         3              3 2       3            2   3       3            5   2   3              3     2   3            2     2 2   3              4   2   3            2 2     2   3            3 2   2   3            2 2   3   3             3     3   3             3     3   3          5 2     3             3 3     3            2   4     3           6       3              4         3            2 2 2       3            3 3       3            2 3 2     3             3     2     3             4 3     3          4 4 4             2 5 4           2 6 4           5 2   4              3 3   4            2   4   4           6 2 4              4   2 4             2 2 2 2 4            3 3 2 4            2 3 3 4             3     3 4             4 4 4
o30 = 13824c d*e f g  - 13824b*c*e f g  + 13824a*e f g  - 110592c d e f g  + 110592b*c*d*e f g  + 13824b e f g  - 165888a*d*e f g  + 221184c d f g  - 221184b*c*d e*f g  - 110592b d*e f g  + 663552a*d e f g  + 221184b d f g  - 884736a*d f g  - 13824c e f g  + 497664c d*e*f g  - 414720b*c e f g  + 497664a*c*e f g  - 995328b*c d*f g  + 1327104b c*e*f g  - 1990656a*c*d*e*f g  - 995328a*b*e f g  - 884736b f g  + 3981312a*b*d*f g  - 373248c f g  + 2985984a*c f g  - 5971968a f g  - 13824c d*e f g*h + 13824b*c*e f g*h - 13824a*e f g*h + 110592c d e f g*h - 110592b*c*d*e f g*h - 13824b e f g*h + 165888a*d*e f g*h - 221184c d e*f g*h + 221184b*c*d e f g*h + 110592b d*e f g*h - 663552a*d e f g*h - 221184b d e*f g*h + 884736a*d e*f g*h + 13824c e f g h - 635904c d*e f g h + 566784b*c e f g h - 663552a*c*e f g h - 331776c d f g h + 1714176b*c d*e*f g h - 1935360b c*e f g h + 2322432a*c*d*e f g h + 1492992a*b*e f g h - 221184b c*d*f g h + 1327104a*c*d f g h + 1327104b e*f g h - 5971968a*b*d*e*f g h + 497664c e*f g h + 497664b*c f g h - 4976640a*c e*f g h - 1990656a*b*c*f g h + 11943936a e*f g h + 13824c d e f h  - 13824b*c*d*e f h  + 13824a*d*e f h  - 110592c d e f h  + 110592b*c*d e f h  + 13824b d*e f h  - 165888a*d e f h  + 221184c d f h  - 221184b*c*d e*f h  - 110592b d e f h  + 663552a*d e f h  + 221184b d f h  - 884736a*d f h  + 110592c d*e f g*h  - 138240b*c e f g*h  + 152064a*c*e f g*h  + 884736c d e*f g*h  - 1161216b*c d*e f g*h  + 566784b c*e f g*h  + 276480a*c*d*e f g*h  - 470016a*b*e f g*h  - 1105920b*c d f g*h  + 1714176b c*d*e*f g*h  - 3538944a*c*d e*f g*h  - 414720b e f g*h  + 774144a*b*d*e f g*h  - 995328b d*f g*h  + 4423680a*b*d f g*h  - 110592c e f g h  - 331776c d*f g h  - 718848b*c e*f g h  + 2239488a*c e f g h  - 27648b c f g h  + 3317760a*c d*f g h  + 2654208a*b*c*e*f g h  - 6967296a e f g h  + 331776a*b f g h  - 7962624a d*f g h  - 110592c d e f h  + 110592b*c d*e f h  + 13824b c*e f h  - 138240a*c*d*e f h  - 13824a*b*e f h  - 442368c d f h  + 884736b*c d e*f h  - 635904b c*d*e f h  + 110592a*c*d e f h  - 13824b e f h  + 608256a*b*d*e f h  - 331776b c*d f h  + 1769472a*c*d f h  + 497664b d*e*f h  - 2211840a*b*d e*f h  - 221184c d*e*f g*h  + 442368b*c e f g*h  - 552960a*c e f g*h  + 1105920b*c d*f g*h  - 718848b c e*f g*h  - 1105920a*c d*e*f g*h  - 55296a*b*c*e f g*h  + 995328a e f g*h  + 497664b c*f g*h  - 4423680a*b*c*d*f g*h  - 331776a*b e*f g*h  + 7962624a d*e*f g*h  + 221184c f g h  - 1880064a*c f g h  + 3981312a c*f g h  + 221184c d f h  - 221184b*c d*e*f h  - 110592b c e f h  + 442368a*c d*e f h  + 110592a*b*c*e f h  + 13824a e f h  - 331776b c d*f h  - 442368a*c d f h  + 497664b c*e*f h  + 221184a*b*c*d*e*f h  - 414720a*b e f h  - 1105920a d*e f h  - 373248b f h  + 1990656a*b d*f h  - 1769472a d f h  - 442368b*c f g*h  + 663552a*c e*f g*h  + 2433024a*b*c f g*h  - 2654208a c*e*f g*h  - 2654208a b*f g*h  + 221184b c f h  - 442368a*c d*f h  - 221184a*b*c e*f h  - 110592a c*e f h  - 995328a*b c*f h  + 1769472a c*d*f h  + 1327104a b*e*f h  + 221184a c f h  - 884736a f h  + 13824c d*e f*g*i - 13824b*c*e f*g*i + 13824a*e f*g*i - 138240c d e f g*i + 138240b*c*d*e f g*i + 13824b e f g*i - 193536a*d*e f g*i + 442368c d e f g*i - 442368b*c*d e f g*i - 138240b d*e f g*i + 995328a*d e f g*i - 442368c d f g*i + 442368b*c*d e*f g*i + 442368b d e f g*i - 2211840a*d e f g*i - 442368b d f g*i + 1769472a*d f g*i - 13824c e f*g i + 566784c d*e f g i - 456192b*c e f g i + 539136a*c*e f g i - 718848c d e*f g i - 691200b*c d*e f g i + 1603584b c*e f g i - 2820096a*c*d*e f g i - 1244160a*b*e f g i + 2101248b*c d f g i - 2433024b c*d*e*f g i + 2654208a*c*d e*f g i - 1105920b e f g i + 6967296a*b*d*e f g i + 1769472b d*f g i - 7962624a*b*d f g i - 414720c e f g i + 497664c d*f g i + 165888b*c e*f g i + 3234816a*c e f g i - 663552b c f g i - 4976640a*c d*f g i + 1990656a*b*c*e*f g i - 8957952a e f g i + 11943936a d*f g i - 13824c d e f*h*i + 13824b*c*d*e f*h*i - 13824a*d*e f*h*i + 110592c d e f h*i - 110592b*c*d e f h*i - 13824b d*e f h*i + 165888a*d e f h*i - 221184c d e*f h*i + 221184b*c*d e f h*i + 110592b d e f h*i - 663552a*d e f h*i - 221184b d e*f h*i + 884736a*d e*f h*i - 110592c d*e f*g*h*i + 138240b*c e f*g*h*i - 152064a*c*e f*g*h*i - 1161216c d e f g*h*i + 1631232b*c d*e f g*h*i - 774144b c*e f g*h*i - 552960a*c*d*e f g*h*i + 691200a*b*e f g*h*i + 1105920c d f g*h*i - 774144b*c d e*f g*h*i - 1105920b c*d*e f g*h*i + 5750784a*c*d e f g*h*i + 608256b e f g*h*i - 2543616a*b*d*e f g*h*i + 884736b c*d f g*h*i - 4423680a*c*d f g*h*i + 221184b d*e*f g*h*i - 884736a*b*d e*f g*h*i + 110592c e f*g h*i + 1714176c d*e*f g h*i - 691200b*c e f g h*i - 870912a*c e f g h*i - 3594240b*c d*f g h*i + 4368384b c e*f g h*i - 6137856a*c d*e*f g h*i - 7299072a*b*c*e f g h*i + 9455616a e f g h*i - 2211840b c*f g h*i + 13934592a*b*c*d*f g h*i - 663552a*b e*f g h*i - 1990656a d*e*f g h*i - 995328c f g h*i + 8460288a*c f g h*i - 17915904a c*f g h*i + 110592c d e f*h i - 110592b*c d*e f*h i - 13824b c*e f*h i + 138240a*c*d*e f*h i + 13824a*b*e f*h i + 884736c d e*f h i - 1492992b*c d e f h i + 787968b c*d*e f h i + 387072a*c*d e f h i + 13824b e f h i - 774144a*b*d*e f h i - 221184b*c d f h i + 1050624b c*d e*f h i - 3760128a*c*d e*f h i - 635904b d*e f h i + 2543616a*b*d e f h i - 331776b d f h i + 1327104a*b*d f h i + 221184c d*e f*g*h i - 442368b*c e f*g*h i + 552960a*c e f*g*h i - 1105920c d f g*h i - 774144b*c d*e*f g*h i + 1078272b c e f g*h i + 663552a*c d*e f g*h i - 27648a*b*c*e f g*h i - 1575936a e f g*h i + 1050624b c d*f g*h i + 3760128a*c d f g*h i - 3262464b c*e*f g*h i + 8736768a*b*c*d*e*f g*h i + 3179520a*b e f g*h i - 12275712a d*e f g*h i + 1990656b f g*h i - 9400320a*b d*f g*h i + 2654208a d f g*h i - 221184c e*f*g h i + 2101248b*c f g h i - 1161216a*c e*f g h i - 11778048a*b*c f g h i + 7962624a c*e*f g h i + 13934592a b*f g h i - 221184c d e*f*h i + 221184b*c d*e f*h i + 110592b c e f*h i - 442368a*c d*e f*h i - 110592a*b*c*e f*h i - 13824a e f*h i - 221184b*c d f h i + 1050624b c d*e*f h i - 221184a*c d e*f h i - 635904b c*e f h i - 1105920a*b*c*d*e f h i + 566784a*b e f h i + 1603584a d*e f h i - 165888b c*d*f h i + 221184a*b*c*d f h i + 497664b e*f h i - 3262464a*b d*e*f h i + 5750784a d e*f h i + 442368b*c e*f*g*h i - 663552a*c e f*g*h i - 774144b c f g*h i + 2654208a*c d*f g*h i - 2985984a*b*c e*f g*h i + 4810752a c*e f g*h i + 5031936a*b c*f g*h i - 10616832a c*d*f g*h i - 3317760a b*e*f g*h i - 221184b c e*f*h i + 442368a*c d*e*f*h i + 221184a*b*c e f*h i + 110592a c*e f*h i - 331776b c f h i + 884736a*b*c d*f h i + 1714176a*b c*e*f h i - 2433024a c*d*e*f h i - 1935360a b*e f h i + 497664a*b f h i - 2211840a b*d*f h i - 1990656a c f g*h i + 7962624a f g*h i - 221184a c e*f*h i - 221184a b*c*f h i + 1327104a e*f h i + 13824c d e f*i  - 13824b*c*d e f*i  + 13824a*d e f*i  - 110592c d e f i  + 110592b*c*d e f i  + 13824b d e f i  - 165888a*d e f i  + 221184c d f i  - 221184b*c*d e*f i  - 110592b d e f i  + 663552a*d e f i  + 221184b d f i  - 884736a*d f i  - 13824c d*e g*i  + 13824b*c e g*i  - 13824a*c*e g*i  + 566784c d e f*g*i  - 774144b*c d*e f*g*i  + 165888b c*e f*g*i  + 691200a*c*d*e f*g*i  - 193536a*b*e f*g*i  - 718848c d e*f g*i  + 1078272b*c d e f g*i  + 387072b c*d*e f g*i  - 3373056a*c*d e f g*i  - 165888b e f g*i  + 940032a*b*d*e f g*i  - 774144b*c d f g*i  - 221184b c*d e*f g*i  + 3317760a*c*d e*f g*i  + 110592b d*e f g*i  - 1216512a*b*d e f g*i  - 442368b d f g*i  + 2211840a*b*d f g*i  + 13824c e g i  - 1935360c d*e f*g i  + 1603584b*c e f*g i  - 1575936a*c e f*g i  - 27648c d f g i  + 4368384b*c d*e*f g i  - 6303744b c e f g i  + 7713792a*c d*e f g i  + 6635520a*b*c*e f g i  - 2861568a e f g i  - 774144b c d*f g i  + 1658880a*c d f g i  + 5750784b c*e*f g i  - 21897216a*b*c*d*e*f g i  - 1658880a*b e f g i  + 3981312a d*e f g i  - 1769472b f g i  + 7962624a*b d*f g i  - 5971968a d f g i  + 1327104c e*f*g i  - 663552b*c f g i  - 10948608a*c e*f g i  + 4976640a*b*c f g i  + 23887872a c*e*f g i  - 11943936a b*f g i  + 13824c d e h*i  - 13824b*c d*e h*i  + 13824a*c*d*e h*i  - 635904c d e f*h*i  + 787968b*c d e f*h*i  - 110592b c*d*e f*h*i  - 774144a*c*d e f*h*i  + 138240a*b*d*e f*h*i  - 331776c d f h*i  + 1050624b*c d e*f h*i  - 1492992b c*d e f h*i  + 2543616a*c*d e f h*i  + 110592b d*e f h*i  + 387072a*b*d e f h*i  - 221184b c*d f h*i  + 1327104a*c*d f h*i  + 884736b d e*f h*i  - 3760128a*b*d e*f h*i  + 110592c d*e g*h*i  - 138240b*c e g*h*i  + 152064a*c e g*h*i  + 1714176c d e*f*g*h*i  - 1105920b*c d*e f*g*h*i  + 387072b c e f*g*h*i  - 27648a*c d*e f*g*h*i  - 552960a*b*c*e f*g*h*i  + 539136a e f*g*h*i  + 1050624b*c d f g*h*i  - 1658880b c d*e*f g*h*i  - 7962624a*c d e*f g*h*i  + 2543616b c*e f g*h*i  - 1990656a*b*c*d*e f g*h*i  - 3373056a*b e f g*h*i  + 6635520a d*e f g*h*i  + 221184b c*d*f g*h*i  - 2433024a*b*c*d f g*h*i  - 2211840b e*f g*h*i  + 10838016a*b d*e*f g*h*i  + 663552a d e*f g*h*i  - 110592c e g h*i  - 221184c d*f*g h*i  - 2433024b*c e*f*g h*i  + 4810752a*c e f*g h*i  - 774144b c f g h*i  - 1161216a*c d*f g h*i  + 19408896a*b*c e*f g h*i  - 25380864a c*e f g h*i  - 3317760a*b c*f g h*i  + 7962624a c*d*f g h*i  - 9953280a b*e*f g h*i  - 110592c d e h i  + 110592b*c d*e h i  + 13824b c e h i  - 138240a*c d*e h i  - 13824a*b*c*e h i  - 331776c d f*h i  + 1050624b*c d e*f*h i  - 1492992b c d*e f*h i  + 1078272a*c d e f*h i  + 110592b c*e f*h i  + 1631232a*b*c*d*e f*h i  - 138240a*b e f*h i  - 456192a d*e f*h i  - 912384b c d f h i  + 2211840a*c d f h i  + 1050624b c*d*e*f h i  - 1658880a*b*c*d e*f h i  - 110592b e f h i  + 1078272a*b d*e f h i  - 6303744a d e f h i  - 331776b d*f h i  + 2211840a*b d f h i  - 3317760a d f h i  - 221184c d*e*g*h i  + 442368b*c e g*h i  - 552960a*c e g*h i  + 884736b*c d*f*g*h i  - 221184b c e*f*g*h i  - 2985984a*c d*e*f*g*h i  + 663552a*b*c e f*g*h i  - 870912a c*e f*g*h i  + 2211840b c f g*h i  - 7630848a*b*c d*f g*h i  - 7962624a*b c*e*f g*h i  + 19408896a c*d*e*f g*h i  + 7713792a b*e f g*h i  - 2543616a*b f g*h i  + 8957952a b*d*f g*h i  + 221184c g h i  - 1990656a*c f*g h i  + 9704448a c f g h i  - 20901888a f g h i  + 221184c d h i  - 221184b*c d*e*h i  - 110592b c e h i  + 442368a*c d*e h i  + 110592a*b*c e h i  + 13824a c*e h i  - 221184b c d*f*h i  - 774144a*c d f*h i  + 884736b c e*f*h i  - 774144a*b*c d*e*f*h i  - 1161216a*b c*e f*h i  - 691200a c*d*e f*h i  + 566784a b*e f*h i  - 331776b c*f h i  + 1050624a*b c*d*f h i  - 774144a c*d f h i  - 718848a*b e*f h i  + 4368384a b*d*e*f h i  - 442368b*c g*h i  + 663552a*c e*g*h i  + 2654208a*b*c f*g*h i  - 1161216a c e*f*g*h i  - 1161216a b*c*f g*h i  - 10948608a e*f g*h i  + 221184b c h i  - 442368a*c d*h i  - 221184a*b*c e*h i  - 110592a c e h i  - 1105920a*b c f*h i  + 2101248a c d*f*h i  + 1714176a b*c*e*f*h i  - 414720a e f*h i  - 27648a b f h i  - 663552a d*f h i  + 221184a c h i  - 995328a c*f*h i  - 13824c d e i  + 13824b*c d e i  - 13824a*c*d e i  + 497664c d e*f*i  - 635904b*c d e f*i  + 110592b c*d e f*i  + 608256a*c*d e f*i  - 138240a*b*d e f*i  - 331776b*c d f i  + 884736b c*d e*f i  - 2211840a*c*d e*f i  - 110592b d e f i  + 110592a*b*d e f i  - 442368b d f i  + 1769472a*b*d f i  - 414720c d e g*i  + 608256b*c d*e g*i  - 165888b c e g*i  - 470016a*c d*e g*i  + 165888a*b*c*e g*i  + 13824a e g*i  + 497664c d f*g*i  - 3262464b*c d e*f*g*i  + 2543616b c d*e f*g*i  + 3179520a*c d e f*g*i  - 663552b c*e f*g*i  - 2543616a*b*c*d*e f*g*i  + 995328a*b e f*g*i  - 1244160a d*e f*g*i  + 2211840b c d f g*i  - 2543616a*c d f g*i  - 3760128b c*d*e*f g*i  + 10838016a*b*c*d e*f g*i  + 663552b e f g*i  - 1216512a*b d*e f g*i  - 1658880a d e f g*i  + 1769472b d*f g*i  - 8404992a*b d f g*i  + 1769472a d f g*i  + 1327104c d*e*g i  - 1105920b*c e g i  + 995328a*c e g i  - 2211840b*c d*f*g i  + 5750784b c e*f*g i  - 3317760a*c d*e*f*g i  - 12275712a*b*c e f*g i  + 9455616a c*e f*g i  - 3317760b c f g i  + 8957952a*b*c d*f g i  + 663552a*b c*e*f g i  - 9953280a c*d*e*f g i  + 3981312a b*e f g i  + 1769472a*b f g i  + 3981312a b*d*f g i  - 884736c g i  + 7962624a*c f*g i  - 20901888a c f g i  + 11943936a f g i  + 497664c d e*h*i  - 635904b*c d e h*i  + 110592b c d*e h*i  + 566784a*c d e h*i  - 110592a*b*c*d*e h*i  - 13824a d*e h*i  - 165888b*c d f*h*i  + 1050624b c d e*f*h*i  - 3262464a*c d e*f*h*i  + 221184b c*d*e f*h*i  - 1105920a*b*c*d e f*h*i  - 442368a*b d*e f*h*i  + 1603584a d e f*h*i  - 221184b c*d f h*i  + 221184a*b*c*d f h*i  - 221184b d*e*f h*i  - 221184a*b d e*f h*i  + 5750784a d e*f h*i  - 995328c d g*h*i  + 221184b*c d*e*g*h*i  + 110592b c e g*h*i  - 55296a*c d*e g*h*i  + 276480a*b*c e g*h*i  - 663552a c*e g*h*i  + 221184b c d*f*g*h*i  + 5031936a*c d f*g*h*i  - 3760128b c e*f*g*h*i  + 8736768a*b*c d*e*f*g*h*i  + 5750784a*b c*e f*g*h*i  - 7299072a c*d*e f*g*h*i  - 2820096a b*e f*g*h*i  + 1327104b c*f g*h*i  - 2433024a*b c*d*f g*h*i  - 3317760a c*d f g*h*i  + 3317760a*b e*f g*h*i  - 21897216a b*d*e*f g*h*i  + 1769472b*c g h*i  - 2654208a*c e*g h*i  - 10616832a*b*c f*g h*i  + 7962624a c e*f*g h*i  + 7962624a b*c*f g h*i  + 23887872a e*f g h*i  - 331776b*c d h i  + 884736b c d*e*h i  - 718848a*c d e*h i  - 110592b c e h i  - 1161216a*b*c d*e h i  + 110592a*b c*e h i  + 566784a c*d*e h i  + 13824a b*e h i  - 221184b c d*f*h i  + 1050624a*b*c d f*h i  - 221184b c*e*f*h i  - 774144a*b c*d*e*f*h i  + 4368384a c*d e*f*h i  + 442368a*b e f*h i  - 691200a b*d*e f*h i  + 221184b f h i  - 774144a*b d*f h i  - 774144a b*d f h i  - 442368b c g*h i  + 2433024a*c d*g*h i  - 1105920a*b*c e*g*h i  + 2239488a c e g*h i  + 3760128a*b c f*g*h i  - 11778048a c d*f*g*h i  - 6137856a b*c*e*f*g*h i  + 3234816a e f*g*h i  + 1658880a b f g*h i  + 4976640a d*f g*h i  - 442368b c h i  + 1105920a*b*c d*h i  + 884736a*b c e*h i  - 718848a c d*e*h i  - 635904a b*c*e h i  - 13824a e h i  + 1105920a*b c*f*h i  - 3594240a b*c*d*f*h i  - 718848a b e*f*h i  + 165888a d*e*f*h i  - 1880064a c g*h i  + 8460288a c*f*g*h i  - 331776a b*c h i  + 497664a c*e*h i  + 497664a b*f*h i  - 373248c d i  + 497664b*c d e*i  - 110592b c d e i  - 414720a*c d e i  + 110592a*b*c*d e i  + 13824a d e i  - 331776b c d f*i  + 1990656a*c d f*i  - 221184b c*d e*f*i  + 221184a*b*c*d e*f*i  + 442368a*b d e f*i  - 1105920a d e f*i  + 221184b d f i  - 442368a*b d f i  - 1769472a d f i  + 1990656b*c d g*i  - 2211840b c d*e*g*i  - 331776a*c d e*g*i  + 663552b c e g*i  + 774144a*b*c d*e g*i  - 663552a*b c*e g*i  + 1492992a c*d*e g*i  - 165888a b*e g*i  + 1327104b c d*f*g*i  - 9400320a*b*c d f*g*i  + 884736b c*e*f*g*i  - 884736a*b c*d*e*f*g*i  - 663552a c*d e*f*g*i  - 2211840a*b e f*g*i  + 6967296a b*d*e f*g*i  - 884736b f g*i  + 2211840a*b d*f g*i  + 7962624a b*d f g*i  - 1769472b c g i  - 2654208a*c d*g i  + 7962624a*b*c e*g i  - 6967296a c e g i  + 2654208a*b c f*g i  + 13934592a c d*f*g i  - 1990656a b*c*e*f*g i  - 8957952a e f*g i  - 5971968a b f g i  - 11943936a d*f g i  - 331776b c d h*i  + 497664a*c d h*i  - 221184b c d*e*h*i  + 1714176a*b*c d e*h*i  + 221184a*b c*d*e h*i  - 1935360a c*d e h*i  + 110592a b*d*e h*i  + 884736a*b c*d f*h*i  - 2211840a c*d f*h*i  + 442368a*b d*e*f*h*i  - 2433024a b*d e*f*h*i  + 1769472b c g*h*i  - 4423680a*b*c d*g*h*i  - 3538944a*b c e*g*h*i  + 2654208a c d*e*g*h*i  + 2322432a b*c*e g*h*i  + 497664a e g*h*i  - 4423680a*b c*f*g*h*i  + 13934592a b*c*d*f*g*h*i  + 2654208a b e*f*g*h*i  + 1990656a d*e*f*g*h*i  + 3981312a c g h*i  - 17915904a c*f*g h*i  + 221184b c h i  - 1105920a*b c d*h i  - 27648a c d h i  - 221184a*b c*e*h i  + 1714176a b*c*d*e*h i  - 110592a b e h i  - 414720a d*e h i  - 442368a*b f*h i  + 2101248a b d*f*h i  - 663552a d f*h i  + 3317760a b*c g*h i  - 4976640a c*e*g*h i  - 4976640a b*f*g*h i  - 331776a b c*h i  + 497664a c*d*h i  + 497664a b*e*h i  - 373248a h i  + 221184b c d i  - 995328a*b*c d i  - 221184a*b c*d e*i  + 1327104a c*d e*i  - 110592a b*d e i  - 442368a*b d f*i  + 1769472a b*d f*i  - 884736b c g*i  + 4423680a*b c d*g*i  + 331776a c d g*i  + 884736a*b c*e*g*i  - 5971968a b*c*d*e*g*i  + 663552a b e g*i  - 995328a d*e g*i  + 1769472a*b f*g*i  - 7962624a b d*f*g*i  - 7962624a b*c g i  + 11943936a c*e*g i  + 11943936a b*f*g i  - 221184a b*c*d h*i  - 221184a b d*e*h*i  + 1327104a d e*h*i  + 1327104a b c*g*h*i  - 1990656a c*d*g*h*i  - 1990656a b*e*g*h*i  + 221184a b h i  - 995328a b*d*h i  + 2985984a g*h i  + 221184a b d i  - 884736a d i  - 884736a b g*i  + 3981312a b*d*g*i  - 5971968a g i  - 13824c d*e g*j + 13824b*c*e g*j - 13824a*e g*j + 152064c d e f*g*j - 152064b*c*d*e f*g*j - 13824b e f*g*j + 207360a*d*e f*g*j - 552960c d e f g*j + 552960b*c*d e f g*j + 152064b d*e f g*j - 1161216a*d e f g*j + 663552c d e*f g*j - 663552b*c*d e f g*j - 552960b d e f g*j + 2875392a*d e f g*j + 663552b d e*f g*j - 2654208a*d e*f g*j + 13824c e g j - 663552c d*e f*g j + 539136b*c e f*g j - 622080a*c*e f*g j + 2239488c d e f g j - 870912b*c d*e f g j - 1575936b c*e f g j + 4727808a*c*d*e f g j + 1119744a*b*e f g j - 1880064c d f g j - 1161216b*c d e*f g j + 4810752b c*d*e f g j - 10948608a*c*d e f g j + 995328b e f g j - 7464960a*b*d*e f g j - 1990656b c*d f g j + 7962624a*c*d f g j - 2654208b d*e*f g j + 11943936a*b*d e*f g j + 497664c e f*g j - 4976640c d*e*f g j + 3234816b*c e f g j - 7091712a*c e f g j + 8460288b*c d*f g j - 10948608b c e*f g j + 25380864a*c d*e*f g j + 7464960a*b*c*e f g j + 7464960a e f g j + 7962624b c*f g j - 35831808a*b*c*d*f g j - 17915904a d*e*f g j + 2985984c f g j - 25380864a*c f g j + 53747712a c*f g j + 13824c d e h*j - 13824b*c*d*e h*j + 13824a*d*e h*j - 138240c d e f*h*j + 138240b*c*d e f*h*j + 13824b d*e f*h*j - 193536a*d e f*h*j + 442368c d e f h*j - 442368b*c*d e f h*j - 138240b d e f h*j + 995328a*d e f h*j - 442368c d f h*j + 442368b*c*d e*f h*j + 442368b d e f h*j - 2211840a*d e f h*j - 442368b d f h*j + 1769472a*d f h*j + 165888c d*e g*h*j - 193536b*c e g*h*j + 207360a*c*e g*h*j + 276480c d e f*g*h*j - 552960b*c d*e f*g*h*j + 691200b c*e f*g*h*j - 663552a*c*d*e f*g*h*j - 539136a*b*e f*g*h*j - 1105920c d e*f g*h*j + 663552b*c d e f g*h*j - 27648b c*d*e f g*h*j - 1658880a*c*d e f g*h*j - 470016b e f g*h*j + 2156544a*b*d*e f g*h*j + 2654208b*c d f g*h*j - 2985984b c*d e*f g*h*j + 3981312a*c*d e*f g*h*j - 55296b d*e f g*h*j + 2654208a*b*d e f g*h*j + 2433024b d f g*h*j - 10616832a*b*d f g*h*j - 165888c e g h*j + 2322432c d*e f*g h*j - 2820096b*c e f*g h*j + 4727808a*c e f*g h*j + 3317760c d f g h*j - 6137856b*c d*e*f g h*j + 7713792b c e f g h*j - 11197440a*c d*e f g h*j - 2737152a*b*c*e f g h*j - 7464960a e f g h*j - 1161216b c d*f g h*j - 16920576a*c d f g h*j - 3317760b c*e*f g h*j + 20901888a*b*c*d*e*f g h*j - 2488320a*b e f g h*j + 8957952a d*e f g h*j - 2654208b f g h*j + 11943936a*b d*f g h*j + 11943936a d f g h*j - 1990656c e*f*g h*j - 4976640b*c f g h*j + 25380864a*c e*f g h*j + 25380864a*b*c f g h*j - 71663616a c*e*f g h*j - 17915904a b*f g h*j - 165888c d e h j + 165888b*c d*e h j + 13824b c*e h j - 193536a*c*d*e h j - 13824a*b*e h j + 110592c d e f*h j + 387072b*c d e f*h j - 774144b c*d*e f*h j + 940032a*c*d e f*h j - 13824b e f*h j + 691200a*b*d*e f*h j - 442368c d f h j - 221184b*c d e*f h j + 1078272b c*d e f h j - 1216512a*c*d e f h j + 566784b d*e f h j - 3373056a*b*d e f h j - 774144b c*d f h j + 2211840a*c*d f h j - 718848b d e*f h j + 3317760a*b*d e*f h j - 663552c d*e g*h j + 995328b*c e g*h j - 1161216a*c e g*h j - 3538944c d e*f*g*h j + 5750784b*c d*e f*g*h j - 3373056b c e f*g*h j - 1658880a*c d*e f*g*h j + 2156544a*b*c*e f*g*h j + 1119744a e f*g*h j + 3760128b*c d f g*h j - 7962624b c d*e*f g*h j + 19906560a*c d e*f g*h j + 3179520b c*e f g*h j - 9455616a*b*c*d*e f g*h j - 1119744a*b e f g*h j + 8460288a d*e f g*h j + 5031936b c*d*f g*h j - 17252352a*b*c*d f g*h j - 331776b e*f g*h j + 2156544a*b d*e*f g*h j - 15925248a d e*f g*h j + 663552c e g h j + 1327104c d*f*g h j + 2654208b*c e*f*g h j - 10948608a*c e f*g h j + 1658880b c f g h j - 16920576a*c d*f g h j - 11943936a*b*c e*f g h j + 34338816a c*e f g h j - 8460288a*b c*f g h j + 47775744a c*d*f g h j + 5971968a b*e*f g h j + 663552c d e h j - 663552b*c d*e h j - 165888b c e h j + 995328a*c d*e h j + 165888a*b*c*e h j + 13824a e h j + 1769472c d f*h j - 3760128b*c d e*f*h j + 2543616b c d*e f*h j - 1216512a*c d e f*h j + 608256b c*e f*h j - 2543616a*b*c*d*e f*h j - 470016a*b e f*h j - 1244160a d*e f*h j + 2211840b c d f h j - 8404992a*c d f h j - 3262464b c*d*e*f h j + 10838016a*b*c*d e*f h j - 414720b e f h j + 3179520a*b d*e f h j - 1658880a d e f h j + 497664b d*f h j - 2543616a*b d f h j + 1769472a d f h j + 884736c d*e*g*h j - 2211840b*c e g*h j + 2875392a*c e g*h j - 4423680b*c d*f*g*h j + 3317760b c e*f*g*h j + 3981312a*c d*e*f*g*h j + 2654208a*b*c e f*g*h j - 7464960a c*e f*g*h j - 2543616b c f g*h j + 17915904a*b*c d*f g*h j + 2156544a*b c*e*f g*h j - 35831808a c*d*e*f g*h j - 2488320a b*e f g*h j - 829440a*b f g*h j + 7962624a b*d*f g*h j - 884736c g h j + 7962624a*c f*g h j - 14929920a c f g h j - 11943936a f g h j - 884736c d h j + 884736b*c d*e*h j + 663552b c e h j - 2211840a*c d*e h j - 663552a*b*c e h j - 165888a c*e h j + 1327104b c d*f*h j + 2211840a*c d f*h j - 2211840b c e*f*h j - 884736a*b*c d*e*f*h j + 774144a*b c*e f*h j + 6967296a c*d*e f*h j + 1492992a b*e f*h j + 1990656b c*f h j - 9400320a*b c*d*f h j + 7962624a c*d f h j - 331776a*b e*f h j - 663552a b*d*e*f h j + 1769472b*c g*h j - 2654208a*c e*g*h j - 10616832a*b*c f*g*h j + 11943936a c e*f*g*h j + 11943936a b*c*f g*h j - 884736b c h j + 1769472a*c d*h j + 884736a*b*c e*h j + 663552a c e h j + 4423680a*b c f*h j - 7962624a c d*f*h j - 5971968a b*c*e*f*h j - 995328a e f*h j + 331776a b f h j - 884736a c h j + 3981312a c*f*h j - 13824c d e i*j + 13824b*c*d e i*j - 13824a*d e i*j + 110592c d e f*i*j - 110592b*c*d e f*i*j - 13824b d e f*i*j + 165888a*d e f*i*j - 221184c d e*f i*j + 221184b*c*d e f i*j + 110592b d e f i*j - 663552a*d e f i*j - 221184b d e*f i*j + 884736a*d e*f i*j - 470016c d e g*i*j + 691200b*c d*e g*i*j - 193536b c*e g*i*j - 539136a*c*d*e g*i*j + 207360a*b*e g*i*j - 55296c d e f*g*i*j - 27648b*c d e f*g*i*j - 552960b c*d*e f*g*i*j + 2156544a*c*d e f*g*i*j + 165888b e f*g*i*j - 663552a*b*d*e f*g*i*j + 2433024c d f g*i*j - 2985984b*c d e*f g*i*j + 663552b c*d e f g*i*j + 2654208a*c*d e f g*i*j + 276480b d*e f g*i*j - 1658880a*b*d e f g*i*j + 2654208b c*d f g*i*j - 10616832a*c*d f g*i*j - 1105920b d e*f g*i*j + 3981312a*b*d e*f g*i*j + 1492992c d*e g i*j - 1244160b*c e g i*j + 1119744a*c e g i*j + 2654208c d e*f*g i*j - 7299072b*c d*e f*g i*j + 6635520b c e f*g i*j - 2737152a*c d*e f*g i*j - 8460288a*b*c*e f*g i*j + 4105728a e f*g i*j - 11778048b*c d f g i*j + 19408896b c d*e*f g i*j - 11943936a*c d e*f g i*j - 12275712b c*e f g i*j + 16422912a*b*c*d*e f g i*j + 8460288a*b e f g i*j - 8957952a d*e f g i*j - 10616832b c*d*f g i*j + 47775744a*b*c*d f g i*j + 7962624b e*f g i*j - 35831808a*b d*e*f g i*j + 5971968a d e*f g i*j - 995328c e g i*j - 1990656c d*f*g i*j + 1990656b*c e*f*g i*j + 7464960a*c e f*g i*j + 4976640b c f g i*j + 25380864a*c d*f g i*j - 40310784a*b*c e*f g i*j + 4478976a c*e f g i*j - 71663616a c*d*f g i*j + 53747712a b*e*f g i*j + 608256c d e h*i*j - 774144b*c d e h*i*j + 138240b c*d*e h*i*j + 691200a*c*d e h*i*j - 152064a*b*d*e h*i*j + 221184c d e*f*h*i*j - 1105920b*c d e f*h*i*j + 1631232b c*d e f*h*i*j - 2543616a*c*d e f*h*i*j - 110592b d*e f*h*i*j - 552960a*b*d e f*h*i*j + 884736b*c d f h*i*j - 774144b c*d e*f h*i*j - 884736a*c*d e*f h*i*j - 1161216b d e f h*i*j + 5750784a*b*d e f h*i*j + 1105920b d f h*i*j - 4423680a*b*d f h*i*j + 774144c d e g*h*i*j - 2543616b*c d*e g*h*i*j + 940032b c e g*h*i*j + 2156544a*c d*e g*h*i*j - 663552a*b*c*e g*h*i*j - 622080a e g*h*i*j - 4423680c d f*g*h*i*j + 8736768b*c d e*f*g*h*i*j - 1990656b c d*e f*g*h*i*j - 9455616a*c d e f*g*h*i*j - 2543616b c*e f*g*h*i*j + 13934592a*b*c*d*e f*g*h*i*j + 2156544a*b e f*g*h*i*j - 8460288a d*e f*g*h*i*j - 7630848b c d f g*h*i*j + 17915904a*c d f g*h*i*j + 8736768b c*d*e*f g*h*i*j - 23887872a*b*c*d e*f g*h*i*j + 774144b e f g*h*i*j - 9455616a*b d*e f g*h*i*j + 5971968a d e f g*h*i*j - 4423680b d*f g*h*i*j + 17915904a*b d f g*h*i*j + 7962624a d f g*h*i*j - 5971968c d*e*g h*i*j + 6967296b*c e g h*i*j - 7464960a*c e g h*i*j + 13934592b*c d*f*g h*i*j - 21897216b c e*f*g h*i*j + 20901888a*c d*e*f*g h*i*j + 16422912a*b*c e f*g h*i*j - 746496a c*e f*g h*i*j + 8957952b c f g h*i*j - 43296768a*b*c d*f g h*i*j + 14929920a*b c*e*f g h*i*j + 20901888a c*d*e*f g h*i*j - 14929920a b*e f g h*i*j + 7962624a*b f g h*i*j - 65691648a b*d*f g h*i*j + 3981312c g h*i*j - 35831808a*c f*g h*i*j + 67184640a c f g h*i*j + 53747712a f g h*i*j - 2211840c d e*h i*j + 2543616b*c d e h i*j + 387072b c d*e h i*j - 3373056a*c d e h i*j - 138240b c*e h i*j - 552960a*b*c*d*e h i*j + 152064a*b e h i*j + 539136a d*e h i*j + 221184b*c d f*h i*j - 1658880b c d e*f*h i*j + 10838016a*c d e*f*h i*j - 1105920b c*d*e f*h i*j - 1990656a*b*c*d e f*h i*j + 110592b e f*h i*j - 27648a*b d*e f*h i*j + 6635520a d e f*h i*j + 1050624b c*d f h i*j - 2433024a*b*c*d f h i*j + 1714176b d*e*f h i*j - 7962624a*b d e*f h i*j + 663552a d e*f h i*j + 4423680c d g*h i*j - 884736b*c d*e*g*h i*j - 1216512b c e g*h i*j + 2654208a*c d*e g*h i*j - 1658880a*b*c e g*h i*j + 4727808a c*e g*h i*j - 2433024b c d*f*g*h i*j - 17252352a*c d f*g*h i*j + 10838016b c e*f*g*h i*j - 23887872a*b*c d*e*f*g*h i*j - 9455616a*b c*e f*g*h i*j + 16422912a c*d*e f*g*h i*j - 2737152a b*e f*g*h i*j - 9400320b c*f g*h i*j + 36329472a*b c*d*f g*h i*j - 11943936a c*d f g*h i*j + 2156544a*b e*f g*h i*j + 14929920a b*d*e*f g*h i*j - 7962624b*c g h i*j + 11943936a*c e*g h i*j + 47775744a*b*c f*g h i*j - 56733696a c e*f*g h i*j - 56733696a b*c*f g h i*j + 17915904a e*f g h i*j + 1327104b*c d h i*j - 3760128b c d*e*h i*j + 3317760a*c d e*h i*j + 110592b c e h i*j + 5750784a*b*c d*e h i*j + 276480a*b c*e h i*j - 2820096a c*d*e h i*j - 663552a b*e h i*j + 221184b c d*f*h i*j - 2433024a*b*c d f*h i*j + 221184b c*e*f*h i*j + 8736768a*b c*d*e*f*h i*j - 21897216a c*d e*f*h i*j - 55296a*b e f*h i*j - 7299072a b*d*e f*h i*j - 995328b f h i*j + 5031936a*b d*f h i*j - 3317760a b*d f h i*j + 2211840b c g*h i*j - 10616832a*c d*g*h i*j + 3981312a*b*c e*g*h i*j - 10948608a c e g*h i*j - 17252352a*b c f*g*h i*j + 47775744a c d*f*g*h i*j + 20901888a b*c*e*f*g*h i*j + 7464960a e f*g*h i*j - 8460288a b f g*h i*j + 1769472b c h i*j - 4423680a*b*c d*h i*j - 3538944a*b c e*h i*j + 2654208a c d*e*h i*j + 2322432a b*c*e h i*j + 497664a e h i*j - 4423680a*b c*f*h i*j + 13934592a b*c*d*f*h i*j + 2654208a b e*f*h i*j + 1990656a d*e*f*h i*j + 7962624a c g*h i*j - 35831808a c*f*g*h i*j + 1327104a b*c h i*j - 1990656a c*e*h i*j - 1990656a b*f*h i*j - 414720c d e i j + 566784b*c d e i j - 138240b c*d e i j - 470016a*c*d e i j + 152064a*b*d e i j - 995328c d f*i j + 1714176b*c d e*f*i j - 1161216b c*d e f*i j + 774144a*c*d e f*i j + 110592b d e f*i j + 276480a*b*d e f*i j - 1105920b c*d f i j + 4423680a*c*d f i j + 884736b d e*f i j - 3538944a*b*d e*f i j - 331776c d e*g*i j + 3179520b*c d e g*i j - 3373056b c d*e g*i j - 1119744a*c d e g*i j + 995328b c*e g*i j + 2156544a*b*c*d*e g*i j - 1161216a*b e g*i j + 1119744a d*e g*i j + 5031936b*c d f*g*i j - 7962624b c d e*f*g*i j + 2156544a*c d e*f*g*i j + 5750784b c*d*e f*g*i j - 9455616a*b*c*d e f*g*i j - 663552b e f*g*i j - 1658880a*b d*e f*g*i j + 8460288a d e f*g*i j + 3760128b c*d f g*i j - 17252352a*b*c*d f g*i j - 3538944b d*e*f g*i j + 19906560a*b d e*f g*i j - 15925248a d e*f g*i j + 331776c d g i j - 663552b*c d*e*g i j - 1658880b c e g i j - 2488320a*c d*e g i j + 8460288a*b*c e g i j - 7464960a c*e g i j - 3317760b c d*f*g i j - 8460288a*c d f*g i j + 663552b c e*f*g i j + 14929920a*b*c d*e*f*g i j + 5971968a*b c*e f*g i j - 14929920a c*d*e f*g i j - 8957952a b*e f*g i j + 2654208b c*f g i j - 11943936a*b c*d*f g i j + 29859840a c*d f g i j - 15925248a*b e*f g i j + 47775744a b*d*e*f g i j + 17915904a c e*f*g i j + 17915904a b*c*f g i j - 107495424a e*f g i j + 1990656c d h*i j - 3262464b*c d e*h*i j + 1078272b c d e h*i j + 3179520a*c d e h*i j - 442368b c*d*e h*i j - 27648a*b*c*d e h*i j + 552960a*b d*e h*i j - 1575936a d e h*i j + 1050624b c d f*h*i j - 9400320a*c d f*h*i j - 774144b c*d e*f*h*i j + 8736768a*b*c*d e*f*h*i j + 221184b d*e f*h*i j + 663552a*b d e f*h*i j - 12275712a d e f*h*i j - 1105920b d f h*i j + 3760128a*b d f h*i j + 2654208a d f h*i j - 9400320b*c d g*h*i j + 10838016b c d*e*g*h*i j + 2156544a*c d e*g*h*i j - 1216512b c e g*h*i j - 9455616a*b*c d*e g*h*i j - 1658880a*b c*e g*h*i j - 2737152a c*d*e g*h*i j + 4727808a b*e g*h*i j - 2433024b c d*f*g*h*i j + 36329472a*b*c d f*g*h*i j - 884736b c*e*f*g*h*i j - 23887872a*b c*d*e*f*g*h*i j + 14929920a c*d e*f*g*h*i j + 2654208a*b e f*g*h*i j + 16422912a b*d*e f*g*h*i j + 4423680b f g*h*i j - 17252352a*b d*f g*h*i j - 11943936a b*d f g*h*i j + 7962624b c g h*i j + 11943936a*c d*g h*i j - 35831808a*b*c e*g h*i j + 34338816a c e g h*i j - 11943936a*b c f*g h*i j - 56733696a c d*f*g h*i j + 20901888a b*c*e*f*g h*i j + 4478976a e f*g h*i j + 29859840a b f g h*i j + 17915904a d*f g h*i j + 2211840b c d h i j - 2543616a*c d h i j - 221184b c d*e*h i j - 7962624a*b*c d e*h i j + 442368b c*e h i j + 663552a*b c*d*e h i j + 7713792a c*d e h i j - 552960a*b e h i j - 870912a b*d*e h i j + 884736b c*d*f*h i j - 7630848a*b c*d f*h i j + 8957952a c*d f*h i j - 221184b e*f*h i j - 2985984a*b d*e*f*h i j + 19408896a b*d e*f*h i j - 8404992b c g*h i j + 17915904a*b*c d*g*h i j + 19906560a*b c e*g*h i j - 11943936a c d*e*g*h i j - 11197440a b*c*e g*h i j - 7091712a e g*h i j + 17915904a*b c*f*g*h i j - 43296768a b*c*d*f*g*h i j - 11943936a b e*f*g*h i j - 40310784a d*e*f*g*h i j - 14929920a c g h i j + 67184640a c*f*g h i j - 442368b c h i j + 3760128a*b c d*h i j + 1658880a c d h i j - 1105920a*b c*e*h i j - 6137856a b*c*d*e*h i j + 2239488a b e h i j + 3234816a d*e h i j + 2433024a*b f*h i j - 11778048a b d*f*h i j + 4976640a d f*h i j - 16920576a b*c g*h i j + 25380864a c*e*g*h i j + 25380864a b*f*g*h i j + 3317760a b c*h i j - 4976640a c*d*h i j - 4976640a b*e*h i j + 2985984a h i j + 497664b*c d i j - 718848b c d e*i j - 331776a*c d e*i j + 442368b c*d e i j - 55296a*b*c*d e i j - 552960a*b d e i j + 995328a d e i j + 1105920b c*d f*i j - 4423680a*b*c*d f*i j - 221184b d e*f*i j - 1105920a*b d e*f*i j + 7962624a d e*f*i j - 2543616b c d g*i j - 829440a*c d g*i j + 3317760b c d*e*g*i j + 2156544a*b*c d e*g*i j - 2211840b c*e g*i j + 2654208a*b c*d*e g*i j - 2488320a c*d e g*i j + 2875392a*b e g*i j - 7464960a b*d*e g*i j - 4423680b c*d*f*g*i j + 17915904a*b c*d f*g*i j + 7962624a c*d f*g*i j + 884736b e*f*g*i j + 3981312a*b d*e*f*g*i j - 35831808a b*d e*f*g*i j + 1769472b c g i j + 7962624a*b*c d*g i j - 15925248a*b c e*g i j + 5971968a c d*e*g i j + 8957952a b*c*e g i j + 7464960a e g i j + 7962624a*b c*f*g i j - 65691648a b*c*d*f*g i j + 5971968a b e*f*g i j + 53747712a d*e*f*g i j - 11943936a c g i j + 53747712a c*f*g i j - 774144b c d h*i j + 5031936a*b*c d h*i j + 442368b c*d*e*h*i j - 2985984a*b c*d e*h*i j - 3317760a c*d e*h*i j - 663552a*b d*e h*i j + 4810752a b*d e h*i j + 2654208a*b d f*h*i j - 10616832a b*d f*h*i j + 2211840b c g*h*i j - 17252352a*b c d*g*h*i j - 8460288a c d g*h*i j + 3981312a*b c*e*g*h*i j + 20901888a b*c*d*e*g*h*i j - 10948608a b e g*h*i j + 7464960a d*e g*h*i j - 10616832a*b f*g*h*i j + 47775744a b d*f*g*h*i j + 47775744a b*c g h*i j - 71663616a c*e*g h*i j - 71663616a b*f*g h*i j - 442368b c*h i j + 2654208a*b c*d*h i j - 1161216a b*c*d h i j + 663552a*b e*h i j - 1161216a b d*e*h i j - 10948608a d e*h i j - 16920576a b c*g*h i j + 25380864a c*d*g*h i j + 25380864a b*e*g*h i j - 1880064a b h i j + 8460288a b*d*h i j - 25380864a g*h i j - 442368b c*d i j + 2433024a*b c*d i j - 2654208a c*d i j + 663552a*b d e*i j - 2654208a b*d e*i j + 1769472b c*g*i j - 10616832a*b c*d*g*i j + 11943936a b*c*d g*i j - 2654208a*b e*g*i j + 11943936a b d*e*g*i j + 11943936a b c*g i j - 17915904a c*d*g i j - 17915904a b*e*g i j - 1990656a b d h*i j + 7962624a d h*i j + 7962624a b g*h*i j - 35831808a b*d*g*h*i j + 53747712a g h*i j + 13824c d e j  - 13824b*c*d e j  + 13824a*d e j  - 110592c d e f*j  + 110592b*c*d e f*j  + 13824b d e f*j  - 165888a*d e f*j  + 221184c d f j  - 221184b*c*d e*f j  - 110592b d e f j  + 663552a*d e f j  + 221184b d f j  - 884736a*d f j  + 995328c d e g*j  - 1575936b*c d e g*j  + 539136b c*d*e g*j  + 1119744a*c*d e g*j  + 13824b e g*j  - 622080a*b*d*e g*j  - 2654208c d e*f*g*j  + 4810752b*c d e f*g*j  - 870912b c*d e f*g*j  - 7464960a*c*d e f*g*j  - 663552b d*e f*g*j  + 4727808a*b*d e f*g*j  - 1990656b*c d f g*j  - 1161216b c*d e*f g*j  + 11943936a*c*d e*f g*j  + 2239488b d e f g*j  - 10948608a*b*d e f g*j  - 1880064b d f g*j  + 7962624a*b*d f g*j  - 6967296c d e g j  + 9455616b*c d*e g j  - 2861568b c e g j  - 7464960a*c d*e g j  + 4105728a*b*c*e g j  - 1119744a e g j  + 3981312c d f*g j  + 7962624b*c d e*f*g j  - 25380864b c d*e f*g j  + 34338816a*c d e f*g j  + 9455616b c*e f*g j  - 746496a*b*c*d*e f*g j  - 7464960a*b e f*g j  + 1119744a d*e f*g j  + 9704448b c d f g j  - 14929920a*c d f g j  + 7962624b c*d*e*f g j  - 56733696a*b*c*d e*f g j  - 6967296b e f g j  + 34338816a*b d*e f g j  + 8957952a d e f g j  + 3981312b d*f g j  - 14929920a*b d f g j  - 17915904a d f g j  + 11943936c d*e*g j  - 8957952b*c e g j  + 7464960a*c e g j  - 17915904b*c d*f*g j  + 23887872b c e*f*g j  - 71663616a*c d*e*f*g j  + 4478976a*b*c e f*g j  - 3359232a c*e f*g j  - 20901888b c f g j  + 67184640a*b*c d*f g j  + 17915904a*b c*e*f g j  + 67184640a c*d*e*f g j  - 60466176a b*e f g j  - 11943936a*b f g j  + 80621568a b*d*f g j  - 5971968c g j  + 53747712a*c f*g j  - 100776960a c f g j  - 80621568a f g j  - 1105920c d e h*j  + 1603584b*c d e h*j  - 456192b c*d e h*j  - 1244160a*c*d e h*j  - 13824b d*e h*j  + 539136a*b*d e h*j  + 1769472c d f*h*j  - 2433024b*c d e*f*h*j  - 691200b c*d e f*h*j  + 6967296a*c*d e f*h*j  + 566784b d e f*h*j  - 2820096a*b*d e f*h*j  + 2101248b c*d f h*j  - 7962624a*c*d f h*j  - 718848b d e*f h*j  + 2654208a*b*d e*f h*j  + 7962624c d e*g*h*j  - 12275712b*c d e g*h*j  + 6635520b c d*e g*h*j  + 8460288a*c d e g*h*j  - 1244160b c*e g*h*j  - 8460288a*b*c*d*e g*h*j  + 1119744a*b e g*h*j  + 4105728a d*e g*h*j  - 10616832b*c d f*g*h*j  + 19408896b c d e*f*g*h*j  - 35831808a*c d e*f*g*h*j  - 7299072b c*d*e f*g*h*j  + 16422912a*b*c*d e f*g*h*j  + 1492992b e f*g*h*j  - 2737152a*b d*e f*g*h*j  - 8957952a d e f*g*h*j  - 11778048b c*d f g*h*j  + 47775744a*b*c*d f g*h*j  + 2654208b d*e*f g*h*j  - 11943936a*b d e*f g*h*j  + 5971968a d e*f g*h*j  - 7962624c d g h*j  - 1990656b*c d*e*g h*j  + 3981312b c e g h*j  + 8957952a*c d*e g h*j  - 8957952a*b*c e g h*j  + 1119744a c*e g h*j  + 7962624b c d*f*g h*j  + 47775744a*c d f*g h*j  - 9953280b c e*f*g h*j  + 20901888a*b*c d*e*f*g h*j  - 14929920a*b c*e f*g h*j  - 38071296a c*d*e f*g h*j  + 41430528a b*e f*g h*j  + 13934592b c*f g h*j  - 56733696a*b c*d*f g h*j  - 44789760a c*d f g h*j  + 5971968a*b e*f g h*j  - 22394880a b*d*e*f g h*j  + 11943936b*c g h*j  - 17915904a*c e*g h*j  - 71663616a*b*c f*g h*j  + 67184640a c e*f*g h*j  + 67184640a b*c*f g h*j  + 80621568a e*f g h*j  - 1769472c d h j  + 5750784b*c d e*h j  - 6303744b c d e h j  - 1658880a*c d e h j  + 1603584b c*d*e h j  + 6635520a*b*c*d e h j  + 13824b e h j  - 1575936a*b d*e h j  - 2861568a d e h j  - 774144b c d f*h j  + 7962624a*c d f*h j  + 4368384b c*d e*f*h j  - 21897216a*b*c*d e*f*h j  - 1935360b d*e f*h j  + 7713792a*b d e f*h j  + 3981312a d e f*h j  - 27648b d f h j  + 1658880a*b d f h j  - 5971968a d f h j  + 2654208b*c d g*h j  + 663552b c d*e*g*h j  - 15925248a*c d e*g*h j  - 1658880b c e g*h j  + 5971968a*b*c d*e g*h j  + 8460288a*b c*e g*h j  - 8957952a c*d*e g*h j  - 7464960a b*e g*h j  - 3317760b c d*f*g*h j  - 11943936a*b*c d f*g*h j  - 663552b c*e*f*g*h j  + 14929920a*b c*d*e*f*g*h j  + 47775744a c*d e*f*g*h j  - 2488320a*b e f*g*h j  - 14929920a b*d*e f*g*h j  + 331776b f g*h j  - 8460288a*b d*f g*h j  + 29859840a b*d f g*h j  - 5971968b c g h j  + 11943936a*c d*g h j  + 5971968a*b*c e*g h j  + 8957952a c e g h j  + 29859840a*b c f*g h j  - 44789760a c d*f*g h j  - 22394880a b*c*e*f*g h j  - 60466176a e f*g h j  + 6718464a b f g h j  - 53747712a d*f g h j  - 3317760b c d h j  + 1769472a*c d h j  + 5750784b c d*e*h j  + 663552a*b*c d e*h j  - 1105920b c*e h j  - 12275712a*b c*d*e h j  + 3981312a c*d e h j  + 995328a*b e h j  + 9455616a b*d*e h j  - 2211840b c*d*f*h j  + 8957952a*b c*d f*h j  + 3981312a c*d f*h j  + 1327104b e*f*h j  - 3317760a*b d*e*f*h j  - 9953280a b*d e*f*h j  + 1769472b c g*h j  + 7962624a*b*c d*g*h j  - 15925248a*b c e*g*h j  + 5971968a c d*e*g*h j  + 8957952a b*c*e g*h j  + 7464960a e g*h j  + 7962624a*b c*f*g*h j  - 65691648a b*c*d*f*g*h j  + 5971968a b e*f*g*h j  + 53747712a d*e*f*g*h j  - 17915904a c g h j  + 80621568a c*f*g h j  - 1769472b c h j  + 2654208a*b c d*h j  - 5971968a c d h j  + 7962624a*b c*e*h j  - 1990656a b*c*d*e*h j  - 6967296a b e h j  - 8957952a d*e h j  - 2654208a*b f*h j  + 13934592a b d*f*h j  - 11943936a d f*h j  + 11943936a b*c g*h j  - 17915904a c*e*g*h j  - 17915904a b*f*g*h j  - 7962624a b c*h j  + 11943936a c*d*h j  + 11943936a b*e*h j  - 5971968a h j  + 1327104c d e*i*j  - 1935360b*c d e i*j  + 566784b c*d e i*j  + 1492992a*c*d e i*j  + 13824b d e i*j  - 663552a*b*d e i*j  - 221184b*c d f*i*j  + 1714176b c*d e*f*i*j  - 5971968a*c*d e*f*i*j  - 635904b d e f*i*j  + 2322432a*b*d e f*i*j  - 331776b d f i*j  + 1327104a*b*d f i*j  - 2654208c d g*i*j  - 3317760b*c d e*g*i*j  + 7713792b c d e g*i*j  - 2488320a*c d e g*i*j  - 2820096b c*d*e g*i*j  - 2737152a*b*c*d e g*i*j  - 165888b e g*i*j  + 4727808a*b d*e g*i*j  - 7464960a d e g*i*j  - 1161216b c d f*g*i*j  + 11943936a*c d f*g*i*j  - 6137856b c*d e*f*g*i*j  + 20901888a*b*c*d e*f*g*i*j  + 2322432b d*e f*g*i*j  - 11197440a*b d e f*g*i*j  + 8957952a d e f*g*i*j  + 3317760b d f g*i*j  - 16920576a*b d f g*i*j  + 11943936a d f g*i*j  + 13934592b*c d g i*j  - 9953280b c d*e*g i*j  + 5971968a*c d e*g i*j  + 3981312b c e g i*j  - 14929920a*b*c d*e g i*j  - 8957952a*b c*e g i*j  + 41430528a c*d*e g i*j  + 1119744a b*e g i*j  + 7962624b c d*f*g i*j  - 56733696a*b*c d f*g i*j  - 1990656b c*e*f*g i*j  + 20901888a*b c*d*e*f*g i*j  - 22394880a c*d e*f*g i*j  + 8957952a*b e f*g i*j  - 38071296a b*d*e f*g i*j  - 7962624b f g i*j  + 47775744a*b d*f g i*j  - 44789760a b*d f g i*j  - 11943936b c g i*j  - 17915904a*c d*g i*j  + 53747712a*b*c e*g i*j  - 60466176a c e g i*j  + 17915904a*b c f*g i*j  + 67184640a c d*f*g i*j  - 67184640a b*c*e*f*g i*j  + 100776960a e f*g i*j  - 53747712a b f g i*j  + 80621568a d*f g i*j  - 2211840b*c d h*i*j  + 4368384b c d e*h*i*j  - 663552a*c d e*h*i*j  - 691200b c*d e h*i*j  - 7299072a*b*c*d e h*i*j  + 110592b d*e h*i*j  - 870912a*b d e h*i*j  + 9455616a d e h*i*j  - 3594240b c*d f*h*i*j  + 13934592a*b*c*d f*h*i*j  + 1714176b d e*f*h*i*j  - 6137856a*b d e*f*h*i*j  - 1990656a d e*f*h*i*j  + 8957952b c d g*h*i*j  + 7962624a*c d g*h*i*j  - 21897216b c d*e*g*h*i*j  + 14929920a*b*c d e*g*h*i*j  + 6967296b c*e g*h*i*j  + 16422912a*b c*d*e g*h*i*j  - 14929920a c*d e g*h*i*j  - 7464960a*b e g*h*i*j  - 746496a b*d*e g*h*i*j  + 13934592b c*d*f*g*h*i*j  - 43296768a*b c*d f*g*h*i*j  - 65691648a c*d f*g*h*i*j  - 5971968b e*f*g*h*i*j  + 20901888a*b d*e*f*g*h*i*j  + 20901888a b*d e*f*g*h*i*j  + 3981312b c g h*i*j  - 65691648a*b*c d*g h*i*j  + 47775744a*b c e*g h*i*j  - 22394880a c d*e*g h*i*j  - 38071296a b*c*e g h*i*j  - 3359232a e g h*i*j  - 65691648a*b c*f*g h*i*j  + 362797056a b*c*d*f*g h*i*j  - 22394880a b e*f*g h*i*j  - 67184640a d*e*f*g h*i*j  + 80621568a c g h*i*j  - 362797056a c*f*g h*i*j  - 774144b c d h i*j  - 3317760a*b*c d h i*j  - 2433024b c*d*e*h i*j  + 19408896a*b c*d e*h i*j  - 9953280a c*d e*h i*j  - 110592b e h i*j  + 4810752a*b d*e h i*j  - 25380864a b*d e h i*j  - 221184b d*f*h i*j  - 1161216a*b d f*h i*j  + 7962624a b*d f*h i*j  + 7962624b c g*h i*j  - 11943936a*b c d*g*h i*j  + 29859840a c d g*h i*j  - 35831808a*b c*e*g*h i*j  + 20901888a b*c*d*e*g*h i*j  + 34338816a b e g*h i*j  + 4478976a d*e g*h i*j  + 11943936a*b f*g*h i*j  - 56733696a b d*f*g*h i*j  + 17915904a d f*g*h i*j  - 44789760a b*c g h i*j  + 67184640a c*e*g h i*j  + 67184640a b*f*g h i*j  + 1769472b c*h i*j  - 10616832a*b c*d*h i*j  + 7962624a b*c*d h i*j  - 2654208a*b e*h i*j  + 7962624a b d*e*h i*j  + 23887872a d e*h i*j  + 47775744a b c*g*h i*j  - 71663616a c*d*g*h i*j  - 71663616a b*e*g*h i*j  + 3981312a b h i*j  - 17915904a b*d*h i*j  + 53747712a g*h i*j  - 27648b c d i j  + 331776a*c d i j  - 718848b c*d e*i j  + 2654208a*b*c*d e*i j  - 110592b d e i j  + 2239488a*b d e i j  - 6967296a d e i j  - 331776b d f*i j  + 3317760a*b d f*i j  - 7962624a d f*i j  + 1658880b c d g*i j  - 8460288a*b*c d g*i j  + 2654208b c*d*e*g*i j  - 11943936a*b c*d e*g*i j  + 5971968a c*d e*g*i j  + 663552b e g*i j  - 10948608a*b d*e g*i j  + 34338816a b*d e g*i j  + 1327104b d*f*g*i j  - 16920576a*b d f*g*i j  + 47775744a b*d f*g*i j  - 5971968b c g i j  + 29859840a*b c d*g i j  + 6718464a c d g i j  + 5971968a*b c*e*g i j  - 22394880a b*c*d*e*g i j  + 8957952a b e g i j  - 60466176a d*e g i j  + 11943936a*b f*g i j  - 44789760a b d*f*g i j  - 53747712a d f*g i j  - 53747712a b*c g i j  + 80621568a c*e*g i j  + 80621568a b*f*g i j  + 2101248b c*d h*i j  - 11778048a*b c*d h*i j  + 13934592a c*d h*i j  - 221184b d*e*h*i j  - 1161216a*b d e*h*i j  + 7962624a b*d e*h*i j  - 7962624b c*g*h*i j  + 47775744a*b c*d*g*h*i j  - 56733696a b*c*d g*h*i j  + 11943936a*b e*g*h*i j  - 56733696a b d*e*g*h*i j  + 17915904a d e*g*h*i j  - 44789760a b c*g h*i j  + 67184640a c*d*g h*i j  + 67184640a b*e*g h*i j  + 221184b h i j  - 1990656a*b d*h i j  + 9704448a b d h i j  - 20901888a d h i j  - 14929920a b g*h i j  + 67184640a b*d*g*h i j  - 100776960a g h i j  + 221184b d i j  - 1880064a*b d i j  + 3981312a b*d i j  - 884736b g*i j  + 7962624a*b d*g*i j  - 14929920a b d g*i j  - 11943936a d g*i j  - 17915904a b g i j  + 80621568a b*d*g i j  - 80621568a g i j  - 884736c d j  + 1327104b*c d e*j  - 414720b c*d e j  - 995328a*c*d e j  - 13824b d e j  + 497664a*b*d e j  - 995328b c*d f*j  + 3981312a*c*d f*j  + 497664b d e*f*j  - 1990656a*b*d e*f*j  + 7962624b*c d g*j  - 10948608b c d e*g*j  + 3234816b c*d e g*j  + 7464960a*b*c*d e g*j  + 497664b d*e g*j  - 7091712a*b d e g*j  + 7464960a d e g*j  + 8460288b c*d f*g*j  - 35831808a*b*c*d f*g*j  - 4976640b d e*f*g*j  + 25380864a*b d e*f*g*j  - 17915904a d e*f*g*j  - 20901888b c d g j  - 11943936a*c d g j  + 23887872b c d*e*g j  + 17915904a*b*c d e*g j  - 8957952b c*e g j  + 4478976a*b c*d*e g j  - 60466176a c*d e g j  + 7464960a*b e g j  - 3359232a b*d*e g j  - 17915904b c*d*f*g j  + 67184640a*b c*d f*g j  + 80621568a c*d f*g j  + 11943936b e*f*g j  - 71663616a*b d*e*f*g j  + 67184640a b*d e*f*g j  + 11943936b c g j  + 53747712a*b*c d*g j  - 107495424a*b c e*g j  + 80621568a c d*e*g j  + 100776960a b*c*e g j  - 30233088a e g j  + 53747712a*b c*f*g j  - 362797056a b*c*d*f*g j  + 80621568a b e*f*g j  - 120932352a d*e*f*g j  - 80621568a c g j  + 362797056a c*f*g j  - 663552b c d h*j  + 165888b c*d e*h*j  + 1990656a*b*c*d e*h*j  - 414720b d e h*j  + 3234816a*b d e h*j  - 8957952a d e h*j  + 497664b d f*h*j  - 4976640a*b d f*h*j  + 11943936a d f*h*j  + 4976640b c d g*h*j  + 1990656b c*d*e*g*h*j  - 40310784a*b c*d e*g*h*j  + 53747712a c*d e*g*h*j  - 995328b e g*h*j  + 7464960a*b d*e g*h*j  + 4478976a b*d e g*h*j  - 1990656b d*f*g*h*j  + 25380864a*b d f*g*h*j  - 71663616a b*d f*g*h*j  - 11943936b c g h*j  + 17915904a*b c d*g h*j  - 53747712a c d g h*j  + 53747712a*b c*e*g h*j  - 67184640a b*c*d*e*g h*j  - 60466176a b e g h*j  + 100776960a d*e g h*j  - 17915904a*b f*g h*j  + 67184640a b d*f*g h*j  + 80621568a d f*g h*j  + 80621568a b*c g h*j  - 120932352a c*e*g h*j  - 120932352a b*f*g h*j  - 663552b c*d h j  + 4976640a*b c*d h j  - 11943936a c*d h j  + 1327104b d*e*h j  - 10948608a*b d e*h j  + 23887872a b*d e*h j  + 17915904a b*c*d g*h j  + 17915904a b d*e*g*h j  - 107495424a d e*g*h j  - 53747712a b c*g h j  + 80621568a c*d*g h j  + 80621568a b*e*g h j  - 884736b h j  + 7962624a*b d*h j  - 20901888a b d h j  + 11943936a d h j  - 11943936a b g*h j  + 53747712a b*d*g*h j  - 80621568a g h j  + 497664b c*d i*j  - 1990656a*b*c*d i*j  + 497664b d e*i*j  - 4976640a*b d e*i*j  + 11943936a d e*i*j  - 4976640b c*d g*i*j  + 25380864a*b c*d g*i*j  - 17915904a c*d g*i*j  - 1990656b d*e*g*i*j  + 25380864a*b d e*g*i*j  - 71663616a b*d e*g*i*j  + 11943936b c*g i*j  - 71663616a*b c*d*g i*j  + 67184640a b*c*d g i*j  - 17915904a*b e*g i*j  + 67184640a b d*e*g i*j  + 80621568a d e*g i*j  + 80621568a b c*g i*j  - 120932352a c*d*g i*j  - 120932352a b*e*g i*j  - 995328b d h*i*j  + 8460288a*b d h*i*j  - 17915904a b*d h*i*j  + 3981312b g*h*i*j  - 35831808a*b d*g*h*i*j  + 67184640a b d g*h*i*j  + 53747712a d g*h*i*j  + 80621568a b g h*i*j  - 362797056a b*d*g h*i*j  + 362797056a g h*i*j  - 373248b d j  + 2985984a*b d j  - 5971968a d j  + 2985984b d g*j  - 25380864a*b d g*j  + 53747712a b*d g*j  - 5971968b g j  + 53747712a*b d*g j  - 100776960a b d g j  - 80621568a d g j  - 80621568a b g j  + 362797056a b*d*g j  - 272097792a g j

o30 : S

i31 : numgens detDiscr

o31 = 1

i32 : # terms detDiscr_0

o32 = 2040
```

---

## schemes / chapter.m2 — chunk 4

### Input

```macaulay2
clearAll
S = QQ[a,b,x,y, MonomialOrder => Eliminate 2];
I1 = ideal(x-a, y-a, a^2-2);
ideal selectInSubring(1, gens gb I1)
I2 = ideal(x-a, y-b, a^2-2, b^2-3);
ideal selectInSubring(1, gens gb I2)
I3 = ideal(x-a, y-a^4, a^4+a^3+a^2+a+1);
ideal selectInSubring(1, gens gb I3)
```

### Output

```
i33 : clearAll

i34 : S = QQ[a,b,x,y, MonomialOrder => Eliminate 2];

i35 : I1 = ideal(x-a, y-a, a^2-2);

o35 : Ideal of S

i36 : ideal selectInSubring(1, gens gb I1)

2
o36 = ideal (x - y, y  - 2)

o36 : Ideal of S

i37 : I2 = ideal(x-a, y-b, a^2-2, b^2-3);

o37 : Ideal of S

i38 : ideal selectInSubring(1, gens gb I2)

2       2
o38 = ideal (y  - 3, x  - 2)

o38 : Ideal of S

i39 : I3 = ideal(x-a, y-a^4, a^4+a^3+a^2+a+1);

o39 : Ideal of S

i40 : ideal selectInSubring(1, gens gb I3)

2    2               3    2
o40 = ideal (x*y - 1, x  + y  + x + y + 1, y  + y  + x + y + 1)

o40 : Ideal of S
```

---

## schemes / chapter.m2 — chunk 5

### Input

```macaulay2
I4 = ideal(a*x+b*y, a^2-2, b^2-3);
ideal selectInSubring(1, gens gb I4)
I5 = ideal(a*x+b*y-1, a^2-2, b^2-3);
ideal selectInSubring(1, gens gb I5)
clearAll
S = QQ[x, y, z];
I = ideal(x^5+y^3+z^3, x^3+y^5+z^3, x^3+y^3+z^5);
multiplicity = degree(I : saturate(I))
```

### Output

```
i41 : I4 = ideal(a*x+b*y, a^2-2, b^2-3);

o41 : Ideal of S

i42 : ideal selectInSubring(1, gens gb I4)

2   3  2
o42 = ideal(x  - -*y )
                 2

o42 : Ideal of S

i43 : I5 = ideal(a*x+b*y-1, a^2-2, b^2-3);

o43 : Ideal of S

i44 : ideal selectInSubring(1, gens gb I5)

4     2 2   9  4    2   3  2   1
o44 = ideal(x  - 3x y  + -*y  - x  - -*y  + -)
                         4           2      4

o44 : Ideal of S

i45 : clearAll

i46 : S = QQ[x, y, z];

i47 : I = ideal(x^5+y^3+z^3, x^3+y^5+z^3, x^3+y^3+z^5);

o47 : Ideal of S

i48 : multiplicity = degree(I : saturate(I))

o48 = 27
```

---

## schemes / chapter.m2 — chunk 6

### Input

```macaulay2
clearAll
PP3 = QQ[t, x, y, z, w];
L = ideal(x, y);
M = ideal(x-t*z, y+t^2*w);
X = intersect(L, M);
Xzero = trim substitute(saturate(X, t), {t => 0})
Xzero == intersect(ideal(x^2, y), ideal(x, y^2, z))
degree(ideal(x^2, y ) / ideal(x, y^2, z))
```

### Output

```
i49 : clearAll

i50 : PP3 = QQ[t, x, y, z, w];

i51 : L = ideal(x, y);

o51 : Ideal of PP3

i52 : M = ideal(x-t*z, y+t^2*w);

o52 : Ideal of PP3

i53 : X = intersect(L, M);

o53 : Ideal of PP3

i54 : Xzero = trim substitute(saturate(X, t), {t => 0})

2        2
o54 = ideal (y*z, y , x*y, x )

o54 : Ideal of PP3

i55 : Xzero == intersect(ideal(x^2, y), ideal(x, y^2, z))

o55 = true

i56 : degree(ideal(x^2, y ) / ideal(x, y^2, z))

o56 = 1
```

---

## schemes / chapter.m2 — chunk 7

### Input

```macaulay2
clearAll
S = QQ[a, b, c, d, e];
IX = trim minors(2, matrix{{a, b^2, b*d, c},{b, a*c, c^2, d}})
IY = ideal(a, d);
codim IX + codim IY == codim (IX + IY)
(degree IX) * (degree IY)
degree (IX + IY)
J = ideal mingens (IX + ideal(a))
```

### Output

```
i57 : clearAll

i58 : S = QQ[a, b, c, d, e];

i59 : IX = trim minors(2, matrix{{a, b^2, b*d, c},{b, a*c, c^2, d}})

3      2     2    2    3    2
o59 = ideal (b*c - a*d, c  - b*d , a*c  - b d, b  - a c)

o59 : Ideal of S

i60 : IY = ideal(a, d);

o60 : Ideal of S

i61 : codim IX + codim IY == codim (IX + IY)

o61 = true

i62 : (degree IX) * (degree IY)

o62 = 4

i63 : degree (IX + IY)

o63 = 5

i64 : J = ideal mingens (IX + ideal(a))

3      2   2    3
o64 = ideal (a, b*c, c  - b*d , b d, b )

o64 : Ideal of S
```

---

## schemes / chapter.m2 — chunk 8

### Input

```macaulay2
J == intersect(ideal(a, b*c, b^2, c^3-b*d^2), 
           ideal(a, d, b*c, c^3, b^3)) -- embedded point
clearAll
blowUpIdeal = (I) -> (
           r := numgens I;
           S := ring I;
           n := numgens S;
           K := coefficientRing S;
           tR := K[t, gens S, vars(0..r-1), 
                     MonomialOrder => Eliminate 1];
           f := map(tR, S, submatrix(vars tR, {1..n}));
           F := f(gens I);
           J := ideal apply(1..r, j -> (gens tR)_(n+j)-t*F_(0,(j-1)));
           L := ideal selectInSubring(1, gens gb J);
           R := K[gens S, vars(0..r-1)];
           g := map(R, tR, 0 | vars R);
           trim g(L));
S = QQ[x, y];
I = ideal(x^3, x*y, y^2);
J = blowUpIdeal(I)
J + ideal jacobian J == ideal gens ring J
clearAll
```

### Output

```
i65 : J == intersect(ideal(a, b*c, b^2, c^3-b*d^2), 
           ideal(a, d, b*c, c^3, b^3)) -- embedded point

o65 = true

i66 : clearAll

i67 : blowUpIdeal = (I) -> (
           r := numgens I;
           S := ring I;
           n := numgens S;
           K := coefficientRing S;
           tR := K[t, gens S, vars(0..r-1), 
                     MonomialOrder => Eliminate 1];
           f := map(tR, S, submatrix(vars tR, {1..n}));
           F := f(gens I);
           J := ideal apply(1..r, j -> (gens tR)_(n+j)-t*F_(0,(j-1)));
           L := ideal selectInSubring(1, gens gb J);
           R := K[gens S, vars(0..r-1)];
           g := map(R, tR, 0 | vars R);
           trim g(L));

i68 : S = QQ[x, y];

i69 : I = ideal(x^3, x*y, y^2);

o69 : Ideal of S

i70 : J = blowUpIdeal(I)

2         2          3     2
o70 = ideal (y*b - x*c, x*b  - a*c, x b - y*a, x c - y a)

o70 : Ideal of QQ [x, y, a, b, c]

i71 : J + ideal jacobian J == ideal gens ring J

o71 = true

i72 : clearAll
```

---

## schemes / chapter.m2 — chunk 9

### Input

```macaulay2
PP4 = QQ[a..e];
S = QQ[r..t, A..E, MonomialOrder => Eliminate 3];
I = ideal(A - r^2, B - s^2, C - r*s, D - r*t, E - s*t);
phi = map(PP4, S, matrix{{0_PP4, 0_PP4, 0_PP4}} | vars PP4)
surfaceA = phi ideal selectInSubring(1, gens gb I)
R = QQ[t, x, y, z, u, v, MonomialOrder => Eliminate 1];
blowUpIdeal = ideal selectInSubring(1, gens gb ideal(u-t*x, 
           v-t*y))
PP2xPP1 = QQ[x, y, z, u, v];
```

### Output

```
i73 : PP4 = QQ[a..e];

i74 : S = QQ[r..t, A..E, MonomialOrder => Eliminate 3];

i75 : I = ideal(A - r^2, B - s^2, C - r*s, D - r*t, E - s*t);

o75 : Ideal of S

i76 : phi = map(PP4, S, matrix{{0_PP4, 0_PP4, 0_PP4}} | vars PP4)

o76 = map(PP4,S,{0, 0, 0, a, b, c, d, e})

o76 : RingMap PP4 <--- S

i77 : surfaceA = phi ideal selectInSubring(1, gens gb I)

2
o77 = ideal (c*d - a*e, b*d - c*e, a*b - c )

o77 : Ideal of PP4

i78 : R = QQ[t, x, y, z, u, v, MonomialOrder => Eliminate 1];

i79 : blowUpIdeal = ideal selectInSubring(1, gens gb ideal(u-t*x, 
           v-t*y))

o79 = ideal(y*u - x*v)

o79 : Ideal of R

i80 : PP2xPP1 = QQ[x, y, z, u, v];
```

---

## schemes / chapter.m2 — chunk 10

### Input

```macaulay2
embed = map(PP2xPP1, R, 0 | vars PP2xPP1);
blowUp = PP2xPP1 / embed(blowUpIdeal);
PP5 = QQ[A .. F];
segre = map(blowUp, PP5, matrix{{x*u,y*u,z*u,x*v,y*v,z*v}});
ker segre
projection = map(PP4, PP5, matrix{{a, c, d, c, b, e}})
surfaceB = trim projection ker segre
determinantal = minors(2, matrix{{a, c, d}, {b, d, e}})
```

### Output

```
i81 : embed = map(PP2xPP1, R, 0 | vars PP2xPP1);

o81 : RingMap PP2xPP1 <--- R

i82 : blowUp = PP2xPP1 / embed(blowUpIdeal);

i83 : PP5 = QQ[A .. F];

i84 : segre = map(blowUp, PP5, matrix{{x*u,y*u,z*u,x*v,y*v,z*v}});

o84 : RingMap blowUp <--- PP5

i85 : ker segre

2
o85 = ideal (B - D, C*E - D*F, D  - A*E, C*D - A*F)

o85 : Ideal of PP5

i86 : projection = map(PP4, PP5, matrix{{a, c, d, c, b, e}})

o86 = map(PP4,PP5,{a, c, d, c, b, e})

o86 : RingMap PP4 <--- PP5

i87 : surfaceB = trim projection ker segre

2
o87 = ideal (c*d - a*e, b*d - c*e, a*b - c )

o87 : Ideal of PP4

i88 : determinantal = minors(2, matrix{{a, c, d}, {b, d, e}})

2
o88 = ideal (- b*c + a*d, - b*d + a*e, - d  + c*e)

o88 : Ideal of PP4
```

---

## schemes / chapter.m2 — chunk 11

### Input

```macaulay2
sigma = map( PP4, PP4, matrix{{d, e, a, c, b}});
surfaceC = sigma determinantal
surfaceA == surfaceB
surfaceB == surfaceC
clearAll
PP3 = QQ[t, x, y, z, w];
Q = ideal( t*x^2+t*y^2+t*z^2+w^2 );
R = QQ[t, u, v, A .. H];
```

### Output

```
i89 : sigma = map( PP4, PP4, matrix{{d, e, a, c, b}});

o89 : RingMap PP4 <--- PP4

i90 : surfaceC = sigma determinantal

2
o90 = ideal (c*d - a*e, b*d - c*e, a*b - c )

o90 : Ideal of PP4

i91 : surfaceA == surfaceB

o91 = true

i92 : surfaceB == surfaceC

o92 = true

i93 : clearAll

i94 : PP3 = QQ[t, x, y, z, w];

i95 : Q = ideal( t*x^2+t*y^2+t*z^2+w^2 );

o95 : Ideal of PP3

i96 : R = QQ[t, u, v, A .. H];
```

---

## schemes / chapter.m2 — chunk 12

### Input

```macaulay2
phi = map(R, PP3, matrix{{t}} | 
              u*matrix{{A, B, C, D}} + v*matrix{{E, F, G, H}});
imageFamily = phi Q;
coeffOfFamily = contract(matrix{{u^2,u*v,v^2}}, gens imageFamily)
S = QQ[t, A..H];
coeffOfFamily = substitute(coeffOfFamily, S);
Sbar = S / (ideal coeffOfFamily);
psi = matrix{{t}} | exteriorPower(2, 
                   matrix{{A, B, C, D}, {E, F, G, H}})
PP5 = QQ[t, a..f];
```

### Output

```
i97 : phi = map(R, PP3, matrix{{t}} | 
              u*matrix{{A, B, C, D}} + v*matrix{{E, F, G, H}});

o97 : RingMap R <--- PP3

i98 : imageFamily = phi Q;

o98 : Ideal of R

i99 : coeffOfFamily = contract(matrix{{u^2,u*v,v^2}}, gens imageFamily)

o99 = | tA2+tB2+tC2+D2 2tAE+2tBF+2tCG+2DH tE2+tF2+tG2+H2 |

              1       3
o99 : Matrix R  <--- R

i100 : S = QQ[t, A..H];

i101 : coeffOfFamily = substitute(coeffOfFamily, S);

1       3
o101 : Matrix S  <--- S

i102 : Sbar = S / (ideal coeffOfFamily);

i103 : psi = matrix{{t}} | exteriorPower(2, 
                   matrix{{A, B, C, D}, {E, F, G, H}})

o103 = | t -BE+AF -CE+AG -CF+BG -DE+AH -DF+BH -DG+CH |

                  1          7
o103 : Matrix Sbar  <--- Sbar

i104 : PP5 = QQ[t, a..f];
```

---

## schemes / chapter.m2 — chunk 13

### Input

```macaulay2
fanoOfFamily = trim ker map(Sbar, PP5, psi);
zeroFibre = trim substitute(saturate(fanoOfFamily, t), {t=>0})
transpose gens zeroFibre
oneFibre = trim substitute(saturate(fanoOfFamily, t), {t => 1})
oneFibre == intersect(ideal(c-d, b+e, a-f, d^2+e^2+f^2), 
            ideal(c+d, b-e, a+f, d^2+e^2+f^2))
i110 :
```

### Output

```
i105 : fanoOfFamily = trim ker map(Sbar, PP5, psi);

o105 : Ideal of PP5

i106 : zeroFibre = trim substitute(saturate(fanoOfFamily, t), {t=>0})

2   2                   2                                          2    2    2
o106 = ideal (e*f, d*f, e , f , d*e, a*e + b*f, d , c*d - b*e + a*f, b*d + c*e, a*d - c*f, a  + b  + c )

o106 : Ideal of PP5

i107 : transpose gens zeroFibre

o107 = {-2} | ef       |
       {-2} | df       |
       {-2} | e2       |
       {-2} | f2       |
       {-2} | de       |
       {-2} | ae+bf    |
       {-2} | d2       |
       {-2} | cd-be+af |
       {-2} | bd+ce    |
       {-2} | ad-cf    |
       {-2} | a2+b2+c2 |

                 11         1
o107 : Matrix PP5   <--- PP5

i108 : oneFibre = trim substitute(saturate(fanoOfFamily, t), {t => 1})

2    2    2                                          2    2    2                         2    2              2    2
o108 = ideal (a*e + b*f, d  + e  + f , c*d - b*e + a*f, b*d + c*e, a*d - c*f, c  + e  + f , b*c + d*e, a*c - d*f, b  - e , a*b + e*f, a  - f )

o108 : Ideal of PP5

i109 : oneFibre == intersect(ideal(c-d, b+e, a-f, d^2+e^2+f^2), 
            ideal(c+d, b-e, a+f, d^2+e^2+f^2))

o109 = true

i110 :
```

---

## schemes / test.m2 — chunk 0

### Input

```macaulay2
S = ZZ[x, y, z];
elementaryBasis = ideal(x+y+z, x*y+x*z+y*z, x*y*z);
saturate(elementaryBasis, x)
powerSumBasis = ideal(x+y+z, x^2+y^2+z^2, x^3+y^3+z^3);
saturate(powerSumBasis, x)
clearAll
S = QQ[t, y_0 .. y_8, a..i, MonomialOrder => Eliminate 10];
N3 = (matrix {{0,1,0},{0,0,1},{0,0,0}}) ** S
```

### Output

```
i1 : S = ZZ[x, y, z];

i2 : elementaryBasis = ideal(x+y+z, x*y+x*z+y*z, x*y*z);

o2 : Ideal of S

i3 : saturate(elementaryBasis, x)

o3 = ideal 1

o3 : Ideal of S

i4 : powerSumBasis = ideal(x+y+z, x^2+y^2+z^2, x^3+y^3+z^3);

o4 : Ideal of S

i5 : saturate(powerSumBasis, x)

2           2
o5 = ideal (6, x + y + z, 3y*z, 2y  - y*z + 2z )

o5 : Ideal of S

i6 : clearAll

i7 : S = QQ[t, y_0 .. y_8, a..i, MonomialOrder => Eliminate 10];

i8 : N3 = (matrix {{0,1,0},{0,0,1},{0,0,0}}) ** S

o8 = | 0 1 0 |
     | 0 0 1 |
     | 0 0 0 |

             3      3
o8 : Matrix S  <-- S
```

---

## schemes / test.m2 — chunk 1

### Input

```macaulay2
G = genericMatrix(S, y_0, 3, 3)
classicalAdjoint = (G) -> (
           n := degree target G;
           m := degree source G;
           matrix table(n, n, (i, j) -> (-1)^(i+j) * det(
                     submatrix(G, {0..j-1, j+1..n-1}, 
                          {0..i-1, i+1..m-1}))));
num = G * N3 * classicalAdjoint(G);
D = det(G);
M = genericMatrix(S, a, 3, 3);
elimIdeal = minors(1, (D*id_(S^3))*M - num) + ideal(1-D*t);
closureOfOrbit = ideal selectInSubring(1, gens gb elimIdeal);
X = ideal substitute(
              contract(matrix{{t^2,t,1}}, det(t-M)),
              {t => 0_S})
```

### Output

```
i9 : G = genericMatrix(S, y_0, 3, 3)

o9 = | y_0 y_3 y_6 |
     | y_1 y_4 y_7 |
     | y_2 y_5 y_8 |

             3      3
o9 : Matrix S  <-- S

i10 : classicalAdjoint = (G) -> (
           n := degree target G;
           m := degree source G;
           matrix table(n, n, (i, j) -> (-1)^(i+j) * det(
                     submatrix(G, {0..j-1, j+1..n-1}, 
                          {0..i-1, i+1..m-1}))));

i11 : num = G * N3 * classicalAdjoint(G);

3      3
o11 : Matrix S  <-- S

i12 : D = det(G);

i13 : M = genericMatrix(S, a, 3, 3);

3      3
o13 : Matrix S  <-- S

i14 : elimIdeal = minors(1, (D*id_(S^3))*M - num) + ideal(1-D*t);

o14 : Ideal of S

i15 : closureOfOrbit = ideal selectInSubring(1, gens gb elimIdeal);

o15 : Ideal of S

i16 : X = ideal substitute(
              contract(matrix{{t^2,t,1}}, det(t-M)),
              {t => 0_S})

o16 = ideal (- a - e - i, - b*d + a*e - c*g - f*h + a*i + e*i, c*e*g - b*f*g - c*d*h + a*f*h + b*d*i - a*e*i)

o16 : Ideal of S
```

---

## schemes / test.m2 — chunk 2

### Input

```macaulay2
closureOfOrbit == X
clearAll
S = QQ[x, y, z, a..j, MonomialOrder => Eliminate 2];
F = a*x^3+b*x^2*y+c*x^2*z+d*x*y^2+e*x*y*z+f*x*z^2+g*y^3+h*y^2*z+
                   i*y*z^2+j*z^3;
partials = submatrix(jacobian matrix{{F}}, {0..2}, {0})
singularities = ideal(partials) + ideal(F);
elimDiscr = time ideal selectInSubring(1,gens gb singularities);
     -- used 18.3771 seconds
elimDiscr = substitute(elimDiscr, {z => 1});
```

### Output

```
i17 : closureOfOrbit == X

o17 = true

i18 : clearAll

i19 : S = QQ[x, y, z, a..j, MonomialOrder => Eliminate 2];

i20 : F = a*x^3+b*x^2*y+c*x^2*z+d*x*y^2+e*x*y*z+f*x*z^2+g*y^3+h*y^2*z+
                   i*y*z^2+j*z^3;

i21 : partials = submatrix(jacobian matrix{{F}}, {0..2}, {0})

o21 = {1} | 3x2a+2xyb+y2d+2xzc+yze+z2f |
      {1} | x2b+2xyd+3y2g+xze+2yzh+z2i |
      {1} | x2c+xye+y2h+2xzf+2yzi+3z2j |

              3      1
o21 : Matrix S  <-- S

i22 : singularities = ideal(partials) + ideal(F);

o22 : Ideal of S

i23 : elimDiscr = time ideal selectInSubring(1,gens gb singularities);
     -- used 18.3771 seconds

o23 : Ideal of S

i24 : elimDiscr = substitute(elimDiscr, {z => 1});

o24 : Ideal of S
```

---

## schemes / test.m2 — chunk 3

### Input

```macaulay2
A = contract(matrix{{x^2,x*y,y^2,x*z,y*z,z^2}},
              diff(transpose matrix{{x,y,z}},F))
hess = det submatrix(jacobian ideal partials, {0..2}, {0..2});
B = contract(matrix{{x^2,x*y,y^2,x*z,y*z,z^2}},
              diff(transpose matrix{{x,y,z}},hess))
detDiscr = ideal det (A || B, Strategy=>Cofactor);
detDiscr == elimDiscr
detDiscr_0
numgens detDiscr
# terms detDiscr_0
```

### Output

```
i25 : A = contract(matrix{{x^2,x*y,y^2,x*z,y*z,z^2}},
              diff(transpose matrix{{x,y,z}},F))

o25 = {1} | 3a 2b d  2c e  f  |
      {1} | b  2d 3g e  2h i  |
      {1} | c  e  h  2f 2i 3j |

              3      6
o25 : Matrix S  <-- S

i26 : hess = det submatrix(jacobian ideal partials, {0..2}, {0..2});

i27 : B = contract(matrix{{x^2,x*y,y^2,x*z,y*z,z^2}},
              diff(transpose matrix{{x,y,z}},hess))

o27 = {1} | -24c2d+24bce-18ae2-24b2f+72adf               4be2-16bdf-48c2g+144afg+32bch-48aeh-16b2i+48adi         2de2-8d2f-24ceg+24bfg+16cdh-24ah2-8bdi+72agi  4ce2-16cdf-16c2h+48afh+32bci-48aei-48b2j+144adj         2e3-8def-24cfg-8ceh+24bfh+24cdi-8bei-24ahi-24bdj+216agj 2e2f-8df2-8cfh+16bfi-24ai2+24cdj-24bej+72ahj  |
      {1} | 2be2-8bdf-24c2g+72afg+16bch-24aeh-8b2i+24adi 4de2-16d2f-48ceg+48bfg+32cdh-48ah2-16bdi+144agi         -18e2g+24deh-24bh2-24d2i+72bgi                2e3-8def-24cfg-8ceh+24bfh+24cdi-8bei-24ahi-24bdj+216agj -48efg+4e2h+32dfh-16ch2+48cgi-16bhi-48d2j+144bgj        -24f2g+2e2i+16dfi-8chi-8bi2-24dej+72cgj+24bhj |
      {1} | 2ce2-8cdf-8c2h+24afh+16bci-24aei-24b2j+72adj 2e3-8def-24cfg-8ceh+24bfh+24cdi-8bei-24ahi-24bdj+216agj -24efg+2e2h+16dfh-8ch2+24cgi-8bhi-24d2j+72bgj 4e2f-16df2-16cfh+32bfi-48ai2+48cdj-48bej+144ahj         -48f2g+4e2i+32dfi-16chi-16bi2-48dej+144cgj+48bhj        -24f2h+24efi-24ci2-18e2j+72chj                |

              3      6
o27 : Matrix S  <-- S

i28 : detDiscr = ideal det (A || B, Strategy=>Cofactor);

o28 : Ideal of S

i29 : detDiscr == elimDiscr

o29 = true

i30 : detDiscr_0

2   4 3 2             5 3 2           6 3 2          2 2 2 4 2                3 4 2         2 4 4 2              4 4 2          2 3 5 2              2   5 2          2   2 5 2            2 2 5 2          2 2 6 2            3 6 2         3 3 3 3          3     4 3            2 2 4 3              3 4 3            2   5 3           2     5 3                   5 3              2 5 3          3 6 3                 6 3          4 4 4             2 5 4           2 6 4         2   5 2                6 2              7 2             2 2 3 3                   4 3            2 5 3                 5 3             2 3   4                 2 2 4             2   3 4               2 3 4             2 2   5               3   5            3 4 2 2           3   2 3 2             2 3 3 2               4 3 2           3 2 4 2              2     4 2            2   2 4 2                  2 4 2                3 4 2           2     5 2                2 5 2            3   5 2                    5 2           4   3 3             3 4 3              2   4 3                  5 3             2   5 3          2 2 4 2 2               5 2 2             6 2 2          2 3 2 3 2              2 3 3 2         2   4 3 2            2 4 3 2          2 4 4 2              3   4 2          2 2 2 4 2            3 2 4 2          2 3 5 2            4 5 2          3   3 2   2            2 4 2   2              5 2   2          3 2   3   2             2   2 3   2          2   3 3   2                3 3   2              4 3   2             2 2 4   2           2       4   2               2   4   2          3 2 4   2                2 4   2          3   5   2               2 5   2          4 2 2 2 2          4   3 2 2            3   3 2 2             2 2 3 2 2         2 2 4 2 2             2   4 2 2                   4 2 2           2 2 4 2 2            2 5 2 2           2   5 2 2          3 2 2 2 3            2   3 2 3         2   4 2 3                4 2 3             5 2 3          3 3 3 3            2 2   3 3          2     2 3 3              2 2 3 3         3 3 3 3                3 3 3          2   2 4 3               3 4 3          3     4 3               2   4 3          4     2   3            3 2 2   3            2 3 2   3             3   3   3          2 2   3   3             2     3   3               2 3   3          2 3 3   3          3   4   3                   4   3            2   4   3           2     4   3          5 2 2 3             3 3 2 3           2   4 2 3          4 2 2 4            3     2 4          2 2 2 2 4            2   2 2 4                3 2 4         2 4 2 4          2 2   3 4            2 2 3 4          3     3 4                    3 4            2 2 3 4           2   2 3 4          4 4 4             2   4 4           2 2 4 4            4 2   4            3   2   4               2 3   4           2     3   4           2   4   4          2 3 2 5            3   2 5              2   2 5          2   2 2 5            2   3 5           2     3 5           2     3 5          2 2 2 6          3 3 6         2   6                  7                8               2 2 4 2                   5 2            2 6 2                 6 2             2 3 2 3                 2 3 3             2   4 3               2 4 3             2 4 4                 3   4             2 2 2 4                3 2 4             2 3 5                4 5            3 5   2           3   3 2 2             2 4 2 2               5 2 2           3 2   3 2             2   2 3 2            2   3 3 2                  3 3 2                4 3 2              2 2 4 2            2       4 2                2   4 2            3 2 4 2                  2 4 2            3   5 2                2 5 2           4 2 2 3           4   3 3             3   3 3              2 2 3 3           2 2 4 3              2   4 3                    4 3            2 2 4 3             2   5 3          2 2 5                    6                  7               2 3 3 2                 2 4 2            2   5 2               2 5 2             2 4   3                 3 2 3             2 2 3 3               3 3 3             2 3   4               4   4             3   4                   2 5                     6                  3 2 2 2                  2   3 2               2   4 2                     4 2                   5 2                3 3 3                 2 2   3                2     2 3                    2 2 3               3 3 3                      3 3               2   2 4                    3 4               3     4                   2   4               4 3   2              4     2 2               3 2 2 2               2 3 2 2                3   3 2              2 2   3 2                2     3 2                    2 3 2              2 3 3 2              3   4 2                       4 2               2   4 2              2     4 2             5 2 3                3 3 3               2   4 3             3 2 3   2             2   4   2          2   5   2                 5   2              6   2           3 3   2 2              2 2 2 2 2           2     3 2 2               2 3 2 2          3 4 2 2                 4 2 2             2 3 3 2            2   2   3 2                3   3 2           3   2 3 2                2 2 3 2           3 2 4 2                3 4 2           4   2     2             3 3     2             2 4     2            4 2 2   2             3     2   2            2 2 2 2   2             2   2 2   2                3 2   2            2 4 2   2            2 2   3   2              2 2 3   2            3     3   2                      3   2              2 2 3   2             2   2 3   2            4 4   2              2   4   2            2 2 4   2           5     2 2              4 2 2 2              3   2 2 2                 2 3 2 2            2     3 2 2             2   4 2 2           4 2     3             3   2   3           2 2 3   3             2   3   3                 4   3          2 5   3             3 2 2 3            2 2     2 3             2 2   2 3           3   2 2 3                    2 2 3             2 3 2 3            2   3 2 3           3     3 3                 2 3 3           4   3 3              2     3 3            2 2   3 3             4       3             3 2     3           2 3 2   3              3   2   3                2   2   3            2   2 2   3              2   3   3             2     3   3            2     3   3           2 3     4             3       4               2 2   4           2   3   4           3 2 2 4               2   2 4              2     2 4            2       2 4            2   2 2 4             3 3 4            2     3 4            2 2 2   4            3 3   4           2 2     5           2     2 5            3   2 5          2 3 4   2             2 5   2           2 6   2          2 4 2 2 2              3 3 2 2         2 2 4 2 2            3 4 2 2          2 5 3 2              4   3 2          2 3 2 3 2            4 2 3 2          2 4 4 2            5 4 2         3   5   2           2 6   2             7   2          3 2 3     2            2   4     2          2   5     2                5     2              6     2          3 3   2   2             2 2 2 2   2          2     3 2   2               2 3 2   2          3 4 2   2                4 2   2            2 3 3   2          2   2   3   2               3   3   2          3   2 3   2               2 2 3   2          3 2 4   2               3 4   2         4 4 2 2           4   2   2 2             3 3   2 2             2 4   2 2         4 2 2 2 2             3     2 2 2           2 2 2 2 2 2             2   2 2 2 2                 3 2 2 2           2 4 2 2 2          2 2   3 2 2             2 2 3 2 2           3     3 2 2                      3 2 2             2 2 3 2 2           2   2 3 2 2           4 4 2 2             2   4 2 2           2 2 4 2 2           5     3 2            4 2 3 2              3   2 3 2               2 3 3 2            2     3 3 2            2   4 3 2         3 2 4   2           2   5   2               6   2          3 3 2     2            2 2 3     2          2     4     2              2 4     2                5     2          3 4 2   2             2 3   2   2           2   2 2 2   2               3 2 2   2          3   3 2   2              2 3 2   2          2   3 3   2               4 3   2          3 2   3   2               3   3   2          4   3     2            3 4     2            2 5     2           4 2         2             3   2       2          2 2 3       2           2   3       2                4       2          2 5       2             3 2 2     2           2 2     2     2             2 2   2     2           3   2 2     2                   2 2     2             2 3 2     2           2   3 2     2          3     3     2                 2 3     2           4   3     2              2     3     2          2 2   3     2          5 2 2   2          5     2   2             4     2   2             3 2   2   2          2 3 2 2   2             3   2 2   2                2   2 2   2            2   2 2 2   2             2   3 2   2           2     3 2   2           2     3 2   2          4 2 2 2 2            3   3 2 2         2 2 4 2 2            2   4 2 2               5 2 2          4 3   2 2             3 2     2 2           2 2   2   2 2             2 2 2   2 2          3   3   2 2                   3   2 2            2 4   2 2          2   4   2 2          2 2 2 2 2 2             2 3 2 2 2           3       2 2 2                 2   2 2 2          4 2 2 2 2             2   2 2 2 2           2 2 2 2 2 2          4   3 2 2             2 2 3 2 2           2 3 3 2 2          5       2 2            4 2   2 2            3 3   2 2            4       2 2          2 3       2 2             3         2 2              2 2     2 2          2   3     2 2           3 2 2   2 2               2   2   2 2             2     2   2 2            2       2   2 2           2   2 2   2 2             3 3   2 2           2     3   2 2          6 2 2 2             4   2 2 2           2 2 2 2 2 2            3 3 2 2 2          5 2 3 2            4     3 2          2 3 2 3 2            3   2 3 2              2 3 3 2         2   4 3 2          2 3     3 2            3 2   3 2          3 2     3 2              2       3 2             2   2   3 2          2     2   3 2          2   3   3 2          4   2 3 2             2     2 3 2          2   2 2 3 2            3   2 3 2           2       2 3 2            5   3 2            4     3 2               3     3 2           2 2       3 2           2     2   3 2            3   2   3 2          2 4 4 2            4   4 2              3   4 2          2 2 2 4 2             2 2   4 2           2 2     4 2           2         4 2          3 2   4 2         2 2 2 4 2          3   2 4 2          2 3 5 2          3     5 2         3 3 3 3           2 2 4 3             2 5 3          3 4     3            2 3 2   3          2   2 3   3              3 3   3              2 4   3            2 4 2 3          2   3   2 3               4   2 3          3 2 2 2 3              3 2 2 3          3 3 3 3               4 3 3          4 2 2   3            3   3   3          2 2 4   3            2   4   3                5   3         2 6   3          4 3     3             3 2       3           2 2   2     3             2 2 2     3          3   3     3                   3     3            2 4     3           2   4     3           2 2 2 2   3             2 3 2   3           3       2   3                  2   2   3          4 2 2   3             2   2 2   3           2 2 2 2   3           4   3   3             2 2 3   3           2 3 3   3           5     2 3             4 2 2 3            3 3 2 3             4     2 3           2 3     2 3             3       2 3                2 2   2 3           2   3   2 3           3 2 2 2 3               2   2 2 3            2     2 2 3           2       2 2 3           2   2 2 2 3             3 3 2 3           2     3 2 3          6 3 3             4   3 3            2 2 2 3 3            3 3 3 3          4 3     3            3 2 2   3          2 2   3   3            2 2 3   3                  4   3         2   5   3            3 3     3           2 2 2       3             2 3       3          3     2     3                 2 2     3            2   3     3           2 2 3     3          3   2 2   3                3 2   3          4     2   3            2 2   2   3           2 3   2   3          5 2     3            4         3          2 3 2     3           3   2     3              2 3     3          2   4     3          2 3         3             3 2       3           3 2         3               2           3             2   2       3           2     2       3           2   3       3           4   2     3             2     2     3           2   2 2     3             3   2     3            2       2     3             5 2   3             4   2   3                3   2   3           2 2     2   3           2     2 2   3            3   2 2   3            4 2 2 3          2 3     2 3            3 2   2 3          3 2 2 2 3               2   2 2 3            2   3 2 3          2     3 2 3         2   4 2 3          3 2     2 3               2 2   2 3          4       2 3            2         2 3           2   2     2 3            3 2   2 3          2     2   2 3          5 2 2 3            3   2 2 3          2   2 2 2 3          2 4   2 3             4     2 3               3     2 3           2 2 2   2 3             2 2     2 3            2 2       2 3           2           2 3           3 2     2 3           2 2 2   2 3           3   2   2 3          3 3 3 3               3   3 3            2 2   3 3          2 2     3 3          2     2 3 3         3 3 3 3             3     3 3           2         3 3          2 2     3 3          3       3 3           2 3   3 3           3       3 3          2   2 4 3          3     4 3          3     4 3          4 4 4            3 3   4          2 2 2 2 4            2 3 2 4                2 3 4         2 2 4 4          2 2 3   4             2 4   4          3   2     4                3     4            2 2 2   4           2 3 2   4          4 2 2 4            2 3 2 4           2 4 2 4             4 2   4           2 3       4            3 2     4          3 2 2   4              2   2   4            2   3   4           2     3   4          2   4   4           3 2       4               2 2     4          4         4            2           4          2   2       4             3 2     4           2     2     4          5 2   4             3   2   4           2   2 2   4           2 4 2 4             4   2 4               3   2 4           2 2 2 2 4             2 2   2 4            2 2     2 4           2         2 4           3 2   2 4           2 2 2 2 4            3   2 2 4          2 3 2   4            3 3   4          3 2       4               2 2     4            2     2   4           2   2 2   4          2     3   4            2   2     4           2   3     4            3         4           2   2       4           3 3     4               3       4             2 2       4           2 2         4           2     2     4          3 3     4             3         4            2             4           2 2         4           3           4           2 3 2   4            3     2   4          4 2 2 4             2 2   2 4         2 2 2 2 4            3     2 4           2         2 4          2 2 2 2 4          3   2 2 4            4   2 4           2 2     2 4          3 2   2 4           2   2   2 4           3       2 4           3       2 4          2 2   3 4          3     3 4          3     3 4          4 4 4          3 2 2 5              2 3 5            2   2   5           2   3   5          2   2 2 5            3 2   5           2   3   5          4 2   5             2 2     5          2 2 2   5            3       5           2           5          2 2 2   5          3   2   5             4     5           2 2       5           2   2 2 5            3     2 5            3     2 5          2     2   5          2 2       5           3 2     5           2 2       5           3         5           3         5          2 3 2 5          3     2 5           4   2 5          2 2 2 6          3 3 6          2 3   6           3       6           4 2 6         2   7                8              9             2 2 5                     6              2 7                   7               2 3 3 2                 2 4 2             2   5 2                2 5 2             2 4   3                 3 2 3             2 2 3 3                3 3 3             2 3   4                4   4            3 6 2           3   4   2             2 5   2               6   2            3 2 2 2 2             2   3 2 2            2   4 2 2                  4 2 2                5 2 2            3 3 3 2              2 2   3 2            2     2 3 2                 2 2 3 2           3 3 3 2                  3 3 2            2   2 4 2                3 4 2            3     4 2                 2   4 2           4 3   3            4     2 3              3 2 2 3              2 3 2 3              3   3 3             2 2   3 3               2     3 3                  2 3 3            2 3 3 3            3   4 3                     4 3             2     4 3            5 2 4               3 3 4             2   4 4          2 2 6                  7                8             2 3 4                   2 5              2   6                 2 6               2 4 2 2                 3 3 2             2 2 4 2               3 4 2             2 5 3                 4   3             2 3 2 3                4 2 3             2 4 4                5 4             3   5                 2 6                   7               3 2 3                   2   4                 2   5                       5                     6                  3 3   2                 2 2 2 2              2     3 2                    2 3 2               3 4 2                      4 2                  2 3 3                2   2   3                    3   3              3   2 3                    2 2 3                3 2 4                     3 4               4 4 2              4   2   2                3 3   2                2 4   2              4 2 2 2                3     2 2              2 2 2 2 2                 2   2 2 2                    3 2 2              2 4 2 2              2 2   3 2                 2 2 3 2              3     3 2                         3 2                2 2 3 2              2   2 3 2              4 4 2                 2   4 2               2 2 4 2              5     3                4 2 3                 3   2 3                   2 3 3               2     3 3               2   4 3             3 2 4 2             2   5 2          2   6 2                 6 2              7 2           3 3 2   2             2 2 3   2           2     4   2               2 4   2          3 5   2                 5   2           3 4 2 2             2 3   2 2            2   2 2 2 2                3 2 2 2           3   3 2 2                2 3 2 2           2   3 3 2                4 3 2           3 2   3 2                3   3 2           4   3   2             3 4   2              2 5   2            4 2       2              3   2     2            2 2 3     2              2   3     2                  4     2            2 5     2              3 2 2   2            2 2     2   2               2 2   2   2            3   2 2   2                    2 2   2              2 3 2   2            2   3 2   2            3     3   2                   2 3   2           4   3   2              2     3   2             2 2   3   2           5 2 2 2            5     2 2              4     2 2               3 2   2 2            2 3 2 2 2               3   2 2 2                 2   2 2 2             2   2 2 2 2              2   3 2 2             2     3 2 2            2     3 2 2           4 2 2 3             3   3 3           2 2 4 3             2   4 3                 5 3          2 6 3            4 3   3              3 2     3            2 2   2   3              2 2 2   3           3   3   3                    3   3             2 4   3            2   4   3            2 2 2 2 3              2 3 2 3            3       2 3                   2   2 3           4 2 2 3              2   2 2 3            2 2 2 2 3           4   3 3              2 2 3 3            2 3 3 3           5       3              4 2   3              3 3   3              4       3            2 3       3              3         3                2 2     3            2   3     3            3 2 2   3                 2   2   3              2     2   3             2       2   3            2   2 2   3             3 3   3            2     3   3           6 2 3              4   2 3             2 2 2 2 3             3 3 2 3           5 2 4             4     4           2 3 2 4              3   2 4               2 3 4           2   4 4            2 3     4              3 2   4            3 2     4               2       4             2   2   4            2     2   4            2   3   4            4   2 4              2     2 4            2   2 2 4             3   2 4           2       2 4              5   4              4     4                 3     4             2 2       4             2     2   4           2 4 5              4   5               3   5           2 2 2 5              2 2   5            2 2     5            2         5           3 2   5           2 2 2 5           2 3 6            3     6          2 3 5                2 6              2 7             2 4 3                   3 4              2 2 5                 3 5               2 5   2                 4 2 2             2 3 3 2               4 3 2             2 4   3               5   3             3 2 4                 2   5               2   6                     6                   7              3 3 2                  2 2 3                 2     4                      2 4                 3 5                       5                  3 4 2                  2 3   2               2   2 2 2                    3 2 2               3   3 2                    2 3 2                2   3 3                     4 3                3 2   3                    3   3                4   3 2                3 4 2                2 5 2              4 2     2                3   2   2              2 2 3   2                2   3   2                    4   2              2 5   2                 3 2 2 2               2 2     2 2                 2 2   2 2               3   2 2 2                       2 2 2                2 3 2 2              2   3 2 2               3     3 2                     2 3 2              4   3 2                 2     3 2              2 2   3 2             5 2 3              5     3                4     3                3 2   3              2 3 2 3                 3   2 3                   2   2 3              2   2 2 3               2     3 3               2     3 3             3 3 3                 2 2 4               2     5                   2 5                     6               3 4                      2 3 2                  2   2 3                      3 3                 3   4                     2 4                   2 4 2               2   3   2                   4   2                3 2 2 2                    3 2 2                3 3 3                    4 3               4 2 2                    3   3                 2 2 4                    2   4                       5                 2 6                  4 3                      3 2                      2 2   2                      2 2 2                    3   3                             3                      2 4                    2   4                    2 2 2 2                     2 3 2                  3       2                         2   2                 4 2 2                    2   2 2                  2 2 2 2                  4   3                     2 2 3                  2 3 3                  5     2                  4 2 2                  3 3 2                   4     2                 2 3     2                   3       2                     2 2   2               2   3   2                3 2 2 2                     2   2 2                   2     2 2                 2       2 2                 2   2 2 2                  3 3 2                 2     3 2                6 3                   4   3                 2 2 2 3                 3 3 3                4 3   2                3 2 2 2             2 2   3 2                2 2 3 2             3   4 2                     4 2               2 5 2             2   5 2               3 3   2              2 2 2     2                 2 3     2              3     2   2                    2 2   2             4 3   2              2   3   2              2 2 3   2              3   2 2 2                    3 2 2              4     2 2                2 2   2 2             2 3   2 2              5 2   2               4       2              2 3 2   2                3   2   2                  2 3   2              2   4   2              2 3       2                 3 2     2               3 2       2                   2         2                2   2     2               2     2     2              2   3     2              4   2   2                 2     2   2               2   2 2   2                3   2   2               2       2   2                5 2 2                 4   2 2                   3   2 2               2 2     2 2               2     2 2 2               3   2 2 2                4 2 3              2 3     3                3 2   3             3 2 2 3                  2   2 3               2   3 3              2     3 3             2   4 3             3 2     3                  2 2   3             4       3                2         3               2   2     3              3 2   3              2     2   3             5 2 3                3   2 3              2   2 2 3              2 4   3                 4     3                  3     3               2 2 2   3                 2 2     3               2 2       3               2           3              3 2     3              2 2 2   3              3 3 4                  3   4                2 2   4              2 2     4              2     2 4             3 3 4                3     4               2         4              2 2     4              3       4              2 3   4               3       4              2   2 5              3     5              3     5             3 4 2 2             2 3 3 2           2   2 4 2               3 4 2               2 5 2           3 5   2              2 4     2            2   3 2   2               4 2   2           3 2 3   2               3 3   2            2   4 2 2                5 2 2           3 3   2 2                4   2 2           4 3     2              3 2 2   2            2 2   3   2              2 2 3   2           3   4   2                    4   2              2 5   2            2   5   2              3 3     2            2 2 2       2              2 3       2            3     2     2                  2 2     2           4 3     2              2   3     2            2 2 3     2            3   2 2   2                   3 2   2            4     2   2               2 2   2   2             2 3   2   2           5 2 2 2             4     2 2            2 3 2 2 2              3   2 2 2                2 3 2 2            2   4 2 2            2 3     2 2              3 2   2 2           3 2     2 2                 2       2 2              2   2   2 2             2     2   2 2            2   3   2 2            4   2 2 2               2     2 2 2             2   2 2 2 2               3   2 2 2             2       2 2 2             2 2     3 2             2     2 3 2              3   2 3 2            4 4   2              3 3     2            2 2 2 2   2              2 3 2   2           3     3   2                2 3   2             2   4   2            2 2 4   2            2 2 3     2              2 4     2           3   2       2                  3       2           4   2     2             2 2 2     2             2 3 2     2            4 2 2   2              2 3 2   2            2 4 2   2              4 2     2             2 3         2              3 2       2            3 2 2     2                2   2     2              2   3     2            2     3     2            2   4     2            3 2         2                 2 2       2           4           2               2             2             2   2         2              3 2       2             2     2       2            5 2     2               3   2     2             2   2 2     2            2 4 2   2               4   2   2                 3   2   2             2 2 2 2   2               2 2   2   2             2 2     2   2             2         2   2            3 2   2   2             2 2 2 2   2             3   2 2   2            2 3 2 2 2              3 3 2 2           3 2     2 2                2 2   2 2           4   2 2 2             2     2 2 2            2   2 2 2 2             3 3 2 2           2     3 2 2           4       2 2              2   2   2 2            2   3   2 2           5     2 2              3       2 2             2   2     2 2            3 3   2 2                 3     2 2               2 2     2 2             2 2       2 2             2     2   2 2            3 3   2 2               3       2 2             2           2 2             2 2       2 2             3         2 2             2 3 2 2 2             3     2 2 2           4 2 3 2              2 2   3 2            2 2 2 3 2              3     3 2            2         3 2            2 2 2 3 2            3   2 3 2              4   3 2             2 2     3 2            3 2   3 2             2   2   3 2             3       3 2             3       3 2            2 2   4 2            3     4 2            3     4 2            4 5 2             3 4 3           2 2 3   3             2 4   3           3   2 2 3                3 2 3             2 2 3 3           2 3 3 3            3   3   3                  4   3           4 2     3              2 3     3            2 4     3            2 3 2   3             3 3   3            3 2       3                2 2     3            4   2   3              2     2   3            2   2 2   3              3 3   3            2     3   3            4         3               2   2     3            2   3     3           5       3              3         3             2   2       3            3 3 2 3                3   2 3               2 2   2 3            2 2     2 3            2     2 2 3            3 3 2 3              3     2 3             2         2 3            2 2     2 3             3       2 3             2 3 3 3             3     3 3           3 2 2   3                2 3   3           4         3              2   2     3            2   3     3             3   2   3            2   2 2   3              3 2     3             2   3     3            4 2     3               2 2       3            2 2 2     3              3         3             2             3             2 2 2     3            3   2     3               4       3             2 2         3             2   2 2   3             3     2   3             3     2   3           5   2 3              3     2 3            2     2 2 3             4   2 3            2 2     2 3             3 2   2 3             2 2     2 3             3       2 3             3       2 3            2 3 3 3            3     3 3             4   3 3           4   2 4              2   3 4            2   4 4             3 2   4            2   3   4            5     4               3       4             2     2   4              4     4             2 2       4             2 2   2 4             3     2 4             3     2 4            2 2 2   4            3 3   4            2 3     4             3         4             4 2   4          2 4 4 2             3 5 2           3 6 2          2 5 2   2              4 3   2         2 3 4   2            4 4   2          2 6 2 2              5   2 2          2 4 2 2 2            5 2 2 2          2 5 3 2            6 3 2          3 3 3   2             2 2 4   2          2     5   2               2 5   2         3 6   2                6   2           3 4       2             2 3 2     2          2   2 3     2               3 3     2          3   4     2               2 4     2             2 4 2   2           2   3   2   2                4   2   2           3 2 2 2   2                3 2 2   2           3 3 3   2               4 3   2           4 2 2 2 2             3   3 2 2           2 2 4 2 2             2   4 2 2                 5 2 2           2 6 2 2           4 3   2 2             3 2     2 2            2 2   2   2 2              2 2 2   2 2           3   3   2 2                  3   2 2             2 4   2 2           2   4   2 2           2 2 2 2 2 2              2 3 2 2 2           3       2 2 2                  2   2 2 2           4 2 2 2 2              2   2 2 2 2           2 2 2 2 2 2           4   3 2 2              2 2 3 2 2            2 3 3 2 2            5     3 2             4 2 3 2             3 3 3 2              4     3 2            2 3     3 2              3       3 2               2 2   3 2           2   3   3 2            3 2 2 3 2                2   2 3 2              2     2 3 2            2       2 3 2            2   2 2 3 2              3 3 3 2            2     3 3 2           6 4 2              4   4 2             2 2 2 4 2            3 3 4 2           3 4 2   2             2 3 3   2          2   2 4   2               3 4   2         3   5   2              2 5   2           3 5     2             2 4       2          2   3 2     2               4 2     2          3 2 3     2               3 3     2           2   4 2   2               5 2   2          3 3   2   2               4   2   2           4 3       2              3 2 2     2           2 2   3     2             2 2 3     2           3   4     2                   4     2             2 5     2           2   5     2              3 3       2            2 2 2         2              2 3         2           3     2       2                  2 2       2           4 3       2             2   3       2           2 2 3       2            3   2 2     2                  3 2     2           4     2     2              2 2   2     2           2 3   2     2           5 2 2   2             4     2   2           2 3 2 2   2             3   2 2   2               2 3 2   2           2   4 2   2           2 3     2   2              3 2   2   2           3 2     2   2                2       2   2              2   2   2   2            2     2   2   2            2   3   2   2            4   2 2   2              2     2 2   2            2   2 2 2   2             3   2 2   2            2       2 2   2              5 3   2              4   3   2                3   3   2            2 2     3   2            2     2 3   2            3   2 3   2           4 4 2 2             3 3   2 2           2 2 2 2 2 2             2 3 2 2 2           3     3 2 2                 2 3 2 2         4 4 2 2             2   4 2 2           2 2 4 2 2          2 2 3   2 2             2 4   2 2           3   2     2 2                  3     2 2           4   2   2 2             2 2 2   2 2           2 3 2   2 2         4 2 2 2 2             2 3 2 2 2           2 4 2 2 2             4 2   2 2          2 3       2 2              3 2     2 2           3 2 2   2 2               2   2   2 2             2   3   2 2           2     3   2 2           2   4   2 2           3 2       2 2                2 2     2 2          4         2 2              2           2 2            2   2       2 2             3 2     2 2            2     2     2 2          5 2   2 2             3   2   2 2            2   2 2   2 2           2 4 2 2 2              4   2 2 2               3   2 2 2           2 2 2 2 2 2              2 2   2 2 2            2 2     2 2 2            2         2 2 2            3 2   2 2 2           2 2 2 2 2 2            3   2 2 2 2           2 3 2 3 2             3 3 3 2           3 2     3 2              2 2   3 2           4   2 3 2              2     2 3 2           2   2 2 3 2            3 3 3 2           2     3 3 2           4       3 2             2   2   3 2           2   3   3 2           5     3 2             3       3 2           2   2     3 2           3 3   3 2               3     3 2              2 2     3 2           2 2       3 2           2     2   3 2           3 3   3 2             3       3 2            2           3 2           2 2       3 2            3         3 2            2 3 2 3 2            3     2 3 2           4 2 4 2             2 2   4 2           2 2 2 4 2             3     4 2           2         4 2           2 2 2 4 2           3   2 4 2             4   4 2            2 2     4 2            3 2   4 2            2   2   4 2            3       4 2            3       4 2           2 2   5 2            3     5 2            3     5 2           4 6 2           3 5     2             2 4 2   2          2   3 3   2               4 3   2         3 2 4   2              3 4   2            2 5     2           2   4       2               5       2          3 3 2     2               4 2     2          3 4 2   2               5 2   2           4 4     2             3 3       2           2 2 2 2     2             2 3 2     2           3     3     2                 2 3     2          4 4     2             2   4     2           2 2 4     2           2 2 3       2              2 4       2           3   2         2                  3         2           4   2       2              2 2 2       2           2 3 2       2           4 2 2     2              2 3 2     2            2 4 2     2              4 2 2   2           2 3     2   2             3 2   2   2           3 2 2 2   2                2   2 2   2             2   3 2   2            2     3 2   2           2   4 2   2           3 2     2   2                2 2   2   2           4       2   2              2         2   2            2   2     2   2             3 2   2   2            2     2   2   2           5 2 2   2              3   2 2   2            2   2 2 2   2            2 4 3   2              4   3   2                3   3   2            2 2 2 3   2              2 2   3   2            2 2     3   2            2         3   2             3 2   3   2            2 2 2 3   2            3   2 3   2             3 4     2           2 2 3       2            2 4       2          3   2 2     2                 3 2     2          4   3     2            2 2 3     2           2 3 3     2           3   3       2                  4       2           4 2         2             2 3         2           2 4         2           2 3 2       2             3 3       2            3 2           2                2 2         2           4   2       2              2     2       2            2   2 2       2             3 3       2          2     3       2            4             2              2   2         2            2   3         2           5           2              3             2            2   2           2           3 3 2     2                3   2     2              2 2   2     2            2 2     2     2            2     2 2     2           3 3 2     2              3     2     2             2         2     2            2 2     2     2            3       2     2            2 3 3     2             3     3     2          3 2 2 2   2               2 3 2   2           4       2   2              2   2   2   2           2   3   2   2          5 2 2   2             3   2 2   2            2   2 2 2   2          5     2   2             3 2   2   2           2   3   2   2           4 2   2   2              2 2     2   2            2 2 2   2   2              3       2   2            2           2   2            2 2 2   2   2           3   2   2   2              4     2   2            2 2       2   2            3 2     2   2            2   2 2 2   2            3     2 2   2            3     2 2   2           5   3   2              3     3   2           2     2 3   2             4   3   2           2 2     3   2            3 2   3   2            2 2     3   2            3       3   2            3       3   2           2 3 4   2            3     4   2            4   4   2         2 2 4 2 2            2 5 2 2          3   3   2 2                 4   2 2          4 2 2 2 2             2 3 2 2 2           2 4 2 2 2          4 3   2 2             2 4   2 2           2 5   2 2           3 2 2   2 2               2 3   2 2           4         2 2              2   2     2 2           2   3     2 2          5 2   2 2              3   2   2 2            2   2 2   2 2           5       2 2              3 2     2 2            2   3     2 2           4 2 2 2 2              2 2   2 2 2           2 2 2 2 2 2             3     2 2 2            2         2 2 2           2 2 2 2 2 2            3   2 2 2 2              4   2 2 2            2 2     2 2 2            3 2   2 2 2            2   2 3 2 2            3     3 2 2            3     3 2 2           4   2   2 2              2   3   2 2            2   4   2 2          5       2 2             3 2     2 2           2   3     2 2           5       2 2              3         2 2            2     2     2 2              4       2 2            2 2         2 2            3 2       2 2            2 2   2   2 2            3     2   2 2            3     2   2 2          6 2 2 2             4   2 2 2           2 2 2 2 2 2            3 3 2 2 2            2 3   2 2 2            3       2 2 2             4 2 2 2 2          5 2 3 2             3 3 3 2           2   4 3 2          6   3 2             4     3 2            2 2 2   3 2            3 3   3 2            2 3 2 3 2            3     2 3 2            4 3 3 2          3 6 3             2 5   3          2   4 2 3              5 2 3         3 3 3 3              4 3 3          2   5   3               6   3          3 4     3               5     3             3 4   3            2 2 3     3           3   2 2   3                 3 2   3          4   3   3             2 2 3   3           2 3 3   3           3   3     3                  4     3           4 2       3              2 3       3            2 4       3            2 3 2 2 3              3 3 2 3            3 2     2 3                2 2   2 3           4   2 2 3             2     2 2 3            2   2 2 2 3             3 3 2 3           2     3 2 3            4       2 3              2   2   2 3            2   3   2 3            5     2 3              3       2 3            2   2     2 3            3 3 3 3                3   3 3               2 2   3 3            2 2     3 3             2     2 3 3            3 3 3 3              3     3 3             2         3 3            2 2     3 3             3       3 3            2 3 4 3             3     4 3          2 2 4   3          3   3     3                 4     3          4 2 2   3             2 3 2   3           2 4 2   3          4 3     3             2 4     3            2 5     3           3 2 2     3           4           3              2   2       3            2   3       3          5 2     3             3   2     3           2   2 2     3           5         3              3 2       3            2   3       3            4 2 2   3              2 2   2   3            2 2 2 2   3              3     2   3            2         2   3            2 2 2 2   3             3   2 2   3              4   2   3            2 2     2   3            3 2   2   3            2   2 3   3             3     3   3             3     3   3          4   2 2 3             2   3 2 3            2   4 2 3           5     2 3              3 2   2 3            2   3   2 3            2     2   2 3            2 2       2 3             3 2     2 3            2 2   2 2 3            3     2 2 3            3     2 2 3          6 3 3             4   3 3            2 2 2 3 3            3 3 3 3            2 3   3 3            3       3 3            4 2 3 3          3   4   3                 5   3          4 3     3             2 4     3            2 5     3           4   2     3              2   3     3            2   4     3           5         3              3 2       3            2   3       3            5   2   3              3     2   3            2     2 2   3              4   2   3            2 2     2   3            3 2   2   3            2 2   3   3             3     3   3             3     3   3          5 2     3             3 3     3            2   4     3           6       3              4         3            2 2 2       3            3 3       3            2 3 2     3             3     2     3             4 3     3          4 4 4             2 5 4           2 6 4           5 2   4              3 3   4            2   4   4           6 2 4              4   2 4             2 2 2 2 4            3 3 2 4            2 3 3 4             3     3 4             4 4 4
o30 = 13824c d*e f g  - 13824b*c*e f g  + 13824a*e f g  - 110592c d e f g  + 110592b*c*d*e f g  + 13824b e f g  - 165888a*d*e f g  + 221184c d f g  - 221184b*c*d e*f g  - 110592b d*e f g  + 663552a*d e f g  + 221184b d f g  - 884736a*d f g  - 13824c e f g  + 497664c d*e*f g  - 414720b*c e f g  + 497664a*c*e f g  - 995328b*c d*f g  + 1327104b c*e*f g  - 1990656a*c*d*e*f g  - 995328a*b*e f g  - 884736b f g  + 3981312a*b*d*f g  - 373248c f g  + 2985984a*c f g  - 5971968a f g  - 13824c d*e f g*h + 13824b*c*e f g*h - 13824a*e f g*h + 110592c d e f g*h - 110592b*c*d*e f g*h - 13824b e f g*h + 165888a*d*e f g*h - 221184c d e*f g*h + 221184b*c*d e f g*h + 110592b d*e f g*h - 663552a*d e f g*h - 221184b d e*f g*h + 884736a*d e*f g*h + 13824c e f g h - 635904c d*e f g h + 566784b*c e f g h - 663552a*c*e f g h - 331776c d f g h + 1714176b*c d*e*f g h - 1935360b c*e f g h + 2322432a*c*d*e f g h + 1492992a*b*e f g h - 221184b c*d*f g h + 1327104a*c*d f g h + 1327104b e*f g h - 5971968a*b*d*e*f g h + 497664c e*f g h + 497664b*c f g h - 4976640a*c e*f g h - 1990656a*b*c*f g h + 11943936a e*f g h + 13824c d e f h  - 13824b*c*d*e f h  + 13824a*d*e f h  - 110592c d e f h  + 110592b*c*d e f h  + 13824b d*e f h  - 165888a*d e f h  + 221184c d f h  - 221184b*c*d e*f h  - 110592b d e f h  + 663552a*d e f h  + 221184b d f h  - 884736a*d f h  + 110592c d*e f g*h  - 138240b*c e f g*h  + 152064a*c*e f g*h  + 884736c d e*f g*h  - 1161216b*c d*e f g*h  + 566784b c*e f g*h  + 276480a*c*d*e f g*h  - 470016a*b*e f g*h  - 1105920b*c d f g*h  + 1714176b c*d*e*f g*h  - 3538944a*c*d e*f g*h  - 414720b e f g*h  + 774144a*b*d*e f g*h  - 995328b d*f g*h  + 4423680a*b*d f g*h  - 110592c e f g h  - 331776c d*f g h  - 718848b*c e*f g h  + 2239488a*c e f g h  - 27648b c f g h  + 3317760a*c d*f g h  + 2654208a*b*c*e*f g h  - 6967296a e f g h  + 331776a*b f g h  - 7962624a d*f g h  - 110592c d e f h  + 110592b*c d*e f h  + 13824b c*e f h  - 138240a*c*d*e f h  - 13824a*b*e f h  - 442368c d f h  + 884736b*c d e*f h  - 635904b c*d*e f h  + 110592a*c*d e f h  - 13824b e f h  + 608256a*b*d*e f h  - 331776b c*d f h  + 1769472a*c*d f h  + 497664b d*e*f h  - 2211840a*b*d e*f h  - 221184c d*e*f g*h  + 442368b*c e f g*h  - 552960a*c e f g*h  + 1105920b*c d*f g*h  - 718848b c e*f g*h  - 1105920a*c d*e*f g*h  - 55296a*b*c*e f g*h  + 995328a e f g*h  + 497664b c*f g*h  - 4423680a*b*c*d*f g*h  - 331776a*b e*f g*h  + 7962624a d*e*f g*h  + 221184c f g h  - 1880064a*c f g h  + 3981312a c*f g h  + 221184c d f h  - 221184b*c d*e*f h  - 110592b c e f h  + 442368a*c d*e f h  + 110592a*b*c*e f h  + 13824a e f h  - 331776b c d*f h  - 442368a*c d f h  + 497664b c*e*f h  + 221184a*b*c*d*e*f h  - 414720a*b e f h  - 1105920a d*e f h  - 373248b f h  + 1990656a*b d*f h  - 1769472a d f h  - 442368b*c f g*h  + 663552a*c e*f g*h  + 2433024a*b*c f g*h  - 2654208a c*e*f g*h  - 2654208a b*f g*h  + 221184b c f h  - 442368a*c d*f h  - 221184a*b*c e*f h  - 110592a c*e f h  - 995328a*b c*f h  + 1769472a c*d*f h  + 1327104a b*e*f h  + 221184a c f h  - 884736a f h  + 13824c d*e f*g*i - 13824b*c*e f*g*i + 13824a*e f*g*i - 138240c d e f g*i + 138240b*c*d*e f g*i + 13824b e f g*i - 193536a*d*e f g*i + 442368c d e f g*i - 442368b*c*d e f g*i - 138240b d*e f g*i + 995328a*d e f g*i - 442368c d f g*i + 442368b*c*d e*f g*i + 442368b d e f g*i - 2211840a*d e f g*i - 442368b d f g*i + 1769472a*d f g*i - 13824c e f*g i + 566784c d*e f g i - 456192b*c e f g i + 539136a*c*e f g i - 718848c d e*f g i - 691200b*c d*e f g i + 1603584b c*e f g i - 2820096a*c*d*e f g i - 1244160a*b*e f g i + 2101248b*c d f g i - 2433024b c*d*e*f g i + 2654208a*c*d e*f g i - 1105920b e f g i + 6967296a*b*d*e f g i + 1769472b d*f g i - 7962624a*b*d f g i - 414720c e f g i + 497664c d*f g i + 165888b*c e*f g i + 3234816a*c e f g i - 663552b c f g i - 4976640a*c d*f g i + 1990656a*b*c*e*f g i - 8957952a e f g i + 11943936a d*f g i - 13824c d e f*h*i + 13824b*c*d*e f*h*i - 13824a*d*e f*h*i + 110592c d e f h*i - 110592b*c*d e f h*i - 13824b d*e f h*i + 165888a*d e f h*i - 221184c d e*f h*i + 221184b*c*d e f h*i + 110592b d e f h*i - 663552a*d e f h*i - 221184b d e*f h*i + 884736a*d e*f h*i - 110592c d*e f*g*h*i + 138240b*c e f*g*h*i - 152064a*c*e f*g*h*i - 1161216c d e f g*h*i + 1631232b*c d*e f g*h*i - 774144b c*e f g*h*i - 552960a*c*d*e f g*h*i + 691200a*b*e f g*h*i + 1105920c d f g*h*i - 774144b*c d e*f g*h*i - 1105920b c*d*e f g*h*i + 5750784a*c*d e f g*h*i + 608256b e f g*h*i - 2543616a*b*d*e f g*h*i + 884736b c*d f g*h*i - 4423680a*c*d f g*h*i + 221184b d*e*f g*h*i - 884736a*b*d e*f g*h*i + 110592c e f*g h*i + 1714176c d*e*f g h*i - 691200b*c e f g h*i - 870912a*c e f g h*i - 3594240b*c d*f g h*i + 4368384b c e*f g h*i - 6137856a*c d*e*f g h*i - 7299072a*b*c*e f g h*i + 9455616a e f g h*i - 2211840b c*f g h*i + 13934592a*b*c*d*f g h*i - 663552a*b e*f g h*i - 1990656a d*e*f g h*i - 995328c f g h*i + 8460288a*c f g h*i - 17915904a c*f g h*i + 110592c d e f*h i - 110592b*c d*e f*h i - 13824b c*e f*h i + 138240a*c*d*e f*h i + 13824a*b*e f*h i + 884736c d e*f h i - 1492992b*c d e f h i + 787968b c*d*e f h i + 387072a*c*d e f h i + 13824b e f h i - 774144a*b*d*e f h i - 221184b*c d f h i + 1050624b c*d e*f h i - 3760128a*c*d e*f h i - 635904b d*e f h i + 2543616a*b*d e f h i - 331776b d f h i + 1327104a*b*d f h i + 221184c d*e f*g*h i - 442368b*c e f*g*h i + 552960a*c e f*g*h i - 1105920c d f g*h i - 774144b*c d*e*f g*h i + 1078272b c e f g*h i + 663552a*c d*e f g*h i - 27648a*b*c*e f g*h i - 1575936a e f g*h i + 1050624b c d*f g*h i + 3760128a*c d f g*h i - 3262464b c*e*f g*h i + 8736768a*b*c*d*e*f g*h i + 3179520a*b e f g*h i - 12275712a d*e f g*h i + 1990656b f g*h i - 9400320a*b d*f g*h i + 2654208a d f g*h i - 221184c e*f*g h i + 2101248b*c f g h i - 1161216a*c e*f g h i - 11778048a*b*c f g h i + 7962624a c*e*f g h i + 13934592a b*f g h i - 221184c d e*f*h i + 221184b*c d*e f*h i + 110592b c e f*h i - 442368a*c d*e f*h i - 110592a*b*c*e f*h i - 13824a e f*h i - 221184b*c d f h i + 1050624b c d*e*f h i - 221184a*c d e*f h i - 635904b c*e f h i - 1105920a*b*c*d*e f h i + 566784a*b e f h i + 1603584a d*e f h i - 165888b c*d*f h i + 221184a*b*c*d f h i + 497664b e*f h i - 3262464a*b d*e*f h i + 5750784a d e*f h i + 442368b*c e*f*g*h i - 663552a*c e f*g*h i - 774144b c f g*h i + 2654208a*c d*f g*h i - 2985984a*b*c e*f g*h i + 4810752a c*e f g*h i + 5031936a*b c*f g*h i - 10616832a c*d*f g*h i - 3317760a b*e*f g*h i - 221184b c e*f*h i + 442368a*c d*e*f*h i + 221184a*b*c e f*h i + 110592a c*e f*h i - 331776b c f h i + 884736a*b*c d*f h i + 1714176a*b c*e*f h i - 2433024a c*d*e*f h i - 1935360a b*e f h i + 497664a*b f h i - 2211840a b*d*f h i - 1990656a c f g*h i + 7962624a f g*h i - 221184a c e*f*h i - 221184a b*c*f h i + 1327104a e*f h i + 13824c d e f*i  - 13824b*c*d e f*i  + 13824a*d e f*i  - 110592c d e f i  + 110592b*c*d e f i  + 13824b d e f i  - 165888a*d e f i  + 221184c d f i  - 221184b*c*d e*f i  - 110592b d e f i  + 663552a*d e f i  + 221184b d f i  - 884736a*d f i  - 13824c d*e g*i  + 13824b*c e g*i  - 13824a*c*e g*i  + 566784c d e f*g*i  - 774144b*c d*e f*g*i  + 165888b c*e f*g*i  + 691200a*c*d*e f*g*i  - 193536a*b*e f*g*i  - 718848c d e*f g*i  + 1078272b*c d e f g*i  + 387072b c*d*e f g*i  - 3373056a*c*d e f g*i  - 165888b e f g*i  + 940032a*b*d*e f g*i  - 774144b*c d f g*i  - 221184b c*d e*f g*i  + 3317760a*c*d e*f g*i  + 110592b d*e f g*i  - 1216512a*b*d e f g*i  - 442368b d f g*i  + 2211840a*b*d f g*i  + 13824c e g i  - 1935360c d*e f*g i  + 1603584b*c e f*g i  - 1575936a*c e f*g i  - 27648c d f g i  + 4368384b*c d*e*f g i  - 6303744b c e f g i  + 7713792a*c d*e f g i  + 6635520a*b*c*e f g i  - 2861568a e f g i  - 774144b c d*f g i  + 1658880a*c d f g i  + 5750784b c*e*f g i  - 21897216a*b*c*d*e*f g i  - 1658880a*b e f g i  + 3981312a d*e f g i  - 1769472b f g i  + 7962624a*b d*f g i  - 5971968a d f g i  + 1327104c e*f*g i  - 663552b*c f g i  - 10948608a*c e*f g i  + 4976640a*b*c f g i  + 23887872a c*e*f g i  - 11943936a b*f g i  + 13824c d e h*i  - 13824b*c d*e h*i  + 13824a*c*d*e h*i  - 635904c d e f*h*i  + 787968b*c d e f*h*i  - 110592b c*d*e f*h*i  - 774144a*c*d e f*h*i  + 138240a*b*d*e f*h*i  - 331776c d f h*i  + 1050624b*c d e*f h*i  - 1492992b c*d e f h*i  + 2543616a*c*d e f h*i  + 110592b d*e f h*i  + 387072a*b*d e f h*i  - 221184b c*d f h*i  + 1327104a*c*d f h*i  + 884736b d e*f h*i  - 3760128a*b*d e*f h*i  + 110592c d*e g*h*i  - 138240b*c e g*h*i  + 152064a*c e g*h*i  + 1714176c d e*f*g*h*i  - 1105920b*c d*e f*g*h*i  + 387072b c e f*g*h*i  - 27648a*c d*e f*g*h*i  - 552960a*b*c*e f*g*h*i  + 539136a e f*g*h*i  + 1050624b*c d f g*h*i  - 1658880b c d*e*f g*h*i  - 7962624a*c d e*f g*h*i  + 2543616b c*e f g*h*i  - 1990656a*b*c*d*e f g*h*i  - 3373056a*b e f g*h*i  + 6635520a d*e f g*h*i  + 221184b c*d*f g*h*i  - 2433024a*b*c*d f g*h*i  - 2211840b e*f g*h*i  + 10838016a*b d*e*f g*h*i  + 663552a d e*f g*h*i  - 110592c e g h*i  - 221184c d*f*g h*i  - 2433024b*c e*f*g h*i  + 4810752a*c e f*g h*i  - 774144b c f g h*i  - 1161216a*c d*f g h*i  + 19408896a*b*c e*f g h*i  - 25380864a c*e f g h*i  - 3317760a*b c*f g h*i  + 7962624a c*d*f g h*i  - 9953280a b*e*f g h*i  - 110592c d e h i  + 110592b*c d*e h i  + 13824b c e h i  - 138240a*c d*e h i  - 13824a*b*c*e h i  - 331776c d f*h i  + 1050624b*c d e*f*h i  - 1492992b c d*e f*h i  + 1078272a*c d e f*h i  + 110592b c*e f*h i  + 1631232a*b*c*d*e f*h i  - 138240a*b e f*h i  - 456192a d*e f*h i  - 912384b c d f h i  + 2211840a*c d f h i  + 1050624b c*d*e*f h i  - 1658880a*b*c*d e*f h i  - 110592b e f h i  + 1078272a*b d*e f h i  - 6303744a d e f h i  - 331776b d*f h i  + 2211840a*b d f h i  - 3317760a d f h i  - 221184c d*e*g*h i  + 442368b*c e g*h i  - 552960a*c e g*h i  + 884736b*c d*f*g*h i  - 221184b c e*f*g*h i  - 2985984a*c d*e*f*g*h i  + 663552a*b*c e f*g*h i  - 870912a c*e f*g*h i  + 2211840b c f g*h i  - 7630848a*b*c d*f g*h i  - 7962624a*b c*e*f g*h i  + 19408896a c*d*e*f g*h i  + 7713792a b*e f g*h i  - 2543616a*b f g*h i  + 8957952a b*d*f g*h i  + 221184c g h i  - 1990656a*c f*g h i  + 9704448a c f g h i  - 20901888a f g h i  + 221184c d h i  - 221184b*c d*e*h i  - 110592b c e h i  + 442368a*c d*e h i  + 110592a*b*c e h i  + 13824a c*e h i  - 221184b c d*f*h i  - 774144a*c d f*h i  + 884736b c e*f*h i  - 774144a*b*c d*e*f*h i  - 1161216a*b c*e f*h i  - 691200a c*d*e f*h i  + 566784a b*e f*h i  - 331776b c*f h i  + 1050624a*b c*d*f h i  - 774144a c*d f h i  - 718848a*b e*f h i  + 4368384a b*d*e*f h i  - 442368b*c g*h i  + 663552a*c e*g*h i  + 2654208a*b*c f*g*h i  - 1161216a c e*f*g*h i  - 1161216a b*c*f g*h i  - 10948608a e*f g*h i  + 221184b c h i  - 442368a*c d*h i  - 221184a*b*c e*h i  - 110592a c e h i  - 1105920a*b c f*h i  + 2101248a c d*f*h i  + 1714176a b*c*e*f*h i  - 414720a e f*h i  - 27648a b f h i  - 663552a d*f h i  + 221184a c h i  - 995328a c*f*h i  - 13824c d e i  + 13824b*c d e i  - 13824a*c*d e i  + 497664c d e*f*i  - 635904b*c d e f*i  + 110592b c*d e f*i  + 608256a*c*d e f*i  - 138240a*b*d e f*i  - 331776b*c d f i  + 884736b c*d e*f i  - 2211840a*c*d e*f i  - 110592b d e f i  + 110592a*b*d e f i  - 442368b d f i  + 1769472a*b*d f i  - 414720c d e g*i  + 608256b*c d*e g*i  - 165888b c e g*i  - 470016a*c d*e g*i  + 165888a*b*c*e g*i  + 13824a e g*i  + 497664c d f*g*i  - 3262464b*c d e*f*g*i  + 2543616b c d*e f*g*i  + 3179520a*c d e f*g*i  - 663552b c*e f*g*i  - 2543616a*b*c*d*e f*g*i  + 995328a*b e f*g*i  - 1244160a d*e f*g*i  + 2211840b c d f g*i  - 2543616a*c d f g*i  - 3760128b c*d*e*f g*i  + 10838016a*b*c*d e*f g*i  + 663552b e f g*i  - 1216512a*b d*e f g*i  - 1658880a d e f g*i  + 1769472b d*f g*i  - 8404992a*b d f g*i  + 1769472a d f g*i  + 1327104c d*e*g i  - 1105920b*c e g i  + 995328a*c e g i  - 2211840b*c d*f*g i  + 5750784b c e*f*g i  - 3317760a*c d*e*f*g i  - 12275712a*b*c e f*g i  + 9455616a c*e f*g i  - 3317760b c f g i  + 8957952a*b*c d*f g i  + 663552a*b c*e*f g i  - 9953280a c*d*e*f g i  + 3981312a b*e f g i  + 1769472a*b f g i  + 3981312a b*d*f g i  - 884736c g i  + 7962624a*c f*g i  - 20901888a c f g i  + 11943936a f g i  + 497664c d e*h*i  - 635904b*c d e h*i  + 110592b c d*e h*i  + 566784a*c d e h*i  - 110592a*b*c*d*e h*i  - 13824a d*e h*i  - 165888b*c d f*h*i  + 1050624b c d e*f*h*i  - 3262464a*c d e*f*h*i  + 221184b c*d*e f*h*i  - 1105920a*b*c*d e f*h*i  - 442368a*b d*e f*h*i  + 1603584a d e f*h*i  - 221184b c*d f h*i  + 221184a*b*c*d f h*i  - 221184b d*e*f h*i  - 221184a*b d e*f h*i  + 5750784a d e*f h*i  - 995328c d g*h*i  + 221184b*c d*e*g*h*i  + 110592b c e g*h*i  - 55296a*c d*e g*h*i  + 276480a*b*c e g*h*i  - 663552a c*e g*h*i  + 221184b c d*f*g*h*i  + 5031936a*c d f*g*h*i  - 3760128b c e*f*g*h*i  + 8736768a*b*c d*e*f*g*h*i  + 5750784a*b c*e f*g*h*i  - 7299072a c*d*e f*g*h*i  - 2820096a b*e f*g*h*i  + 1327104b c*f g*h*i  - 2433024a*b c*d*f g*h*i  - 3317760a c*d f g*h*i  + 3317760a*b e*f g*h*i  - 21897216a b*d*e*f g*h*i  + 1769472b*c g h*i  - 2654208a*c e*g h*i  - 10616832a*b*c f*g h*i  + 7962624a c e*f*g h*i  + 7962624a b*c*f g h*i  + 23887872a e*f g h*i  - 331776b*c d h i  + 884736b c d*e*h i  - 718848a*c d e*h i  - 110592b c e h i  - 1161216a*b*c d*e h i  + 110592a*b c*e h i  + 566784a c*d*e h i  + 13824a b*e h i  - 221184b c d*f*h i  + 1050624a*b*c d f*h i  - 221184b c*e*f*h i  - 774144a*b c*d*e*f*h i  + 4368384a c*d e*f*h i  + 442368a*b e f*h i  - 691200a b*d*e f*h i  + 221184b f h i  - 774144a*b d*f h i  - 774144a b*d f h i  - 442368b c g*h i  + 2433024a*c d*g*h i  - 1105920a*b*c e*g*h i  + 2239488a c e g*h i  + 3760128a*b c f*g*h i  - 11778048a c d*f*g*h i  - 6137856a b*c*e*f*g*h i  + 3234816a e f*g*h i  + 1658880a b f g*h i  + 4976640a d*f g*h i  - 442368b c h i  + 1105920a*b*c d*h i  + 884736a*b c e*h i  - 718848a c d*e*h i  - 635904a b*c*e h i  - 13824a e h i  + 1105920a*b c*f*h i  - 3594240a b*c*d*f*h i  - 718848a b e*f*h i  + 165888a d*e*f*h i  - 1880064a c g*h i  + 8460288a c*f*g*h i  - 331776a b*c h i  + 497664a c*e*h i  + 497664a b*f*h i  - 373248c d i  + 497664b*c d e*i  - 110592b c d e i  - 414720a*c d e i  + 110592a*b*c*d e i  + 13824a d e i  - 331776b c d f*i  + 1990656a*c d f*i  - 221184b c*d e*f*i  + 221184a*b*c*d e*f*i  + 442368a*b d e f*i  - 1105920a d e f*i  + 221184b d f i  - 442368a*b d f i  - 1769472a d f i  + 1990656b*c d g*i  - 2211840b c d*e*g*i  - 331776a*c d e*g*i  + 663552b c e g*i  + 774144a*b*c d*e g*i  - 663552a*b c*e g*i  + 1492992a c*d*e g*i  - 165888a b*e g*i  + 1327104b c d*f*g*i  - 9400320a*b*c d f*g*i  + 884736b c*e*f*g*i  - 884736a*b c*d*e*f*g*i  - 663552a c*d e*f*g*i  - 2211840a*b e f*g*i  + 6967296a b*d*e f*g*i  - 884736b f g*i  + 2211840a*b d*f g*i  + 7962624a b*d f g*i  - 1769472b c g i  - 2654208a*c d*g i  + 7962624a*b*c e*g i  - 6967296a c e g i  + 2654208a*b c f*g i  + 13934592a c d*f*g i  - 1990656a b*c*e*f*g i  - 8957952a e f*g i  - 5971968a b f g i  - 11943936a d*f g i  - 331776b c d h*i  + 497664a*c d h*i  - 221184b c d*e*h*i  + 1714176a*b*c d e*h*i  + 221184a*b c*d*e h*i  - 1935360a c*d e h*i  + 110592a b*d*e h*i  + 884736a*b c*d f*h*i  - 2211840a c*d f*h*i  + 442368a*b d*e*f*h*i  - 2433024a b*d e*f*h*i  + 1769472b c g*h*i  - 4423680a*b*c d*g*h*i  - 3538944a*b c e*g*h*i  + 2654208a c d*e*g*h*i  + 2322432a b*c*e g*h*i  + 497664a e g*h*i  - 4423680a*b c*f*g*h*i  + 13934592a b*c*d*f*g*h*i  + 2654208a b e*f*g*h*i  + 1990656a d*e*f*g*h*i  + 3981312a c g h*i  - 17915904a c*f*g h*i  + 221184b c h i  - 1105920a*b c d*h i  - 27648a c d h i  - 221184a*b c*e*h i  + 1714176a b*c*d*e*h i  - 110592a b e h i  - 414720a d*e h i  - 442368a*b f*h i  + 2101248a b d*f*h i  - 663552a d f*h i  + 3317760a b*c g*h i  - 4976640a c*e*g*h i  - 4976640a b*f*g*h i  - 331776a b c*h i  + 497664a c*d*h i  + 497664a b*e*h i  - 373248a h i  + 221184b c d i  - 995328a*b*c d i  - 221184a*b c*d e*i  + 1327104a c*d e*i  - 110592a b*d e i  - 442368a*b d f*i  + 1769472a b*d f*i  - 884736b c g*i  + 4423680a*b c d*g*i  + 331776a c d g*i  + 884736a*b c*e*g*i  - 5971968a b*c*d*e*g*i  + 663552a b e g*i  - 995328a d*e g*i  + 1769472a*b f*g*i  - 7962624a b d*f*g*i  - 7962624a b*c g i  + 11943936a c*e*g i  + 11943936a b*f*g i  - 221184a b*c*d h*i  - 221184a b d*e*h*i  + 1327104a d e*h*i  + 1327104a b c*g*h*i  - 1990656a c*d*g*h*i  - 1990656a b*e*g*h*i  + 221184a b h i  - 995328a b*d*h i  + 2985984a g*h i  + 221184a b d i  - 884736a d i  - 884736a b g*i  + 3981312a b*d*g*i  - 5971968a g i  - 13824c d*e g*j + 13824b*c*e g*j - 13824a*e g*j + 152064c d e f*g*j - 152064b*c*d*e f*g*j - 13824b e f*g*j + 207360a*d*e f*g*j - 552960c d e f g*j + 552960b*c*d e f g*j + 152064b d*e f g*j - 1161216a*d e f g*j + 663552c d e*f g*j - 663552b*c*d e f g*j - 552960b d e f g*j + 2875392a*d e f g*j + 663552b d e*f g*j - 2654208a*d e*f g*j + 13824c e g j - 663552c d*e f*g j + 539136b*c e f*g j - 622080a*c*e f*g j + 2239488c d e f g j - 870912b*c d*e f g j - 1575936b c*e f g j + 4727808a*c*d*e f g j + 1119744a*b*e f g j - 1880064c d f g j - 1161216b*c d e*f g j + 4810752b c*d*e f g j - 10948608a*c*d e f g j + 995328b e f g j - 7464960a*b*d*e f g j - 1990656b c*d f g j + 7962624a*c*d f g j - 2654208b d*e*f g j + 11943936a*b*d e*f g j + 497664c e f*g j - 4976640c d*e*f g j + 3234816b*c e f g j - 7091712a*c e f g j + 8460288b*c d*f g j - 10948608b c e*f g j + 25380864a*c d*e*f g j + 7464960a*b*c*e f g j + 7464960a e f g j + 7962624b c*f g j - 35831808a*b*c*d*f g j - 17915904a d*e*f g j + 2985984c f g j - 25380864a*c f g j + 53747712a c*f g j + 13824c d e h*j - 13824b*c*d*e h*j + 13824a*d*e h*j - 138240c d e f*h*j + 138240b*c*d e f*h*j + 13824b d*e f*h*j - 193536a*d e f*h*j + 442368c d e f h*j - 442368b*c*d e f h*j - 138240b d e f h*j + 995328a*d e f h*j - 442368c d f h*j + 442368b*c*d e*f h*j + 442368b d e f h*j - 2211840a*d e f h*j - 442368b d f h*j + 1769472a*d f h*j + 165888c d*e g*h*j - 193536b*c e g*h*j + 207360a*c*e g*h*j + 276480c d e f*g*h*j - 552960b*c d*e f*g*h*j + 691200b c*e f*g*h*j - 663552a*c*d*e f*g*h*j - 539136a*b*e f*g*h*j - 1105920c d e*f g*h*j + 663552b*c d e f g*h*j - 27648b c*d*e f g*h*j - 1658880a*c*d e f g*h*j - 470016b e f g*h*j + 2156544a*b*d*e f g*h*j + 2654208b*c d f g*h*j - 2985984b c*d e*f g*h*j + 3981312a*c*d e*f g*h*j - 55296b d*e f g*h*j + 2654208a*b*d e f g*h*j + 2433024b d f g*h*j - 10616832a*b*d f g*h*j - 165888c e g h*j + 2322432c d*e f*g h*j - 2820096b*c e f*g h*j + 4727808a*c e f*g h*j + 3317760c d f g h*j - 6137856b*c d*e*f g h*j + 7713792b c e f g h*j - 11197440a*c d*e f g h*j - 2737152a*b*c*e f g h*j - 7464960a e f g h*j - 1161216b c d*f g h*j - 16920576a*c d f g h*j - 3317760b c*e*f g h*j + 20901888a*b*c*d*e*f g h*j - 2488320a*b e f g h*j + 8957952a d*e f g h*j - 2654208b f g h*j + 11943936a*b d*f g h*j + 11943936a d f g h*j - 1990656c e*f*g h*j - 4976640b*c f g h*j + 25380864a*c e*f g h*j + 25380864a*b*c f g h*j - 71663616a c*e*f g h*j - 17915904a b*f g h*j - 165888c d e h j + 165888b*c d*e h j + 13824b c*e h j - 193536a*c*d*e h j - 13824a*b*e h j + 110592c d e f*h j + 387072b*c d e f*h j - 774144b c*d*e f*h j + 940032a*c*d e f*h j - 13824b e f*h j + 691200a*b*d*e f*h j - 442368c d f h j - 221184b*c d e*f h j + 1078272b c*d e f h j - 1216512a*c*d e f h j + 566784b d*e f h j - 3373056a*b*d e f h j - 774144b c*d f h j + 2211840a*c*d f h j - 718848b d e*f h j + 3317760a*b*d e*f h j - 663552c d*e g*h j + 995328b*c e g*h j - 1161216a*c e g*h j - 3538944c d e*f*g*h j + 5750784b*c d*e f*g*h j - 3373056b c e f*g*h j - 1658880a*c d*e f*g*h j + 2156544a*b*c*e f*g*h j + 1119744a e f*g*h j + 3760128b*c d f g*h j - 7962624b c d*e*f g*h j + 19906560a*c d e*f g*h j + 3179520b c*e f g*h j - 9455616a*b*c*d*e f g*h j - 1119744a*b e f g*h j + 8460288a d*e f g*h j + 5031936b c*d*f g*h j - 17252352a*b*c*d f g*h j - 331776b e*f g*h j + 2156544a*b d*e*f g*h j - 15925248a d e*f g*h j + 663552c e g h j + 1327104c d*f*g h j + 2654208b*c e*f*g h j - 10948608a*c e f*g h j + 1658880b c f g h j - 16920576a*c d*f g h j - 11943936a*b*c e*f g h j + 34338816a c*e f g h j - 8460288a*b c*f g h j + 47775744a c*d*f g h j + 5971968a b*e*f g h j + 663552c d e h j - 663552b*c d*e h j - 165888b c e h j + 995328a*c d*e h j + 165888a*b*c*e h j + 13824a e h j + 1769472c d f*h j - 3760128b*c d e*f*h j + 2543616b c d*e f*h j - 1216512a*c d e f*h j + 608256b c*e f*h j - 2543616a*b*c*d*e f*h j - 470016a*b e f*h j - 1244160a d*e f*h j + 2211840b c d f h j - 8404992a*c d f h j - 3262464b c*d*e*f h j + 10838016a*b*c*d e*f h j - 414720b e f h j + 3179520a*b d*e f h j - 1658880a d e f h j + 497664b d*f h j - 2543616a*b d f h j + 1769472a d f h j + 884736c d*e*g*h j - 2211840b*c e g*h j + 2875392a*c e g*h j - 4423680b*c d*f*g*h j + 3317760b c e*f*g*h j + 3981312a*c d*e*f*g*h j + 2654208a*b*c e f*g*h j - 7464960a c*e f*g*h j - 2543616b c f g*h j + 17915904a*b*c d*f g*h j + 2156544a*b c*e*f g*h j - 35831808a c*d*e*f g*h j - 2488320a b*e f g*h j - 829440a*b f g*h j + 7962624a b*d*f g*h j - 884736c g h j + 7962624a*c f*g h j - 14929920a c f g h j - 11943936a f g h j - 884736c d h j + 884736b*c d*e*h j + 663552b c e h j - 2211840a*c d*e h j - 663552a*b*c e h j - 165888a c*e h j + 1327104b c d*f*h j + 2211840a*c d f*h j - 2211840b c e*f*h j - 884736a*b*c d*e*f*h j + 774144a*b c*e f*h j + 6967296a c*d*e f*h j + 1492992a b*e f*h j + 1990656b c*f h j - 9400320a*b c*d*f h j + 7962624a c*d f h j - 331776a*b e*f h j - 663552a b*d*e*f h j + 1769472b*c g*h j - 2654208a*c e*g*h j - 10616832a*b*c f*g*h j + 11943936a c e*f*g*h j + 11943936a b*c*f g*h j - 884736b c h j + 1769472a*c d*h j + 884736a*b*c e*h j + 663552a c e h j + 4423680a*b c f*h j - 7962624a c d*f*h j - 5971968a b*c*e*f*h j - 995328a e f*h j + 331776a b f h j - 884736a c h j + 3981312a c*f*h j - 13824c d e i*j + 13824b*c*d e i*j - 13824a*d e i*j + 110592c d e f*i*j - 110592b*c*d e f*i*j - 13824b d e f*i*j + 165888a*d e f*i*j - 221184c d e*f i*j + 221184b*c*d e f i*j + 110592b d e f i*j - 663552a*d e f i*j - 221184b d e*f i*j + 884736a*d e*f i*j - 470016c d e g*i*j + 691200b*c d*e g*i*j - 193536b c*e g*i*j - 539136a*c*d*e g*i*j + 207360a*b*e g*i*j - 55296c d e f*g*i*j - 27648b*c d e f*g*i*j - 552960b c*d*e f*g*i*j + 2156544a*c*d e f*g*i*j + 165888b e f*g*i*j - 663552a*b*d*e f*g*i*j + 2433024c d f g*i*j - 2985984b*c d e*f g*i*j + 663552b c*d e f g*i*j + 2654208a*c*d e f g*i*j + 276480b d*e f g*i*j - 1658880a*b*d e f g*i*j + 2654208b c*d f g*i*j - 10616832a*c*d f g*i*j - 1105920b d e*f g*i*j + 3981312a*b*d e*f g*i*j + 1492992c d*e g i*j - 1244160b*c e g i*j + 1119744a*c e g i*j + 2654208c d e*f*g i*j - 7299072b*c d*e f*g i*j + 6635520b c e f*g i*j - 2737152a*c d*e f*g i*j - 8460288a*b*c*e f*g i*j + 4105728a e f*g i*j - 11778048b*c d f g i*j + 19408896b c d*e*f g i*j - 11943936a*c d e*f g i*j - 12275712b c*e f g i*j + 16422912a*b*c*d*e f g i*j + 8460288a*b e f g i*j - 8957952a d*e f g i*j - 10616832b c*d*f g i*j + 47775744a*b*c*d f g i*j + 7962624b e*f g i*j - 35831808a*b d*e*f g i*j + 5971968a d e*f g i*j - 995328c e g i*j - 1990656c d*f*g i*j + 1990656b*c e*f*g i*j + 7464960a*c e f*g i*j + 4976640b c f g i*j + 25380864a*c d*f g i*j - 40310784a*b*c e*f g i*j + 4478976a c*e f g i*j - 71663616a c*d*f g i*j + 53747712a b*e*f g i*j + 608256c d e h*i*j - 774144b*c d e h*i*j + 138240b c*d*e h*i*j + 691200a*c*d e h*i*j - 152064a*b*d*e h*i*j + 221184c d e*f*h*i*j - 1105920b*c d e f*h*i*j + 1631232b c*d e f*h*i*j - 2543616a*c*d e f*h*i*j - 110592b d*e f*h*i*j - 552960a*b*d e f*h*i*j + 884736b*c d f h*i*j - 774144b c*d e*f h*i*j - 884736a*c*d e*f h*i*j - 1161216b d e f h*i*j + 5750784a*b*d e f h*i*j + 1105920b d f h*i*j - 4423680a*b*d f h*i*j + 774144c d e g*h*i*j - 2543616b*c d*e g*h*i*j + 940032b c e g*h*i*j + 2156544a*c d*e g*h*i*j - 663552a*b*c*e g*h*i*j - 622080a e g*h*i*j - 4423680c d f*g*h*i*j + 8736768b*c d e*f*g*h*i*j - 1990656b c d*e f*g*h*i*j - 9455616a*c d e f*g*h*i*j - 2543616b c*e f*g*h*i*j + 13934592a*b*c*d*e f*g*h*i*j + 2156544a*b e f*g*h*i*j - 8460288a d*e f*g*h*i*j - 7630848b c d f g*h*i*j + 17915904a*c d f g*h*i*j + 8736768b c*d*e*f g*h*i*j - 23887872a*b*c*d e*f g*h*i*j + 774144b e f g*h*i*j - 9455616a*b d*e f g*h*i*j + 5971968a d e f g*h*i*j - 4423680b d*f g*h*i*j + 17915904a*b d f g*h*i*j + 7962624a d f g*h*i*j - 5971968c d*e*g h*i*j + 6967296b*c e g h*i*j - 7464960a*c e g h*i*j + 13934592b*c d*f*g h*i*j - 21897216b c e*f*g h*i*j + 20901888a*c d*e*f*g h*i*j + 16422912a*b*c e f*g h*i*j - 746496a c*e f*g h*i*j + 8957952b c f g h*i*j - 43296768a*b*c d*f g h*i*j + 14929920a*b c*e*f g h*i*j + 20901888a c*d*e*f g h*i*j - 14929920a b*e f g h*i*j + 7962624a*b f g h*i*j - 65691648a b*d*f g h*i*j + 3981312c g h*i*j - 35831808a*c f*g h*i*j + 67184640a c f g h*i*j + 53747712a f g h*i*j - 2211840c d e*h i*j + 2543616b*c d e h i*j + 387072b c d*e h i*j - 3373056a*c d e h i*j - 138240b c*e h i*j - 552960a*b*c*d*e h i*j + 152064a*b e h i*j + 539136a d*e h i*j + 221184b*c d f*h i*j - 1658880b c d e*f*h i*j + 10838016a*c d e*f*h i*j - 1105920b c*d*e f*h i*j - 1990656a*b*c*d e f*h i*j + 110592b e f*h i*j - 27648a*b d*e f*h i*j + 6635520a d e f*h i*j + 1050624b c*d f h i*j - 2433024a*b*c*d f h i*j + 1714176b d*e*f h i*j - 7962624a*b d e*f h i*j + 663552a d e*f h i*j + 4423680c d g*h i*j - 884736b*c d*e*g*h i*j - 1216512b c e g*h i*j + 2654208a*c d*e g*h i*j - 1658880a*b*c e g*h i*j + 4727808a c*e g*h i*j - 2433024b c d*f*g*h i*j - 17252352a*c d f*g*h i*j + 10838016b c e*f*g*h i*j - 23887872a*b*c d*e*f*g*h i*j - 9455616a*b c*e f*g*h i*j + 16422912a c*d*e f*g*h i*j - 2737152a b*e f*g*h i*j - 9400320b c*f g*h i*j + 36329472a*b c*d*f g*h i*j - 11943936a c*d f g*h i*j + 2156544a*b e*f g*h i*j + 14929920a b*d*e*f g*h i*j - 7962624b*c g h i*j + 11943936a*c e*g h i*j + 47775744a*b*c f*g h i*j - 56733696a c e*f*g h i*j - 56733696a b*c*f g h i*j + 17915904a e*f g h i*j + 1327104b*c d h i*j - 3760128b c d*e*h i*j + 3317760a*c d e*h i*j + 110592b c e h i*j + 5750784a*b*c d*e h i*j + 276480a*b c*e h i*j - 2820096a c*d*e h i*j - 663552a b*e h i*j + 221184b c d*f*h i*j - 2433024a*b*c d f*h i*j + 221184b c*e*f*h i*j + 8736768a*b c*d*e*f*h i*j - 21897216a c*d e*f*h i*j - 55296a*b e f*h i*j - 7299072a b*d*e f*h i*j - 995328b f h i*j + 5031936a*b d*f h i*j - 3317760a b*d f h i*j + 2211840b c g*h i*j - 10616832a*c d*g*h i*j + 3981312a*b*c e*g*h i*j - 10948608a c e g*h i*j - 17252352a*b c f*g*h i*j + 47775744a c d*f*g*h i*j + 20901888a b*c*e*f*g*h i*j + 7464960a e f*g*h i*j - 8460288a b f g*h i*j + 1769472b c h i*j - 4423680a*b*c d*h i*j - 3538944a*b c e*h i*j + 2654208a c d*e*h i*j + 2322432a b*c*e h i*j + 497664a e h i*j - 4423680a*b c*f*h i*j + 13934592a b*c*d*f*h i*j + 2654208a b e*f*h i*j + 1990656a d*e*f*h i*j + 7962624a c g*h i*j - 35831808a c*f*g*h i*j + 1327104a b*c h i*j - 1990656a c*e*h i*j - 1990656a b*f*h i*j - 414720c d e i j + 566784b*c d e i j - 138240b c*d e i j - 470016a*c*d e i j + 152064a*b*d e i j - 995328c d f*i j + 1714176b*c d e*f*i j - 1161216b c*d e f*i j + 774144a*c*d e f*i j + 110592b d e f*i j + 276480a*b*d e f*i j - 1105920b c*d f i j + 4423680a*c*d f i j + 884736b d e*f i j - 3538944a*b*d e*f i j - 331776c d e*g*i j + 3179520b*c d e g*i j - 3373056b c d*e g*i j - 1119744a*c d e g*i j + 995328b c*e g*i j + 2156544a*b*c*d*e g*i j - 1161216a*b e g*i j + 1119744a d*e g*i j + 5031936b*c d f*g*i j - 7962624b c d e*f*g*i j + 2156544a*c d e*f*g*i j + 5750784b c*d*e f*g*i j - 9455616a*b*c*d e f*g*i j - 663552b e f*g*i j - 1658880a*b d*e f*g*i j + 8460288a d e f*g*i j + 3760128b c*d f g*i j - 17252352a*b*c*d f g*i j - 3538944b d*e*f g*i j + 19906560a*b d e*f g*i j - 15925248a d e*f g*i j + 331776c d g i j - 663552b*c d*e*g i j - 1658880b c e g i j - 2488320a*c d*e g i j + 8460288a*b*c e g i j - 7464960a c*e g i j - 3317760b c d*f*g i j - 8460288a*c d f*g i j + 663552b c e*f*g i j + 14929920a*b*c d*e*f*g i j + 5971968a*b c*e f*g i j - 14929920a c*d*e f*g i j - 8957952a b*e f*g i j + 2654208b c*f g i j - 11943936a*b c*d*f g i j + 29859840a c*d f g i j - 15925248a*b e*f g i j + 47775744a b*d*e*f g i j + 17915904a c e*f*g i j + 17915904a b*c*f g i j - 107495424a e*f g i j + 1990656c d h*i j - 3262464b*c d e*h*i j + 1078272b c d e h*i j + 3179520a*c d e h*i j - 442368b c*d*e h*i j - 27648a*b*c*d e h*i j + 552960a*b d*e h*i j - 1575936a d e h*i j + 1050624b c d f*h*i j - 9400320a*c d f*h*i j - 774144b c*d e*f*h*i j + 8736768a*b*c*d e*f*h*i j + 221184b d*e f*h*i j + 663552a*b d e f*h*i j - 12275712a d e f*h*i j - 1105920b d f h*i j + 3760128a*b d f h*i j + 2654208a d f h*i j - 9400320b*c d g*h*i j + 10838016b c d*e*g*h*i j + 2156544a*c d e*g*h*i j - 1216512b c e g*h*i j - 9455616a*b*c d*e g*h*i j - 1658880a*b c*e g*h*i j - 2737152a c*d*e g*h*i j + 4727808a b*e g*h*i j - 2433024b c d*f*g*h*i j + 36329472a*b*c d f*g*h*i j - 884736b c*e*f*g*h*i j - 23887872a*b c*d*e*f*g*h*i j + 14929920a c*d e*f*g*h*i j + 2654208a*b e f*g*h*i j + 16422912a b*d*e f*g*h*i j + 4423680b f g*h*i j - 17252352a*b d*f g*h*i j - 11943936a b*d f g*h*i j + 7962624b c g h*i j + 11943936a*c d*g h*i j - 35831808a*b*c e*g h*i j + 34338816a c e g h*i j - 11943936a*b c f*g h*i j - 56733696a c d*f*g h*i j + 20901888a b*c*e*f*g h*i j + 4478976a e f*g h*i j + 29859840a b f g h*i j + 17915904a d*f g h*i j + 2211840b c d h i j - 2543616a*c d h i j - 221184b c d*e*h i j - 7962624a*b*c d e*h i j + 442368b c*e h i j + 663552a*b c*d*e h i j + 7713792a c*d e h i j - 552960a*b e h i j - 870912a b*d*e h i j + 884736b c*d*f*h i j - 7630848a*b c*d f*h i j + 8957952a c*d f*h i j - 221184b e*f*h i j - 2985984a*b d*e*f*h i j + 19408896a b*d e*f*h i j - 8404992b c g*h i j + 17915904a*b*c d*g*h i j + 19906560a*b c e*g*h i j - 11943936a c d*e*g*h i j - 11197440a b*c*e g*h i j - 7091712a e g*h i j + 17915904a*b c*f*g*h i j - 43296768a b*c*d*f*g*h i j - 11943936a b e*f*g*h i j - 40310784a d*e*f*g*h i j - 14929920a c g h i j + 67184640a c*f*g h i j - 442368b c h i j + 3760128a*b c d*h i j + 1658880a c d h i j - 1105920a*b c*e*h i j - 6137856a b*c*d*e*h i j + 2239488a b e h i j + 3234816a d*e h i j + 2433024a*b f*h i j - 11778048a b d*f*h i j + 4976640a d f*h i j - 16920576a b*c g*h i j + 25380864a c*e*g*h i j + 25380864a b*f*g*h i j + 3317760a b c*h i j - 4976640a c*d*h i j - 4976640a b*e*h i j + 2985984a h i j + 497664b*c d i j - 718848b c d e*i j - 331776a*c d e*i j + 442368b c*d e i j - 55296a*b*c*d e i j - 552960a*b d e i j + 995328a d e i j + 1105920b c*d f*i j - 4423680a*b*c*d f*i j - 221184b d e*f*i j - 1105920a*b d e*f*i j + 7962624a d e*f*i j - 2543616b c d g*i j - 829440a*c d g*i j + 3317760b c d*e*g*i j + 2156544a*b*c d e*g*i j - 2211840b c*e g*i j + 2654208a*b c*d*e g*i j - 2488320a c*d e g*i j + 2875392a*b e g*i j - 7464960a b*d*e g*i j - 4423680b c*d*f*g*i j + 17915904a*b c*d f*g*i j + 7962624a c*d f*g*i j + 884736b e*f*g*i j + 3981312a*b d*e*f*g*i j - 35831808a b*d e*f*g*i j + 1769472b c g i j + 7962624a*b*c d*g i j - 15925248a*b c e*g i j + 5971968a c d*e*g i j + 8957952a b*c*e g i j + 7464960a e g i j + 7962624a*b c*f*g i j - 65691648a b*c*d*f*g i j + 5971968a b e*f*g i j + 53747712a d*e*f*g i j - 11943936a c g i j + 53747712a c*f*g i j - 774144b c d h*i j + 5031936a*b*c d h*i j + 442368b c*d*e*h*i j - 2985984a*b c*d e*h*i j - 3317760a c*d e*h*i j - 663552a*b d*e h*i j + 4810752a b*d e h*i j + 2654208a*b d f*h*i j - 10616832a b*d f*h*i j + 2211840b c g*h*i j - 17252352a*b c d*g*h*i j - 8460288a c d g*h*i j + 3981312a*b c*e*g*h*i j + 20901888a b*c*d*e*g*h*i j - 10948608a b e g*h*i j + 7464960a d*e g*h*i j - 10616832a*b f*g*h*i j + 47775744a b d*f*g*h*i j + 47775744a b*c g h*i j - 71663616a c*e*g h*i j - 71663616a b*f*g h*i j - 442368b c*h i j + 2654208a*b c*d*h i j - 1161216a b*c*d h i j + 663552a*b e*h i j - 1161216a b d*e*h i j - 10948608a d e*h i j - 16920576a b c*g*h i j + 25380864a c*d*g*h i j + 25380864a b*e*g*h i j - 1880064a b h i j + 8460288a b*d*h i j - 25380864a g*h i j - 442368b c*d i j + 2433024a*b c*d i j - 2654208a c*d i j + 663552a*b d e*i j - 2654208a b*d e*i j + 1769472b c*g*i j - 10616832a*b c*d*g*i j + 11943936a b*c*d g*i j - 2654208a*b e*g*i j + 11943936a b d*e*g*i j + 11943936a b c*g i j - 17915904a c*d*g i j - 17915904a b*e*g i j - 1990656a b d h*i j + 7962624a d h*i j + 7962624a b g*h*i j - 35831808a b*d*g*h*i j + 53747712a g h*i j + 13824c d e j  - 13824b*c*d e j  + 13824a*d e j  - 110592c d e f*j  + 110592b*c*d e f*j  + 13824b d e f*j  - 165888a*d e f*j  + 221184c d f j  - 221184b*c*d e*f j  - 110592b d e f j  + 663552a*d e f j  + 221184b d f j  - 884736a*d f j  + 995328c d e g*j  - 1575936b*c d e g*j  + 539136b c*d*e g*j  + 1119744a*c*d e g*j  + 13824b e g*j  - 622080a*b*d*e g*j  - 2654208c d e*f*g*j  + 4810752b*c d e f*g*j  - 870912b c*d e f*g*j  - 7464960a*c*d e f*g*j  - 663552b d*e f*g*j  + 4727808a*b*d e f*g*j  - 1990656b*c d f g*j  - 1161216b c*d e*f g*j  + 11943936a*c*d e*f g*j  + 2239488b d e f g*j  - 10948608a*b*d e f g*j  - 1880064b d f g*j  + 7962624a*b*d f g*j  - 6967296c d e g j  + 9455616b*c d*e g j  - 2861568b c e g j  - 7464960a*c d*e g j  + 4105728a*b*c*e g j  - 1119744a e g j  + 3981312c d f*g j  + 7962624b*c d e*f*g j  - 25380864b c d*e f*g j  + 34338816a*c d e f*g j  + 9455616b c*e f*g j  - 746496a*b*c*d*e f*g j  - 7464960a*b e f*g j  + 1119744a d*e f*g j  + 9704448b c d f g j  - 14929920a*c d f g j  + 7962624b c*d*e*f g j  - 56733696a*b*c*d e*f g j  - 6967296b e f g j  + 34338816a*b d*e f g j  + 8957952a d e f g j  + 3981312b d*f g j  - 14929920a*b d f g j  - 17915904a d f g j  + 11943936c d*e*g j  - 8957952b*c e g j  + 7464960a*c e g j  - 17915904b*c d*f*g j  + 23887872b c e*f*g j  - 71663616a*c d*e*f*g j  + 4478976a*b*c e f*g j  - 3359232a c*e f*g j  - 20901888b c f g j  + 67184640a*b*c d*f g j  + 17915904a*b c*e*f g j  + 67184640a c*d*e*f g j  - 60466176a b*e f g j  - 11943936a*b f g j  + 80621568a b*d*f g j  - 5971968c g j  + 53747712a*c f*g j  - 100776960a c f g j  - 80621568a f g j  - 1105920c d e h*j  + 1603584b*c d e h*j  - 456192b c*d e h*j  - 1244160a*c*d e h*j  - 13824b d*e h*j  + 539136a*b*d e h*j  + 1769472c d f*h*j  - 2433024b*c d e*f*h*j  - 691200b c*d e f*h*j  + 6967296a*c*d e f*h*j  + 566784b d e f*h*j  - 2820096a*b*d e f*h*j  + 2101248b c*d f h*j  - 7962624a*c*d f h*j  - 718848b d e*f h*j  + 2654208a*b*d e*f h*j  + 7962624c d e*g*h*j  - 12275712b*c d e g*h*j  + 6635520b c d*e g*h*j  + 8460288a*c d e g*h*j  - 1244160b c*e g*h*j  - 8460288a*b*c*d*e g*h*j  + 1119744a*b e g*h*j  + 4105728a d*e g*h*j  - 10616832b*c d f*g*h*j  + 19408896b c d e*f*g*h*j  - 35831808a*c d e*f*g*h*j  - 7299072b c*d*e f*g*h*j  + 16422912a*b*c*d e f*g*h*j  + 1492992b e f*g*h*j  - 2737152a*b d*e f*g*h*j  - 8957952a d e f*g*h*j  - 11778048b c*d f g*h*j  + 47775744a*b*c*d f g*h*j  + 2654208b d*e*f g*h*j  - 11943936a*b d e*f g*h*j  + 5971968a d e*f g*h*j  - 7962624c d g h*j  - 1990656b*c d*e*g h*j  + 3981312b c e g h*j  + 8957952a*c d*e g h*j  - 8957952a*b*c e g h*j  + 1119744a c*e g h*j  + 7962624b c d*f*g h*j  + 47775744a*c d f*g h*j  - 9953280b c e*f*g h*j  + 20901888a*b*c d*e*f*g h*j  - 14929920a*b c*e f*g h*j  - 38071296a c*d*e f*g h*j  + 41430528a b*e f*g h*j  + 13934592b c*f g h*j  - 56733696a*b c*d*f g h*j  - 44789760a c*d f g h*j  + 5971968a*b e*f g h*j  - 22394880a b*d*e*f g h*j  + 11943936b*c g h*j  - 17915904a*c e*g h*j  - 71663616a*b*c f*g h*j  + 67184640a c e*f*g h*j  + 67184640a b*c*f g h*j  + 80621568a e*f g h*j  - 1769472c d h j  + 5750784b*c d e*h j  - 6303744b c d e h j  - 1658880a*c d e h j  + 1603584b c*d*e h j  + 6635520a*b*c*d e h j  + 13824b e h j  - 1575936a*b d*e h j  - 2861568a d e h j  - 774144b c d f*h j  + 7962624a*c d f*h j  + 4368384b c*d e*f*h j  - 21897216a*b*c*d e*f*h j  - 1935360b d*e f*h j  + 7713792a*b d e f*h j  + 3981312a d e f*h j  - 27648b d f h j  + 1658880a*b d f h j  - 5971968a d f h j  + 2654208b*c d g*h j  + 663552b c d*e*g*h j  - 15925248a*c d e*g*h j  - 1658880b c e g*h j  + 5971968a*b*c d*e g*h j  + 8460288a*b c*e g*h j  - 8957952a c*d*e g*h j  - 7464960a b*e g*h j  - 3317760b c d*f*g*h j  - 11943936a*b*c d f*g*h j  - 663552b c*e*f*g*h j  + 14929920a*b c*d*e*f*g*h j  + 47775744a c*d e*f*g*h j  - 2488320a*b e f*g*h j  - 14929920a b*d*e f*g*h j  + 331776b f g*h j  - 8460288a*b d*f g*h j  + 29859840a b*d f g*h j  - 5971968b c g h j  + 11943936a*c d*g h j  + 5971968a*b*c e*g h j  + 8957952a c e g h j  + 29859840a*b c f*g h j  - 44789760a c d*f*g h j  - 22394880a b*c*e*f*g h j  - 60466176a e f*g h j  + 6718464a b f g h j  - 53747712a d*f g h j  - 3317760b c d h j  + 1769472a*c d h j  + 5750784b c d*e*h j  + 663552a*b*c d e*h j  - 1105920b c*e h j  - 12275712a*b c*d*e h j  + 3981312a c*d e h j  + 995328a*b e h j  + 9455616a b*d*e h j  - 2211840b c*d*f*h j  + 8957952a*b c*d f*h j  + 3981312a c*d f*h j  + 1327104b e*f*h j  - 3317760a*b d*e*f*h j  - 9953280a b*d e*f*h j  + 1769472b c g*h j  + 7962624a*b*c d*g*h j  - 15925248a*b c e*g*h j  + 5971968a c d*e*g*h j  + 8957952a b*c*e g*h j  + 7464960a e g*h j  + 7962624a*b c*f*g*h j  - 65691648a b*c*d*f*g*h j  + 5971968a b e*f*g*h j  + 53747712a d*e*f*g*h j  - 17915904a c g h j  + 80621568a c*f*g h j  - 1769472b c h j  + 2654208a*b c d*h j  - 5971968a c d h j  + 7962624a*b c*e*h j  - 1990656a b*c*d*e*h j  - 6967296a b e h j  - 8957952a d*e h j  - 2654208a*b f*h j  + 13934592a b d*f*h j  - 11943936a d f*h j  + 11943936a b*c g*h j  - 17915904a c*e*g*h j  - 17915904a b*f*g*h j  - 7962624a b c*h j  + 11943936a c*d*h j  + 11943936a b*e*h j  - 5971968a h j  + 1327104c d e*i*j  - 1935360b*c d e i*j  + 566784b c*d e i*j  + 1492992a*c*d e i*j  + 13824b d e i*j  - 663552a*b*d e i*j  - 221184b*c d f*i*j  + 1714176b c*d e*f*i*j  - 5971968a*c*d e*f*i*j  - 635904b d e f*i*j  + 2322432a*b*d e f*i*j  - 331776b d f i*j  + 1327104a*b*d f i*j  - 2654208c d g*i*j  - 3317760b*c d e*g*i*j  + 7713792b c d e g*i*j  - 2488320a*c d e g*i*j  - 2820096b c*d*e g*i*j  - 2737152a*b*c*d e g*i*j  - 165888b e g*i*j  + 4727808a*b d*e g*i*j  - 7464960a d e g*i*j  - 1161216b c d f*g*i*j  + 11943936a*c d f*g*i*j  - 6137856b c*d e*f*g*i*j  + 20901888a*b*c*d e*f*g*i*j  + 2322432b d*e f*g*i*j  - 11197440a*b d e f*g*i*j  + 8957952a d e f*g*i*j  + 3317760b d f g*i*j  - 16920576a*b d f g*i*j  + 11943936a d f g*i*j  + 13934592b*c d g i*j  - 9953280b c d*e*g i*j  + 5971968a*c d e*g i*j  + 3981312b c e g i*j  - 14929920a*b*c d*e g i*j  - 8957952a*b c*e g i*j  + 41430528a c*d*e g i*j  + 1119744a b*e g i*j  + 7962624b c d*f*g i*j  - 56733696a*b*c d f*g i*j  - 1990656b c*e*f*g i*j  + 20901888a*b c*d*e*f*g i*j  - 22394880a c*d e*f*g i*j  + 8957952a*b e f*g i*j  - 38071296a b*d*e f*g i*j  - 7962624b f g i*j  + 47775744a*b d*f g i*j  - 44789760a b*d f g i*j  - 11943936b c g i*j  - 17915904a*c d*g i*j  + 53747712a*b*c e*g i*j  - 60466176a c e g i*j  + 17915904a*b c f*g i*j  + 67184640a c d*f*g i*j  - 67184640a b*c*e*f*g i*j  + 100776960a e f*g i*j  - 53747712a b f g i*j  + 80621568a d*f g i*j  - 2211840b*c d h*i*j  + 4368384b c d e*h*i*j  - 663552a*c d e*h*i*j  - 691200b c*d e h*i*j  - 7299072a*b*c*d e h*i*j  + 110592b d*e h*i*j  - 870912a*b d e h*i*j  + 9455616a d e h*i*j  - 3594240b c*d f*h*i*j  + 13934592a*b*c*d f*h*i*j  + 1714176b d e*f*h*i*j  - 6137856a*b d e*f*h*i*j  - 1990656a d e*f*h*i*j  + 8957952b c d g*h*i*j  + 7962624a*c d g*h*i*j  - 21897216b c d*e*g*h*i*j  + 14929920a*b*c d e*g*h*i*j  + 6967296b c*e g*h*i*j  + 16422912a*b c*d*e g*h*i*j  - 14929920a c*d e g*h*i*j  - 7464960a*b e g*h*i*j  - 746496a b*d*e g*h*i*j  + 13934592b c*d*f*g*h*i*j  - 43296768a*b c*d f*g*h*i*j  - 65691648a c*d f*g*h*i*j  - 5971968b e*f*g*h*i*j  + 20901888a*b d*e*f*g*h*i*j  + 20901888a b*d e*f*g*h*i*j  + 3981312b c g h*i*j  - 65691648a*b*c d*g h*i*j  + 47775744a*b c e*g h*i*j  - 22394880a c d*e*g h*i*j  - 38071296a b*c*e g h*i*j  - 3359232a e g h*i*j  - 65691648a*b c*f*g h*i*j  + 362797056a b*c*d*f*g h*i*j  - 22394880a b e*f*g h*i*j  - 67184640a d*e*f*g h*i*j  + 80621568a c g h*i*j  - 362797056a c*f*g h*i*j  - 774144b c d h i*j  - 3317760a*b*c d h i*j  - 2433024b c*d*e*h i*j  + 19408896a*b c*d e*h i*j  - 9953280a c*d e*h i*j  - 110592b e h i*j  + 4810752a*b d*e h i*j  - 25380864a b*d e h i*j  - 221184b d*f*h i*j  - 1161216a*b d f*h i*j  + 7962624a b*d f*h i*j  + 7962624b c g*h i*j  - 11943936a*b c d*g*h i*j  + 29859840a c d g*h i*j  - 35831808a*b c*e*g*h i*j  + 20901888a b*c*d*e*g*h i*j  + 34338816a b e g*h i*j  + 4478976a d*e g*h i*j  + 11943936a*b f*g*h i*j  - 56733696a b d*f*g*h i*j  + 17915904a d f*g*h i*j  - 44789760a b*c g h i*j  + 67184640a c*e*g h i*j  + 67184640a b*f*g h i*j  + 1769472b c*h i*j  - 10616832a*b c*d*h i*j  + 7962624a b*c*d h i*j  - 2654208a*b e*h i*j  + 7962624a b d*e*h i*j  + 23887872a d e*h i*j  + 47775744a b c*g*h i*j  - 71663616a c*d*g*h i*j  - 71663616a b*e*g*h i*j  + 3981312a b h i*j  - 17915904a b*d*h i*j  + 53747712a g*h i*j  - 27648b c d i j  + 331776a*c d i j  - 718848b c*d e*i j  + 2654208a*b*c*d e*i j  - 110592b d e i j  + 2239488a*b d e i j  - 6967296a d e i j  - 331776b d f*i j  + 3317760a*b d f*i j  - 7962624a d f*i j  + 1658880b c d g*i j  - 8460288a*b*c d g*i j  + 2654208b c*d*e*g*i j  - 11943936a*b c*d e*g*i j  + 5971968a c*d e*g*i j  + 663552b e g*i j  - 10948608a*b d*e g*i j  + 34338816a b*d e g*i j  + 1327104b d*f*g*i j  - 16920576a*b d f*g*i j  + 47775744a b*d f*g*i j  - 5971968b c g i j  + 29859840a*b c d*g i j  + 6718464a c d g i j  + 5971968a*b c*e*g i j  - 22394880a b*c*d*e*g i j  + 8957952a b e g i j  - 60466176a d*e g i j  + 11943936a*b f*g i j  - 44789760a b d*f*g i j  - 53747712a d f*g i j  - 53747712a b*c g i j  + 80621568a c*e*g i j  + 80621568a b*f*g i j  + 2101248b c*d h*i j  - 11778048a*b c*d h*i j  + 13934592a c*d h*i j  - 221184b d*e*h*i j  - 1161216a*b d e*h*i j  + 7962624a b*d e*h*i j  - 7962624b c*g*h*i j  + 47775744a*b c*d*g*h*i j  - 56733696a b*c*d g*h*i j  + 11943936a*b e*g*h*i j  - 56733696a b d*e*g*h*i j  + 17915904a d e*g*h*i j  - 44789760a b c*g h*i j  + 67184640a c*d*g h*i j  + 67184640a b*e*g h*i j  + 221184b h i j  - 1990656a*b d*h i j  + 9704448a b d h i j  - 20901888a d h i j  - 14929920a b g*h i j  + 67184640a b*d*g*h i j  - 100776960a g h i j  + 221184b d i j  - 1880064a*b d i j  + 3981312a b*d i j  - 884736b g*i j  + 7962624a*b d*g*i j  - 14929920a b d g*i j  - 11943936a d g*i j  - 17915904a b g i j  + 80621568a b*d*g i j  - 80621568a g i j  - 884736c d j  + 1327104b*c d e*j  - 414720b c*d e j  - 995328a*c*d e j  - 13824b d e j  + 497664a*b*d e j  - 995328b c*d f*j  + 3981312a*c*d f*j  + 497664b d e*f*j  - 1990656a*b*d e*f*j  + 7962624b*c d g*j  - 10948608b c d e*g*j  + 3234816b c*d e g*j  + 7464960a*b*c*d e g*j  + 497664b d*e g*j  - 7091712a*b d e g*j  + 7464960a d e g*j  + 8460288b c*d f*g*j  - 35831808a*b*c*d f*g*j  - 4976640b d e*f*g*j  + 25380864a*b d e*f*g*j  - 17915904a d e*f*g*j  - 20901888b c d g j  - 11943936a*c d g j  + 23887872b c d*e*g j  + 17915904a*b*c d e*g j  - 8957952b c*e g j  + 4478976a*b c*d*e g j  - 60466176a c*d e g j  + 7464960a*b e g j  - 3359232a b*d*e g j  - 17915904b c*d*f*g j  + 67184640a*b c*d f*g j  + 80621568a c*d f*g j  + 11943936b e*f*g j  - 71663616a*b d*e*f*g j  + 67184640a b*d e*f*g j  + 11943936b c g j  + 53747712a*b*c d*g j  - 107495424a*b c e*g j  + 80621568a c d*e*g j  + 100776960a b*c*e g j  - 30233088a e g j  + 53747712a*b c*f*g j  - 362797056a b*c*d*f*g j  + 80621568a b e*f*g j  - 120932352a d*e*f*g j  - 80621568a c g j  + 362797056a c*f*g j  - 663552b c d h*j  + 165888b c*d e*h*j  + 1990656a*b*c*d e*h*j  - 414720b d e h*j  + 3234816a*b d e h*j  - 8957952a d e h*j  + 497664b d f*h*j  - 4976640a*b d f*h*j  + 11943936a d f*h*j  + 4976640b c d g*h*j  + 1990656b c*d*e*g*h*j  - 40310784a*b c*d e*g*h*j  + 53747712a c*d e*g*h*j  - 995328b e g*h*j  + 7464960a*b d*e g*h*j  + 4478976a b*d e g*h*j  - 1990656b d*f*g*h*j  + 25380864a*b d f*g*h*j  - 71663616a b*d f*g*h*j  - 11943936b c g h*j  + 17915904a*b c d*g h*j  - 53747712a c d g h*j  + 53747712a*b c*e*g h*j  - 67184640a b*c*d*e*g h*j  - 60466176a b e g h*j  + 100776960a d*e g h*j  - 17915904a*b f*g h*j  + 67184640a b d*f*g h*j  + 80621568a d f*g h*j  + 80621568a b*c g h*j  - 120932352a c*e*g h*j  - 120932352a b*f*g h*j  - 663552b c*d h j  + 4976640a*b c*d h j  - 11943936a c*d h j  + 1327104b d*e*h j  - 10948608a*b d e*h j  + 23887872a b*d e*h j  + 17915904a b*c*d g*h j  + 17915904a b d*e*g*h j  - 107495424a d e*g*h j  - 53747712a b c*g h j  + 80621568a c*d*g h j  + 80621568a b*e*g h j  - 884736b h j  + 7962624a*b d*h j  - 20901888a b d h j  + 11943936a d h j  - 11943936a b g*h j  + 53747712a b*d*g*h j  - 80621568a g h j  + 497664b c*d i*j  - 1990656a*b*c*d i*j  + 497664b d e*i*j  - 4976640a*b d e*i*j  + 11943936a d e*i*j  - 4976640b c*d g*i*j  + 25380864a*b c*d g*i*j  - 17915904a c*d g*i*j  - 1990656b d*e*g*i*j  + 25380864a*b d e*g*i*j  - 71663616a b*d e*g*i*j  + 11943936b c*g i*j  - 71663616a*b c*d*g i*j  + 67184640a b*c*d g i*j  - 17915904a*b e*g i*j  + 67184640a b d*e*g i*j  + 80621568a d e*g i*j  + 80621568a b c*g i*j  - 120932352a c*d*g i*j  - 120932352a b*e*g i*j  - 995328b d h*i*j  + 8460288a*b d h*i*j  - 17915904a b*d h*i*j  + 3981312b g*h*i*j  - 35831808a*b d*g*h*i*j  + 67184640a b d g*h*i*j  + 53747712a d g*h*i*j  + 80621568a b g h*i*j  - 362797056a b*d*g h*i*j  + 362797056a g h*i*j  - 373248b d j  + 2985984a*b d j  - 5971968a d j  + 2985984b d g*j  - 25380864a*b d g*j  + 53747712a b*d g*j  - 5971968b g j  + 53747712a*b d*g j  - 100776960a b d g j  - 80621568a d g j  - 80621568a b g j  + 362797056a b*d*g j  - 272097792a g j

o30 : S

i31 : numgens detDiscr

o31 = 1

i32 : # terms detDiscr_0

o32 = 2040
```

---

## schemes / test.m2 — chunk 4

### Input

```macaulay2
clearAll
S = QQ[a,b,x,y, MonomialOrder => Eliminate 2];
I1 = ideal(x-a, y-a, a^2-2);
ideal selectInSubring(1, gens gb I1)
I2 = ideal(x-a, y-b, a^2-2, b^2-3);
ideal selectInSubring(1, gens gb I2)
I3 = ideal(x-a, y-a^4, a^4+a^3+a^2+a+1);
ideal selectInSubring(1, gens gb I3)
```

### Output

```
i33 : clearAll

i34 : S = QQ[a,b,x,y, MonomialOrder => Eliminate 2];

i35 : I1 = ideal(x-a, y-a, a^2-2);

o35 : Ideal of S

i36 : ideal selectInSubring(1, gens gb I1)

2
o36 = ideal (x - y, y  - 2)

o36 : Ideal of S

i37 : I2 = ideal(x-a, y-b, a^2-2, b^2-3);

o37 : Ideal of S

i38 : ideal selectInSubring(1, gens gb I2)

2       2
o38 = ideal (y  - 3, x  - 2)

o38 : Ideal of S

i39 : I3 = ideal(x-a, y-a^4, a^4+a^3+a^2+a+1);

o39 : Ideal of S

i40 : ideal selectInSubring(1, gens gb I3)

2    2               3    2
o40 = ideal (x*y - 1, x  + y  + x + y + 1, y  + y  + x + y + 1)

o40 : Ideal of S
```

---

## schemes / test.m2 — chunk 5

### Input

```macaulay2
I4 = ideal(a*x+b*y, a^2-2, b^2-3);
ideal selectInSubring(1, gens gb I4)
I5 = ideal(a*x+b*y-1, a^2-2, b^2-3);
ideal selectInSubring(1, gens gb I5)
clearAll
S = QQ[x, y, z];
I = ideal(x^5+y^3+z^3, x^3+y^5+z^3, x^3+y^3+z^5);
degree(I : saturate(I))
```

### Output

```
i41 : I4 = ideal(a*x+b*y, a^2-2, b^2-3);

o41 : Ideal of S

i42 : ideal selectInSubring(1, gens gb I4)

2     2
o42 = ideal(2x  - 3y )

o42 : Ideal of S

i43 : I5 = ideal(a*x+b*y-1, a^2-2, b^2-3);

o43 : Ideal of S

i44 : ideal selectInSubring(1, gens gb I5)

4      2 2     4     2     2
o44 = ideal(4x  - 12x y  + 9y  - 4x  - 6y  + 1)

o44 : Ideal of S

i45 : clearAll

i46 : S = QQ[x, y, z];

i47 : I = ideal(x^5+y^3+z^3, x^3+y^5+z^3, x^3+y^3+z^5);

o47 : Ideal of S

i48 : degree(I : saturate(I))

o48 = 27
```

---

## schemes / test.m2 — chunk 6

### Input

```macaulay2
clearAll
PP3 = QQ[t, x, y, z, w];
L = ideal(x, y);
M = ideal(x-t*z, y+t^2*w);
X = intersect(L, M);
Xzero = trim substitute(saturate(X, t), {t => 0})
Xzero == intersect(ideal(x^2, y), ideal(x, y^2, z))
degree(ideal(x^2, y ) / ideal(x, y^2, z))
```

### Output

```
i49 : clearAll

i50 : PP3 = QQ[t, x, y, z, w];

i51 : L = ideal(x, y);

o51 : Ideal of PP3

i52 : M = ideal(x-t*z, y+t^2*w);

o52 : Ideal of PP3

i53 : X = intersect(L, M);

o53 : Ideal of PP3

i54 : Xzero = trim substitute(saturate(X, t), {t => 0})

2        2
o54 = ideal (y*z, y , x*y, x )

o54 : Ideal of PP3

i55 : Xzero == intersect(ideal(x^2, y), ideal(x, y^2, z))

o55 = true

i56 : degree(ideal(x^2, y ) / ideal(x, y^2, z))

o56 = 1
```

---

## schemes / test.m2 — chunk 7

### Input

```macaulay2
clearAll
S = QQ[a, b, c, d, e];
IX = trim minors(2, matrix{{a, b^2, b*d, c},{b, a*c, c^2, d}})
IY = ideal(a, d);
codim IX + codim IY == codim (IX + IY)
(degree IX) * (degree IY)
degree (IX + IY)
J = ideal mingens (IX + ideal(a))
```

### Output

```
i57 : clearAll

i58 : S = QQ[a, b, c, d, e];

i59 : IX = trim minors(2, matrix{{a, b^2, b*d, c},{b, a*c, c^2, d}})

3      2     2    2    3    2
o59 = ideal (b*c - a*d, c  - b*d , a*c  - b d, b  - a c)

o59 : Ideal of S

i60 : IY = ideal(a, d);

o60 : Ideal of S

i61 : codim IX + codim IY == codim (IX + IY)

o61 = true

i62 : (degree IX) * (degree IY)

o62 = 4

i63 : degree (IX + IY)

o63 = 5

i64 : J = ideal mingens (IX + ideal(a))

2    3      2   3
o64 = ideal (a, b*c, b d, c  - b*d , b )

o64 : Ideal of S
```

---

## schemes / test.m2 — chunk 8

### Input

```macaulay2
J == intersect(ideal(a, b*c, b^2, c^3-b*d^2), 
           ideal(a, d, b*c, c^3, b^3)) -- embedded point
clearAll
blowUpIdeal = (I) -> (
           r := numgens I;
           S := ring I;
           n := numgens S;
           K := coefficientRing S;
           tR := K[t, gens S, vars(0..r-1), 
                     MonomialOrder => Eliminate 1];
           f := map(tR, S, submatrix(vars tR, {1..n}));
           F := f(gens I);
           J := ideal apply(1..r, j -> (gens tR)_(n+j)-t*F_(0,(j-1)));
           L := ideal selectInSubring(1, gens gb J);
           R := K[gens S, vars(0..r-1)];
           g := map(R, tR, 0 | vars R);
           trim g(L));
S = QQ[x, y];
I = ideal(x^3, x*y, y^2);
J = blowUpIdeal(I)
saturate(J + minors(2, jacobian J)) == 1
clearAll
```

### Output

```
i65 : J == intersect(ideal(a, b*c, b^2, c^3-b*d^2), 
           ideal(a, d, b*c, c^3, b^3)) -- embedded point

o65 = true

i66 : clearAll

i67 : blowUpIdeal = (I) -> (
           r := numgens I;
           S := ring I;
           n := numgens S;
           K := coefficientRing S;
           tR := K[t, gens S, vars(0..r-1), 
                     MonomialOrder => Eliminate 1];
           f := map(tR, S, submatrix(vars tR, {1..n}));
           F := f(gens I);
           J := ideal apply(1..r, j -> (gens tR)_(n+j)-t*F_(0,(j-1)));
           L := ideal selectInSubring(1, gens gb J);
           R := K[gens S, vars(0..r-1)];
           g := map(R, tR, 0 | vars R);
           trim g(L));

i68 : S = QQ[x, y];

i69 : I = ideal(x^3, x*y, y^2);

o69 : Ideal of S

i70 : J = blowUpIdeal(I)

2         2
o70 = ideal (y*b - x*c, x*b  - a*c, x b - y*a)

o70 : Ideal of QQ[x..y, a..c]

i71 : saturate(J + minors(2, jacobian J)) == 1

o71 = true

i72 : clearAll
```

---

## schemes / test.m2 — chunk 9

### Input

```macaulay2
PP4 = QQ[a..e];
S = QQ[r..t, A..E, MonomialOrder => Eliminate 3];
I = ideal(A - r^2, B - s^2, C - r*s, D - r*t, E - s*t);
phi = map(PP4, S, matrix{{0_PP4, 0_PP4, 0_PP4}} | vars PP4)
surfaceA = phi ideal selectInSubring(1, gens gb I)
R = QQ[t, x, y, z, u, v, MonomialOrder => Eliminate 1];
blowUpIdeal = ideal selectInSubring(1, gens gb ideal(u-t*x, 
           v-t*y))
PP2xPP1 = QQ[x, y, z, u, v];
```

### Output

```
i73 : PP4 = QQ[a..e];

i74 : S = QQ[r..t, A..E, MonomialOrder => Eliminate 3];

i75 : I = ideal(A - r^2, B - s^2, C - r*s, D - r*t, E - s*t);

o75 : Ideal of S

i76 : phi = map(PP4, S, matrix{{0_PP4, 0_PP4, 0_PP4}} | vars PP4)

o76 = map (PP4, S, {0, 0, 0, a, b, c, d, e})

o76 : RingMap PP4 <-- S

i77 : surfaceA = phi ideal selectInSubring(1, gens gb I)

2
o77 = ideal (c*d - a*e, b*d - c*e, a*b - c )

o77 : Ideal of PP4

i78 : R = QQ[t, x, y, z, u, v, MonomialOrder => Eliminate 1];

i79 : blowUpIdeal = ideal selectInSubring(1, gens gb ideal(u-t*x, 
           v-t*y))

o79 = ideal(y*u - x*v)

o79 : Ideal of R

i80 : PP2xPP1 = QQ[x, y, z, u, v];
```

---

## schemes / test.m2 — chunk 10

### Input

```macaulay2
embed = map(PP2xPP1, R, 0 | vars PP2xPP1);
blowUp = PP2xPP1 / embed(blowUpIdeal);
PP5 = QQ[A .. F];
segre = map(blowUp, PP5, matrix{{x*u,y*u,z*u,x*v,y*v,z*v}});
ker segre
projection = map(PP4, PP5, matrix{{a, c, d, c, b, e}})
surfaceB = trim projection ker segre
determinantal = minors(2, matrix{{a, c, d}, {b, d, e}})
```

### Output

```
i81 : embed = map(PP2xPP1, R, 0 | vars PP2xPP1);

o81 : RingMap PP2xPP1 <-- R

i82 : blowUp = PP2xPP1 / embed(blowUpIdeal);

i83 : PP5 = QQ[A .. F];

i84 : segre = map(blowUp, PP5, matrix{{x*u,y*u,z*u,x*v,y*v,z*v}});

o84 : RingMap blowUp <-- PP5

i85 : ker segre

2
o85 = ideal (B - D, C*E - D*F, D  - A*E, C*D - A*F)

o85 : Ideal of PP5

i86 : projection = map(PP4, PP5, matrix{{a, c, d, c, b, e}})

o86 = map (PP4, PP5, {a, c, d, c, b, e})

o86 : RingMap PP4 <-- PP5

i87 : surfaceB = trim projection ker segre

2
o87 = ideal (c*d - a*e, b*d - c*e, a*b - c )

o87 : Ideal of PP4

i88 : determinantal = minors(2, matrix{{a, c, d}, {b, d, e}})

2
o88 = ideal (- b*c + a*d, - b*d + a*e, - d  + c*e)

o88 : Ideal of PP4
```

---

## schemes / test.m2 — chunk 11

### Input

```macaulay2
sigma = map( PP4, PP4, matrix{{d, e, a, c, b}});
surfaceC = sigma determinantal
surfaceA == surfaceB
surfaceB == surfaceC
clearAll
PP3 = QQ[t, x, y, z, w];
Q = ideal( t*x^2+t*y^2+t*z^2+w^2 );
R = QQ[t, u, v, A .. H];
```

### Output

```
i89 : sigma = map( PP4, PP4, matrix{{d, e, a, c, b}});

o89 : RingMap PP4 <-- PP4

i90 : surfaceC = sigma determinantal

2
o90 = ideal (c*d - a*e, b*d - c*e, a*b - c )

o90 : Ideal of PP4

i91 : surfaceA == surfaceB

o91 = true

i92 : surfaceB == surfaceC

o92 = true

i93 : clearAll

i94 : PP3 = QQ[t, x, y, z, w];

i95 : Q = ideal( t*x^2+t*y^2+t*z^2+w^2 );

o95 : Ideal of PP3

i96 : R = QQ[t, u, v, A .. H];
```

---

## schemes / test.m2 — chunk 12

### Input

```macaulay2
phi = map(R, PP3, matrix{{t}} | 
              u*matrix{{A, B, C, D}} + v*matrix{{E, F, G, H}});
imageFamily = phi Q;
coeffOfFamily = contract(matrix{{u^2,u*v,v^2}}, gens imageFamily)
S = QQ[t, A..H];
coeffOfFamily = substitute(coeffOfFamily, S);
Sbar = S / (ideal coeffOfFamily);
psi = matrix{{t}} | exteriorPower(2, 
                   matrix{{A, B, C, D}, {E, F, G, H}})
PP5 = QQ[t, a..f];
```

### Output

```
i97 : phi = map(R, PP3, matrix{{t}} | 
              u*matrix{{A, B, C, D}} + v*matrix{{E, F, G, H}});

o97 : RingMap R <-- PP3

i98 : imageFamily = phi Q;

o98 : Ideal of R

i99 : coeffOfFamily = contract(matrix{{u^2,u*v,v^2}}, gens imageFamily)

o99 = | tA2+tB2+tC2+D2 2tAE+2tBF+2tCG+2DH tE2+tF2+tG2+H2 |

              1      3
o99 : Matrix R  <-- R

i100 : S = QQ[t, A..H];

i101 : coeffOfFamily = substitute(coeffOfFamily, S);

1      3
o101 : Matrix S  <-- S

i102 : Sbar = S / (ideal coeffOfFamily);

i103 : psi = matrix{{t}} | exteriorPower(2, 
                   matrix{{A, B, C, D}, {E, F, G, H}})

o103 = | t -BE+AF -CE+AG -CF+BG -DE+AH -DF+BH -DG+CH |

                  1         7
o103 : Matrix Sbar  <-- Sbar

i104 : PP5 = QQ[t, a..f];
```

---

## schemes / test.m2 — chunk 13

### Input

```macaulay2
fanoOfFamily = trim ker map(Sbar, PP5, psi);
zeroFibre = trim substitute(saturate(fanoOfFamily, t), {t=>0})
transpose gens zeroFibre
oneFibre = trim substitute(saturate(fanoOfFamily, t), {t => 1})
oneFibre == intersect(ideal(c-d, b+e, a-f, d^2+e^2+f^2), 
            ideal(c+d, b-e, a+f, d^2+e^2+f^2))
i110 :
```

### Output

```
i105 : fanoOfFamily = trim ker map(Sbar, PP5, psi);

o105 : Ideal of PP5

i106 : zeroFibre = trim substitute(saturate(fanoOfFamily, t), {t=>0})

2             2                   2                                          2    2    2
o106 = ideal (f , e*f, d*f, e , d*e, a*e + b*f, d , c*d - b*e + a*f, b*d + c*e, a*d - c*f, a  + b  + c )

o106 : Ideal of PP5

i107 : transpose gens zeroFibre

o107 = {-2} | f2       |
       {-2} | ef       |
       {-2} | df       |
       {-2} | e2       |
       {-2} | de       |
       {-2} | ae+bf    |
       {-2} | d2       |
       {-2} | cd-be+af |
       {-2} | bd+ce    |
       {-2} | ad-cf    |
       {-2} | a2+b2+c2 |

                 11        1
o107 : Matrix PP5   <-- PP5

i108 : oneFibre = trim substitute(saturate(fanoOfFamily, t), {t => 1})

2    2    2                                          2    2    2                         2    2              2    2
o108 = ideal (a*e + b*f, d  + e  + f , c*d - b*e + a*f, b*d + c*e, a*d - c*f, c  + e  + f , b*c + d*e, a*c - d*f, b  - e , a*b + e*f, a  - f )

o108 : Ideal of PP5

i109 : oneFibre == intersect(ideal(c-d, b+e, a-f, d^2+e^2+f^2), 
            ideal(c+d, b-e, a+f, d^2+e^2+f^2))

o109 = true

i110 :
```

---

## solving / chapter.m2 — chunk 0

### Input

```macaulay2
R = ZZ/101[y11, y12, y21, y22];
PolynomialSystem = apply(1..4, i -> 
                     random(0, R) + random(1, R) + random(2, R));
I = ideal PolynomialSystem;
dim I, degree I
J = ideal (random(R^4, R^7) *  transpose(
             matrix{{1, y11, y12, y21, y22, y11*y22, y12*y21}}));
dim J, degree J
K = ideal (random(R^4, R^6) * transpose( 
             matrix{{1, y11, y12, y21, y22, y11*y22 - y12*y21}}));
dim K, degree K
```

### Output

```
i1 : R = ZZ/101[y11, y12, y21, y22];

i2 : PolynomialSystem = apply(1..4, i -> 
                     random(0, R) + random(1, R) + random(2, R));

i3 : I = ideal PolynomialSystem;

o3 : Ideal of R

i4 : dim I, degree I

o4 = (0, 16)

o4 : Sequence

i5 : J = ideal (random(R^4, R^7) *  transpose(
             matrix{{1, y11, y12, y21, y22, y11*y22, y12*y21}}));

o5 : Ideal of R

i6 : dim J, degree J

o6 = (0, 4)

o6 : Sequence

i7 : K = ideal (random(R^4, R^6) * transpose( 
             matrix{{1, y11, y12, y21, y22, y11*y22 - y12*y21}}));

o7 : Ideal of R

i8 : dim K, degree K

o8 = (0, 2)

o8 : Sequence
```

---

## solving / chapter.m2 — chunk 1

### Input

```macaulay2
R = ZZ/7[y, x, MonomialOrder=>Lex];
I = ideal (y^3*x^2 + 2*y^2*x + 3*x*y,  3*y^2 + x*y - 3*y);
J = saturate(I, ideal(y))
factor(J_0)
load "realroots.m2"
code eliminant
code regularRep
code charPoly
```

### Output

```
i9 : R = ZZ/7[y, x, MonomialOrder=>Lex];

i10 : I = ideal (y^3*x^2 + 2*y^2*x + 3*x*y,  3*y^2 + x*y - 3*y);

o10 : Ideal of R

i11 : J = saturate(I, ideal(y))

4    3     2
o11 = ideal (x  + x  + 3x  + 3x, y - 2x - 1)

o11 : Ideal of R

i12 : factor(J_0)

o12 = (x)(x - 2)(x + 2)(x + 1)

o12 : Product

i13 : load "realroots.m2"

i14 : code eliminant

o14 = -- realroots.m2:65-80
      eliminant = (h, C) -> (
           Z := C_0;
           A := ring h;
           assert( dim A == 0 );
           F := coefficientRing A;
           assert( isField F );
           assert( F == coefficientRing C );
           B := basis A;
           d := numgens source B;
           M := fold((M, i) -> M || 
                     substitute(contract(B, h^(i+1)), F), 
                     substitute(contract(B, 1_A), F), 
                     flatten subsets(d, d));
           N := ((ker transpose M)).generators;
           P := matrix {toList apply(0..d, i -> Z^i)} * N;
                (flatten entries(P))_0)

i15 : code regularRep

o15 = -- realroots.m2:96-100
      regularRep = f -> (
           assert( dim ring f == 0 );
           b := basis ring f;
           k := coefficientRing ring f;
           substitute(contract(transpose b, f*b), k))

i16 : code charPoly

o16 = -- realroots.m2:106-113
      charPoly = (h, Z) -> (
           A := ring h;
           F := coefficientRing A;
           S := F[Z];
           Z  = value Z;     
           mh := regularRep(h) ** S;
           Idz := S_0 * id_(S^(numgens source mh));
           det(Idz - mh))
```

---

## solving / chapter.m2 — chunk 2

### Input

```macaulay2
code SturmSequence
code numRealSturm
code numPosRoots
code variations
code traceForm
code traceFormSignature
code numRealTrace
R = QQ[x, y];
```

### Output

```
i17 : code SturmSequence

o17 = -- realroots.m2:117-131
      SturmSequence = f -> (
           assert( isPolynomialRing ring f );
           assert( numgens ring f === 1 );
           R := ring f;
           assert( char R == 0 );
           x := R_0;
           n := first degree f;
           c := new MutableList from toList (0 .. n);
           if n >= 0 then (
                c#0 = f;
                if n >= 1 then (
                     c#1 = diff(x,f);
                     scan(2 .. n, i -> c#i = - c#(i-2) % c#(i-1));
                     ));
           toList c)

i18 : code numRealSturm

o18 = -- realroots.m2:160-163
      numRealSturm = f -> (
           c := SturmSequence f;
           variations (signAtMinusInfinity \ c) 
               - variations (signAtInfinity \ c))

i19 : code numPosRoots

o19 = -- realroots.m2:168-171
      numPosRoots = f -> (  
           c := SturmSequence f;
           variations (signAtZero \ c) 
               - variations (signAtInfinity \ c))

i20 : code variations

o20 = -- realroots.m2:183-191
      variations = c -> (
           n := 0;
           last := 0;
           scan(c, x -> if x != 0 then (
                     if last < 0 and x > 0 or last > 0 
                        and x < 0 then n = n+1;
                     last = x;
                     ));
           n)

i21 : code traceForm

o21 = -- realroots.m2:196-203
      traceForm = h -> (
           assert( dim ring h == 0 );
           b  := basis ring h;
           k  := coefficientRing ring h;
           mm := substitute(contract(transpose b, h * b ** b), k);
           tr := matrix {apply(first entries b, x ->
                     trace regularRep x)};
           adjoint(tr * mm, source tr, source tr))

i22 : code traceFormSignature

o22 = -- realroots.m2:208-218
      traceFormSignature = h -> (
           A := ring h;
           assert( dim A == 0 );
           assert( char A == 0 );
           S := QQ[Z];
           TrF := traceForm(h) ** S;
           IdZ := Z * id_(S^(numgens source TrF));
           f := det(TrF - IdZ);
           << "The trace form S_h with h = " << h << 
             " has rank " << rank(TrF) << " and signature " << 
             numPosRoots(f) - numNegRoots(f) << endl; )

i23 : code numRealTrace

o23 = -- realroots.m2:223-230
      numRealTrace = A -> (
           assert( dim A == 0 );
           assert( char A == 0 );
           S := QQ[Z];
           TrF := traceForm(1_A) ** S;
           IdZ := Z * id_(S^(numgens source TrF));
           f := det(TrF - IdZ);
           numPosRoots(f)-numNegRoots(f))

i24 : R = QQ[x, y];
```

---

## solving / chapter.m2 — chunk 3

### Input

```macaulay2
I = ideal (1 - x^2*y + 2*x*y^2,  y - 2*x - x*y + x^2);
dim I, degree I
A = R/I;
time g = eliminant(x, QQ[Z])
     -- used 0.09 seconds
time g = charPoly(x, Z)
     -- used 0.02 seconds
numRealSturm(g), numRealTrace(A)
traceFormSignature(x*y);
The trace form S_h with h = x*y has rank 5 and signature 3
traceFormSignature(x - 2);
The trace form S_h with h = x - 2 has rank 5 and signature 1
```

### Output

```
i25 : I = ideal (1 - x^2*y + 2*x*y^2,  y - 2*x - x*y + x^2);

o25 : Ideal of R

i26 : dim I, degree I

o26 = (0, 5)

o26 : Sequence

i27 : A = R/I;

i28 : time g = eliminant(x, QQ[Z])
     -- used 0.09 seconds

5     4     3    2
o28 = Z  - 5Z  + 6Z  + Z  - 2Z + 1

o28 : QQ [Z]

i29 : time g = charPoly(x, Z)
     -- used 0.02 seconds

5     4     3    2
o29 = Z  - 5Z  + 6Z  + Z  - 2Z + 1

o29 : QQ [Z]

i30 : numRealSturm(g), numRealTrace(A)

o30 = (3, 3)

o30 : Sequence

i31 : traceFormSignature(x*y);
The trace form S_h with h = x*y has rank 5 and signature 3

i32 : traceFormSignature(x - 2);
The trace form S_h with h = x - 2 has rank 5 and signature 1
```

---

## solving / chapter.m2 — chunk 4

### Input

```macaulay2
traceFormSignature(x + y - 3);
The trace form S_h with h = x + y - 3 has rank 5 and signature -1
Points = {{2, 2,  0 }, {1, -2,  0}, {-3, 0, 0}, 
                {0, 0, 5/2}, {0,  0, -3}};
R = QQ[r, y11, y12, y21, y22];
P = matrix{{0, y11, y12}};
V = matrix{{1, y21, y22}};
Points = matrix Points ** R;
I = ideal apply(0..4, i -> (
                X := Points^{i};
                r * (V * transpose V)  +
                 ((X - P) * transpose V)^2) -
                 ((X - P) * transpose(X - P)) * (V * transpose V)
                );
dim I, degree I
```

### Output

```
i33 : traceFormSignature(x + y - 3);
The trace form S_h with h = x + y - 3 has rank 5 and signature -1

i34 : Points = {{2, 2,  0 }, {1, -2,  0}, {-3, 0, 0}, 
                {0, 0, 5/2}, {0,  0, -3}};

i35 : R = QQ[r, y11, y12, y21, y22];

i36 : P = matrix{{0, y11, y12}};

1       3
o36 : Matrix R  <--- R

i37 : V = matrix{{1, y21, y22}};

1       3
o37 : Matrix R  <--- R

i38 : Points = matrix Points ** R;

5       3
o38 : Matrix R  <--- R

i39 : I = ideal apply(0..4, i -> (
                X := Points^{i};
                r * (V * transpose V)  +
                 ((X - P) * transpose V)^2) -
                 ((X - P) * transpose(X - P)) * (V * transpose V)
                );

o39 : Ideal of R

i40 : dim I, degree I

o40 = (0, 6)

o40 : Sequence
```

---

## solving / chapter.m2 — chunk 5

### Input

```macaulay2
A = R/I; numPosRoots(charPoly(r, Z))
Sphere = (a, b, c, r) -> (
              matrix{{a^2 + b^2 + c^2 - r ,-a ,-b ,-c },
                     {         -a         , 1 , 0 , 0 },
                     {         -b         , 0 , 1 , 0 },
                     {         -c         , 0 , 0 , 1 }}
              );
R = QQ[y11, y12, y21, y22];
tangentTo = (M) -> (
           P := matrix{{1, 0, y11, y12}};
           V := matrix{{0, 1, y21, y22}};
           (P * M * transpose V)^2 - 
             (P * M * transpose P) * (V * M * transpose V)
           );
I = ideal (tangentTo(Sphere(0,0,0,5)), 
                 tangentTo(Sphere(4,1,1,5)), 
                 tangentTo(Sphere(1,4,1,5)), 
                 tangentTo(Sphere(1,1,4,5)));
dim I, degree I
A = R/I;
numRealSturm(eliminant(y11 - y12 + y21 + y22, QQ[Z]))
```

### Output

```
i41 : A = R/I; numPosRoots(charPoly(r, Z))

o42 = 6

i43 : Sphere = (a, b, c, r) -> (
              matrix{{a^2 + b^2 + c^2 - r ,-a ,-b ,-c },
                     {         -a         , 1 , 0 , 0 },
                     {         -b         , 0 , 1 , 0 },
                     {         -c         , 0 , 0 , 1 }}
              );

i44 : R = QQ[y11, y12, y21, y22];

i45 : tangentTo = (M) -> (
           P := matrix{{1, 0, y11, y12}};
           V := matrix{{0, 1, y21, y22}};
           (P * M * transpose V)^2 - 
             (P * M * transpose P) * (V * M * transpose V)
           );

i46 : I = ideal (tangentTo(Sphere(0,0,0,5)), 
                 tangentTo(Sphere(4,1,1,5)), 
                 tangentTo(Sphere(1,4,1,5)), 
                 tangentTo(Sphere(1,1,4,5)));

o46 : Ideal of R

i47 : dim I, degree I

o47 = (0, 12)

o47 : Sequence

i48 : A = R/I;

i49 : numRealSturm(eliminant(y11 - y12 + y21 + y22, QQ[Z]))

o49 = 12
```

---

## solving / chapter.m2 — chunk 6

### Input

```macaulay2
R = ZZ/101[apply(subsets(5,2), i -> p_i )];
I = Grassmannian(1, 4, R)
dim(Proj(R/I)), degree(I)
oscPlane = (i, n, s) -> (
           gamma := matrix {toList apply(1..n, i -> s^(i-1))};
           L := gamma;
           j := 0;
           while j < i-1 do (gamma = diff(s, gamma); 
                L = L || gamma;
                j = j+1);
           L);
QQ[s]; oscPlane(3, 6, s)
spSchub = (r, L, P) -> (
           I := ideal apply(subsets(numgens source L, 
                            r + numgens target L), S -> 
                fold((sum, U) -> sum +
                 fold((term,i) -> term*(-1)^i, P_(S_U) * det(
                  submatrix(L, sort toList(set(S) - set(S_U)))), U), 
                     0, subsets(#S, r))));
R = QQ[apply(subsets(6,3), i -> p_i )];
I = fold((J, i) -> J +
            spSchub(3, substitute(oscPlane(3, 6, s), {s=> 1+i}), p) +
            spSchub(3, substitute(oscPlane(2, 6, s), {s=> 4+i}), p), 
            Grassmannian(2, 5, R), {0,1,2}) + 
           ideal (p_{0,1,5} - 1);
```

### Output

```
i50 : R = ZZ/101[apply(subsets(5,2), i -> p_i )];

i51 : I = Grassmannian(1, 4, R)

o51 = ideal (p      p       - p      p       + p      p      , p      p       - p      p       + p      p      , p      p       - p      p       + p      p      , p      p       - p      p       + p      p      , p      p       - p      p       + p      p      )
              {2, 3} {1, 4}    {1, 3} {2, 4}    {1, 2} {3, 4}   {2, 3} {0, 4}    {0, 3} {2, 4}    {0, 2} {3, 4}   {1, 3} {0, 4}    {0, 3} {1, 4}    {0, 1} {3, 4}   {1, 2} {0, 4}    {0, 2} {1, 4}    {0, 1} {2, 4}   {1, 2} {0, 3}    {0, 2} {1, 3}    {0, 1} {2, 3}

o51 : Ideal of R

i52 : dim(Proj(R/I)), degree(I)

o52 = (6, 5)

o52 : Sequence

i53 : oscPlane = (i, n, s) -> (
           gamma := matrix {toList apply(1..n, i -> s^(i-1))};
           L := gamma;
           j := 0;
           while j < i-1 do (gamma = diff(s, gamma); 
                L = L || gamma;
                j = j+1);
           L);

i54 : QQ[s]; oscPlane(3, 6, s)

o55 = | 1 s s2 s3  s4   s5   |
      | 0 1 2s 3s2 4s3  5s4  |
      | 0 0 2  6s  12s2 20s3 |

                   3            6
o55 : Matrix QQ [s]  <--- QQ [s]

i56 : spSchub = (r, L, P) -> (
           I := ideal apply(subsets(numgens source L, 
                            r + numgens target L), S -> 
                fold((sum, U) -> sum +
                 fold((term,i) -> term*(-1)^i, P_(S_U) * det(
                  submatrix(L, sort toList(set(S) - set(S_U)))), U), 
                     0, subsets(#S, r))));

i57 : R = QQ[apply(subsets(6,3), i -> p_i )];

i58 : I = fold((J, i) -> J +
            spSchub(3, substitute(oscPlane(3, 6, s), {s=> 1+i}), p) +
            spSchub(3, substitute(oscPlane(2, 6, s), {s=> 4+i}), p), 
            Grassmannian(2, 5, R), {0,1,2}) + 
           ideal (p_{0,1,5} - 1);

o58 : Ideal of R
```

---

## solving / chapter.m2 — chunk 7

### Input

```macaulay2
dim I, degree I
A = R/I; numRealSturm(eliminant(p_{2,3,4}, QQ[Z]))
randL = (R, n, r, l) -> 
                matrix table(n-r+1-l, n, (i, j) -> random(0, R));
testTransverse = F -> (
            R := F[apply(subsets(6, 3), i -> q_i )];
            continue := true;
            j := 0;  
            limit := 5;
            while continue and (j < limit) do (
                 j = j + 1;
                 I := fold((J, i) -> J + 
                           spSchub(3, randL(R, 6, 3, 1), q) +
                           spSchub(3, randL(R, 6, 3, 2), q),
                           Grassmannian(2, 5, R) + 
                           ideal (1 + random(1, R)),
                           {0, 1, 2});
                 if (dim I == 0) and (degree I == 6) then (
                 lin := promote(random(1, R), (R/I));
                 g := charPoly(lin, Z);
                 continue = not(1 == gcd(g, diff(Z, g)));
                 ));
            if continue then << "Failed for the prime " << char F << 
               " with " << j << " iterations" << endl;
            if not continue then << "Succeeded for the prime " <<
                char F << " in " << j << " iteration(s)" << endl;
            );
testTransverse(ZZ/2);
Failed for the prime 2 with 5 iterations
testTransverse(GF 4);
Succeeded for the prime 2 in 3 iteration(s)
testTransverse(ZZ/7);
Succeeded for the prime 7 in 2 iteration(s)
randomSymmetricMatrix = (R, n) -> (
          entries := new MutableHashTable;
          scan(0..n-1, i -> scan(i..n-1, j -> 
                       entries#(i, j) = random(0, R)));
          matrix table(n, n, (i, j) -> if i > j then 
                       entries#(j, i) else entries#(i, j))
          );
```

### Output

```
i59 : dim I, degree I

o59 = (0, 6)

o59 : Sequence

i60 : A = R/I; numRealSturm(eliminant(p_{2,3,4}, QQ[Z]))

o61 = 6

i62 : randL = (R, n, r, l) -> 
                matrix table(n-r+1-l, n, (i, j) -> random(0, R));

i63 : testTransverse = F -> (
            R := F[apply(subsets(6, 3), i -> q_i )];
            continue := true;
            j := 0;  
            limit := 5;
            while continue and (j < limit) do (
                 j = j + 1;
                 I := fold((J, i) -> J + 
                           spSchub(3, randL(R, 6, 3, 1), q) +
                           spSchub(3, randL(R, 6, 3, 2), q),
                           Grassmannian(2, 5, R) + 
                           ideal (1 + random(1, R)),
                           {0, 1, 2});
                 if (dim I == 0) and (degree I == 6) then (
                 lin := promote(random(1, R), (R/I));
                 g := charPoly(lin, Z);
                 continue = not(1 == gcd(g, diff(Z, g)));
                 ));
            if continue then << "Failed for the prime " << char F << 
               " with " << j << " iterations" << endl;
            if not continue then << "Succeeded for the prime " <<
                char F << " in " << j << " iteration(s)" << endl;
            );

i64 : testTransverse(ZZ/2);
Failed for the prime 2 with 5 iterations

i65 : testTransverse(GF 4);
Succeeded for the prime 2 in 3 iteration(s)

i66 : testTransverse(ZZ/7);
Succeeded for the prime 7 in 2 iteration(s)

i67 : randomSymmetricMatrix = (R, n) -> (
          entries := new MutableHashTable;
          scan(0..n-1, i -> scan(i..n-1, j -> 
                       entries#(i, j) = random(0, R)));
          matrix table(n, n, (i, j) -> if i > j then 
                       entries#(j, i) else entries#(i, j))
          );
```

---

## solving / chapter.m2 — chunk 8

### Input

```macaulay2
tangentEquation = (r, R, M) -> (
           g := matrix {gens(R)};
           (entries(g * exteriorPower(r, M) * transpose g))_0_0
           );
R = QQ[apply(subsets(4, 2), i -> p_i )];
I = Grassmannian(1, 3, R) + ideal apply(0..3, i -> 
           tangentEquation(2, R, randomSymmetricMatrix(R, 4)));
dim Proj(R/I), degree I
I = Grassmannian(1, 3, R) + 
              ideal (tangentEquation(2, R, Sphere(0,0,0,5)),
                     tangentEquation(2, R, Sphere(4,1,1,5)),
                     tangentEquation(2, R, Sphere(1,4,1,5)),
                     tangentEquation(2, R, Sphere(1,1,4,5)));
dim Proj(R/I), degree I
Lines = saturate(I, ideal (p_{0,1}));
dim Proj(R/Lines), degree(Lines)
```

### Output

```
i68 : tangentEquation = (r, R, M) -> (
           g := matrix {gens(R)};
           (entries(g * exteriorPower(r, M) * transpose g))_0_0
           );

i69 : R = QQ[apply(subsets(4, 2), i -> p_i )];

i70 : I = Grassmannian(1, 3, R) + ideal apply(0..3, i -> 
           tangentEquation(2, R, randomSymmetricMatrix(R, 4)));

o70 : Ideal of R

i71 : dim Proj(R/I), degree I

o71 = (0, 32)

o71 : Sequence

i72 : I = Grassmannian(1, 3, R) + 
              ideal (tangentEquation(2, R, Sphere(0,0,0,5)),
                     tangentEquation(2, R, Sphere(4,1,1,5)),
                     tangentEquation(2, R, Sphere(1,4,1,5)),
                     tangentEquation(2, R, Sphere(1,1,4,5)));

o72 : Ideal of R

i73 : dim Proj(R/I), degree I

o73 = (1, 4)

o73 : Sequence

i74 : Lines = saturate(I, ideal (p_{0,1}));

o74 : Ideal of R

i75 : dim Proj(R/Lines), degree(Lines)

o75 = (0, 12)

o75 : Sequence
```

---

## solving / chapter.m2 — chunk 9

### Input

```macaulay2
Junk = I : Lines;
dim Proj(R/Junk), degree Junk
radical(Junk)
Two = (a, b, c, r) -> (
           matrix{{a^2 + b^2 - c^2 + r ,-a ,-b , c },
                  {         -a         , 1 , 0 , 0 },
                  {         -b         , 0 , 1 , 0 },
                  {          c         , 0 , 0 ,-1 }}
           );
One = (a, b, c, r) -> (
           matrix{{a^2 + b^2 - c^2 - r ,-a ,-b , c },
                  {         -a         , 1 , 0 , 0 },
                  {         -b         , 0 , 1 , 0 },
                  {          c         , 0 , 0 ,-1 }}
           );
R = QQ[y11, y12, y21, y22];
I = ideal (tangentTo(One( 5, 3, 3,16)), 
                 tangentTo(One( 5,-4, 2, 1)),  
                 tangentTo(One(-3,-1, 1, 1)), 
                 tangentTo(One( 2,-7, 0, 1)));
numRealSturm(charPoly(promote(y22, R/I), Z))
```

### Output

```
i76 : Junk = I : Lines;

o76 : Ideal of R

i77 : dim Proj(R/Junk), degree Junk

o77 = (1, 4)

o77 : Sequence

i78 : radical(Junk)

2         2         2
o78 = ideal (p      , p      , p      , p       + p       + p      )
              {0, 3}   {0, 2}   {0, 1}   {1, 2}    {1, 3}    {2, 3}

o78 : Ideal of R

i79 : Two = (a, b, c, r) -> (
           matrix{{a^2 + b^2 - c^2 + r ,-a ,-b , c },
                  {         -a         , 1 , 0 , 0 },
                  {         -b         , 0 , 1 , 0 },
                  {          c         , 0 , 0 ,-1 }}
           );

i80 : One = (a, b, c, r) -> (
           matrix{{a^2 + b^2 - c^2 - r ,-a ,-b , c },
                  {         -a         , 1 , 0 , 0 },
                  {         -b         , 0 , 1 , 0 },
                  {          c         , 0 , 0 ,-1 }}
           );

i81 : R = QQ[y11, y12, y21, y22];

i82 : I = ideal (tangentTo(One( 5, 3, 3,16)), 
                 tangentTo(One( 5,-4, 2, 1)),  
                 tangentTo(One(-3,-1, 1, 1)), 
                 tangentTo(One( 2,-7, 0, 1)));

o82 : Ideal of R

i83 : numRealSturm(charPoly(promote(y22, R/I), Z))

o83 = 12
```

---

## solving / chapter.m2 — chunk 10

### Input

```macaulay2
I = ideal (tangentTo(One( 3,-2,-3, 6)), 
                 tangentTo(One(-3,-7,-6, 7)),  
                 tangentTo(One(-6, 3,-5, 2)), 
                 tangentTo(Two( 1, 6,-2, 5)));
numRealSturm(charPoly(promote(y22, R/I), Z))
I = ideal (tangentTo(One( 6, 4, 6, 4)),  
                 tangentTo(One(-1, 3, 3, 6)), 
                 tangentTo(Two(-7,-2, 3, 3)), 
                 tangentTo(Two(-6, 7,-2, 5)));
numRealSturm(charPoly(promote(y22, R/I), Z))
I = ideal (tangentTo(One(-1,-4,-1, 1)),
                 tangentTo(Two(-3, 3,-1, 1)),  
                 tangentTo(Two(-7, 6, 2, 9)), 
                 tangentTo(Two( 5, 6,-1,12)));
numRealSturm(charPoly(promote(y22, R/I), Z))
I = ideal (tangentTo(Two( 5, 2,-1,25)), 
                 tangentTo(Two( 6,-6, 2,25)), 
                 tangentTo(Two(-7, 1, 6, 1)), 
                 tangentTo(Two( 3, 1, 0, 1)));
numRealSturm(charPoly(promote(y22, R/I), Z))
```

### Output

```
i84 : I = ideal (tangentTo(One( 3,-2,-3, 6)), 
                 tangentTo(One(-3,-7,-6, 7)),  
                 tangentTo(One(-6, 3,-5, 2)), 
                 tangentTo(Two( 1, 6,-2, 5)));

o84 : Ideal of R

i85 : numRealSturm(charPoly(promote(y22, R/I), Z))

o85 = 12

i86 : I = ideal (tangentTo(One( 6, 4, 6, 4)),  
                 tangentTo(One(-1, 3, 3, 6)), 
                 tangentTo(Two(-7,-2, 3, 3)), 
                 tangentTo(Two(-6, 7,-2, 5)));

o86 : Ideal of R

i87 : numRealSturm(charPoly(promote(y22, R/I), Z))

o87 = 12

i88 : I = ideal (tangentTo(One(-1,-4,-1, 1)),
                 tangentTo(Two(-3, 3,-1, 1)),  
                 tangentTo(Two(-7, 6, 2, 9)), 
                 tangentTo(Two( 5, 6,-1,12)));

o88 : Ideal of R

i89 : numRealSturm(charPoly(promote(y22, R/I), Z))

o89 = 12

i90 : I = ideal (tangentTo(Two( 5, 2,-1,25)), 
                 tangentTo(Two( 6,-6, 2,25)), 
                 tangentTo(Two(-7, 1, 6, 1)), 
                 tangentTo(Two( 3, 1, 0, 1)));

o90 : Ideal of R

i91 : numRealSturm(charPoly(promote(y22, R/I), Z))

o91 = 12
```

---

## solving / chapter.m2 — chunk 11

### Input

```macaulay2
tanQuad = (M, X) -> (
           u := X^{0};
           v := X^{1};
           (u * M * transpose v)^2 - 
           (u * M * transpose u) * (v * M * transpose v)
           );
nSphere = (V, r) -> 
               (matrix {{r + V * transpose V}} || transpose V ) |
               ( V || id_((ring r)^n)
               );
V = () -> matrix table(1, n, (i,j) -> random(0, R));
r = () -> random(0, R);
n = 4;
R = ZZ/1009[flatten(table(2, n-1, (i,j) -> z_(i,j)))];
X = 1 | matrix table(2, n-1, (i,j) -> z_(i,j))
I = ideal (apply(1..(2*n-2), 
                     i -> tanQuad(nSphere(V(), r()), X)));
```

### Output

```
i92 : tanQuad = (M, X) -> (
           u := X^{0};
           v := X^{1};
           (u * M * transpose v)^2 - 
           (u * M * transpose u) * (v * M * transpose v)
           );

i93 : nSphere = (V, r) -> 
               (matrix {{r + V * transpose V}} || transpose V ) |
               ( V || id_((ring r)^n)
               );

i94 : V = () -> matrix table(1, n, (i,j) -> random(0, R));

i95 : r = () -> random(0, R);

i96 : n = 4;

i97 : R = ZZ/1009[flatten(table(2, n-1, (i,j) -> z_(i,j)))];

i98 : X = 1 | matrix table(2, n-1, (i,j) -> z_(i,j))

o98 = | 1 0 z_(0,0) z_(0,1) z_(0,2) |
      | 0 1 z_(1,0) z_(1,1) z_(1,2) |

              2       5
o98 : Matrix R  <--- R

i99 : I = ideal (apply(1..(2*n-2), 
                     i -> tanQuad(nSphere(V(), r()), X)));

o99 : Ideal of R
```

---

## solving / chapter.m2 — chunk 12

### Input

```macaulay2
dim I, degree I
i101 :
```

### Output

```
i100 : dim I, degree I

o100 = (0, 24)

o100 : Sequence

i101 :
```

---

## solving / test.m2 — chunk 0

### Input

```macaulay2
setRandomSeed();
 -- initializing random seed
R = ZZ/101[y11, y12, y21, y22];
PolynomialSystem = apply(1..4, i -> 
                     random(0, R) + random(1, R) + random(2, R));
I = ideal PolynomialSystem;
dim I, degree I
J = ideal (random(R^4, R^7) *  transpose(
             matrix{{1, y11, y12, y21, y22, y11*y22, y12*y21}}));
dim J, degree J
K = ideal (random(R^4, R^6) * transpose( 
             matrix{{1, y11, y12, y21, y22, y11*y22 - y12*y21}}));
```

### Output

```
i1 : setRandomSeed();
 -- initializing random seed

i2 : R = ZZ/101[y11, y12, y21, y22];

i3 : PolynomialSystem = apply(1..4, i -> 
                     random(0, R) + random(1, R) + random(2, R));

i4 : I = ideal PolynomialSystem;

o4 : Ideal of R

i5 : dim I, degree I

o5 = (0, 16)

o5 : Sequence

i6 : J = ideal (random(R^4, R^7) *  transpose(
             matrix{{1, y11, y12, y21, y22, y11*y22, y12*y21}}));

o6 : Ideal of R

i7 : dim J, degree J

o7 = (0, 4)

o7 : Sequence

i8 : K = ideal (random(R^4, R^6) * transpose( 
             matrix{{1, y11, y12, y21, y22, y11*y22 - y12*y21}}));

o8 : Ideal of R
```

---

## solving / test.m2 — chunk 1

### Input

```macaulay2
dim K, degree K
R = ZZ/7[y, x, MonomialOrder=>Lex];
I = ideal (y^3*x^2 + 2*y^2*x + 3*x*y,  3*y^2 + x*y - 3*y);
J = saturate(I, ideal(y))
factor(J_1)
load "realroots.m2"
code eliminant
code regularRep
```

### Output

```
i9 : dim K, degree K

o9 = (0, 2)

o9 : Sequence

i10 : R = ZZ/7[y, x, MonomialOrder=>Lex];

i11 : I = ideal (y^3*x^2 + 2*y^2*x + 3*x*y,  3*y^2 + x*y - 3*y);

o11 : Ideal of R

i12 : J = saturate(I, ideal(y))

4    3     2
o12 = ideal (y - 2x - 1, x  + x  + 3x  + 3x)

o12 : Ideal of R

i13 : factor(J_1)

o13 = (x)(x - 2)(x + 2)(x + 1)

o13 : Expression of class Product

i14 : load "realroots.m2"

i15 : code eliminant

o15 = /Users/dan/src/M2/Macaulay2/packages/ComputationsBook/solving/realroots.m2:65:20-80:32: --source code:
      eliminant = (h, C) -> (
           Z := C_0;
           A := ring h;
           assert( dim A == 0 );
           F := coefficientRing A;
           assert( isField F );
           assert( F === coefficientRing C );
           B := basis A;
           d := numgens source B;
           M := fold((M, i) -> M || 
                     substitute(contract(B, h^(i+1)), F), 
                     substitute(contract(B, 1_A), F), 
                     flatten subsets(d, d));
           N := ((ker transpose M)).generators;
           P := matrix {toList apply(0..d, i -> Z^i)} * N;
                (flatten entries(P))_0)

i16 : code regularRep

o16 = /Users/dan/src/M2/Macaulay2/packages/ComputationsBook/solving/realroots.m2:96:16-100:45: --source code:
      regularRep = f -> (
           assert( dim ring f == 0 );
           b := basis ring f;
           k := coefficientRing ring f;
           substitute(contract(transpose b, f*b), k))
```

---

## solving / test.m2 — chunk 2

### Input

```macaulay2
code charPoly
code SturmSequence
code numRealSturm
code numPosRoots
code variations
code traceForm
code traceFormSignature
code numRealTrace
```

### Output

```
i17 : code charPoly

o17 = /Users/dan/src/M2/Macaulay2/packages/ComputationsBook/solving/realroots.m2:106:19-113:16: --source code:
      charPoly = (h, Z) -> (
           A := ring h;
           F := coefficientRing A;
           S := F[Z];
           Z  = value Z;     
           mh := regularRep(h) ** S;
           Idz := S_0 * id_(S^(numgens source mh));
           det(Idz - mh))

i18 : code SturmSequence

o18 = /Users/dan/src/M2/Macaulay2/packages/ComputationsBook/solving/realroots.m2:117:19-131:13: --source code:
      SturmSequence = f -> (
           assert( isPolynomialRing ring f );
           assert( numgens ring f === 1 );
           R := ring f;
           assert( char R == 0 );
           x := R_0;
           n := first degree f;
           c := new MutableList from toList (0 .. n);
           if n >= 0 then (
                c#0 = f;
                if n >= 1 then (
                     c#1 = diff(x,f);
                     scan(2 .. n, i -> c#i = - c#(i-2) % c#(i-1));
                     ));
           toList c)

i19 : code numRealSturm

o19 = /Users/dan/src/M2/Macaulay2/packages/ComputationsBook/solving/realroots.m2:160:18-163:41: --source code:
      numRealSturm = f -> (
           c := SturmSequence f;
           variations (signAtMinusInfinity \ c) 
               - variations (signAtInfinity \ c))

i20 : code numPosRoots

o20 = /Users/dan/src/M2/Macaulay2/packages/ComputationsBook/solving/realroots.m2:168:17-171:41: --source code:
      numPosRoots = f -> (  
           c := SturmSequence f;
           variations (signAtZero \ c) 
               - variations (signAtInfinity \ c))

i21 : code variations

o21 = /Users/dan/src/M2/Macaulay2/packages/ComputationsBook/solving/realroots.m2:183:16-191:6: --source code:
      variations = c -> (
           n := 0;
           last := 0;
           scan(c, x -> if x != 0 then (
                     if last < 0 and x > 0 or last > 0 
                        and x < 0 then n = n+1;
                     last = x;
                     ));
           n)

i22 : code traceForm

o22 = /Users/dan/src/M2/Macaulay2/packages/ComputationsBook/solving/realroots.m2:196:15-203:41: --source code:
      traceForm = h -> (
           assert( dim ring h == 0 );
           b  := basis ring h;
           k  := coefficientRing ring h;
           mm := substitute(contract(transpose b, h * b ** b), k);
           tr := matrix {apply(first entries b, x ->
                     trace regularRep x)};
           adjoint(tr * mm, source tr, source tr))

i23 : code traceFormSignature

o23 = /Users/dan/src/M2/Macaulay2/packages/ComputationsBook/solving/realroots.m2:208:24-218:43: --source code:
      traceFormSignature = h -> (
           A := ring h;
           assert( dim A == 0 );
           assert( char A == 0 );
           S := QQ[Z];
           TrF := traceForm(h) ** S;
           IdZ := Z * id_(S^(numgens source TrF));
           f := det(TrF - IdZ);
           << "The trace form S_h with h = " << h << 
             " has rank " << rank(TrF) << " and signature " << 
             numPosRoots(f) - numNegRoots(f) << endl; )

i24 : code numRealTrace

o24 = /Users/dan/src/M2/Macaulay2/packages/ComputationsBook/solving/realroots.m2:223:18-230:33: --source code:
      numRealTrace = A -> (
           assert( dim A == 0 );
           assert( char A == 0 );
           S := QQ[Z];
           TrF := traceForm(1_A) ** S;
           IdZ := Z * id_(S^(numgens source TrF));
           f := det(TrF - IdZ);
           numPosRoots(f)-numNegRoots(f))
```

---

## solving / test.m2 — chunk 3

### Input

```macaulay2
R = QQ[x, y];
I = ideal (1 - x^2*y + 2*x*y^2,  y - 2*x - x*y + x^2);
dim I, degree I
A = R/I;
time g = eliminant(x, QQ[Z])
     -- used 0.016091 seconds
time g = charPoly(x, Z)
     -- used 0.003583 seconds
numRealSturm(g), numRealTrace(A)
traceFormSignature(x*y);
The trace form S_h with h = x*y has rank 5 and signature 3
```

### Output

```
i25 : R = QQ[x, y];

i26 : I = ideal (1 - x^2*y + 2*x*y^2,  y - 2*x - x*y + x^2);

o26 : Ideal of R

i27 : dim I, degree I

o27 = (0, 5)

o27 : Sequence

i28 : A = R/I;

i29 : time g = eliminant(x, QQ[Z])
     -- used 0.016091 seconds

5     4     3    2
o29 = Z  - 5Z  + 6Z  + Z  - 2Z + 1

o29 : QQ[Z]

i30 : time g = charPoly(x, Z)
     -- used 0.003583 seconds

5     4     3    2
o30 = Z  - 5Z  + 6Z  + Z  - 2Z + 1

o30 : QQ[Z]

i31 : numRealSturm(g), numRealTrace(A)

o31 = (3, 3)

o31 : Sequence

i32 : traceFormSignature(x*y);
The trace form S_h with h = x*y has rank 5 and signature 3
```

---

## solving / test.m2 — chunk 4

### Input

```macaulay2
traceFormSignature(x - 2);
The trace form S_h with h = x - 2 has rank 5 and signature 1
traceFormSignature(x + y - 3);
The trace form S_h with h = x + y - 3 has rank 5 and signature -1
Points = {{2, 2,  0 }, {1, -2,  0}, {-3, 0, 0}, 
                {0, 0, 5/2}, {0,  0, -3}};
R = QQ[r, y11, y12, y21, y22];
P = matrix{{0, y11, y12}};
V = matrix{{1, y21, y22}};
Points = matrix Points ** R;
I = ideal apply(0..4, i -> (
                X := Points^{i};
                r * (V * transpose V)  +
                 ((X - P) * transpose V)^2) -
                 ((X - P) * transpose(X - P)) * (V * transpose V)
                );
```

### Output

```
i33 : traceFormSignature(x - 2);
The trace form S_h with h = x - 2 has rank 5 and signature 1

i34 : traceFormSignature(x + y - 3);
The trace form S_h with h = x + y - 3 has rank 5 and signature -1

i35 : Points = {{2, 2,  0 }, {1, -2,  0}, {-3, 0, 0}, 
                {0, 0, 5/2}, {0,  0, -3}};

i36 : R = QQ[r, y11, y12, y21, y22];

i37 : P = matrix{{0, y11, y12}};

1      3
o37 : Matrix R  <-- R

i38 : V = matrix{{1, y21, y22}};

1      3
o38 : Matrix R  <-- R

i39 : Points = matrix Points ** R;

5      3
o39 : Matrix R  <-- R

i40 : I = ideal apply(0..4, i -> (
                X := Points^{i};
                r * (V * transpose V)  +
                 ((X - P) * transpose V)^2) -
                 ((X - P) * transpose(X - P)) * (V * transpose V)
                );

o40 : Ideal of R
```

---

## solving / test.m2 — chunk 5

### Input

```macaulay2
dim I, degree I
A = R/I; numPosRoots(charPoly(r, Z))
Sphere = (a, b, c, r) -> (
              matrix{{a^2 + b^2 + c^2 - r ,-a ,-b ,-c },
                     {         -a         , 1 , 0 , 0 },
                     {         -b         , 0 , 1 , 0 },
                     {         -c         , 0 , 0 , 1 }}
              );
R = QQ[y11, y12, y21, y22];
tangentTo = (M) -> (
           P := matrix{{1, 0, y11, y12}};
           V := matrix{{0, 1, y21, y22}};
           (P * M * transpose V)^2 - 
             (P * M * transpose P) * (V * M * transpose V)
           );
I = ideal (tangentTo(Sphere(0,0,0,5)), 
                 tangentTo(Sphere(4,1,1,5)), 
                 tangentTo(Sphere(1,4,1,5)), 
                 tangentTo(Sphere(1,1,4,5)));
dim I, degree I
A = R/I;
```

### Output

```
i41 : dim I, degree I

o41 = (0, 6)

o41 : Sequence

i42 : A = R/I; numPosRoots(charPoly(r, Z))

o43 = 6

i44 : Sphere = (a, b, c, r) -> (
              matrix{{a^2 + b^2 + c^2 - r ,-a ,-b ,-c },
                     {         -a         , 1 , 0 , 0 },
                     {         -b         , 0 , 1 , 0 },
                     {         -c         , 0 , 0 , 1 }}
              );

i45 : R = QQ[y11, y12, y21, y22];

i46 : tangentTo = (M) -> (
           P := matrix{{1, 0, y11, y12}};
           V := matrix{{0, 1, y21, y22}};
           (P * M * transpose V)^2 - 
             (P * M * transpose P) * (V * M * transpose V)
           );

i47 : I = ideal (tangentTo(Sphere(0,0,0,5)), 
                 tangentTo(Sphere(4,1,1,5)), 
                 tangentTo(Sphere(1,4,1,5)), 
                 tangentTo(Sphere(1,1,4,5)));

o47 : Ideal of R

i48 : dim I, degree I

o48 = (0, 12)

o48 : Sequence

i49 : A = R/I;
```

---

## solving / test.m2 — chunk 6

### Input

```macaulay2
numRealSturm(eliminant(y11 - y12 + y21 + y22, QQ[Z]))
R = ZZ/101[apply(subsets(5,2), i -> p_i )];
I = Grassmannian(1, 4, R)
dim(Proj(R/I)), degree(I)
oscPlane = (i, n, s) -> (
           gamma := matrix {toList apply(1..n, i -> s^(i-1))};
           L := gamma;
           j := 0;
           while j < i-1 do (gamma = diff(s, gamma); 
                L = L || gamma;
                j = j+1);
           L);
QQ[s]; oscPlane(3, 6, s)
spSchub = (r, L, P) -> (
           I := ideal apply(subsets(numgens source L, 
                            r + numgens target L), S -> 
                fold((sum, U) -> sum +
                 fold((term,i) -> term*(-1)^i, P_(S_U) * det(
                  submatrix(L, sort toList(set(S) - set(S_U)))), U), 
                     0, subsets(#S, r))));
R = QQ[apply(subsets(6,3), i -> p_i )];
```

### Output

```
i50 : numRealSturm(eliminant(y11 - y12 + y21 + y22, QQ[Z]))

o50 = 12

i51 : R = ZZ/101[apply(subsets(5,2), i -> p_i )];

i52 : I = Grassmannian(1, 4, R)

o52 = ideal (p      p       - p      p       + p      p      , p      p       - p      p       + p      p      , p      p       - p      p       + p      p      , p      p       - p      p       + p      p      , p      p       - p      p       + p      p      )
              {2, 3} {1, 4}    {1, 3} {2, 4}    {1, 2} {3, 4}   {2, 3} {0, 4}    {0, 3} {2, 4}    {0, 2} {3, 4}   {1, 3} {0, 4}    {0, 3} {1, 4}    {0, 1} {3, 4}   {1, 2} {0, 4}    {0, 2} {1, 4}    {0, 1} {2, 4}   {1, 2} {0, 3}    {0, 2} {1, 3}    {0, 1} {2, 3}

o52 : Ideal of R

i53 : dim(Proj(R/I)), degree(I)

o53 = (6, 5)

o53 : Sequence

i54 : oscPlane = (i, n, s) -> (
           gamma := matrix {toList apply(1..n, i -> s^(i-1))};
           L := gamma;
           j := 0;
           while j < i-1 do (gamma = diff(s, gamma); 
                L = L || gamma;
                j = j+1);
           L);

i55 : QQ[s]; oscPlane(3, 6, s)

o56 = | 1 s s2 s3  s4   s5   |
      | 0 1 2s 3s2 4s3  5s4  |
      | 0 0 2  6s  12s2 20s3 |

                    3            6
o56 : Matrix (QQ[s])  <-- (QQ[s])

i57 : spSchub = (r, L, P) -> (
           I := ideal apply(subsets(numgens source L, 
                            r + numgens target L), S -> 
                fold((sum, U) -> sum +
                 fold((term,i) -> term*(-1)^i, P_(S_U) * det(
                  submatrix(L, sort toList(set(S) - set(S_U)))), U), 
                     0, subsets(#S, r))));

i58 : R = QQ[apply(subsets(6,3), i -> p_i )];
```

---

## solving / test.m2 — chunk 7

### Input

```macaulay2
I = fold((J, i) -> J +
            spSchub(3, substitute(oscPlane(3, 6, s), {s=> 1+i}), p) +
            spSchub(3, substitute(oscPlane(2, 6, s), {s=> 4+i}), p), 
            Grassmannian(2, 5, R), {0,1,2}) + 
           ideal (p_{0,1,5} - 1);
dim I, degree I
A = R/I; numRealSturm(eliminant(p_{2,3,4}, QQ[Z]))
randL = (R, n, r, l) -> 
                matrix table(n-r+1-l, n, (i, j) -> random(0, R));
testTransverse = F -> (
            R := F[apply(subsets(6, 3), i -> q_i )];
            Continue := true;
            j := 0;  
            limit := 5;
            while Continue and (j < limit) do (
                 j = j + 1;
                 I := fold((J, i) -> J + 
                           spSchub(3, randL(R, 6, 3, 1), q) +
                           spSchub(3, randL(R, 6, 3, 2), q),
                           Grassmannian(2, 5, R) + 
                           ideal (1 + random(1, R)),
                           {0, 1, 2});
                 if (dim I == 0) and (degree I == 6) then (
                 lin := promote(random(1, R), (R/I));
                 g := charPoly(lin, Z);
                 Continue = not(1 == gcd(g, diff(Z, g)));
                 ));
            if Continue then << "Failed for the prime " << char F << 
               " with " << j << " iterations" << endl;
            if not Continue then << "Succeeded for the prime " <<
                char F << " in " << j << " iteration(s)" << endl;
            );
testTransverse(ZZ/2);
Failed for the prime 2 with 5 iterations
(random 10;for i to 8 do random 2; testTransverse(GF 4);)
Succeeded for the prime 2 in 4 iteration(s)
(for i to 2 do random 2; testTransverse(ZZ/7);)
Succeeded for the prime 7 in 1 iteration(s)
```

### Output

```
i59 : I = fold((J, i) -> J +
            spSchub(3, substitute(oscPlane(3, 6, s), {s=> 1+i}), p) +
            spSchub(3, substitute(oscPlane(2, 6, s), {s=> 4+i}), p), 
            Grassmannian(2, 5, R), {0,1,2}) + 
           ideal (p_{0,1,5} - 1);

o59 : Ideal of R

i60 : dim I, degree I

o60 = (0, 6)

o60 : Sequence

i61 : A = R/I; numRealSturm(eliminant(p_{2,3,4}, QQ[Z]))

o62 = 6

i63 : randL = (R, n, r, l) -> 
                matrix table(n-r+1-l, n, (i, j) -> random(0, R));

i64 : testTransverse = F -> (
            R := F[apply(subsets(6, 3), i -> q_i )];
            Continue := true;
            j := 0;  
            limit := 5;
            while Continue and (j < limit) do (
                 j = j + 1;
                 I := fold((J, i) -> J + 
                           spSchub(3, randL(R, 6, 3, 1), q) +
                           spSchub(3, randL(R, 6, 3, 2), q),
                           Grassmannian(2, 5, R) + 
                           ideal (1 + random(1, R)),
                           {0, 1, 2});
                 if (dim I == 0) and (degree I == 6) then (
                 lin := promote(random(1, R), (R/I));
                 g := charPoly(lin, Z);
                 Continue = not(1 == gcd(g, diff(Z, g)));
                 ));
            if Continue then << "Failed for the prime " << char F << 
               " with " << j << " iterations" << endl;
            if not Continue then << "Succeeded for the prime " <<
                char F << " in " << j << " iteration(s)" << endl;
            );

i65 : testTransverse(ZZ/2);
Failed for the prime 2 with 5 iterations

i66 : (random 10;for i to 8 do random 2; testTransverse(GF 4);)
Succeeded for the prime 2 in 4 iteration(s)

i67 : (for i to 2 do random 2; testTransverse(ZZ/7);)
Succeeded for the prime 7 in 1 iteration(s)
```

---

## solving / test.m2 — chunk 8

### Input

```macaulay2
randomSymmetricMatrix = (R, n) -> (
          entries := new MutableHashTable;
          scan(0..n-1, i -> scan(i..n-1, j -> 
                       entries#(i, j) = random(0, R)));
          matrix table(n, n, (i, j) -> if i > j then 
                       entries#(j, i) else entries#(i, j))
          );
tangentEquation = (r, R, M) -> (
           g := matrix {gens(R)};
           (entries(g * exteriorPower(r, M) * transpose g))_0_0
           );
R = QQ[apply(subsets(4, 2), i -> p_i )];
I = Grassmannian(1, 3, R) + ideal apply(0..3, i -> 
           tangentEquation(2, R, randomSymmetricMatrix(R, 4)));
dim Proj(R/I), degree I
I = Grassmannian(1, 3, R) + 
              ideal (tangentEquation(2, R, Sphere(0,0,0,5)),
                     tangentEquation(2, R, Sphere(4,1,1,5)),
                     tangentEquation(2, R, Sphere(1,4,1,5)),
                     tangentEquation(2, R, Sphere(1,1,4,5)));
dim Proj(R/I), degree I
Lines = saturate(I, ideal (p_{0,1}));
```

### Output

```
i68 : randomSymmetricMatrix = (R, n) -> (
          entries := new MutableHashTable;
          scan(0..n-1, i -> scan(i..n-1, j -> 
                       entries#(i, j) = random(0, R)));
          matrix table(n, n, (i, j) -> if i > j then 
                       entries#(j, i) else entries#(i, j))
          );

i69 : tangentEquation = (r, R, M) -> (
           g := matrix {gens(R)};
           (entries(g * exteriorPower(r, M) * transpose g))_0_0
           );

i70 : R = QQ[apply(subsets(4, 2), i -> p_i )];

i71 : I = Grassmannian(1, 3, R) + ideal apply(0..3, i -> 
           tangentEquation(2, R, randomSymmetricMatrix(R, 4)));

o71 : Ideal of R

i72 : dim Proj(R/I), degree I

o72 = (0, 32)

o72 : Sequence

i73 : I = Grassmannian(1, 3, R) + 
              ideal (tangentEquation(2, R, Sphere(0,0,0,5)),
                     tangentEquation(2, R, Sphere(4,1,1,5)),
                     tangentEquation(2, R, Sphere(1,4,1,5)),
                     tangentEquation(2, R, Sphere(1,1,4,5)));

o73 : Ideal of R

i74 : dim Proj(R/I), degree I

o74 = (1, 4)

o74 : Sequence

i75 : Lines = saturate(I, ideal (p_{0,1}));

o75 : Ideal of R
```

---

## solving / test.m2 — chunk 9

### Input

```macaulay2
dim Proj(R/Lines), degree(Lines)
Junk = I : Lines;
dim Proj(R/Junk), degree Junk
radical(Junk)
Two = (a, b, c, r) -> (
           matrix{{a^2 + b^2 - c^2 + r ,-a ,-b , c },
                  {         -a         , 1 , 0 , 0 },
                  {         -b         , 0 , 1 , 0 },
                  {          c         , 0 , 0 ,-1 }}
           );
One = (a, b, c, r) -> (
           matrix{{a^2 + b^2 - c^2 - r ,-a ,-b , c },
                  {         -a         , 1 , 0 , 0 },
                  {         -b         , 0 , 1 , 0 },
                  {          c         , 0 , 0 ,-1 }}
           );
R = QQ[y11, y12, y21, y22];
I = ideal (tangentTo(One( 5, 3, 3,16)), 
                 tangentTo(One( 5,-4, 2, 1)),  
                 tangentTo(One(-3,-1, 1, 1)), 
                 tangentTo(One( 2,-7, 0, 1)));
```

### Output

```
i76 : dim Proj(R/Lines), degree(Lines)

o76 = (0, 12)

o76 : Sequence

i77 : Junk = I : Lines;

o77 : Ideal of R

i78 : dim Proj(R/Junk), degree Junk

o78 = (1, 4)

o78 : Sequence

i79 : radical(Junk)

2         2         2
o79 = ideal (p      , p      , p      , p       + p       + p      )
              {0, 3}   {0, 2}   {0, 1}   {1, 2}    {1, 3}    {2, 3}

o79 : Ideal of R

i80 : Two = (a, b, c, r) -> (
           matrix{{a^2 + b^2 - c^2 + r ,-a ,-b , c },
                  {         -a         , 1 , 0 , 0 },
                  {         -b         , 0 , 1 , 0 },
                  {          c         , 0 , 0 ,-1 }}
           );

i81 : One = (a, b, c, r) -> (
           matrix{{a^2 + b^2 - c^2 - r ,-a ,-b , c },
                  {         -a         , 1 , 0 , 0 },
                  {         -b         , 0 , 1 , 0 },
                  {          c         , 0 , 0 ,-1 }}
           );

i82 : R = QQ[y11, y12, y21, y22];

i83 : I = ideal (tangentTo(One( 5, 3, 3,16)), 
                 tangentTo(One( 5,-4, 2, 1)),  
                 tangentTo(One(-3,-1, 1, 1)), 
                 tangentTo(One( 2,-7, 0, 1)));

o83 : Ideal of R
```

---

## solving / test.m2 — chunk 10

### Input

```macaulay2
numRealSturm(charPoly(promote(y22, R/I), Z))
I = ideal (tangentTo(One( 3,-2,-3, 6)), 
                 tangentTo(One(-3,-7,-6, 7)),  
                 tangentTo(One(-6, 3,-5, 2)), 
                 tangentTo(Two( 1, 6,-2, 5)));
numRealSturm(charPoly(promote(y22, R/I), Z))
I = ideal (tangentTo(One( 6, 4, 6, 4)),  
                 tangentTo(One(-1, 3, 3, 6)), 
                 tangentTo(Two(-7,-2, 3, 3)), 
                 tangentTo(Two(-6, 7,-2, 5)));
numRealSturm(charPoly(promote(y22, R/I), Z))
I = ideal (tangentTo(One(-1,-4,-1, 1)),
                 tangentTo(Two(-3, 3,-1, 1)),  
                 tangentTo(Two(-7, 6, 2, 9)), 
                 tangentTo(Two( 5, 6,-1,12)));
numRealSturm(charPoly(promote(y22, R/I), Z))
I = ideal (tangentTo(Two( 5, 2,-1,25)), 
                 tangentTo(Two( 6,-6, 2,25)), 
                 tangentTo(Two(-7, 1, 6, 1)), 
                 tangentTo(Two( 3, 1, 0, 1)));
```

### Output

```
i84 : numRealSturm(charPoly(promote(y22, R/I), Z))

o84 = 12

i85 : I = ideal (tangentTo(One( 3,-2,-3, 6)), 
                 tangentTo(One(-3,-7,-6, 7)),  
                 tangentTo(One(-6, 3,-5, 2)), 
                 tangentTo(Two( 1, 6,-2, 5)));

o85 : Ideal of R

i86 : numRealSturm(charPoly(promote(y22, R/I), Z))

o86 = 12

i87 : I = ideal (tangentTo(One( 6, 4, 6, 4)),  
                 tangentTo(One(-1, 3, 3, 6)), 
                 tangentTo(Two(-7,-2, 3, 3)), 
                 tangentTo(Two(-6, 7,-2, 5)));

o87 : Ideal of R

i88 : numRealSturm(charPoly(promote(y22, R/I), Z))

o88 = 12

i89 : I = ideal (tangentTo(One(-1,-4,-1, 1)),
                 tangentTo(Two(-3, 3,-1, 1)),  
                 tangentTo(Two(-7, 6, 2, 9)), 
                 tangentTo(Two( 5, 6,-1,12)));

o89 : Ideal of R

i90 : numRealSturm(charPoly(promote(y22, R/I), Z))

o90 = 12

i91 : I = ideal (tangentTo(Two( 5, 2,-1,25)), 
                 tangentTo(Two( 6,-6, 2,25)), 
                 tangentTo(Two(-7, 1, 6, 1)), 
                 tangentTo(Two( 3, 1, 0, 1)));

o91 : Ideal of R
```

---

## solving / test.m2 — chunk 11

### Input

```macaulay2
numRealSturm(charPoly(promote(y22, R/I), Z))
tanQuad = (M, X) -> (
           u := X^{0};
           v := X^{1};
           (u * M * transpose v)^2 - 
           (u * M * transpose u) * (v * M * transpose v)
           );
nSphere = (V, r) -> 
               (matrix {{r + V * transpose V}} || transpose V ) |
               ( V || id_((ring r)^n)
               );
V = () -> matrix table(1, n, (i,j) -> random(0, R));
r = () -> random(0, R);
n = 4;
R = ZZ/1009[flatten(table(2, n-1, (i,j) -> z_(i,j)))];
X = 1 | matrix table(2, n-1, (i,j) -> z_(i,j))
```

### Output

```
i92 : numRealSturm(charPoly(promote(y22, R/I), Z))

o92 = 12

i93 : tanQuad = (M, X) -> (
           u := X^{0};
           v := X^{1};
           (u * M * transpose v)^2 - 
           (u * M * transpose u) * (v * M * transpose v)
           );

i94 : nSphere = (V, r) -> 
               (matrix {{r + V * transpose V}} || transpose V ) |
               ( V || id_((ring r)^n)
               );

i95 : V = () -> matrix table(1, n, (i,j) -> random(0, R));

i96 : r = () -> random(0, R);

i97 : n = 4;

i98 : R = ZZ/1009[flatten(table(2, n-1, (i,j) -> z_(i,j)))];

i99 : X = 1 | matrix table(2, n-1, (i,j) -> z_(i,j))

o99 = | 1 0 z_(0,0) z_(0,1) z_(0,2) |
      | 0 1 z_(1,0) z_(1,1) z_(1,2) |

              2      5
o99 : Matrix R  <-- R
```

---

## solving / test.m2 — chunk 12

### Input

```macaulay2
I = ideal (apply(1..(2*n-2), 
                      i -> tanQuad(nSphere(V(), r()), X)));
dim I, degree I
i102 :
```

### Output

```
i100 : I = ideal (apply(1..(2*n-2), 
                      i -> tanQuad(nSphere(V(), r()), X)));

o100 : Ideal of R

i101 : dim I, degree I

o101 = (0, 24)

o101 : Sequence

i102 :
```

---

## toricHilbertScheme / chapter.m2 — chunk 0

### Input

```macaulay2
A = {{1,1,1,1,1},{0,1,2,7,8}};
R = QQ[a..e,Degrees=>transpose A];
describe R 
B = transpose syz matrix A 
load "LLL.m2";
LLL syz matrix A 
B = transpose LLL syz matrix A 
toBinomial = (b,R) -> (
          top := 1_R; bottom := 1_R;
          scan(#b, i -> if b_i > 0 then top = top * R_i^(b_i)
               else if b_i < 0 then bottom = bottom * R_i^(-b_i));
          top - bottom);
```

### Output

```
i1 : A = {{1,1,1,1,1},{0,1,2,7,8}};

i2 : R = QQ[a..e,Degrees=>transpose A];

i3 : describe R 

o3 = QQ [a, b, c, d, e, Degrees => {{1, 0}, {1, 1}, {1, 2}, {1, 7}, {1, 8}}]

i4 : B = transpose syz matrix A 

o4 = | 1 -2 1  0 0 |
     | 0 5  -6 1 0 |
     | 0 6  -7 0 1 |

              3        5
o4 : Matrix ZZ  <--- ZZ

i5 : load "LLL.m2";

i6 : LLL syz matrix A 

o6 = | 0  1  2  |
     | 1  -1 0  |
     | -1 0  -3 |
     | -1 -1 2  |
     | 1  1  -1 |

              5        3
o6 : Matrix ZZ  <--- ZZ

i7 : B = transpose LLL syz matrix A 

o7 = | 0 1  -1 -1 1  |
     | 1 -1 0  -1 1  |
     | 2 0  -3 2  -1 |

              3        5
o7 : Matrix ZZ  <--- ZZ

i8 : toBinomial = (b,R) -> (
          top := 1_R; bottom := 1_R;
          scan(#b, i -> if b_i > 0 then top = top * R_i^(b_i)
               else if b_i < 0 then bottom = bottom * R_i^(-b_i));
          top - bottom);
```

---

## toricHilbertScheme / chapter.m2 — chunk 1

### Input

```macaulay2
J = ideal apply(entries B, b -> toBinomial(b,R)) 
scan(gens ring J, f -> J = saturate(J,f))
toricIdeal = (A) -> (
          n := #(A_0);  
          R = QQ[vars(0..n-1),Degrees=>transpose A,MonomialSize=>16]; 
          B := transpose LLL syz matrix A;
          J := ideal apply(entries B, b -> toBinomial(b,R));
          scan(gens ring J, f -> J = saturate(J,f));
          J
          );
I = toricIdeal A; 
transpose mingens I
graver = (I) -> (
          R := ring I;
          k := coefficientRing R;
          n := numgens R;
          -- construct new ring S with 2n variables
          S := k[Variables=>2*n,MonomialSize=>16];
          toS := map(S,R,(vars S)_{0..n-1});
          toR := map(R,S,vars R | matrix(R, {toList(n:1)}));
          -- embed I in S
          m := gens toS I;
          -- construct the toric ideal of the Lawrence 
          -- lifting of A
          i := 0;
          while i < n do (
              wts := join(toList(i:0),{1},toList(n-i-1:0));
              wts = join(wts,wts);
              m = homogenize(m,S_(n+i),wts);
              i=i+1;
              );
         J := ideal m;
         scan(gens ring J, f -> J = saturate(J,f));
         -- apply the map toR to the minimal generators of J 
         f := matrix entries toR mingens J;
         p := sortColumns f;
         f_p) ;
Graver = graver I 
graverFibers = (Graver) -> (
           ProductIdeal := (I) -> ( trim ideal(
              apply(numgens I, a -> ( 
                  f := I_a; leadTerm f * (leadTerm f - f))))); 
           PI := ProductIdeal ideal Graver; 
           R := ring Graver; 
           new HashTable from apply(
               unique degrees source Graver,
               d -> d => compress (basis(d,R) % PI) ));
```

### Output

```
i9 : J = ideal apply(entries B, b -> toBinomial(b,R)) 

2 2    3
o9 = ideal (- c*d + b*e, - b*d + a*e, a d  - c e)

o9 : Ideal of R

i10 : scan(gens ring J, f -> J = saturate(J,f))

i11 : toricIdeal = (A) -> (
          n := #(A_0);  
          R = QQ[vars(0..n-1),Degrees=>transpose A,MonomialSize=>16]; 
          B := transpose LLL syz matrix A;
          J := ideal apply(entries B, b -> toBinomial(b,R));
          scan(gens ring J, f -> J = saturate(J,f));
          J
          );

i12 : I = toricIdeal A; 

o12 : Ideal of R

i13 : transpose mingens I

o13 = {-2, -9}  | cd-be    |
      {-2, -8}  | bd-ae    |
      {-2, -2}  | b2-ac    |
      {-4, -14} | a2d2-c3e |
      {-4, -8}  | c4-a3e   |
      {-4, -7}  | bc3-a3d  |
      {-5, -28} | ad4-c2e3 |
      {-6, -42} | d6-ce5   |

              8       1
o13 : Matrix R  <--- R

i14 : graver = (I) -> (
          R := ring I;
          k := coefficientRing R;
          n := numgens R;
          -- construct new ring S with 2n variables
          S := k[Variables=>2*n,MonomialSize=>16];
          toS := map(S,R,(vars S)_{0..n-1});
          toR := map(R,S,vars R | matrix(R, {toList(n:1)}));
          -- embed I in S
          m := gens toS I;
          -- construct the toric ideal of the Lawrence 
          -- lifting of A
          i := 0;
          while i < n do (
              wts := join(toList(i:0),{1},toList(n-i-1:0));
              wts = join(wts,wts);
              m = homogenize(m,S_(n+i),wts);
              i=i+1;
              );
         J := ideal m;
         scan(gens ring J, f -> J = saturate(J,f));
         -- apply the map toR to the minimal generators of J 
         f := matrix entries toR mingens J;
         p := sortColumns f;
         f_p) ;

i15 : Graver = graver I 

o15 = | -cd+be -bd+ae -b2+ac -cd2+ae2 -a2d2+c3e -c4+a2bd -c4+a3e -bc3+a3d -ad4+c2e3 -abd3+c3e2 -a2d3+bc2e2 -ab2d2+c4e -a3d2+b2c2e -c5+ab3d -c5+a2b2e -b2c3+a4e -b3c2+a4d -d6+ce5 -bd5+c2e4 -ad5+bce4 -b2d4+c3e3 -a2d4+b2ce3 -b3d3+c4e2 -a3d3+b3ce2 -b4d2+c5e -a4d2+b4ce -c6+b5d -c6+ab4e -b4c2+a5e -b5c+a5d -d7+be6 -ad6+b2e5 -a2d5+b3e4 -a3d4+b4e3 -a4d3+b5e2 -a5d2+b6e -c7+a5d2 -c7+b6e -b6c+a6e -b7+a6d -d8+ae7 -b8+a7e |

              1       42
o15 : Matrix R  <--- R

i16 : graverFibers = (Graver) -> (
           ProductIdeal := (I) -> ( trim ideal(
              apply(numgens I, a -> ( 
                  f := I_a; leadTerm f * (leadTerm f - f))))); 
           PI := ProductIdeal ideal Graver; 
           R := ring Graver; 
           new HashTable from apply(
               unique degrees source Graver,
               d -> d => compress (basis(d,R) % PI) ));
```

---

## toricHilbertScheme / chapter.m2 — chunk 2

### Input

```macaulay2
fibers = graverFibers Graver 
generateAmonos = (Graver) -> (
           trueHS := poincare coker Graver;
           fibers := graverFibers Graver;
           fibers = apply(sort pairs fibers, last);
           monos = {};
           selectStandard := (fibers, J) -> (
           if #fibers == 0 then (
              if trueHS == poincare coker gens J
              then (monos = append(monos,flatten entries mingens J));
           ) else (
              P := fibers_0;
              fibers = drop(fibers,1);
              P = compress(P % J);
              nP := numgens source P; 
              -- nP is the number of monomials not in J.
              if nP > 0 then (
                 if nP == 1 then selectStandard(fibers,J)
                 else (--remove one monomial from P,take the rest.
                       P = flatten entries P;
                       scan(#P, i -> (
                            J1 := J + ideal drop(P,{i,i});
                            selectStandard(fibers, J1)))));
           ));
           selectStandard(fibers, ideal(0_(ring Graver)));
           ) ;
generateAmonos Graver;
#monos 
scan(0..9, i -> print toString monos#i) 
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, b*c*e^4, d^6}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, c*e^5, b*c*e^4, d^7}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, c*e^5, b*c*e^4, b*e^6, d^8}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, c*e^5, b*c*e^4, b*e^6, a*e^7}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, d^6, a*d^5}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, b*c^2*e^2, a*d^4, d^6}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, a*d^4, a^2*d^3, d^6}
{c*d, b*d, b^2, a^2*d^2, c^4, b*c^3, a*d^4, d^6}
{c*d, b*d, b^2, a^2*d^2, a^3*d, c^4, a*d^4, d^6}
{c*d, b*d, b^2, a^3*e, a^2*d^2, a^3*d, a*d^4, d^6}
findPositiveVector = (m,s) -> (
           expvector := first exponents s - first exponents m;
           n := #expvector;
           i := first positions(0..n-1, j -> expvector_j > 0);
           splice {i:0, 1, (n-i-1):0}
           );
flips = (M) -> (
           R := ring M;
           -- store generators of M in monoms
           monoms := first entries generators M;
           result := {};
           -- test each generator of M to see if it leads to a neighbor 
           scan(#monoms, i -> (
             m := monoms_i;
             rest := drop(monoms,{i,i});
             b := basis(degree m, R);
             s := (compress (b % M))_(0,0);
             J := ideal(m-s) + ideal rest;
             if poincare coker gens J == poincare coker gens M then (
               w := findPositiveVector(m,s);
               R1 := (coefficientRing R)[generators R, Weights=>w];
               J = substitute(J,R1);
               J = trim ideal leadTerm J;
               result = append(result,J);
               )));
           result
      );
R = QQ[a..e,Degrees=>transpose A];
```

### Output

```
i17 : fibers = graverFibers Graver 

o17 = HashTable{{2, 2} => | ac b2 |                                  }
                {2, 8} => | ae bd |
                {2, 9} => | be cd |
                {3, 16} => | ae2 bde cd2 |
                {4, 14} => | a2d2 c3e |
                {4, 7} => | a3d bc3 |
                {4, 8} => | a3e a2bd c4 |
                {5, 10} => | a3ce a2b2e a2bcd ab3d c5 |
                {5, 14} => | a3d2 ac3e b2c2e bc3d |
                {5, 16} => | a3e2 a2cd2 ab2d2 c4e |
                {5, 21} => | a2d3 bc2e2 c3de |
                {5, 22} => | a2d2e abd3 c3e2 |
                {5, 28} => | ad4 c2e3 |
                {5, 7} => | a4d abc3 b3c2 |
                {5, 8} => | a4e a3bd ac4 b2c3 |
                {6, 12} => | a3c2e a2bc2d ab4e b5d c6 |
                {6, 14} => | a4d2 a2c3e abc3d b4ce b3c2d |
                {6, 18} => | a3ce2 a2b2e2 a2c2d2 b4d2 c5e |
                {6, 21} => | a3d3 abc2e2 ac3de b3ce2 bc3d2 |
                {6, 24} => | a3e3 a2cd2e abcd3 b3d3 c4e2 |
                {6, 28} => | a2d4 ac2e3 b2ce3 c3d2e |
                {6, 30} => | a2d2e2 acd4 b2d4 c3e3 |
                {6, 35} => | ad5 bce4 c2de3 |
                {6, 36} => | ad4e bd5 c2e4 |
                {6, 42} => | ce5 d6 |
                {6, 7} => | a5d a2bc3 b5c |
                {6, 8} => | a5e a4bd a2c4 b4c2 |
                {7, 14} => | a5d2 a3c3e a2bc3d b6e b5cd c7 |
                {7, 21} => | a4d3 a2bc2e2 a2c3de abc3d2 b5e2 b3c2d2 |
                {7, 28} => | a3d4 a2c2e3 ac3d2e b4e3 bc3d3 |
                {7, 35} => | a2d5 abce4 ac2de3 b3e4 c3d3e |
                {7, 42} => | ace5 ad6 b2e5 c2d2e3 |
                {7, 49} => | be6 cde5 d7 |
                {7, 7} => | a6d a3bc3 b7 |
                {7, 8} => | a6e a5bd a3c4 b6c |
                {8, 56} => | ae7 bde6 cd2e5 d8 |
                {8, 8} => | a7e a6bd a4c4 b8 |

o17 : HashTable

i18 : generateAmonos = (Graver) -> (
           trueHS := poincare coker Graver;
           fibers := graverFibers Graver;
           fibers = apply(sort pairs fibers, last);
           monos = {};
           selectStandard := (fibers, J) -> (
           if #fibers == 0 then (
              if trueHS == poincare coker gens J
              then (monos = append(monos,flatten entries mingens J));
           ) else (
              P := fibers_0;
              fibers = drop(fibers,1);
              P = compress(P % J);
              nP := numgens source P; 
              -- nP is the number of monomials not in J.
              if nP > 0 then (
                 if nP == 1 then selectStandard(fibers,J)
                 else (--remove one monomial from P,take the rest.
                       P = flatten entries P;
                       scan(#P, i -> (
                            J1 := J + ideal drop(P,{i,i});
                            selectStandard(fibers, J1)))));
           ));
           selectStandard(fibers, ideal(0_(ring Graver)));
           ) ;

i19 : generateAmonos Graver;

i20 : #monos 

o20 = 281

i21 : scan(0..9, i -> print toString monos#i) 
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, b*c*e^4, d^6}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, c*e^5, b*c*e^4, d^7}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, c*e^5, b*c*e^4, b*e^6, d^8}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, c*e^5, b*c*e^4, b*e^6, a*e^7}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, d^6, a*d^5}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, b*c^2*e^2, a*d^4, d^6}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, a*d^4, a^2*d^3, d^6}
{c*d, b*d, b^2, a^2*d^2, c^4, b*c^3, a*d^4, d^6}
{c*d, b*d, b^2, a^2*d^2, a^3*d, c^4, a*d^4, d^6}
{c*d, b*d, b^2, a^3*e, a^2*d^2, a^3*d, a*d^4, d^6}

i22 : findPositiveVector = (m,s) -> (
           expvector := first exponents s - first exponents m;
           n := #expvector;
           i := first positions(0..n-1, j -> expvector_j > 0);
           splice {i:0, 1, (n-i-1):0}
           );

i23 : flips = (M) -> (
           R := ring M;
           -- store generators of M in monoms
           monoms := first entries generators M;
           result := {};
           -- test each generator of M to see if it leads to a neighbor 
           scan(#monoms, i -> (
             m := monoms_i;
             rest := drop(monoms,{i,i});
             b := basis(degree m, R);
             s := (compress (b % M))_(0,0);
             J := ideal(m-s) + ideal rest;
             if poincare coker gens J == poincare coker gens M then (
               w := findPositiveVector(m,s);
               R1 := (coefficientRing R)[generators R, Weights=>w];
               J = substitute(J,R1);
               J = trim ideal leadTerm J;
               result = append(result,J);
               )));
           result
      );

i24 : R = QQ[a..e,Degrees=>transpose A];
```

---

## toricHilbertScheme / chapter.m2 — chunk 3

### Input

```macaulay2
M = ideal(a*e,c*d,a*c,a^2*d^2,a^2*b*d,a^3*d,c^2*e^3,
                c^3*e^2,c^4*e,c^5,c*e^5,a*d^5,b*e^6);
F = flips M
#F
scan(#F, i -> print toString entries mingens F_i)
{{a*e, c*d, a*c, a^2*d^2, a^3*d, c^4, c^2*e^3, c^3*e^2, a*d^5, c*e^5, b*e^6}}
{{c*d, a*e, a*c, a^2*d^2, a^2*b*d, a^3*d, c^3*e^2, c^4*e, c^5, a*d^4, c*e^5, c^2*e^4, b*e^6}}
{{a*e, c*d, a*c, a^2*d^2, a^3*d, a^2*b*d, c^2*e^3, c^3*e^2, c^4*e, c^5, c*e^5, b*c*e^4, a*d^6, b*e^6}}
{{a*e, a*c, c*d, a^2*b*d, a^3*d, a^2*d^2, c^2*e^3, c^3*e^2, c^4*e, c^5, c*e^5, a*d^5, d^7}}
stdMonomials = (M) -> (
           R := ring M;
           RM := R/M;
           apply(numgens M, i -> (
                 s := basis(degree(M_i),RM); lift(s_(0,0), R)))
           );
R = QQ[a..e,Degrees => transpose A ];
M = ideal(a^3*d, a^2*b*d, a^2*d^2, a*b^3*d, a*b^2*d^2, a*b*d^3, 
                a*c, a*d^4, a*e, b^5*d, b^4*d^2, b^3*d^3, b^2*d^4, 
                b*d^5, b*e, c*e^5); 
toString stdMonomials M
```

### Output

```
i25 : M = ideal(a*e,c*d,a*c,a^2*d^2,a^2*b*d,a^3*d,c^2*e^3,
                c^3*e^2,c^4*e,c^5,c*e^5,a*d^5,b*e^6);

o25 : Ideal of R

i26 : F = flips M

2 2   3    4   2 3   3 2     5     5     6                          2 2   2      3    3 2   4    5     4     5   2 4     6                          2 2   3    2      2 3   3 2   4    5     5       4     6     6                          2      3    2 2   2 3   3 2   4    5     5     5   7
o26 = {ideal (a*e, c*d, a*c, a d , a d, c , c e , c e , a*d , c*e , b*e ), ideal (c*d, a*e, a*c, a d , a b*d, a d, c e , c e, c , a*d , c*e , c e , b*e ), ideal (a*e, c*d, a*c, a d , a d, a b*d, c e , c e , c e, c , c*e , b*c*e , a*d , b*e ), ideal (a*e, a*c, c*d, a b*d, a d, a d , c e , c e , c e, c , c*e , a*d , d )}

o26 : List

i27 : #F

o27 = 4

i28 : scan(#F, i -> print toString entries mingens F_i)
{{a*e, c*d, a*c, a^2*d^2, a^3*d, c^4, c^2*e^3, c^3*e^2, a*d^5, c*e^5, b*e^6}}
{{c*d, a*e, a*c, a^2*d^2, a^2*b*d, a^3*d, c^3*e^2, c^4*e, c^5, a*d^4, c*e^5, c^2*e^4, b*e^6}}
{{a*e, c*d, a*c, a^2*d^2, a^3*d, a^2*b*d, c^2*e^3, c^3*e^2, c^4*e, c^5, c*e^5, b*c*e^4, a*d^6, b*e^6}}
{{a*e, a*c, c*d, a^2*b*d, a^3*d, a^2*d^2, c^2*e^3, c^3*e^2, c^4*e, c^5, c*e^5, a*d^5, d^7}}

i29 : stdMonomials = (M) -> (
           R := ring M;
           RM := R/M;
           apply(numgens M, i -> (
                 s := basis(degree(M_i),RM); lift(s_(0,0), R)))
           );

i30 : R = QQ[a..e,Degrees => transpose A ];

i31 : M = ideal(a^3*d, a^2*b*d, a^2*d^2, a*b^3*d, a*b^2*d^2, a*b*d^3, 
                a*c, a*d^4, a*e, b^5*d, b^4*d^2, b^3*d^3, b^2*d^4, 
                b*d^5, b*e, c*e^5); 

o31 : Ideal of R

i32 : toString stdMonomials M 

o32 = {b*c^3, c^4, c^3*e, c^5, c^4*e, c^3*e^2, b^2, c^2*e^3, b*d, c^6, c^5*e, c^4*e^2, c^3*e^3, c^2*e^4, c*d, d^6}
```

---

## toricHilbertScheme / chapter.m2 — chunk 4

### Input

```macaulay2
inequalities = (M) -> (
              stds := stdMonomials(M);
              transpose matrix apply(numgens M, i -> (
                  flatten exponents(M_i) - 
                      flatten exponents(stds_i))));
inequalities M
primitive := (L) -> (
           n := #L-1; g := L#n;
           while n > 0 do (n = n-1; g = gcd(g, L#n););
           if g === 1 then L else apply(L, i -> i // g));
load "polarCone.m2"
decideCoherence = (M) -> (
           ineqs := inequalities M;
           c := first polarCone ineqs;
           m := - sum(numgens source c, i -> c_{i});
           prods := (transpose m) * ineqs;
           if numgens source prods != numgens source compress prods
           then false else primitive (first entries transpose m));
decideCoherence M
N = ideal(a*e,c*d,a*c,c^3*e,a^3*d,c^4,a*d^4,a^2*d^3,c*e^5,
                 c^2*e^4,d^7);
decideCoherence N
```

### Output

```
i33 : inequalities = (M) -> (
              stds := stdMonomials(M);
              transpose matrix apply(numgens M, i -> (
                  flatten exponents(M_i) - 
                      flatten exponents(stds_i))));

i34 : inequalities M

o34 = | 3  2  2  1  1  1  1  1  1  0  0  0  0  0  0  0  |
      | -1 1  0  3  2  1  -2 0  -1 5  4  3  2  1  1  0  |
      | -3 -4 -3 -5 -4 -3 1  -2 0  -6 -5 -4 -3 -2 -1 1  |
      | 1  1  2  1  2  3  0  4  -1 1  2  3  4  5  -1 -6 |
      | 0  0  -1 0  -1 -2 0  -3 1  0  -1 -2 -3 -4 1  5  |

               5        16
o34 : Matrix ZZ  <--- ZZ

i35 : primitive := (L) -> (
           n := #L-1; g := L#n;
           while n > 0 do (n = n-1; g = gcd(g, L#n););
           if g === 1 then L else apply(L, i -> i // g));

i36 : load "polarCone.m2"

i37 : decideCoherence = (M) -> (
           ineqs := inequalities M;
           c := first polarCone ineqs;
           m := - sum(numgens source c, i -> c_{i});
           prods := (transpose m) * ineqs;
           if numgens source prods != numgens source compress prods
           then false else primitive (first entries transpose m));

i38 : decideCoherence M

o38 = {0, 0, 1, 15, 18}

o38 : List

i39 : N = ideal(a*e,c*d,a*c,c^3*e,a^3*d,c^4,a*d^4,a^2*d^3,c*e^5,
                 c^2*e^4,d^7);

o39 : Ideal of R

i40 : decideCoherence N

o40 = false
```

---

## toricHilbertScheme / chapter.m2 — chunk 5

### Input

```macaulay2
A22 =
        {{1,1,1,1,1,1,1,1,1},{0,0,0,1,1,1,0,0,0},{0,0,0,0,0,0,1,1,1},
        {1,0,0,1,0,0,1,0,0},{0,1,0,0,1,0,0,1,0},{0,0,1,0,0,1,0,0,1}};
I22 = toricIdeal A22
Graver22 = graver I22;
generateAmonos(Graver22);
#monos
scan(0..9,i->print toString monos#i) 
{f*h, c*h, f*g, e*g, c*g, b*g, c*e, c*d, b*d}
{f*h, d*h, c*h, f*g, c*g, b*g, c*e, c*d, b*d}
{d*i, f*h, d*h, c*h, c*g, b*g, c*e, c*d, b*d}
{e*i, c*h, f*g, e*g, c*g, b*g, c*e, c*d, b*d}
{e*i, d*i, c*h, e*g, c*g, b*g, c*e, c*d, b*d}
{e*i, d*i, d*h, c*h, c*g, b*g, c*e, c*d, b*d}
{f*h, c*h, f*g, e*g, c*g, b*g, c*e, a*e, c*d}
{e*i, c*h, f*g, e*g, c*g, b*g, c*e, a*e, c*d, b*d*i}
{e*i, c*h, f*g, e*g, c*g, b*g, c*e, a*e, c*d, a*f*h}
{e*i, d*i, c*h, e*g, c*g, b*g, c*e, a*e, c*d}
localCoherentEquations = (IA) -> (
           -- IA is the toric ideal of A living in a ring equipped
           -- with weight order w, if we are computing the local 
           -- equations about the initial ideal of IA w.r.t. w.
           R := ring IA;
           w := (monoid R).Options.Weights;
           M := ideal leadTerm IA;
           S := first entries ((gens M) % IA);
           -- Make the universal family J in a new ring.
           nv := numgens R; n := numgens M;
           T = (coefficientRing R)[generators R, z_1 .. z_n, 
                                   Weights => flatten splice{w, n:0},
                                   MonomialSize=>16];
           M = substitute(generators M,T);
           S = apply(S, s -> substitute(s,T));
           J = ideal apply(n, i -> 
                     M_(0,i) - T_(nv + i) * S_i);
           -- Find the ideal Ihilb of local equations about M:
           spairs := (gens J) * (syz M);
           g := forceGB gens J;
           B = (coefficientRing R)[z_1 .. z_n,MonomialSize=>16];
           Fones := map(B,T, matrix(B,{splice {nv:1}}) | vars B);
           Ihilb := ideal Fones (spairs % g);
           Ihilb
           );
IA = toricIdeal A;
```

### Output

```
i41 : A22 =
        {{1,1,1,1,1,1,1,1,1},{0,0,0,1,1,1,0,0,0},{0,0,0,0,0,0,1,1,1},
        {1,0,0,1,0,0,1,0,0},{0,1,0,0,1,0,0,1,0},{0,0,1,0,0,1,0,0,1}};

i42 : I22 = toricIdeal A22

o42 = ideal (f*h - e*i, c*h - b*i, f*g - d*i, e*g - d*h, c*g - a*i, b*g - a*h, c*e - b*f, c*d - a*f, b*d - a*e)

o42 : Ideal of R

i43 : Graver22 = graver I22;

1       15
o43 : Matrix R  <--- R

i44 : generateAmonos(Graver22);

i45 : #monos

o45 = 108

i46 : scan(0..9,i->print toString monos#i) 
{f*h, c*h, f*g, e*g, c*g, b*g, c*e, c*d, b*d}
{f*h, d*h, c*h, f*g, c*g, b*g, c*e, c*d, b*d}
{d*i, f*h, d*h, c*h, c*g, b*g, c*e, c*d, b*d}
{e*i, c*h, f*g, e*g, c*g, b*g, c*e, c*d, b*d}
{e*i, d*i, c*h, e*g, c*g, b*g, c*e, c*d, b*d}
{e*i, d*i, d*h, c*h, c*g, b*g, c*e, c*d, b*d}
{f*h, c*h, f*g, e*g, c*g, b*g, c*e, a*e, c*d}
{e*i, c*h, f*g, e*g, c*g, b*g, c*e, a*e, c*d, b*d*i}
{e*i, c*h, f*g, e*g, c*g, b*g, c*e, a*e, c*d, a*f*h}
{e*i, d*i, c*h, e*g, c*g, b*g, c*e, a*e, c*d}

i47 : localCoherentEquations = (IA) -> (
           -- IA is the toric ideal of A living in a ring equipped
           -- with weight order w, if we are computing the local 
           -- equations about the initial ideal of IA w.r.t. w.
           R := ring IA;
           w := (monoid R).Options.Weights;
           M := ideal leadTerm IA;
           S := first entries ((gens M) % IA);
           -- Make the universal family J in a new ring.
           nv := numgens R; n := numgens M;
           T = (coefficientRing R)[generators R, z_1 .. z_n, 
                                   Weights => flatten splice{w, n:0},
                                   MonomialSize=>16];
           M = substitute(generators M,T);
           S = apply(S, s -> substitute(s,T));
           J = ideal apply(n, i -> 
                     M_(0,i) - T_(nv + i) * S_i);
           -- Find the ideal Ihilb of local equations about M:
           spairs := (gens J) * (syz M);
           g := forceGB gens J;
           B = (coefficientRing R)[z_1 .. z_n,MonomialSize=>16];
           Fones := map(B,T, matrix(B,{splice {nv:1}}) | vars B);
           Ihilb := ideal Fones (spairs % g);
           Ihilb
           );

i48 : IA = toricIdeal A;

o48 : Ideal of R
```

---

## toricHilbertScheme / chapter.m2 — chunk 6

### Input

```macaulay2
Y = QQ[a..e, MonomialSize => 16,
                  Degrees => transpose A, Weights => {9,3,5,0,0}];
IA = substitute(IA,Y);
JM = localCoherentEquations(IA)
load "minPres.m2";
G = removeRedundantVariables JM
ideal gens gb(G JM)
CX = QQ[a..e, z_5,z_10,z_11,z_13, Weights =>
            {9,3,5,0,0,0,0,0,0}];
F = map(CX, ring J, matrix{{a,b,c,d,e}} | 
                  substitute(G.matrix,CX))
```

### Output

```
i49 : Y = QQ[a..e, MonomialSize => 16,
                  Degrees => transpose A, Weights => {9,3,5,0,0}];

i50 : IA = substitute(IA,Y);

o50 : Ideal of Y

i51 : JM = localCoherentEquations(IA)

2                                         2                                                                                                                                                     3
o51 = ideal (z z  - z , z z  - z , - z z  + z , - z z  + z , - z z  + z , z z z  - z z , z z  - z z , z z z  - z , z z  - z z , z z  - z , z z z  - z , - z  z   + z , - z z  + z z  , z z   - z , - z z z   + z z , z z  - z z , z z  - z , - z z z  + z z , z z  - z z , z z  - z , - z z z  + z z , - z z  + z , z z   - z  , - z  z   + z , z z   - z z  , - z z  z   + z z , - z z  z   + z z , z z  - z z  , - z z   + z  , - z z  z   + z )
              1 2    3   1 2    3     4 7    2     5 8    2     1 5    4   1 5 8    4 8   1 2    5 9   1 2 5    6   3 4    1 6   3 5    6   1 2 5    6     10 11    1     2 7    3 10   1 10    7     1 4 10    1 2   3 7    2 8   1 7    8     1 5 7    1 2   3 8    2 9   1 8    9     1 5 8    1 2     5 9    3   1 13    12     11 12    2   2 10    1 12     1 11 12    1 2     2 10 11    1 2   1 4    3 11     1 13    12     1 11 13    2

o51 : Ideal of B

i52 : load "minPres.m2";

i53 : G = removeRedundantVariables JM

3  2      4  3                  2 4  3    2       3  2    4  3
o53 = map(B,B,{z  z  , z z  z  , z z  z  , z z  z  , z , z z  z  , z  z  , z  z  , z  z  , z  , z  , z  z  z  , z  })
                10 11   5 10 11   5 10 11   5 10 11   5   5 10 11   10 11   10 11   10 11   10   11   10 11 13   13

o53 : RingMap B <--- B

i54 : ideal gens gb(G JM)

3  2        2
o54 = ideal(z z  z   - z  z  z  )
             5 10 11    10 11 13

o54 : Ideal of B

i55 : CX = QQ[a..e, z_5,z_10,z_11,z_13, Weights =>
            {9,3,5,0,0,0,0,0,0}];

i56 : F = map(CX, ring J, matrix{{a,b,c,d,e}} | 
                  substitute(G.matrix,CX))

3  2      4  3                  2 4  3    2       3  2    4  3
o56 = map(CX,T,{a, b, c, d, e, z  z  , z z  z  , z z  z  , z z  z  , z , z z  z  , z  z  , z  z  , z  z  , z  , z  , z  z  z  , z  })
                                10 11   5 10 11   5 10 11   5 10 11   5   5 10 11   10 11   10 11   10 11   10   11   10 11 13   13

o56 : RingMap CX <--- T
```

---

## toricHilbertScheme / chapter.m2 — chunk 7

### Input

```macaulay2
J1 = F J
substitute(ideal(z_11^2),CX) + J1
A = {{1,1,1,1,1,1,1},{0,6,7,5,8,4,3},{3,7,2,0,7,6,1},
         {6,5,2,6,5,0,0}};
IA = toricIdeal A
Y = QQ[a..g, MonomialSize => 16,
                 Weights => {0,0,276,220,0,0,215},
                 Degrees =>transpose A];
IA = substitute(IA,Y);
M = ideal leadTerm IA
JM = localCoherentEquations(IA)
```

### Output

```
i57 : J1 = F J

3  2          2   4  3    2 2    3             2       4     3       3 2 4  3    3 2        3 2       4       2 2 3  2    5      3   4  3    2 3      4        5        4        5    6              6    7
o57 = ideal (c*d - b*e*z  z  , a*e - b*d*z z  z  , a*c - b z z  z  , a d  - c e*z z  z  , a b*d - c z , a d - b*c z z  z  , c e  - a*b*d z  z  , c e - a*b d z  z  , c  - a*b d*z  z  , c e  - a*d z  , a*d  - b*c*e z  , c*e  - d z  z  z  , b*e  - d z  )
                        10 11             5 10 11           5 10 11              5 10 11             5             5 10 11                10 11               10 11              10 11              10                11            10 11 13            13

o57 : Ideal of CX

i58 : substitute(ideal(z_11^2),CX) + J1

2                                  3  2          2   4  3    2 2    3             2       4     3       3 2 4  3    3 2        3 2       4       2 2 3  2    5      3   4  3    2 3      4        5        4        5    6              6    7
o58 = ideal (z  , c*d - b*e*z  z  , a*e - b*d*z z  z  , a*c - b z z  z  , a d  - c e*z z  z  , a b*d - c z , a d - b*c z z  z  , c e  - a*b*d z  z  , c e - a*b d z  z  , c  - a*b d*z  z  , c e  - a*d z  , a*d  - b*c*e z  , c*e  - d z  z  z  , b*e  - d z  )
              11             10 11             5 10 11           5 10 11              5 10 11             5             5 10 11                10 11               10 11              10 11              10                11            10 11 13            13

o58 : Ideal of CX

i59 : A = {{1,1,1,1,1,1,1},{0,6,7,5,8,4,3},{3,7,2,0,7,6,1},
         {6,5,2,6,5,0,0}};

i60 : IA = toricIdeal A

2 3       3 2   2     4 4    8 4   4 3 6    7 2 4     4 7 3    8 7   7 2 8    2 6 5 4   3 3 10     3 7 7   12 6        12   3     5 4 9    3 5 11   3 8   7    4 4 11   13 3 2     3 13 3   2 7 11      2 6 11   5 2 13    6 6   7   10   10    4 5 8 4   5 11 5    5 2 3 11     11 9    4 11 3 3   10 13    3     7 11   7 14 3    6 5 2 11   7   16    9 5 3 7   13 12    6 4 11 4   5 17 3    21 2      3 10 12    7 10 5 3   3 2 16 5    20 5    7   18     22 4    9 17     7 8   11   9 19    12 4 5 7   34 5 3    8 30 2 2   35 2 6    10 31 2   57   10    17 49      58 13     19 2 50    79 14    24 67 2
o60 = ideal (a c e - b*d f , a c*d*e f  - b g , d e f  - b c g , a*b c f  - e g , d e f  - a b c g , a b c  f - d e g , b  c  - a*d*e  f*g , a*c d f  - b e g  , a c d*f  - b e g  , b  c d f - a e  g , c d f   - a*b e g  , a b c   - d e f*g , d  e*f   - a b c g , a c  f  - b d e g  , a*b  c  - d e  f g , d  f   - a b*c*e g  , a c  f  - b d e g  , a b*c   - d e f g , d  f   - a b c  g , a e  f  - b  c d*g, a b  c   - d e  f g , a d e  f  - b  c g, a c*e  f - b  d g, a c  f - b d e*g  , a c   - d  e f g , b  c d  - a e  f g , b  c d  - a  e  g , b  c*d   - a  e  f*g, b  d  f - a  c e  g, b  d   - a  e  f )

o60 : Ideal of R

i61 : Y = QQ[a..g, MonomialSize => 16,
                 Weights => {0,0,276,220,0,0,215},
                 Degrees =>transpose A];

i62 : IA = substitute(IA,Y);

o62 : Ideal of Y

i63 : M = ideal leadTerm IA

2 3    8 4   7 2 4     4 7 3   5 4 3 5   2 6 5 4   3 3 10    12 6   13 3 2    3 5 11   3 8   7   6   6 7     2 6 11   5 2 13     11 9   5 11 5   4 5 8 4   14 5 3   3     7 11   7 14 3   7   16   5 2 11 7   21 2      3 10 12   6 4 11 4   20 5    22 4    9 17    9 19   2   12 4 12   2 9 7 14   2 15 18   34 5 3   35 2 6   13 15 16   36 9 2     14 11 23     20 29   57   10   58 13    79 14     39 58     34 32 62   59 57 110
o63 = ideal (a c e, b g , b c g , a*b c f , b c d f , a b c g , a b c  f, b  c , b  c d f, b e g  , a c d*f , b c*d f , a*b e g  , a b c  , a*b  c , a c  f , a b c g , b  d f , a b*c*e g  , a c  f , a b*c  , a c e  g , b  c d*g, a b  c  , a b c  g , b  c g, b  d g, a c  f, a c  , a b*c  d f  , b c d f  , a e  g  , b  c d , b  c d , b  d  f  , b  d f , a*c  d  f  , a*e  g  , b  c*d  , b  d  f, b  d  , b*e  g  , b*c  d  f  , c  d  f   )

o63 : Ideal of Y

i64 : JM = localCoherentEquations(IA)

2
o64 = ideal (z z  - z , z z  - z , z z  - z , z z  - z , z z  - z , z z  - z , z z   - z , - z  z   + z , z z  - z , z z  - z , z z   - z  , - z z  + z , z z  - z  , z z   - z , - z z  + z , z z  - z  , z z z  - z , - z z   + z , z z   - z , z z   - z  , z z  - z  , z z  - z  , z z  - z  , z z  - z , z z z   - z , - z z   + z , - z z   + z , z z  - z  , - z z   + z , - z z   + z , z z  - z  , z z   - z  , - z z   + z , - z z   + z , z z   - z  , z z   - z  , - z  z   + z , z z   - z  , - z z   + z , z z   - z  , z z  - z , - z z   + z , - z  z   + z , z z  - z  , z z   - z , - z z   + z , z z   - z  , z z z  - z  , - z z   + z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z z  - z , - z  z   + z , - z  z   + z , - z  z   + z , z z  - z  , z z   - z  , z z   - z  , z z   - z  , - z z   + z  , z z   - z  , z z   - z  , z z   - z  , z z  - z  , z z   - z  , z  z   - z  , z  z   - z  , z z  - z  , z z   - z  , z z z   - z  , z z   - z  , z z   - z  , z z   - z  , - z z   + z  , z z   - z  , z z   - z  , - z z   + z  , z z  - z  , - z z   + z , z z  - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , - z z   + z  , z z   - z  , - z  z   + z , z z   - z  , - z  z   + z , z z   - z  , z z   - z  , - z  z   + z , - z  z   + z , - z  z   + z , - z  z   + z , - z  z   + z , z  z   - z  , - z  z   + z  , - z z   + z  , - z z   + z  , - z z   + z  , - z  z   + z , - z  z   + z  , z z   - z  , z z  z   - z  , z z   - z  , z  z   - z  , - z  z   + z  , z z   - z  , z z   - z  , - z  z   + z  , - z  z   + z  , z  z   - z  , - z z   + z  , z z   - z  , z  z   - z  , z  z   - z  , - z z  z   + z , - z z   + z  , z  z   - z  , - z  z   + z  , z  z   - z  , - z  z   + z , - z  z   + z  , - z  z   + z  , - z  z   + z  , - z  z   + z  , z  z   - z  , z  z   - z  , z  z   - z  , z  z   - z  , z  z   - z  , - z z   + z  , z  z   - z  , z  z   - z  , z  z   - z  , z  z   - z  , - z  z   + z  , z  z   - z  z  , - z  z   + z  , - z  z   + z  , z  z   - z  z  , z  z   - z  , - z  z   + z  , z  z   - z  z  )
              1 2    3   1 2    3   1 5    4   1 3    6   1 3    6   1 4    7   1 12    5     10 11    1   1 4    7   1 9    8   1 10    13     1 5    4   1 7    14   1 18    9     1 9    8   1 8    15   1 2 5    8     4 10    3   4 13    6   1 11    16   1 6    17   1 6    17   1 7    14   2 4    8   1 2 12    9     1 12    5     2 11    4   1 8    15     5 13    3     5 10    2   3 4    15   1 13    19     3 11    7     2 16    7   4 19    17   1 10    13     10 11    1   1 11    16     7 10    6   7 13    17   2 5    9     1 18    9     12 22    1   2 7    15   5 19    6     4 10    3   1 13    19   1 2 4    15     3 16    14   1 16    20   1 14    21   1 14    21   2 12    18   3 5    8     12 22    1     12 13    2     12 19    3   3 7    24   1 15    24   1 15    24   1 16    20     2 20    14   7 19    25   1 17    25   1 17    25   2 8    26   3 20    21   10 14    17   13 14    25   2 9    23   2 12    18   1 2 18    23   1 23    26   2 14    24   1 20    28     2 28    21   1 27    23   1 23    26     1 27    23   3 9    26     3 12    9   2 8    26   2 14    24   1 20    28   3 28    29   1 21    29   1 21    29   2 18    27     2 22    19   2 18    27     10 30    4   3 18    23     18 22    3   1 31    30   5 11    30     10 31    5     10 30    4     31 32    1     10 31    5     13 31    4   11 12    31     12 32    10     5 32    13     1 31    30     4 32    19     31 32    1     11 32    22   9 23    33   1 18 23    33   8 27    33   18 23    34     22 35    12   1 34    33   9 27    34     19 35    18     22 35    12   18 23    34     1 34    33   1 36    34   18 27    36   18 27    36     1 32 35    2     1 36    34   10 37    31     31 38    13   10 32    38     37 38    1     10 37    31     13 37    30     32 37    11     31 38    13   27 34    39   27 34    39   23 36    39   27 36    40   27 36    40     1 40    39   23 40    41   27 39    41   27 39    41   37 42    38     37 42    38   10 38    31 42     42 43    31     42 43    31   31 37    38 43   42 44    43     42 44    43   37 43    38 44

o64 : Ideal of B
```

---

## toricHilbertScheme / chapter.m2 — chunk 8

### Input

```macaulay2
G = removeRedundantVariables JM;
toString ideal gens gb(G JM)
K = ideal(z_32*z_42*z_44-z_37^2,z_32^4*z_35-z_42,
          z_32^3*z_35*z_37^2-z_42^2*z_44,z_32^2*z_35*z_37^4-z_42^3*z_44^2,
          z_32*z_35*z_37^6-z_42^4*z_44^3,z_35*z_37^8-z_42^5*z_44^4);
GG = removeRedundantVariables K;
ideal gens gb (GG K)
A = {{1,1,1,1},{0,1,2,3}};
I = toricIdeal A;
Graver = graver I;
```

### Output

```
i65 : G = removeRedundantVariables JM;

o65 : RingMap B <--- B

i66 : toString ideal gens gb(G JM)

o66 = ideal(z_32*z_42^2*z_44-z_37^2*z_42,z_32^3*z_35*z_37^2-z_42^2*z_44,z_32^4*z_35*z_37-z_37*z_42,z_32^2*z_35*z_37^4*z_42-z_42^4*z_44^2,z_32*z_35*z_37^6*z_42-z_42^5*z_44^3,z_35*z_37^8*z_42-z_42^6*z_44^4)

i67 : K = ideal(z_32*z_42*z_44-z_37^2,z_32^4*z_35-z_42,
          z_32^3*z_35*z_37^2-z_42^2*z_44,z_32^2*z_35*z_37^4-z_42^3*z_44^2,
          z_32*z_35*z_37^6-z_42^4*z_44^3,z_35*z_37^8-z_42^5*z_44^4);

o67 : Ideal of B

i68 : GG = removeRedundantVariables K;

o68 : RingMap B <--- B

i69 : ideal gens gb (GG K)

5           2
o69 = ideal(z  z  z   - z  )
             32 35 44    37

o69 : Ideal of B

i70 : A = {{1,1,1,1},{0,1,2,3}};

i71 : I = toricIdeal A;

o71 : Ideal of R

i72 : Graver = graver I;

1       5
o72 : Matrix R  <--- R
```

---

## toricHilbertScheme / chapter.m2 — chunk 9

### Input

```macaulay2
fibers = graverFibers Graver;
peek fibers
G = trim product(values fibers, ideal)
numgens G
z = symbol z;
S = QQ[a,b,c,d,z];
zG = z ** substitute(gens G, S);
R = QQ[y_1 .. y_22];
```

### Output

```
i73 : fibers = graverFibers Graver;

i74 : peek fibers

o74 = HashTable{{2, 2} => | ac b2 |     }
                {2, 3} => | ad bc |
                {2, 4} => | bd c2 |
                {3, 3} => | a2d abc b3 |
                {3, 6} => | ad2 bcd c3 |

i75 : G = trim product(values fibers, ideal)

5     5   4 3 5   5 3 4   4 2 2 4   3 4   4   2 6 4   4   4 3   3 3 3 3   2 5 2 3     7   3   4 6 2   3 2 5 2   2 4 4 2     6 3 2   8 2 2   3   7    2 3 6      5 5    7 4    2 2 8     4 7   6 6
o75 = ideal (a b*c*d , a b d , a c d , a b c d , a b c*d , a b d , a b*c d , a b c d , a b c d , a*b c*d , a c d , a b c d , a b c d , a*b c d , b c d , a b*c d, a b c d, a*b c d, b c d, a b c , a*b c , b c )

o75 : Ideal of R

i76 : numgens G

o76 = 22

i77 : z = symbol z;

i78 : S = QQ[a,b,c,d,z];

i79 : zG = z ** substitute(gens G, S);

1       22
o79 : Matrix S  <--- S

i80 : R = QQ[y_1 .. y_22];
```

---

## toricHilbertScheme / chapter.m2 — chunk 10

### Input

```macaulay2
F = map(S,R,zG)
PA = trim ker F
codim PA
degree PA
Aff = apply(1..22, v -> (
                             K = substitute(PA,y_v => 1);
                             FF = removeRedundantVariables K;
                             ideal gens gb (FF K)));
scan(Aff, i -> print toString i);
ideal()
ideal()
ideal()
ideal(y_1^4*y_5*y_21-1)
ideal(y_1^4*y_6^6*y_21-1)
ideal()
ideal(y_1^2*y_11^2*y_17-1)
ideal(y_1^3*y_9^2*y_21^2-1)
ideal(y_6^3*y_21-y_10,y_1*y_10^3-y_6^2,y_1*y_6*y_10^2*y_21-1)
ideal(y_6*y_15-1,y_2*y_15^2-y_6*y_14,y_6^2*y_14-y_2*y_15)
ideal()
ideal(y_11*y_13-1,y_1^2*y_21^3-y_13^2)
ideal(y_1^2*y_14^3*y_21^3-1)
ideal(y_10^2*y_21-1,y_1*y_15^4-y_10^3)
ideal()
ideal(y_11*y_20-1,y_3*y_20^2-y_11*y_17,y_11^2*y_17-y_3*y_20)
ideal(y_11*y_18*y_21-1,y_1*y_21^3-y_11*y_18^2,y_11^2*y_18^3-y_1*y_21^2)
ideal(y_1*y_19^4*y_21^4-1)
ideal(y_15*y_22-1)
ideal()
ideal(y_20*y_22-1)
ideal()
code primitive
code toZZ
```

### Output

```
i81 : F = map(S,R,zG)

5     5    4 3 5    5 3 4    4 2 2 4    3 4   4    2 6 4    4   4 3    3 3 3 3    2 5 2 3      7   3    4 6 2    3 2 5 2    2 4 4 2      6 3 2    8 2 2    3   7      2 3 6        5 5      7 4      2 2 8      4 7    6 6
o81 = map(S,R,{a b*c*d z, a b d z, a c d z, a b c d z, a b c*d z, a b d z, a b*c d z, a b c d z, a b c d z, a*b c*d z, a c d z, a b c d z, a b c d z, a*b c d z, b c d z, a b*c d*z, a b c d*z, a*b c d*z, b c d*z, a b c z, a*b c z, b c z})

o81 : RingMap S <--- R

i82 : PA = trim ker F

2                                                                                                                                                                                                                                                                                                                                                                                                                                                                               2                                                                                                                                                                                                            2                                                                                                                                                                                                                                                                        2                                                                                                                                                                                                                                                      2                                                                                                                                                                                                                                                                                                                                                  2                                                                                                                                                                                                    2                                                                                                                                                                                    2                                                                                                                                                                                                                                                                                             2                                                                                                      2                                                                                                             2                                                                                              2                                                                                                                         2                                                  2
o82 = ideal (y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y  y  , y  y   - y  y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y  y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y  y   - y  y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y , y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y , y y  - y y  , y y  - y y  , y y  - y y , y  - y y  , y y  - y y , y y  - y y , y y  - y y , y  - y y , y y  - y y , y y  - y y , y y  - y y )
              21    20 22   19 21    18 22   18 21    17 22   17 21    16 22   15 21    14 22   14 21    13 22   13 21    12 22   12 21    11 22   10 21    9 22   9 21    8 22   8 21    7 22   6 21    5 22   5 21    4 22   4 21    3 22   2 21    1 22   19 20    17 22   18 20    16 22   17 20    16 21   15 20    13 22   14 20    12 22   13 20    11 22   12 20    11 21   10 20    8 22   9 20    7 22   8 20    7 21   6 20    4 22   5 20    3 22   4 20    3 21   2 20    1 21   19    15 22   18 19    14 22   17 19    13 22   16 19    12 22   14 19    10 22   13 19    9 22   12 19    8 22   11 19    7 22   9 19    6 22   8 19    5 22   7 19    4 22   4 19    2 22   3 19    1 22   18    13 22   17 18    12 22   16 18    11 22   15 18    10 22   14 18    9 22   13 18    8 22   12 18    7 22   11 18    7 21   10 18    6 22   9 18    5 22   8 18    4 22   7 18    3 22   6 18    5 19   5 18    2 22   4 18    1 22   3 18    1 21   2 18    1 19   17    11 22   16 17    11 21   15 17    9 22   14 17    8 22   13 17    7 22   12 17    7 21   11 17    7 20   10 17    5 22   9 17    4 22   8 17    3 22   7 17    3 21   6 17    2 22   5 17    1 22   4 17    1 21   3 17    1 20   2 17    1 18   16    11 20   15 16    8 22   14 16    7 22   13 16    7 21   12 16    7 20   10 16    4 22   9 16    3 22   8 16    3 21   7 16    3 20   6 16    1 22   5 16    1 21   4 16    1 20   2 16    1 17   14 15    10 19   13 15    6 22   12 15    5 22   11 15    4 22   9 15    6 19   8 15    5 19   7 15    2 22   4 15    2 19   3 15    1 19   14    6 22   13 14    5 22   12 14    4 22   11 14    3 22   10 14    6 19   9 14    5 19   8 14    2 22   7 14    1 22   6 14    5 15   5 14    2 19   4 14    1 19   3 14    1 18   2 14    1 15   13    4 22   12 13    3 22   11 13    3 21   10 13    5 19   9 13    2 22   8 13    1 22   7 13    1 21   6 13    2 19   5 13    1 19   4 13    1 18   3 13    1 17   2 13    1 14   12    3 21   11 12    3 20   10 12    2 22   9 12    1 22   8 12    1 21   7 12    1 20   6 12    1 19   5 12    1 18   4 12    1 17   3 12    1 16   2 12    1 13   10 11    1 22   9 11    1 21   8 11    1 20   7 11    3 16   6 11    1 18   5 11    1 17   4 11    1 16   2 11    1 12   10    6 15   9 10    5 15   8 10    2 19   7 10    1 19   5 10    2 15   4 10    1 15   3 10    1 14   9    2 19   8 9    1 19   7 9    1 18   6 9    2 15   5 9    1 15   4 9    1 14   3 9    1 13   2 9    1 10   8    1 18   7 8    1 17   6 8    1 15   5 8    1 14   4 8    1 13   3 8    1 12   2 8    1 9   7    1 16   6 7    1 14   5 7    1 13   4 7    1 12   3 7    1 11   2 7    1 8   5 6    2 10   4 6    1 10   3 6    1 9   5    1 10   4 5    1 9   3 5    1 8   2 5    1 6   4    1 8   3 4    1 7   2 4    1 5   2 3    1 4

o82 : Ideal of R

i83 : codim PA

o83 = 19

i84 : degree PA

o84 = 30

i85 : Aff = apply(1..22, v -> (
                             K = substitute(PA,y_v => 1);
                             FF = removeRedundantVariables K;
                             ideal gens gb (FF K)));

i86 : scan(Aff, i -> print toString i);
ideal()
ideal()
ideal()
ideal(y_1^4*y_5*y_21-1)
ideal(y_1^4*y_6^6*y_21-1)
ideal()
ideal(y_1^2*y_11^2*y_17-1)
ideal(y_1^3*y_9^2*y_21^2-1)
ideal(y_6^3*y_21-y_10,y_1*y_10^3-y_6^2,y_1*y_6*y_10^2*y_21-1)
ideal(y_6*y_15-1,y_2*y_15^2-y_6*y_14,y_6^2*y_14-y_2*y_15)
ideal()
ideal(y_11*y_13-1,y_1^2*y_21^3-y_13^2)
ideal(y_1^2*y_14^3*y_21^3-1)
ideal(y_10^2*y_21-1,y_1*y_15^4-y_10^3)
ideal()
ideal(y_11*y_20-1,y_3*y_20^2-y_11*y_17,y_11^2*y_17-y_3*y_20)
ideal(y_11*y_18*y_21-1,y_1*y_21^3-y_11*y_18^2,y_11^2*y_18^3-y_1*y_21^2)
ideal(y_1*y_19^4*y_21^4-1)
ideal(y_15*y_22-1)
ideal()
ideal(y_20*y_22-1)
ideal()

i87 : code primitive

o87 = -- polarCone.m2:16-20
      primitive = (L) -> (
           n := #L-1;                    g := L#n;
           while n > 0 do (n = n-1;      g = gcd(g, L#n);
                if g === 1 then n = 0);
           if g === 1 then L else apply(L, i -> i // g));

i88 : code toZZ

o88 = -- polarCone.m2:28-32
      toZZ = (L) -> (
           d := apply(L, e -> denominator e);
           R := ring d#0;             l := 1_R;
           scan(d, i -> (l = (l*i // gcd(l,i))));    
           apply(L, e -> (numerator(l*e))));
```

---

## toricHilbertScheme / chapter.m2 — chunk 11

### Input

```macaulay2
code rotateMatrix
code isRedundant
code fourierMotzkin
code(polarCone,Matrix,Matrix)
code(polarCone,Matrix)
H = transpose matrix{
      {1,2,3},
      {1,3,2},
      {2,1,3},
      {2,3,1},
      {3,1,2},
      {3,2,1}};
P = polarCone H
Q = polarCone P_0
```

### Output

```
i89 : code rotateMatrix

o89 = -- polarCone.m2:41-43
      rotateMatrix = (M) -> (
           r := rank source M;        c := rank target M;
           matrix table(r, c, (i,j) -> M_(c-j-1, r-i-1)));

i90 : code isRedundant

o90 = -- polarCone.m2:57-65
      isRedundant = (V, vert) -> (
           -- the row vector is redundant iff 'vert' contains an
           -- entry in 'V'.
           x := 0;            k := 0;
           numRow := #V;      -- equals the number of inequalities
           while x < 1 and k < numRow do (
                if isSubset(V#k, vert) then x = x+1;
                k = k+1;);     
           x === 1);

i91 : code fourierMotzkin

o91 = -- polarCone.m2:89-118
      fourierMotzkin = (A, V, spot) -> (
           -- initializing local variables
           numRow := #A;               -- equal to the length of V
           numCol := #(A#0);           pos := {};       
           neg := {};                  projA := {};     
           projV := {};                k := 0;
           -- divide the inequalities into three groups.
           while k < numRow do (
                if A#k#0 < 0 then neg = append(neg, k)
                else if A#k#0 > 0 then pos = append(pos, k)
                else (projA = append(projA, A#k);
                     projV = append(projV, V#k););
                k = k+1;);      
           -- generate new irredundant inequalities.
           scan(pos, i -> scan(neg, j -> (vert := V#i + V#j;
                          if not isRedundant(projV, vert)  
                          then (iRow := A#i;     jRow := A#j;
                               iCoeff := - jRow#0;
                               jCoeff := iRow#0;
                               a := iCoeff*iRow + jCoeff*jRow;
                               projA = append(projA, a);
                               projV = append(projV, vert););)));
           -- don't forget the implicit inequalities '-t <= 0'.
           scan(pos, i -> (vert := V#i + set{spot};
                if not isRedundant(projV, vert) then (
                     projA = append(projA, A#i);
                     projV = append(projV, vert););));
           -- remove the first column 
           projA = apply(projA, e -> e_{1..(numCol-1)});
           {projA, projV});

i92 : code(polarCone,Matrix,Matrix)

o92 = -- polarCone.m2:137-192
      polarCone(Matrix, Matrix) := (Z, H) -> (
           R := ring source Z;
           if R =!= ring source H then error ("polarCone: " | 
                "expected matrices over the same ring");
           if rank target Z =!= rank target H then error (
                "polarCone: expected matrices to have the " |
                "same number of rows");     
           if (R =!= ZZ) then error ("polarCone: expected " | 
                "matrices over 'ZZ'");
           -- expressing 'cone(Y)+affine(B)' as '{x : Ax <= 0}'
           Y := substitute(Z, QQ);     B := substitute(H, QQ);   
           if rank source B > 0 then Y = Y | B | -B;
           n := rank source Y;         d := rank target Y;     
           A := Y | -id_(QQ^d);
           -- computing the row echelon form of 'A'
           A = gens gb rotateMatrix A;
           L := rotateMatrix leadTerm A;
           A = rotateMatrix A;
           -- find pivots
           numRow = rank target A;                  -- numRow <= d
           i := 0;                     pivotCol := {};
           while i < numRow do (j := 0;
                while j < n+d and L_(i,j) =!= 1_QQ do j = j+1;
                pivotCol = append(pivotCol, j);
                i = i+1;);
           -- computing the row-reduced echelon form of 'A'
           A = ((submatrix(A, pivotCol))^(-1)) * A;
           -- converting 'A' into a list of integer row vectors 
           A = entries A;
           A = apply(A, e -> primitive toZZ e);
           -- creating the vertex list 'V' for double description
           -- and listing the variables 'T' which remain to be
           -- eliminated
           V := {};                    T := toList(0..(n-1));
           scan(pivotCol, e -> (if e < n then (T = delete(e, T);
                          V = append(V, set{e});)));
           -- separating inequalities 'A' and equalities 'E'
           eqnRow := {};               ineqnRow := {};
           scan(numRow, i -> (if pivotCol#i >= n then 
                     eqnRow = append(eqnRow, i)
                     else ineqnRow = append(ineqnRow, i);));    
           E := apply(eqnRow, i -> A#i);
           E = apply(E, e -> e_{n..(n+d-1)});
           A = apply(ineqnRow, i -> A#i);
           A = apply(A, e -> e_(T | toList(n..(n+d-1)))); 
           -- successive projections eliminate the variables 'T'.
           if A =!= {} then scan(T, t -> (
                     D := fourierMotzkin(A, V, t);
                     A = D#0;          V = D#1;));
           -- output formatting
           A = apply(A, e -> primitive e);
           if A === {} then A = map(ZZ^d, ZZ^0, 0)
           else A = transpose matrix A;
           if E === {} then E = map(ZZ^d, ZZ^0, 0)
           else E = transpose matrix E;
           (A, E));

i93 : code(polarCone,Matrix)

o93 = -- polarCone.m2:199-200
      polarCone(Matrix) := (Z) -> (
           polarCone(Z, map(ZZ^(rank target Z), ZZ^0, 0)));

i94 : H = transpose matrix{
      {1,2,3},
      {1,3,2},
      {2,1,3},
      {2,3,1},
      {3,1,2},
      {3,2,1}};

3        6
o94 : Matrix ZZ  <--- ZZ

i95 : P = polarCone H

o95 = (| 1  1  1  -1 -1 -5 |, 0)
       | -1 1  -5 1  -1 1  |
       | -1 -5 1  -1 1  1  |

o95 : Sequence

i96 : Q = polarCone P_0

o96 = (| 1 1 2 2 3 3 |, 0)
       | 2 3 1 3 1 2 |
       | 3 2 3 1 2 1 |

o96 : Sequence
```

---

## toricHilbertScheme / chapter.m2 — chunk 12

### Input

```macaulay2
A = QQ[a..e];
I = ideal(a-b^2-1, b-c^2, c-d^2, a^2-e^2)
F = removeRedundantVariables I
I1 = ideal gens gb(F I)
ideal compress (F.matrix - vars A) + I1
code findRedundant
code removeRedundantVariables
i104 :
```

### Output

```
i97 : A = QQ[a..e];

i98 : I = ideal(a-b^2-1, b-c^2, c-d^2, a^2-e^2)

2             2         2       2    2
o98 = ideal (- b  + a - 1, - c  + b, - d  + c, a  - e )

o98 : Ideal of A

i99 : F = removeRedundantVariables I

8       4   2
o99 = map(A,A,{d  + 1, d , d , d, e})

o99 : RingMap A <--- A

i100 : I1 = ideal gens gb(F I)

16     8    2
o100 = ideal(d   + 2d  - e  + 1)

o100 : Ideal of A

i101 : ideal compress (F.matrix - vars A) + I1

8           4       2       16     8    2
o101 = ideal (d  - a + 1, d  - b, d  - c, d   + 2d  - e  + 1)

o101 : Ideal of A

i102 : code findRedundant

o102 = -- minPres.m2:1-12
       findRedundant=(f)->(
            A := ring(f);
            p := first entries contract(vars A,f);
            i := position(p, g -> g != 0 and first degree g === 0);
            if i === null then
                null
            else (
                 v := A_i;
                 c := f_v;
                 {i,(-1)*(c^(-1)*(f-c*v))}
                 )
            )

i103 : code removeRedundantVariables

o103 = -- minPres.m2:14-39
       removeRedundantVariables = (I) -> (
            A := ring I;
            xmap := new MutableList from gens A;       
            M := gens I;
            findnext := () -> (
                 p := null;
                 next := 0;
                 done := false;
                 ngens := numgens source M;
                 while next < ngens and not done do (
                   p = findRedundant(M_(0,next));
                   if p =!= null then
                        done = true
                   else next=next+1;
                 );
                 p);
            p := findnext();
            while p =!= null do (
                 xmap#(p#0) = p#1;
                 F1 := map(A,A,toList xmap);
                 F2 := map(A,A, F1 (F1.matrix));
                 xmap = new MutableList from first entries F2.matrix;
                 M = compress(F2 M);
                 p = findnext();
                 );
            map(A,A,toList xmap));

i104 :
```

---

## toricHilbertScheme / test.m2 — chunk 0

### Input

```macaulay2
A = {{1,1,1,1,1},{0,1,2,7,8}};
R = QQ[a..e,Degrees=>transpose A];
describe R 
B = transpose syz matrix A 
needsPackage "LLLBases";
LLL syz matrix A 
B = transpose LLL syz matrix A 
toBinomial = (b,R) -> (
          top := 1_R; bottom := 1_R;
          scan(#b, i -> if b_i > 0 then top = top * R_i^(b_i)
               else if b_i < 0 then bottom = bottom * R_i^(-b_i));
          top - bottom);
```

### Output

```
i1 : A = {{1,1,1,1,1},{0,1,2,7,8}};

i2 : R = QQ[a..e,Degrees=>transpose A];

i3 : describe R 

o3 = QQ[a..e, Degrees => {{1}, {1}, {1}, {1}, {1}}, Heft => {1, 0}]
                          {0}  {1}  {2}  {7}  {8}

i4 : B = transpose syz matrix A 

o4 = | 1 -2 1  0 0 |
     | 0 5  -6 1 0 |
     | 0 6  -7 0 1 |

              3       5
o4 : Matrix ZZ  <-- ZZ

i5 : needsPackage "LLLBases";

i6 : LLL syz matrix A 

o6 = | 0  1  2  |
     | 1  -1 0  |
     | -1 0  -3 |
     | -1 -1 2  |
     | 1  1  -1 |

              5       3
o6 : Matrix ZZ  <-- ZZ

i7 : B = transpose LLL syz matrix A 

o7 = | 0 1  -1 -1 1  |
     | 1 -1 0  -1 1  |
     | 2 0  -3 2  -1 |

              3       5
o7 : Matrix ZZ  <-- ZZ

i8 : toBinomial = (b,R) -> (
          top := 1_R; bottom := 1_R;
          scan(#b, i -> if b_i > 0 then top = top * R_i^(b_i)
               else if b_i < 0 then bottom = bottom * R_i^(-b_i));
          top - bottom);
```

---

## toricHilbertScheme / test.m2 — chunk 1

### Input

```macaulay2
J = ideal apply(entries B, b -> toBinomial(b,R)) 
scan(gens ring J, f -> J = saturate(J,f))
toricIdeal = (A) -> (
          n := #(A_0);  
          R = QQ[vars(0..n-1),Degrees=>transpose A,MonomialSize=>16]; 
          B := transpose LLL syz matrix A;
          J := ideal apply(entries B, b -> toBinomial(b,R));
          scan(gens ring J, f -> J = saturate(J,f));
          J
          );
I = toricIdeal A; 
transpose mingens I
graver = (I) -> (
          R := ring I;
          k := coefficientRing R;
          n := numgens R;
          -- construct new ring S with 2n variables
          S := k[Variables=>2*n,MonomialSize=>16];
          toS := map(S,R,(vars S)_{0..n-1});
          toR := map(R,S,vars R | matrix(R, {toList(n:1)}));
          -- embed I in S
          m := gens toS I;
          -- construct the toric ideal of the Lawrence 
          -- lifting of A
          i := 0;
          while i < n do (
              wts := join(toList(i:0),{1},toList(n-i-1:0));
              wts = join(wts,wts);
              m = homogenize(m,S_(n+i),wts);
              i=i+1;
              );
         J := ideal m;
         scan(gens ring J, f -> J = saturate(J,f));
         -- apply the map toR to the minimal generators of J 
         f := matrix entries toR mingens J;
         p := sortColumns f;
         f_p) ;
Graver = graver I 
graverFibers = (Graver) -> (
           ProductIdeal := (I) -> ( trim ideal(
              apply(numgens I, a -> ( 
                  f := I_a; leadTerm f * (leadTerm f - f))))); 
           PI := ProductIdeal ideal Graver; 
           R := ring Graver; 
           new HashTable from apply(
               unique degrees source Graver,
               d -> d => compress (basis(d,R) % PI) ));
```

### Output

```
i9 : J = ideal apply(entries B, b -> toBinomial(b,R)) 

2 2    3
o9 = ideal (- c*d + b*e, - b*d + a*e, a d  - c e)

o9 : Ideal of R

i10 : scan(gens ring J, f -> J = saturate(J,f))

i11 : toricIdeal = (A) -> (
          n := #(A_0);  
          R = QQ[vars(0..n-1),Degrees=>transpose A,MonomialSize=>16]; 
          B := transpose LLL syz matrix A;
          J := ideal apply(entries B, b -> toBinomial(b,R));
          scan(gens ring J, f -> J = saturate(J,f));
          J
          );

i12 : I = toricIdeal A; 

o12 : Ideal of R

i13 : transpose mingens I

o13 = {-2, -9}  | cd-be    |
      {-2, -8}  | bd-ae    |
      {-2, -2}  | b2-ac    |
      {-4, -14} | a2d2-c3e |
      {-4, -8}  | c4-a3e   |
      {-4, -7}  | bc3-a3d  |
      {-5, -28} | ad4-c2e3 |
      {-6, -42} | d6-ce5   |

              8      1
o13 : Matrix R  <-- R

i14 : graver = (I) -> (
          R := ring I;
          k := coefficientRing R;
          n := numgens R;
          -- construct new ring S with 2n variables
          S := k[Variables=>2*n,MonomialSize=>16];
          toS := map(S,R,(vars S)_{0..n-1});
          toR := map(R,S,vars R | matrix(R, {toList(n:1)}));
          -- embed I in S
          m := gens toS I;
          -- construct the toric ideal of the Lawrence 
          -- lifting of A
          i := 0;
          while i < n do (
              wts := join(toList(i:0),{1},toList(n-i-1:0));
              wts = join(wts,wts);
              m = homogenize(m,S_(n+i),wts);
              i=i+1;
              );
         J := ideal m;
         scan(gens ring J, f -> J = saturate(J,f));
         -- apply the map toR to the minimal generators of J 
         f := matrix entries toR mingens J;
         p := sortColumns f;
         f_p) ;

i15 : Graver = graver I 

o15 = | -cd+be -bd+ae -b2+ac -cd2+ae2 -a2d2+c3e -c4+a3e -c4+a2bd -bc3+a3d -ad4+c2e3 -abd3+c3e2 -a2d3+bc2e2 -ab2d2+c4e -a3d2+b2c2e -c5+a2b2e -c5+ab3d -b2c3+a4e -b3c2+a4d -d6+ce5 -bd5+c2e4 -ad5+bce4 -b2d4+c3e3 -a2d4+b2ce3 -b3d3+c4e2 -a3d3+b3ce2 -b4d2+c5e -a4d2+b4ce -c6+ab4e -c6+b5d -b4c2+a5e -b5c+a5d -d7+be6 -ad6+b2e5 -a2d5+b3e4 -a3d4+b4e3 -a4d3+b5e2 -a5d2+b6e -c7+b6e -c7+a5d2 -b6c+a6e -b7+a6d -d8+ae7 -b8+a7e |

              1      42
o15 : Matrix R  <-- R

i16 : graverFibers = (Graver) -> (
           ProductIdeal := (I) -> ( trim ideal(
              apply(numgens I, a -> ( 
                  f := I_a; leadTerm f * (leadTerm f - f))))); 
           PI := ProductIdeal ideal Graver; 
           R := ring Graver; 
           new HashTable from apply(
               unique degrees source Graver,
               d -> d => compress (basis(d,R) % PI) ));
```

---

## toricHilbertScheme / test.m2 — chunk 2

### Input

```macaulay2
fibers = graverFibers Graver 
generateAmonos = (Graver) -> (
           trueHS := poincare coker Graver;
           fibers := graverFibers Graver;
           fibers = apply(sort pairs fibers, last);
           monos = {};
           selectStandard := (fibers, J) -> (
           if #fibers == 0 then (
              if trueHS == poincare coker gens J
              then (monos = append(monos,flatten entries mingens J));
           ) else (
              P := fibers_0;
              fibers = drop(fibers,1);
              P = compress(P % J);
              nP := numgens source P; 
              -- nP is the number of monomials not in J.
              if nP > 0 then (
                 if nP == 1 then selectStandard(fibers,J)
                 else (--remove one monomial from P,take the rest.
                       P = flatten entries P;
                       scan(#P, i -> (
                            J1 := J + ideal drop(P,{i,i});
                            selectStandard(fibers, J1)))));
           ));
           selectStandard(fibers, ideal(0_(ring Graver)));
           ) ;
generateAmonos Graver;
#monos 
scan(0..9, i -> print toString monos#i) 
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, b*c*e^4, d^6}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, c*e^5, b*c*e^4, d^7}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, c*e^5, b*c*e^4, b*e^6, d^8}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, c*e^5, b*c*e^4, b*e^6, a*e^7}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, d^6, a*d^5}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, b*c^2*e^2, a*d^4, d^6}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, a*d^4, a^2*d^3, d^6}
{c*d, b*d, b^2, a^2*d^2, c^4, b*c^3, a*d^4, d^6}
{c*d, b*d, b^2, a^2*d^2, a^3*d, c^4, a*d^4, d^6}
{c*d, b*d, b^2, a^3*e, a^2*d^2, a^3*d, a*d^4, d^6}
findPositiveVector = (m,s) -> (
           expvector := first exponents s - first exponents m;
           n := #expvector;
           i := first positions(0..n-1, j -> expvector_j > 0);
           splice {i:0, 1, (n-i-1):0}
           );
flips = (M) -> (
           R := ring M;
           -- store generators of M in monoms
           monoms := first entries generators M;
           result := {};
           -- test each generator of M to see if it leads to a neighbor 
           scan(#monoms, i -> (
             m := monoms_i;
             rest := drop(monoms,{i,i});
             b := basis(degree m, R);
             s := (compress (b % M))_(0,0);
             J := ideal(m-s) + ideal rest;
             if poincare coker gens J == poincare coker gens M then (
               w := findPositiveVector(m,s);
               R1 := (coefficientRing R)[generators R, Weights=>w];
               J = substitute(J,R1);
               J = trim ideal leadTerm J;
               result = append(result,J);
               )));
           result
      );
R = QQ[a..e,Degrees=>transpose A];
```

### Output

```
i17 : fibers = graverFibers Graver 

o17 = HashTable{{2, 2} => | ac b2 |                                  }
                {2, 8} => | ae bd |
                {2, 9} => | be cd |
                {3, 16} => | ae2 bde cd2 |
                {4, 7} => | a3d bc3 |
                {4, 8} => | a3e a2bd c4 |
                {4, 14} => | a2d2 c3e |
                {5, 7} => | a4d abc3 b3c2 |
                {5, 8} => | a4e a3bd ac4 b2c3 |
                {5, 10} => | a3ce a2b2e a2bcd ab3d c5 |
                {5, 14} => | a3d2 ac3e b2c2e bc3d |
                {5, 16} => | a3e2 a2cd2 ab2d2 c4e |
                {5, 21} => | a2d3 bc2e2 c3de |
                {5, 22} => | a2d2e abd3 c3e2 |
                {5, 28} => | ad4 c2e3 |
                {6, 7} => | a5d a2bc3 b5c |
                {6, 8} => | a5e a4bd a2c4 b4c2 |
                {6, 12} => | a3c2e a2bc2d ab4e b5d c6 |
                {6, 14} => | a4d2 a2c3e abc3d b4ce b3c2d |
                {6, 18} => | a3ce2 a2b2e2 a2c2d2 b4d2 c5e |
                {6, 21} => | a3d3 abc2e2 ac3de b3ce2 bc3d2 |
                {6, 24} => | a3e3 a2cd2e abcd3 b3d3 c4e2 |
                {6, 28} => | a2d4 ac2e3 b2ce3 c3d2e |
                {6, 30} => | a2d2e2 acd4 b2d4 c3e3 |
                {6, 35} => | ad5 bce4 c2de3 |
                {6, 36} => | ad4e bd5 c2e4 |
                {6, 42} => | ce5 d6 |
                {7, 7} => | a6d a3bc3 b7 |
                {7, 8} => | a6e a5bd a3c4 b6c |
                {7, 14} => | a5d2 a3c3e a2bc3d b6e b5cd c7 |
                {7, 21} => | a4d3 a2bc2e2 a2c3de abc3d2 b5e2 b3c2d2 |
                {7, 28} => | a3d4 a2c2e3 ac3d2e b4e3 bc3d3 |
                {7, 35} => | a2d5 abce4 ac2de3 b3e4 c3d3e |
                {7, 42} => | ace5 ad6 b2e5 c2d2e3 |
                {7, 49} => | be6 cde5 d7 |
                {8, 8} => | a7e a6bd a4c4 b8 |
                {8, 56} => | ae7 bde6 cd2e5 d8 |

o17 : HashTable

i18 : generateAmonos = (Graver) -> (
           trueHS := poincare coker Graver;
           fibers := graverFibers Graver;
           fibers = apply(sort pairs fibers, last);
           monos = {};
           selectStandard := (fibers, J) -> (
           if #fibers == 0 then (
              if trueHS == poincare coker gens J
              then (monos = append(monos,flatten entries mingens J));
           ) else (
              P := fibers_0;
              fibers = drop(fibers,1);
              P = compress(P % J);
              nP := numgens source P; 
              -- nP is the number of monomials not in J.
              if nP > 0 then (
                 if nP == 1 then selectStandard(fibers,J)
                 else (--remove one monomial from P,take the rest.
                       P = flatten entries P;
                       scan(#P, i -> (
                            J1 := J + ideal drop(P,{i,i});
                            selectStandard(fibers, J1)))));
           ));
           selectStandard(fibers, ideal(0_(ring Graver)));
           ) ;

i19 : generateAmonos Graver;

i20 : #monos 

o20 = 281

i21 : scan(0..9, i -> print toString monos#i) 
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, b*c*e^4, d^6}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, c*e^5, b*c*e^4, d^7}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, c*e^5, b*c*e^4, b*e^6, d^8}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, c*e^5, b*c*e^4, b*e^6, a*e^7}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, c^2*e^3, b*c^2*e^2, d^6, a*d^5}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, b*c^2*e^2, a*d^4, d^6}
{c*d, b*d, b^2, c^3*e, c^4, b*c^3, a*d^4, a^2*d^3, d^6}
{c*d, b*d, b^2, a^2*d^2, c^4, b*c^3, a*d^4, d^6}
{c*d, b*d, b^2, a^2*d^2, a^3*d, c^4, a*d^4, d^6}
{c*d, b*d, b^2, a^3*e, a^2*d^2, a^3*d, a*d^4, d^6}

i22 : findPositiveVector = (m,s) -> (
           expvector := first exponents s - first exponents m;
           n := #expvector;
           i := first positions(0..n-1, j -> expvector_j > 0);
           splice {i:0, 1, (n-i-1):0}
           );

i23 : flips = (M) -> (
           R := ring M;
           -- store generators of M in monoms
           monoms := first entries generators M;
           result := {};
           -- test each generator of M to see if it leads to a neighbor 
           scan(#monoms, i -> (
             m := monoms_i;
             rest := drop(monoms,{i,i});
             b := basis(degree m, R);
             s := (compress (b % M))_(0,0);
             J := ideal(m-s) + ideal rest;
             if poincare coker gens J == poincare coker gens M then (
               w := findPositiveVector(m,s);
               R1 := (coefficientRing R)[generators R, Weights=>w];
               J = substitute(J,R1);
               J = trim ideal leadTerm J;
               result = append(result,J);
               )));
           result
      );

i24 : R = QQ[a..e,Degrees=>transpose A];
```

---

## toricHilbertScheme / test.m2 — chunk 3

### Input

```macaulay2
M = ideal(a*e,c*d,a*c,a^2*d^2,a^2*b*d,a^3*d,c^2*e^3,
                c^3*e^2,c^4*e,c^5,c*e^5,a*d^5,b*e^6);
F = flips M
#F
scan(#F, i -> print toString entries mingens F_i)
{{a*e, c*d, a*c, a^2*d^2, a^3*d, c^4, c^2*e^3, c^3*e^2, a*d^5, c*e^5, b*e^6}}
{{c*d, a*e, a*c, a^2*d^2, a^2*b*d, a^3*d, c^3*e^2, c^4*e, c^5, a*d^4, c*e^5, c^2*e^4, b*e^6}}
{{a*e, c*d, a*c, a^2*d^2, a^3*d, a^2*b*d, c^2*e^3, c^3*e^2, c^4*e, c^5, c*e^5, b*c*e^4, a*d^6, b*e^6}}
{{a*e, a*c, c*d, a^2*b*d, a^3*d, a^2*d^2, c^2*e^3, c^3*e^2, c^4*e, c^5, c*e^5, a*d^5, d^7}}
stdMonomials = (M) -> (
           R := ring M;
           RM := R/M;
           apply(numgens M, i -> (
                 s := basis(degree(M_i),RM); lift(s_(0,0), R)))
           );
R = QQ[a..e,Degrees => transpose A ];
M = ideal(a^3*d, a^2*b*d, a^2*d^2, a*b^3*d, a*b^2*d^2, a*b*d^3, 
                a*c, a*d^4, a*e, b^5*d, b^4*d^2, b^3*d^3, b^2*d^4, 
                b*d^5, b*e, c*e^5); 
toString stdMonomials M
```

### Output

```
i25 : M = ideal(a*e,c*d,a*c,a^2*d^2,a^2*b*d,a^3*d,c^2*e^3,
                c^3*e^2,c^4*e,c^5,c*e^5,a*d^5,b*e^6);

o25 : Ideal of R

i26 : F = flips M

2 2   3    4   2 3   3 2     5     5     6                          2 2   2      3    3 2   4    5     4     5   2 4     6                          2 2   3    2      2 3   3 2   4    5     5       4     6     6                          2      3    2 2   2 3   3 2   4    5     5     5   7
o26 = {ideal (a*e, c*d, a*c, a d , a d, c , c e , c e , a*d , c*e , b*e ), ideal (c*d, a*e, a*c, a d , a b*d, a d, c e , c e, c , a*d , c*e , c e , b*e ), ideal (a*e, c*d, a*c, a d , a d, a b*d, c e , c e , c e, c , c*e , b*c*e , a*d , b*e ), ideal (a*e, a*c, c*d, a b*d, a d, a d , c e , c e , c e, c , c*e , a*d , d )}

o26 : List

i27 : #F

o27 = 4

i28 : scan(#F, i -> print toString entries mingens F_i)
{{a*e, c*d, a*c, a^2*d^2, a^3*d, c^4, c^2*e^3, c^3*e^2, a*d^5, c*e^5, b*e^6}}
{{c*d, a*e, a*c, a^2*d^2, a^2*b*d, a^3*d, c^3*e^2, c^4*e, c^5, a*d^4, c*e^5, c^2*e^4, b*e^6}}
{{a*e, c*d, a*c, a^2*d^2, a^3*d, a^2*b*d, c^2*e^3, c^3*e^2, c^4*e, c^5, c*e^5, b*c*e^4, a*d^6, b*e^6}}
{{a*e, a*c, c*d, a^2*b*d, a^3*d, a^2*d^2, c^2*e^3, c^3*e^2, c^4*e, c^5, c*e^5, a*d^5, d^7}}

i29 : stdMonomials = (M) -> (
           R := ring M;
           RM := R/M;
           apply(numgens M, i -> (
                 s := basis(degree(M_i),RM); lift(s_(0,0), R)))
           );

i30 : R = QQ[a..e,Degrees => transpose A ];

i31 : M = ideal(a^3*d, a^2*b*d, a^2*d^2, a*b^3*d, a*b^2*d^2, a*b*d^3, 
                a*c, a*d^4, a*e, b^5*d, b^4*d^2, b^3*d^3, b^2*d^4, 
                b*d^5, b*e, c*e^5); 

o31 : Ideal of R

i32 : toString stdMonomials M 

o32 = {b*c^3, c^4, c^3*e, c^5, c^4*e, c^3*e^2, b^2, c^2*e^3, b*d, c^6, c^5*e, c^4*e^2, c^3*e^3, c^2*e^4, c*d, d^6}
```

---

## toricHilbertScheme / test.m2 — chunk 4

### Input

```macaulay2
inequalities = (M) -> (
              stds := stdMonomials(M);
              transpose matrix apply(numgens M, i -> (
                  flatten exponents(M_i) - 
                      flatten exponents(stds_i))));
inequalities M
primitive := (L) -> (
           n := #L-1; g := L#n;
           while n > 0 do (n = n-1; g = gcd(g, L#n););
           if g === 1 then L else apply(L, i -> i // g));
load "polarCone.m2"
decideCoherence = (M) -> (
           ineqs := inequalities M;
           c := first polarCone ineqs;
           m := - sum(numgens source c, i -> c_{i});
           prods := (transpose m) * ineqs;
           if numgens source prods != numgens source compress prods
           then false else primitive (first entries transpose m));
decideCoherence M
N = ideal(a*e,c*d,a*c,c^3*e,a^3*d,c^4,a*d^4,a^2*d^3,c*e^5,
                 c^2*e^4,d^7);
decideCoherence N
```

### Output

```
i33 : inequalities = (M) -> (
              stds := stdMonomials(M);
              transpose matrix apply(numgens M, i -> (
                  flatten exponents(M_i) - 
                      flatten exponents(stds_i))));

i34 : inequalities M

o34 = | 3  2  2  1  1  1  1  1  1  0  0  0  0  0  0  0  |
      | -1 1  0  3  2  1  -2 0  -1 5  4  3  2  1  1  0  |
      | -3 -4 -3 -5 -4 -3 1  -2 0  -6 -5 -4 -3 -2 -1 1  |
      | 1  1  2  1  2  3  0  4  -1 1  2  3  4  5  -1 -6 |
      | 0  0  -1 0  -1 -2 0  -3 1  0  -1 -2 -3 -4 1  5  |

               5       16
o34 : Matrix ZZ  <-- ZZ

i35 : primitive := (L) -> (
           n := #L-1; g := L#n;
           while n > 0 do (n = n-1; g = gcd(g, L#n););
           if g === 1 then L else apply(L, i -> i // g));

i36 : load "polarCone.m2"

i37 : decideCoherence = (M) -> (
           ineqs := inequalities M;
           c := first polarCone ineqs;
           m := - sum(numgens source c, i -> c_{i});
           prods := (transpose m) * ineqs;
           if numgens source prods != numgens source compress prods
           then false else primitive (first entries transpose m));

i38 : decideCoherence M

o38 = {0, 0, 1, 15, 18}

o38 : List

i39 : N = ideal(a*e,c*d,a*c,c^3*e,a^3*d,c^4,a*d^4,a^2*d^3,c*e^5,
                 c^2*e^4,d^7);

o39 : Ideal of R

i40 : decideCoherence N

o40 = false
```

---

## toricHilbertScheme / test.m2 — chunk 5

### Input

```macaulay2
A22 =
        {{1,1,1,1,1,1,1,1,1},{0,0,0,1,1,1,0,0,0},{0,0,0,0,0,0,1,1,1},
        {1,0,0,1,0,0,1,0,0},{0,1,0,0,1,0,0,1,0},{0,0,1,0,0,1,0,0,1}};
I22 = toricIdeal A22
Graver22 = graver I22;
generateAmonos(Graver22);
#monos
scan(0..9,i->print toString monos#i) 
{f*h, c*h, f*g, e*g, c*g, b*g, c*e, c*d, b*d}
{f*h, d*h, c*h, f*g, c*g, b*g, c*e, c*d, b*d}
{d*i, f*h, d*h, c*h, c*g, b*g, c*e, c*d, b*d}
{e*i, c*h, f*g, e*g, c*g, b*g, c*e, c*d, b*d}
{e*i, d*i, c*h, e*g, c*g, b*g, c*e, c*d, b*d}
{e*i, d*i, d*h, c*h, c*g, b*g, c*e, c*d, b*d}
{f*h, c*h, f*g, e*g, c*g, b*g, c*e, a*e, c*d}
{e*i, c*h, f*g, e*g, c*g, b*g, c*e, a*e, c*d, b*d*i}
{e*i, c*h, f*g, e*g, c*g, b*g, c*e, a*e, c*d, a*f*h}
{e*i, d*i, c*h, e*g, c*g, b*g, c*e, a*e, c*d}
localCoherentEquations = (IA,w) -> (
           -- IA is the toric ideal of A living in a ring equipped
           -- with weight order w, if we are computing the local 
           -- equations about the initial ideal of IA w.r.t. w.
           R := ring IA;
           M := ideal leadTerm IA;
           S := first entries ((gens M) % IA);
           -- Make the universal family J in a new ring.
           nv := numgens R; n := numgens M;
           T = (coefficientRing R)[generators R, z_1 .. z_n, 
                                   Weights => flatten splice{w, n:0},
                                   MonomialSize=>16];
           M = substitute(generators M,T);
           S = apply(S, s -> substitute(s,T));
           J = ideal apply(n, i -> 
                     M_(0,i) - T_(nv + i) * S_i);
           -- Find the ideal Ihilb of local equations about M:
           spairs := (gens J) * (syz M);
           g := forceGB gens J;
           B = (coefficientRing R)[z_1 .. z_n,MonomialSize=>16];
           Fones := map(B,T, matrix(B,{splice {nv:1}}) | vars B);
           Ihilb := ideal Fones (spairs % g);
           Ihilb
           );
IA = toricIdeal A;
```

### Output

```
i41 : A22 =
        {{1,1,1,1,1,1,1,1,1},{0,0,0,1,1,1,0,0,0},{0,0,0,0,0,0,1,1,1},
        {1,0,0,1,0,0,1,0,0},{0,1,0,0,1,0,0,1,0},{0,0,1,0,0,1,0,0,1}};

i42 : I22 = toricIdeal A22

o42 = ideal (f*h - e*i, c*h - b*i, f*g - d*i, e*g - d*h, c*g - a*i, b*g - a*h, c*e - b*f, c*d - a*f, b*d - a*e)

o42 : Ideal of R

i43 : Graver22 = graver I22;

1      15
o43 : Matrix R  <-- R

i44 : generateAmonos(Graver22);

i45 : #monos

o45 = 108

i46 : scan(0..9,i->print toString monos#i) 
{f*h, c*h, f*g, e*g, c*g, b*g, c*e, c*d, b*d}
{f*h, d*h, c*h, f*g, c*g, b*g, c*e, c*d, b*d}
{d*i, f*h, d*h, c*h, c*g, b*g, c*e, c*d, b*d}
{e*i, c*h, f*g, e*g, c*g, b*g, c*e, c*d, b*d}
{e*i, d*i, c*h, e*g, c*g, b*g, c*e, c*d, b*d}
{e*i, d*i, d*h, c*h, c*g, b*g, c*e, c*d, b*d}
{f*h, c*h, f*g, e*g, c*g, b*g, c*e, a*e, c*d}
{e*i, c*h, f*g, e*g, c*g, b*g, c*e, a*e, c*d, b*d*i}
{e*i, c*h, f*g, e*g, c*g, b*g, c*e, a*e, c*d, a*f*h}
{e*i, d*i, c*h, e*g, c*g, b*g, c*e, a*e, c*d}

i47 : localCoherentEquations = (IA,w) -> (
           -- IA is the toric ideal of A living in a ring equipped
           -- with weight order w, if we are computing the local 
           -- equations about the initial ideal of IA w.r.t. w.
           R := ring IA;
           M := ideal leadTerm IA;
           S := first entries ((gens M) % IA);
           -- Make the universal family J in a new ring.
           nv := numgens R; n := numgens M;
           T = (coefficientRing R)[generators R, z_1 .. z_n, 
                                   Weights => flatten splice{w, n:0},
                                   MonomialSize=>16];
           M = substitute(generators M,T);
           S = apply(S, s -> substitute(s,T));
           J = ideal apply(n, i -> 
                     M_(0,i) - T_(nv + i) * S_i);
           -- Find the ideal Ihilb of local equations about M:
           spairs := (gens J) * (syz M);
           g := forceGB gens J;
           B = (coefficientRing R)[z_1 .. z_n,MonomialSize=>16];
           Fones := map(B,T, matrix(B,{splice {nv:1}}) | vars B);
           Ihilb := ideal Fones (spairs % g);
           Ihilb
           );

i48 : IA = toricIdeal A;

o48 : Ideal of R
```

---

## toricHilbertScheme / test.m2 — chunk 6

### Input

```macaulay2
Y = QQ[a..e, MonomialSize => 16,
                  Degrees => transpose A, Weights => (w = {9,3,5,0,0})];
IA = substitute(IA,Y);
JM = trim localCoherentEquations(IA,w)
load "minPres.m2";
G = removeRedundantVariables JM
ideal gens gb(G JM)
CX = QQ[a..e, z_1,z_5,z_6,z_11, Weights =>
            {9,3,5,0,0,0,0,0,0}];
F = map(CX, ring J, matrix{{a,b,c,d,e}} | 
                  substitute(G.matrix,CX))
```

### Output

```
i49 : Y = QQ[a..e, MonomialSize => 16,
                  Degrees => transpose A, Weights => (w = {9,3,5,0,0})];

i50 : IA = substitute(IA,Y);

o50 : Ideal of Y

i51 : JM = trim localCoherentEquations(IA,w)

3
o51 = ideal (z  z   - z , z  z   - z , z z   - z  , z z   - z , z z   - z , z z   - z  , z z  - z , z z  - z  , z z  - z  , z z  - z , z z  - z , z z  - z , z z  - z , z z  - z z , z z  - z , z z  - z z )
              11 12    7   10 11    4   7 11    13   2 11    9   9 10    7   2 10    12   8 9    4   4 9    13   2 8    10   5 6    2   2 6    8   3 5    4   2 4    7   2 3    4 6   1 2    3   2 9    5 7

o51 : Ideal of B

i52 : load "minPres.m2";

i53 : G = removeRedundantVariables JM

2 3              3 4        2            2 3        3 4   3 4 2
o53 = map (B, B, {z , z z , z z z , z z z  , z , z , z z z  , z z , z z z  , z z , z  , z z , z z z  })
                   1   5 6   1 5 6   5 6 11   5   6   5 6 11   5 6   5 6 11   5 6   11   5 6   5 6 11

o53 : RingMap B <-- B

i54 : ideal gens gb(G JM)

2 3         2
o54 = ideal(z z z   - z z z )
             5 6 11    1 5 6

o54 : Ideal of B

i55 : CX = QQ[a..e, z_1,z_5,z_6,z_11, Weights =>
            {9,3,5,0,0,0,0,0,0}];

i56 : F = map(CX, ring J, matrix{{a,b,c,d,e}} | 
                  substitute(G.matrix,CX))

2 3              3 4        2            2 3        3 4   3 4 2
o56 = map (CX, T, {a, b, c, d, e, z , z z , z z z , z z z  , z , z , z z z  , z z , z z z  , z z , z  , z z , z z z  })
                                   1   5 6   1 5 6   5 6 11   5   6   5 6 11   5 6   5 6 11   5 6   11   5 6   5 6 11

o56 : RingMap CX <-- T
```

---

## toricHilbertScheme / test.m2 — chunk 7

### Input

```macaulay2
J1 = F J
substitute(ideal(z_5^2),CX) + J1
A = {{1,1,1,1,1,1,1},{0,6,7,5,8,4,3},{3,7,2,0,7,6,1},
         {6,5,2,6,5,0,0}};
IA = toricIdeal A
Y = QQ[a..g, MonomialSize => 16,
                 Weights => (w = {0,0,276,220,0,0,215}),
                 Degrees =>transpose A];
IA = substitute(IA,Y);
M = ideal leadTerm IA
JM = trim localCoherentEquations(IA,w)
```

### Output

```
i57 : J1 = F J

6    7                       5    6                   2 3        5        4     2 3      4           2 3 4      3 2        3   2   2 2    3            4       2 2 2 3   2       4      5      3   3 4   3       3 3 4 2
o57 = ideal (b*e  - d z , c*d - b*e*z z , c*e  - d z z z , a*e - b*d*z z z  , a*d  - b*c*e z , c e  - a*d z , a*c - b z z z  , c e  - a*b*d z z , a d  - c e*z z z  , c e - a*b d z z , a b*d - c z  , c  - a*b d*z z , a d - b*c z z z  )
                       1             5 6            1 5 6             5 6 11                5              6           5 6 11                5 6              5 6 11               5 6             11              5 6             5 6 11

o57 : Ideal of CX

i58 : substitute(ideal(z_5^2),CX) + J1

2     6    7                       5    6                   2 3        5        4     2 3      4           2 3 4      3 2        3   2   2 2    3            4       2 2 2 3   2       4      5      3   3 4   3       3 3 4 2
o58 = ideal (z , b*e  - d z , c*d - b*e*z z , c*e  - d z z z , a*e - b*d*z z z  , a*d  - b*c*e z , c e  - a*d z , a*c - b z z z  , c e  - a*b*d z z , a d  - c e*z z z  , c e - a*b d z z , a b*d - c z  , c  - a*b d*z z , a d - b*c z z z  )
              5            1             5 6            1 5 6             5 6 11                5              6           5 6 11                5 6              5 6 11               5 6             11              5 6             5 6 11

o58 : Ideal of CX

i59 : A = {{1,1,1,1,1,1,1},{0,6,7,5,8,4,3},{3,7,2,0,7,6,1},
         {6,5,2,6,5,0,0}};

i60 : IA = toricIdeal A

2 3       3 2   2     4 4    8 4   4 3 6    7 2 4     4 7 3    8 7   7 2 8    2 6 5 4   3 3 10     3 7 7   12 6        12   3     5 4 9    3 5 11   3 8   7    4 4 11   13 3 2     3 13 3   2 7 11      2 6 11   5 2 13    6 6   7   10   10    4 5 8 4   5 11 5    5 2 3 11     11 9    4 11 3 3   10 13    3     7 11   7 14 3    6 5 2 11   7   16    9 5 3 7   13 12    6 4 11 4   5 17 3    21 2      3 10 12    7 10 5 3   3 2 16 5    20 5    7   18     22 4    9 17     7 8   11   9 19    12 4 5 7   34 5 3    8 30 2 2   35 2 6    10 31 2   57   10    17 49      58 13     19 2 50    79 14    24 67 2
o60 = ideal (a c e - b*d f , a c*d*e f  - b g , d e f  - b c g , a*b c f  - e g , d e f  - a b c g , a b c  f - d e g , b  c  - a*d*e  f*g , a*c d f  - b e g  , a c d*f  - b e g  , b  c d f - a e  g , c d f   - a*b e g  , a b c   - d e f*g , d  e*f   - a b c g , a c  f  - b d e g  , a*b  c  - d e  f g , d  f   - a b*c*e g  , a c  f  - b d e g  , a b*c   - d e f g , d  f   - a b c  g , a e  f  - b  c d*g, a b  c   - d e  f g , a d e  f  - b  c g, a c*e  f - b  d g, a c  f - b d e*g  , a c   - d  e f g , b  c d  - a e  f g , b  c d  - a  e  g , b  c*d   - a  e  f*g, b  d  f - a  c e  g, b  d   - a  e  f )

o60 : Ideal of R

i61 : Y = QQ[a..g, MonomialSize => 16,
                 Weights => (w = {0,0,276,220,0,0,215}),
                 Degrees =>transpose A];

i62 : IA = substitute(IA,Y);

o62 : Ideal of Y

i63 : M = ideal leadTerm IA

2 3    8 4   21 2      22 4    14 5 3   13 3 2    7 2 4   20 5    6   6 7   12 6   5 4 3 5   35 2 6     4 7 3   36 9 2   34 5 3   5 2 11 7   2 6 5 4   3 5 11     2 6 11   3 8   7   57   10     11 9   3     7 11   3 3 10    58 13    5 11 5   4 5 8 4   79 14   13 15 16   3 10 12   5 2 13   7 14 3   2 15 18   6 4 11 4   2 9 7 14   2   12 4 12   7   16   9 17    9 19     20 29     14 11 23     39 58     34 32 62   59 57 110
o63 = ideal (a c e, b g , b  c d*g, b  d g, b  d f , b  c d f, b c g , b  c g, b c*d f , b  c , b c d f , b  c d , a*b c f , b  d f , b  c d , a c e  g , a b c g , b e g  , a*b e g  , a c d*f , b  c*d  , a*b  c , a b*c*e g  , a b c  f, b  d  f, a c  f , a b c g , b  d  , b  d  f  , a b  c  , a b c  , a c  f , a e  g  , a b c  g , b c d f  , a b*c  d f  , a b*c  , a c  f, a c  , a*e  g  , a*c  d  f  , b*e  g  , b*c  d  f  , c  d  f   )

o63 : Ideal of Y

i64 : JM = trim localCoherentEquations(IA,w)

2
o64 = ideal (z  z   - z  , z  z   - z  , z  z   - z  z  , z  z   - z  , z  z   - z , z  z   - z  z  , z  z   - z  , z  z   - z  , z  z   - z  , z  z   - z  , z  z   - z  z  , z z   - z  , z z   - z  , z z   - z  , z  z   - z  , z  z   - z , z  z   - z  , z  z   - z  , z z   - z  , z  z   - z  , z  z   - z  , z  z   - z  , z  z   - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z  z   - z  , z  z   - z  , z z   - z  , z z   - z  , z  z   - z , z  z   - z , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z  z   - z  , z  z   - z  , z  z   - z  , z z   - z  , z z   - z  , z z   - z  , z  z   - z  , z  z   - z  , z z   - z , z z   - z  , z z   - z  , z  z   - z , z  z   - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z  z   - z  , z  z   - z , z z   - z , z z   - z  , z  z   - z , z  z   - z , z z   - z  , z z   - z  , z z   - z , z z   - z , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z  , z z   - z , z z   - z  , z z   - z  , z z   - z , z z   - z  , z z  - z , z z  - z , z z  - z  , z z  - z , z z  - z , z z  - z  , z z  - z  , z z  - z  , z z  - z , z z  - z  , z z  - z  , z z  - z  , z z  - z , z z  - z , z z  - z , z z  - z , z z  - z , z z  z   - z )
              42 44    43   42 43    35   41 43    40 44   41 42    40   40 41    1   35 41    40 43   33 41    20   19 41    36   18 41    35   35 40    19   18 40    35 42   7 38    39   2 38    37   1 37    39   18 36    13   33 35    1   19 35    13   18 35    11   1 35    36   20 33    16   18 33    40   13 33    23   11 33    19   9 33    18   7 32    37   2 32    31   1 32    38   19 31    34   18 31    27   2 31    30   1 31    37   23 29    5   16 29    9   1 27    34   7 26    31   2 26    24   1 26    32   3 25    28   1 25    21   23 24    34   19 24    27   18 24    17   7 24    30   2 24    22   1 24    31   13 23    27   11 23    17   9 23    7   1 22    30   4 21    28   18 20    1   11 20    36   9 20    35   7 20    24   2 20    13   1 20    26   13 19    17   11 19    7   9 19    2   1 19    23   13 18    7   11 18    2   1 18    19   1 17    27   9 16    1   5 16    7   2 16    23   4 14    25   3 14    21   1 14    12   7 13    22   2 13    10   1 13    24   4 12    21   1 12    15   7 11    10   2 11    6   1 11    13   4 10    15   2 10    8   1 10    22   7 9    6   2 9    5   1 9    11   6 7    8   5 7    3   1 7    17   4 6    12   3 6    15   2 6    3   1 6    10   4 5    14   3 5    12   2 5    4   1 5    6   1 4    3   1 3    8   1 2    7   1 29 33    2

o64 : Ideal of B
```

---

## toricHilbertScheme / test.m2 — chunk 8

### Input

```macaulay2
G = removeRedundantVariables JM;
toString ideal gens gb(G JM)
K = ideal(z_32*z_42*z_44-z_37^2,z_32^4*z_35-z_42,
          z_32^3*z_35*z_37^2-z_42^2*z_44,z_32^2*z_35*z_37^4-z_42^3*z_44^2,
          z_32*z_35*z_37^6-z_42^4*z_44^3,z_35*z_37^8-z_42^5*z_44^4);
GG = removeRedundantVariables K;
ideal gens gb (GG K)
A = {{1,1,1,1},{0,1,2,3}};
I = toricIdeal A;
Graver = graver I;
```

### Output

```
i65 : G = removeRedundantVariables JM;

o65 : RingMap B <-- B

i66 : toString ideal gens gb(G JM)

o66 = ideal(z_33*z_42^2*z_44-z_41^2*z_42,z_29*z_33^3*z_41^2-z_42^2*z_44,z_29*z_33^4*z_41-z_41*z_42,z_29*z_33^2*z_41^4*z_42-z_42^4*z_44^2,z_29*z_33*z_41^6*z_42-z_42^5*z_44^3,z_29*z_41^8*z_42-z_42^6*z_44^4)

i67 : K = ideal(z_32*z_42*z_44-z_37^2,z_32^4*z_35-z_42,
          z_32^3*z_35*z_37^2-z_42^2*z_44,z_32^2*z_35*z_37^4-z_42^3*z_44^2,
          z_32*z_35*z_37^6-z_42^4*z_44^3,z_35*z_37^8-z_42^5*z_44^4);

o67 : Ideal of B

i68 : GG = removeRedundantVariables K;

o68 : RingMap B <-- B

i69 : ideal gens gb (GG K)

5           2
o69 = ideal(z  z  z   - z  )
             32 35 44    37

o69 : Ideal of B

i70 : A = {{1,1,1,1},{0,1,2,3}};

i71 : I = toricIdeal A;

o71 : Ideal of R

i72 : Graver = graver I;

1      5
o72 : Matrix R  <-- R
```

---

## toricHilbertScheme / test.m2 — chunk 9

### Input

```macaulay2
fibers = graverFibers Graver;
peek fibers
G = trim product(values fibers, ideal)
numgens G
z = symbol z;
S = QQ[a,b,c,d,z];
zG = z ** substitute(gens G, S);
R = QQ[y_1 .. y_22];
```

### Output

```
i73 : fibers = graverFibers Graver;

i74 : peek fibers

o74 = HashTable{{2, 2} => | ac b2 |     }
                {2, 3} => | ad bc |
                {2, 4} => | bd c2 |
                {3, 3} => | a2d abc b3 |
                {3, 6} => | ad2 bcd c3 |

i75 : G = trim product(values fibers, ideal)

5     5   4 3 5   5 3 4   4 2 2 4   3 4   4   2 6 4   4   4 3   3 3 3 3   2 5 2 3     7   3   4 6 2   3 2 5 2   2 4 4 2     6 3 2   8 2 2   3   7    2 3 6      5 5    7 4    2 2 8     4 7   6 6
o75 = ideal (a b*c*d , a b d , a c d , a b c d , a b c*d , a b d , a b*c d , a b c d , a b c d , a*b c*d , a c d , a b c d , a b c d , a*b c d , b c d , a b*c d, a b c d, a*b c d, b c d, a b c , a*b c , b c )

o75 : Ideal of R

i76 : numgens G

o76 = 22

i77 : z = symbol z;

i78 : S = QQ[a,b,c,d,z];

i79 : zG = z ** substitute(gens G, S);

1      22
o79 : Matrix S  <-- S

i80 : R = QQ[y_1 .. y_22];
```

---

## toricHilbertScheme / test.m2 — chunk 10

### Input

```macaulay2
F = map(S,R,zG)
PA = trim ker F
codim PA
degree PA
Aff = apply(1..22, v -> (
                             K = substitute(PA,y_v => 1);
                             FF = removeRedundantVariables K;
                             ideal gens gb (FF K)));
scan(Aff, i -> print toString i);
ideal()
ideal()
ideal()
ideal(y_1^4*y_5*y_21-1)
ideal(y_1^4*y_6^6*y_21-1)
ideal()
ideal(y_1^2*y_11^2*y_17-1)
ideal(y_1^3*y_9^2*y_21^2-1)
ideal(y_6^3*y_21-y_10,y_1*y_10^3-y_6^2,y_1*y_6*y_10^2*y_21-1)
ideal(y_6*y_15-1,y_2*y_15^2-y_6*y_14,y_6^2*y_14-y_2*y_15)
ideal()
ideal(y_11*y_13-1,y_1^2*y_21^3-y_13^2)
ideal(y_1^2*y_14^3*y_21^3-1)
ideal(y_10^2*y_21-1,y_1*y_15^4-y_10^3)
ideal()
ideal(y_11*y_20-1,y_3*y_20^2-y_11*y_17,y_11^2*y_17-y_3*y_20)
ideal(y_11*y_18*y_21-1,y_1*y_21^3-y_11*y_18^2,y_11^2*y_18^3-y_1*y_21^2)
ideal(y_1*y_19^4*y_21^4-1)
ideal(y_15*y_22-1)
ideal()
ideal(y_20*y_22-1)
ideal()
code primitive
code toZZ
```

### Output

```
i81 : F = map(S,R,zG)

5     5    4 3 5    5 3 4    4 2 2 4    3 4   4    2 6 4    4   4 3    3 3 3 3    2 5 2 3      7   3    4 6 2    3 2 5 2    2 4 4 2      6 3 2    8 2 2    3   7      2 3 6        5 5      7 4      2 2 8      4 7    6 6
o81 = map (S, R, {a b*c*d z, a b d z, a c d z, a b c d z, a b c*d z, a b d z, a b*c d z, a b c d z, a b c d z, a*b c*d z, a c d z, a b c d z, a b c d z, a*b c d z, b c d z, a b*c d*z, a b c d*z, a*b c d*z, b c d*z, a b c z, a*b c z, b c z})

o81 : RingMap S <-- R

i82 : PA = trim ker F

2                                                                                                                                                                                                                                                                                                                                                                                                                                                                               2                                                                                                                                                                                                            2                                                                                                                                                                                                                                                                        2                                                                                                                                                                                                                                                      2                                                                                                                                                                                                                                                                                                                                                  2                                                                                                                                                                                                    2                                                                                                                                                                                    2                                                                                                                                                                                                                                                                                             2                                                                                                      2                                                                                                             2                                                                                              2                                                                                                                         2                                                  2
o82 = ideal (y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y  y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y  y  , y  y   - y  y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y  y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y  y   - y  y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y y  , y  y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y y  , y  y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y  y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y y   - y y  , y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y , y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y  , y y  - y y , y y  - y y  , y y  - y y  , y y  - y y , y  - y y  , y y  - y y , y y  - y y , y y  - y y , y  - y y , y y  - y y , y y  - y y , y y  - y y )
              21    20 22   19 21    18 22   18 21    17 22   17 21    16 22   15 21    14 22   14 21    13 22   13 21    12 22   12 21    11 22   10 21    9 22   9 21    8 22   8 21    7 22   6 21    5 22   5 21    4 22   4 21    3 22   2 21    1 22   19 20    17 22   18 20    16 22   17 20    16 21   15 20    13 22   14 20    12 22   13 20    11 22   12 20    11 21   10 20    8 22   9 20    7 22   8 20    7 21   6 20    4 22   5 20    3 22   4 20    3 21   2 20    1 21   19    15 22   18 19    14 22   17 19    13 22   16 19    12 22   14 19    10 22   13 19    9 22   12 19    8 22   11 19    7 22   9 19    6 22   8 19    5 22   7 19    4 22   4 19    2 22   3 19    1 22   18    13 22   17 18    12 22   16 18    11 22   15 18    10 22   14 18    9 22   13 18    8 22   12 18    7 22   11 18    7 21   10 18    6 22   9 18    5 22   8 18    4 22   7 18    3 22   6 18    5 19   5 18    2 22   4 18    1 22   3 18    1 21   2 18    1 19   17    11 22   16 17    11 21   15 17    9 22   14 17    8 22   13 17    7 22   12 17    7 21   11 17    7 20   10 17    5 22   9 17    4 22   8 17    3 22   7 17    3 21   6 17    2 22   5 17    1 22   4 17    1 21   3 17    1 20   2 17    1 18   16    11 20   15 16    8 22   14 16    7 22   13 16    7 21   12 16    7 20   10 16    4 22   9 16    3 22   8 16    3 21   7 16    3 20   6 16    1 22   5 16    1 21   4 16    1 20   2 16    1 17   14 15    10 19   13 15    6 22   12 15    5 22   11 15    4 22   9 15    6 19   8 15    5 19   7 15    2 22   4 15    2 19   3 15    1 19   14    6 22   13 14    5 22   12 14    4 22   11 14    3 22   10 14    6 19   9 14    5 19   8 14    2 22   7 14    1 22   6 14    5 15   5 14    2 19   4 14    1 19   3 14    1 18   2 14    1 15   13    4 22   12 13    3 22   11 13    3 21   10 13    5 19   9 13    2 22   8 13    1 22   7 13    1 21   6 13    2 19   5 13    1 19   4 13    1 18   3 13    1 17   2 13    1 14   12    3 21   11 12    3 20   10 12    2 22   9 12    1 22   8 12    1 21   7 12    1 20   6 12    1 19   5 12    1 18   4 12    1 17   3 12    1 16   2 12    1 13   10 11    1 22   9 11    1 21   8 11    1 20   7 11    3 16   6 11    1 18   5 11    1 17   4 11    1 16   2 11    1 12   10    6 15   9 10    5 15   8 10    2 19   7 10    1 19   5 10    2 15   4 10    1 15   3 10    1 14   9    2 19   8 9    1 19   7 9    1 18   6 9    2 15   5 9    1 15   4 9    1 14   3 9    1 13   2 9    1 10   8    1 18   7 8    1 17   6 8    1 15   5 8    1 14   4 8    1 13   3 8    1 12   2 8    1 9   7    1 16   6 7    1 14   5 7    1 13   4 7    1 12   3 7    1 11   2 7    1 8   5 6    2 10   4 6    1 10   3 6    1 9   5    1 10   4 5    1 9   3 5    1 8   2 5    1 6   4    1 8   3 4    1 7   2 4    1 5   2 3    1 4

o82 : Ideal of R

i83 : codim PA

o83 = 19

i84 : degree PA

o84 = 30

i85 : Aff = apply(1..22, v -> (
                             K = substitute(PA,y_v => 1);
                             FF = removeRedundantVariables K;
                             ideal gens gb (FF K)));

i86 : scan(Aff, i -> print toString i);
ideal()
ideal()
ideal()
ideal(y_1^4*y_5*y_21-1)
ideal(y_1^4*y_6^6*y_21-1)
ideal()
ideal(y_1^2*y_11^2*y_17-1)
ideal(y_1^3*y_9^2*y_21^2-1)
ideal(y_6^3*y_21-y_10,y_1*y_10^3-y_6^2,y_1*y_6*y_10^2*y_21-1)
ideal(y_6*y_15-1,y_2*y_15^2-y_6*y_14,y_6^2*y_14-y_2*y_15)
ideal()
ideal(y_11*y_13-1,y_1^2*y_21^3-y_13^2)
ideal(y_1^2*y_14^3*y_21^3-1)
ideal(y_10^2*y_21-1,y_1*y_15^4-y_10^3)
ideal()
ideal(y_11*y_20-1,y_3*y_20^2-y_11*y_17,y_11^2*y_17-y_3*y_20)
ideal(y_11*y_18*y_21-1,y_1*y_21^3-y_11*y_18^2,y_11^2*y_18^3-y_1*y_21^2)
ideal(y_1*y_19^4*y_21^4-1)
ideal(y_15*y_22-1)
ideal()
ideal(y_20*y_22-1)
ideal()

i87 : code primitive

o87 = /home/dan/src/M2/1.2/Macaulay2/packages/ComputationsBook/toricHilbertScheme/test.m2:139:18-142:48: --source code:
      primitive := (L) -> (
           n := #L-1; g := L#n;
           while n > 0 do (n = n-1; g = gcd(g, L#n););
           if g === 1 then L else apply(L, i -> i // g));

i88 : code toZZ

o88 = /home/dan/src/M2/1.2/Macaulay2/packages/ComputationsBook/toricHilbertScheme/polarCone.m2:28:12-32:33: --source code:
      toZZ = (L) -> (
           d := apply(L, e -> denominator e);
           R := ring d#0;             l := 1_R;
           scan(d, i -> (l = (l*i // gcd(l,i))));    
           apply(L, e -> (numerator(l*e))));
```

---

## toricHilbertScheme / test.m2 — chunk 11

### Input

```macaulay2
code rotateMatrix
code isRedundant
code fourierMotzkin'
code(polarCone,Matrix,Matrix)
code(polarCone,Matrix)
H = transpose matrix{
      {1,2,3},
      {1,3,2},
      {2,1,3},
      {2,3,1},
      {3,1,2},
      {3,2,1}};
P = polarCone H
Q = polarCone P_0
```

### Output

```
i89 : code rotateMatrix

o89 = /home/dan/src/M2/1.2/Macaulay2/packages/ComputationsBook/toricHilbertScheme/polarCone.m2:41:20-43:48: --source code:
      rotateMatrix = (M) -> (
           r := rank source M;        c := rank target M;
           matrix table(r, c, (i,j) -> M_(c-j-1, r-i-1)));

i90 : code isRedundant

o90 = /home/dan/src/M2/1.2/Macaulay2/packages/ComputationsBook/toricHilbertScheme/polarCone.m2:57:25-65:12: --source code:
      isRedundant = (V, vert) -> (
           -- the row vector is redundant iff 'vert' contains an
           -- entry in 'V'.
           x := 0;            k := 0;
           numRow := #V;      -- equals the number of inequalities
           while x < 1 and k < numRow do (
                if isSubset(V#k, vert) then x = x+1;
                k = k+1;);     
           x === 1);

i91 : code fourierMotzkin'

o91 = /home/dan/src/M2/1.2/Macaulay2/packages/ComputationsBook/toricHilbertScheme/polarCone.m2:89:32-118:14: --source code:
      fourierMotzkin' = (A, V, spot) -> (
           -- initializing local variables
           numRow := #A;               -- equal to the length of V
           numCol := #(A#0);           pos := {};       
           neg := {};                  projA := {};     
           projV := {};                k := 0;
           -- divide the inequalities into three groups.
           while k < numRow do (
                if A#k#0 < 0 then neg = append(neg, k)
                else if A#k#0 > 0 then pos = append(pos, k)
                else (projA = append(projA, A#k);
                     projV = append(projV, V#k););
                k = k+1;);      
           -- generate new irredundant inequalities.
           scan(pos, i -> scan(neg, j -> (vert := V#i + V#j;
                          if not isRedundant(projV, vert)  
                          then (iRow := A#i;     jRow := A#j;
                               iCoeff := - jRow#0;
                               jCoeff := iRow#0;
                               a := iCoeff*iRow + jCoeff*jRow;
                               projA = append(projA, a);
                               projV = append(projV, vert););)));
           -- don't forget the implicit inequalities '-t <= 0'.
           scan(pos, i -> (vert := V#i + set{spot};
                if not isRedundant(projV, vert) then (
                     projA = append(projA, A#i);
                     projV = append(projV, vert););));
           -- remove the first column 
           projA = apply(projA, e -> e_{1..(numCol-1)});
           {projA, projV});

i92 : code(polarCone,Matrix,Matrix)

o92 = -- code for method: polarCone(Matrix,Matrix)
      /home/dan/src/M2/1.2/Macaulay2/packages/ComputationsBook/toricHilbertScheme/polarCone.m2:137:37-192:10: --source code:
      polarCone(Matrix, Matrix) := (Z, H) -> (
           R := ring source Z;
           if R =!= ring source H then error ("polarCone: " | 
                "expected matrices over the same ring");
           if rank target Z =!= rank target H then error (
                "polarCone: expected matrices to have the " |
                "same number of rows");     
           if (R =!= ZZ) then error ("polarCone: expected " | 
                "matrices over 'ZZ'");
           -- expressing 'cone(Y)+affine(B)' as '{x : Ax <= 0}'
           Y := substitute(Z, QQ);     B := substitute(H, QQ);   
           if rank source B > 0 then Y = Y | B | -B;
           n := rank source Y;         d := rank target Y;     
           A := Y | -id_(QQ^d);
           -- computing the row echelon form of 'A'
           A = gens gb rotateMatrix A;
           L := rotateMatrix leadTerm A;
           A = rotateMatrix A;
           -- find pivots
           numRow = rank target A;                  -- numRow <= d
           i := 0;                     pivotCol := {};
           while i < numRow do (j := 0;
                while j < n+d and L_(i,j) =!= 1_QQ do j = j+1;
                pivotCol = append(pivotCol, j);
                i = i+1;);
           -- computing the row-reduced echelon form of 'A'
           A = ((submatrix(A, pivotCol))^(-1)) * A;
           -- converting 'A' into a list of integer row vectors 
           A = entries A;
           A = apply(A, e -> primitive toZZ e);
           -- creating the vertex list 'V' for double description
           -- and listing the variables 'T' which remain to be
           -- eliminated
           V := {};                    T := toList(0..(n-1));
           scan(pivotCol, e -> (if e < n then (T = delete(e, T);
                          V = append(V, set{e});)));
           -- separating inequalities 'A' and equalities 'E'
           eqnRow := {};               ineqnRow := {};
           scan(numRow, i -> (if pivotCol#i >= n then 
                     eqnRow = append(eqnRow, i)
                     else ineqnRow = append(ineqnRow, i);));    
           E := apply(eqnRow, i -> A#i);
           E = apply(E, e -> e_{n..(n+d-1)});
           A = apply(ineqnRow, i -> A#i);
           A = apply(A, e -> e_(T | toList(n..(n+d-1)))); 
           -- successive projections eliminate the variables 'T'.
           if A =!= {} then scan(T, t -> (
                     D := fourierMotzkin'(A, V, t);
                     A = D#0;          V = D#1;));
           -- output formatting
           A = apply(A, e -> primitive e);
           if A === {} then A = map(ZZ^d, ZZ^0, 0)
           else A = transpose matrix A;
           if E === {} then E = map(ZZ^d, ZZ^0, 0)
           else E = transpose matrix E;
           (A, E));

i93 : code(polarCone,Matrix)

o93 = -- code for method: polarCone(Matrix)
      /home/dan/src/M2/1.2/Macaulay2/packages/ComputationsBook/toricHilbertScheme/polarCone.m2:199:26-200:49: --source code:
      polarCone(Matrix) := (Z) -> (
           polarCone(Z, map(ZZ^(rank target Z), ZZ^0, 0)));

i94 : H = transpose matrix{
      {1,2,3},
      {1,3,2},
      {2,1,3},
      {2,3,1},
      {3,1,2},
      {3,2,1}};

3       6
o94 : Matrix ZZ  <-- ZZ

i95 : P = polarCone H

o95 = (| 1  1  1  -1 -1 -5 |, 0)
       | -1 1  -5 1  -1 1  |
       | -1 -5 1  -1 1  1  |

o95 : Sequence

i96 : Q = polarCone P_0

o96 = (| 1 1 2 2 3 3 |, 0)
       | 2 3 1 3 1 2 |
       | 3 2 3 1 2 1 |

o96 : Sequence
```

---

## toricHilbertScheme / test.m2 — chunk 12

### Input

```macaulay2
A = QQ[a..e];
I = ideal(a-b^2-1, b-c^2, c-d^2, a^2-e^2)
F = removeRedundantVariables I
I1 = ideal gens gb(F I)
ideal compress (F.matrix - vars A) + I1
code findRedundant
code removeRedundantVariables
i104 :
```

### Output

```
i97 : A = QQ[a..e];

i98 : I = ideal(a-b^2-1, b-c^2, c-d^2, a^2-e^2)

2             2         2       2    2
o98 = ideal (- b  + a - 1, - c  + b, - d  + c, a  - e )

o98 : Ideal of A

i99 : F = removeRedundantVariables I

8       4   2
o99 = map (A, A, {d  + 1, d , d , d, e})

o99 : RingMap A <-- A

i100 : I1 = ideal gens gb(F I)

16     8    2
o100 = ideal(d   + 2d  - e  + 1)

o100 : Ideal of A

i101 : ideal compress (F.matrix - vars A) + I1

8           4       2       16     8    2
o101 = ideal (d  - a + 1, d  - b, d  - c, d   + 2d  - e  + 1)

o101 : Ideal of A

i102 : code findRedundant

o102 = /home/dan/src/M2/1.2/Macaulay2/packages/ComputationsBook/toricHilbertScheme/minPres.m2:1:18-12:32: --source code:
       findRedundant=(f)->(
            A := ring(f);
            p := first entries contract(vars A,f);
            i := position(p, g -> g != 0 and first degree g === 0);
            if i === null then
                null
            else (
                 v := A_i;
                 c := f_v;
                 {i,(-1)*(c^(-1)*(f-c*v))}
                 )
            )

i103 : code removeRedundantVariables

o103 = /home/dan/src/M2/1.2/Macaulay2/packages/ComputationsBook/toricHilbertScheme/minPres.m2:14:32-39:21: --source code:
       removeRedundantVariables = (I) -> (
            A := ring I;
            xmap := new MutableList from gens A;       
            M := gens I;
            findnext := () -> (
                 p := null;
                 next := 0;
                 done := false;
                 ngens := numgens source M;
                 while next < ngens and not done do (
                   p = findRedundant(M_(0,next));
                   if p =!= null then
                        done = true
                   else next=next+1;
                 );
                 p);
            p := findnext();
            while p =!= null do (
                 xmap#(p#0) = p#1;
                 F1 := map(A,A,toList xmap);
                 F2 := map(A,A, F1 (F1.matrix));
                 xmap = new MutableList from first entries F2.matrix;
                 M = compress(F2 M);
                 p = findnext();
                 );
            map(A,A,toList xmap));

i104 :
```

---

## varieties / chapter.m2 — chunk 0

### Input

```macaulay2
R = QQ[x,y,z]
curve = ideal( x^4-y^5, x^3-y^7 )
gb curve
dim curve
codim curve
degree curve
curve1 = saturate(curve,ideal(x))
curve2 = saturate(curve,curve1)
```

### Output

```
i1 : R = QQ[x,y,z]

o1 = R

o1 : PolynomialRing

i2 : curve = ideal( x^4-y^5, x^3-y^7 )

5    4     7    3
o2 = ideal (- y  + x , - y  + x )

o2 : Ideal of R

i3 : gb curve

o3 = | y5-x4 x4y2-x3 x8-x3y3 |

o3 : GroebnerBasis

i4 : dim curve

o4 = 1

i5 : codim curve

o5 = 2

i6 : degree curve

o6 = 28

i7 : curve1 = saturate(curve,ideal(x))

2       5    4   5    3
o7 = ideal (x*y  - 1, y  - x , x  - y )

o7 : Ideal of R

i8 : curve2 = saturate(curve,curve1)

3   5
o8 = ideal (x , y )

o8 : Ideal of R
```

---

## varieties / chapter.m2 — chunk 1

### Input

```macaulay2
curve == radical curve
curve = curve1
degree curve
curve == radical curve
surface = ideal( x^5 + y^5 + z^5 - 1)
theirunion = intersect(curve,surface)
curve*surface == theirunion
ourpoints = curve + surface
```

### Output

```
i9 : curve == radical curve

o9 = false

i10 : curve = curve1

2       5    4   5    3
o10 = ideal (x*y  - 1, y  - x , x  - y )

o10 : Ideal of R

i11 : degree curve

o11 = 13

i12 : curve == radical curve

o12 = true

i13 : surface = ideal( x^5 + y^5 + z^5 - 1)

5    5    5
o13 = ideal(x  + y  + z  - 1)

o13 : Ideal of R

i14 : theirunion = intersect(curve,surface)

6 2      7      2 5    5    5    5      2       5 5    10    5 5    9    4 5    4 5    5    4   10    5 5    5 5    5 3    8    3 5    5    3
o14 = ideal (x y  + x*y  + x*y z  - x  - y  - z  - x*y  + 1, x y  + y   + y z  - x  - x y  - x z  - y  + x , x   + x y  + x z  - x y  - y  - y z  - x  + y )

o14 : Ideal of R

i15 : curve*surface == theirunion

o15 = true

i16 : ourpoints = curve + surface

2       5    4   5    3   5    5    5
o16 = ideal (x*y  - 1, y  - x , x  - y , x  + y  + z  - 1)

o16 : Ideal of R
```

---

## varieties / chapter.m2 — chunk 2

### Input

```macaulay2
dim ourpoints
degree ourpoints
degree radical ourpoints
staircase = ideal leadTerm ourpoints
T = R/staircase;
basis T
use R;
anyOldPolynomial = y^5*x^5-x^9-y^8+y^3*x^5
```

### Output

```
i17 : dim ourpoints

o17 = 0

i18 : degree ourpoints

o18 = 65

i19 : degree radical ourpoints

o19 = 65

i20 : staircase = ideal leadTerm ourpoints

2   5   5   5
o20 = ideal (x*y , z , y , x )

o20 : Ideal of R

i21 : T = R/staircase;

i22 : basis T

o22 = | 1 x x2 x3 x4 x4y x4yz x4yz2 x4yz3 x4yz4 x4z x4z2 x4z3 x4z4 x3y x3yz x3yz2 x3yz3 x3yz4 x3z x3z2 x3z3 x3z4 x2y x2yz x2yz2 x2yz3 x2yz4 x2z x2z2 x2z3 x2z4 xy xyz xyz2 xyz3 xyz4 xz xz2 xz3 xz4 y y2 y3 y4 y4z y4z2 y4z3 y4z4 y3z y3z2 y3z3 y3z4 y2z y2z2 y2z3 y2z4 yz yz2 yz3 yz4 z z2 z3 z4 |

              1       65
o22 : Matrix T  <--- T

i23 : use R;

i24 : anyOldPolynomial = y^5*x^5-x^9-y^8+y^3*x^5

5 5    9    5 3    8
o24 = x y  - x  + x y  - y

o24 : R
```

---

## varieties / chapter.m2 — chunk 3

### Input

```macaulay2
anyOldPolynomial % ourpoints
anotherPolynomial = y^5*x^5-x^9-y^8+y^3*x^4
anotherPolynomial % ourpoints
R' = ZZ/101[x,y,z];
ourpoints' = substitute(ourpoints,R')
decompose ourpoints'
oo / print @@ print;
ideal (z + 36, y - 1, x - 1)
ooo / degree
```

### Output

```
i25 : anyOldPolynomial % ourpoints

4     3
o25 = x y - x y

o25 : R

i26 : anotherPolynomial = y^5*x^5-x^9-y^8+y^3*x^4

5 5    9    8    4 3
o26 = x y  - x  - y  + x y

o26 : R

i27 : anotherPolynomial % ourpoints

o27 = 0

o27 : R

i28 : R' = ZZ/101[x,y,z];

i29 : ourpoints' = substitute(ourpoints,R')

2       5    4   5    3   5    5    5
o29 = ideal (x*y  - 1, y  - x , x  - y , x  + y  + z  - 1)

o29 : Ideal of R'

i30 : decompose ourpoints'

3      2              2                      3    2     2                                3      2      2             2                   3      2              2                  5      2             2                                2                                            2            2                                   2              2                                        2            2                          3      2            2                   3    2     2                                      2                                         2            2                                      2             2                                           2            2                          3      2            2                   3    2     2                                        2                                           2            2                                 2              2                                       2            2                         3      2            2                   3    2     2                                      2                                            2            2                                 2              2                                          2            2                         3      2            2                   3    2     2                                        2                                          2            2                                     2              2                                           2            2                          3      2            2                   3    2     2
o30 = {ideal (z + 36, y - 1, x - 1), ideal (z + 1, y - 1, x - 1), ideal (z - 6, y - 1, x - 1), ideal (z - 14, y - 1, x - 1), ideal (z - 17, y - 1, x - 1), ideal (x  - 46x  + 28x*y - 27y  + 46x + y + 27, - 16x  + x y + x  - 15x*y + 16x - 15y + 17, - 26x  + x*y  - 16x  - 21x*y - 5y  + 16x - 26y + 4, y  + 28x  - 27x*y + 46y  - 27x + y - 28, z  + 46x  - 46x*y + 8y  - 48x - 19y - 29), ideal (- 32x  - 16x*y + x*z - 16x - 27y - 30z - 14, - 34x  - 14x*y + y  + 9x*z - 5x - 20y - 8z + 43, - 26x  - 38x*y - 37y  + 40x*z + y*z + 41x - 43y - 27z + 1, 5x  + 37x*y + z  - 48x - 46y + 30z - 46, x  + 11x  + 6x*y - 5y  - 11x + y + 5, 19x  + x y + x  + 20x*y - 19x + 20y - 18), ideal (44x  + 22x*y + x*z + 22x - 26y - 30z - 6, 18x  + 12x*y + y  + 13x*z + 21x - 14y - 48z - 10, - 20x  - 11x*y - 3y  + 41x*z + y*z - 49x + 38y + 26z + 3, - 30x  - 20x*y + z  - 15x - 27y - 16z - 27, x  + 11x  + 6x*y - 5y  - 11x + y + 5, 19x  + x y + x  + 20x*y - 19x + 20y - 18), ideal (- 41x  + 30x*y + x*z + 30x + 38y - 30z + 1, - 26x  - 10x*y + y  + 29x*z - x + 12y + 7z - 4, - 7x  + 29x*y - 28y  + x*z + y*z - 36x + 13y + 17z - 9, 16x  - 23x*y + z  + 8x - 26y - 31z - 26, x  + 11x  + 6x*y - 5y  - 11x + y + 5, 19x  + x y + x  + 20x*y - 19x + 20y - 18), ideal (39x  - 31x*y + x*z - 31x - 46y - 30z + 36, - 32x  - 13x*y + y  - 41x*z - 4x - 12y - 39z + 6, 8x  + 22x*y + 22y  - 19x*z + y*z - 17x - 10y - 18z + 13, 31x  - 13x*y + z  - 35x + 38y - 5z + 38, x  + 11x  + 6x*y - 5y  - 11x + y + 5, 19x  + x y + x  + 20x*y - 19x + 20y - 18), ideal (- 10x  - 5x*y + x*z - 5x - 40y - 30z - 17, - 37x  + 35x*y + y  + 19x*z + 44x - 32y + 26z + 48, - 2x  + 24x*y + 12y  - 6x*z + y*z - 17x + 11y + 19z + 30, - 22x  + 19x*y + z  - 11x - 40y + 22z - 40, x  + 11x  + 6x*y - 5y  - 11x + y + 5, 19x  + x y + x  + 20x*y - 19x + 20y - 18)}

o30 : List

i31 : oo / print @@ print;
ideal (z + 36, y - 1, x - 1)

ideal (z + 1, y - 1, x - 1)

ideal (z - 6, y - 1, x - 1)

ideal (z - 14, y - 1, x - 1)

ideal (z - 17, y - 1, x - 1)

        3      2              2                      3    2     2                                3      2      2             2                   3      2              2                  5      2             2
ideal (x  - 46x  + 28x*y - 27y  + 46x + y + 27, - 16x  + x y + x  - 15x*y + 16x - 15y + 17, - 26x  + x*y  - 16x  - 21x*y - 5y  + 16x - 26y + 4, y  + 28x  - 27x*y + 46y  - 27x + y - 28, z  + 46x  - 46x*y + 8y  - 48x - 19y - 29)

            2                                            2            2                                   2              2                                        2            2                          3      2            2                   3    2     2
ideal (- 32x  - 16x*y + x*z - 16x - 27y - 30z - 14, - 34x  - 14x*y + y  + 9x*z - 5x - 20y - 8z + 43, - 26x  - 38x*y - 37y  + 40x*z + y*z + 41x - 43y - 27z + 1, 5x  + 37x*y + z  - 48x - 46y + 30z - 46, x  + 11x  + 6x*y - 5y  - 11x + y + 5, 19x  + x y + x  + 20x*y - 19x + 20y - 18)

          2                                         2            2                                      2             2                                           2            2                          3      2            2                   3    2     2
ideal (44x  + 22x*y + x*z + 22x - 26y - 30z - 6, 18x  + 12x*y + y  + 13x*z + 21x - 14y - 48z - 10, - 20x  - 11x*y - 3y  + 41x*z + y*z - 49x + 38y + 26z + 3, - 30x  - 20x*y + z  - 15x - 27y - 16z - 27, x  + 11x  + 6x*y - 5y  - 11x + y + 5, 19x  + x y + x  + 20x*y - 19x + 20y - 18)

            2                                           2            2                                 2              2                                       2            2                         3      2            2                   3    2     2
ideal (- 41x  + 30x*y + x*z + 30x + 38y - 30z + 1, - 26x  - 10x*y + y  + 29x*z - x + 12y + 7z - 4, - 7x  + 29x*y - 28y  + x*z + y*z - 36x + 13y + 17z - 9, 16x  - 23x*y + z  + 8x - 26y - 31z - 26, x  + 11x  + 6x*y - 5y  - 11x + y + 5, 19x  + x y + x  + 20x*y - 19x + 20y - 18)

          2                                            2            2                                 2              2                                          2            2                         3      2            2                   3    2     2
ideal (39x  - 31x*y + x*z - 31x - 46y - 30z + 36, - 32x  - 13x*y + y  - 41x*z - 4x - 12y - 39z + 6, 8x  + 22x*y + 22y  - 19x*z + y*z - 17x - 10y - 18z + 13, 31x  - 13x*y + z  - 35x + 38y - 5z + 38, x  + 11x  + 6x*y - 5y  - 11x + y + 5, 19x  + x y + x  + 20x*y - 19x + 20y - 18)

            2                                          2            2                                     2              2                                           2            2                          3      2            2                   3    2     2
ideal (- 10x  - 5x*y + x*z - 5x - 40y - 30z - 17, - 37x  + 35x*y + y  + 19x*z + 44x - 32y + 26z + 48, - 2x  + 24x*y + 12y  - 6x*z + y*z - 17x + 11y + 19z + 30, - 22x  + 19x*y + z  - 11x - 40y + 22z - 40, x  + 11x  + 6x*y - 5y  - 11x + y + 5, 19x  + x y + x  + 20x*y - 19x + 20y - 18)

i32 : ooo / degree

o32 = {1, 1, 1, 1, 1, 30, 6, 6, 6, 6, 6}

o32 : List
```

---

## varieties / chapter.m2 — chunk 4

### Input

```macaulay2
S = QQ[z,y,x, MonomialOrder => Eliminate 2]
ourpoints'' = substitute(ourpoints,S)
G = gens gb ourpoints''
ideal selectInSubring(1,G)
M = staircase^3
numgens M
transpose gens M
degree M
```

### Output

```
i33 : S = QQ[z,y,x, MonomialOrder => Eliminate 2]

o33 = S

o33 : PolynomialRing

i34 : ourpoints'' = substitute(ourpoints,S)

2        5    4     3    5   5    5    5
o34 = ideal (y x - 1, y  - x , - y  + x , z  + y  + x  - 1)

o34 : Ideal of S

i35 : G = gens gb ourpoints''

o35 = | x13-1 y-x6 z5+x5+x4-1 |

              1       3
o35 : Matrix S  <--- S

i36 : ideal selectInSubring(1,G)

13
o36 = ideal(x   - 1)

o36 : Ideal of S

i37 : M = staircase^3

3 6   2 4 5   2 9   7 4     2 10     7 5   6 2 5     12   6 7   11 2   15   5 10   5 10   10 5   5 5 5   10 5   15   5 10   10 5   15
o37 = ideal (x y , x y z , x y , x y , x*y z  , x*y z , x y z , x*y  , x y , x  y , z  , y z  , x z  , y  z , x y z , x  z , y  , x y  , x  y , x  )

o37 : Ideal of R

i38 : numgens M

o38 = 20

i39 : transpose gens M

o39 = {-9}  | x3y6   |
      {-11} | x2y4z5 |
      {-11} | x2y9   |
      {-11} | x7y4   |
      {-13} | xy2z10 |
      {-13} | xy7z5  |
      {-13} | x6y2z5 |
      {-13} | xy12   |
      {-13} | x6y7   |
      {-13} | x11y2  |
      {-15} | z15    |
      {-15} | y5z10  |
      {-15} | x5z10  |
      {-15} | y10z5  |
      {-15} | x5y5z5 |
      {-15} | x10z5  |
      {-15} | y15    |
      {-15} | x5y10  |
      {-15} | x10y5  |
      {-15} | x15    |

              20       1
o39 : Matrix R   <--- R

i40 : degree M

o40 = 690
```

---

## varieties / chapter.m2 — chunk 5

### Input

```macaulay2
S = R/M
basis S
tally apply(flatten entries basis(S),degree)
basis(19,S)
(x+y+z)^19
C = res M
C.dd_1
set flatten entries gens M - set flatten entries C.dd_1
```

### Output

```
i41 : S = R/M

o41 = S

o41 : QuotientRing

i42 : basis S

o42 = | 1 x x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x14y x14yz x14yz2 x14yz3 x14yz4 x14z x14z2 x14z3 x14z4 x13y x13yz x13yz2 x13yz3 x13yz4 x13z x13z2 x13z3 x13z4 x12y x12yz x12yz2 x12yz3 x12yz4 x12z x12z2 x12z3 x12z4 x11y x11yz x11yz2 x11yz3 x11yz4 x11z x11z2 x11z3 x11z4 x10y x10y2 x10y3 x10y3z x10y3z2 x10y3z3 x10y3z4 x10y2z x10y2z2 x10y2z3 x10y2z4 x10yz x10yz2 x10yz3 x10yz4 x10z x10z2 x10z3 x10z4 x9y x9y2 x9y3 x9y3z x9y3z2 x9y3z3 x9y3z4 x9y2z x9y2z2 x9y2z3 x9y2z4 x9yz x9yz2 x9yz3 x9yz4 x9yz5 x9yz6 x9yz7 x9yz8 x9yz9 x9z x9z2 x9z3 x9z4 x9z5 x9z6 x9z7 x9z8 x9z9 x8y x8y2 x8y3 x8y3z x8y3z2 x8y3z3 x8y3z4 x8y2z x8y2z2 x8y2z3 x8y2z4 x8yz x8yz2 x8yz3 x8yz4 x8yz5 x8yz6 x8yz7 x8yz8 x8yz9 x8z x8z2 x8z3 x8z4 x8z5 x8z6 x8z7 x8z8 x8z9 x7y x7y2 x7y3 x7y3z x7y3z2 x7y3z3 x7y3z4 x7y2z x7y2z2 x7y2z3 x7y2z4 x7yz x7yz2 x7yz3 x7yz4 x7yz5 x7yz6 x7yz7 x7yz8 x7yz9 x7z x7z2 x7z3 x7z4 x7z5 x7z6 x7z7 x7z8 x7z9 x6y x6y2 x6y3 x6y4 x6y5 x6y5z x6y5z2 x6y5z3 x6y5z4 x6y4z x6y4z2 x6y4z3 x6y4z4 x6y3z x6y3z2 x6y3z3 x6y3z4 x6y2z x6y2z2 x6y2z3 x6y2z4 x6yz x6yz2 x6yz3 x6yz4 x6yz5 x6yz6 x6yz7 x6yz8 x6yz9 x6z x6z2 x6z3 x6z4 x6z5 x6z6 x6z7 x6z8 x6z9 x5y x5y2 x5y3 x5y4 x5y5 x5y5z x5y5z2 x5y5z3 x5y5z4 x5y4z x5y4z2 x5y4z3 x5y4z4 x5y3z x5y3z2 x5y3z3 x5y3z4 x5y3z5 x5y3z6 x5y3z7 x5y3z8 x5y3z9 x5y2z x5y2z2 x5y2z3 x5y2z4 x5y2z5 x5y2z6 x5y2z7 x5y2z8 x5y2z9 x5yz x5yz2 x5yz3 x5yz4 x5yz5 x5yz6 x5yz7 x5yz8 x5yz9 x5z x5z2 x5z3 x5z4 x5z5 x5z6 x5z7 x5z8 x5z9 x4y x4y2 x4y3 x4y4 x4y5 x4y5z x4y5z2 x4y5z3 x4y5z4 x4y4z x4y4z2 x4y4z3 x4y4z4 x4y3z x4y3z2 x4y3z3 x4y3z4 x4y3z5 x4y3z6 x4y3z7 x4y3z8 x4y3z9 x4y2z x4y2z2 x4y2z3 x4y2z4 x4y2z5 x4y2z6 x4y2z7 x4y2z8 x4y2z9 x4yz x4yz2 x4yz3 x4yz4 x4yz5 x4yz6 x4yz7 x4yz8 x4yz9 x4yz10 x4yz11 x4yz12 x4yz13 x4yz14 x4z x4z2 x4z3 x4z4 x4z5 x4z6 x4z7 x4z8 x4z9 x4z10 x4z11 x4z12 x4z13 x4z14 x3y x3y2 x3y3 x3y4 x3y5 x3y5z x3y5z2 x3y5z3 x3y5z4 x3y4z x3y4z2 x3y4z3 x3y4z4 x3y3z x3y3z2 x3y3z3 x3y3z4 x3y3z5 x3y3z6 x3y3z7 x3y3z8 x3y3z9 x3y2z x3y2z2 x3y2z3 x3y2z4 x3y2z5 x3y2z6 x3y2z7 x3y2z8 x3y2z9 x3yz x3yz2 x3yz3 x3yz4 x3yz5 x3yz6 x3yz7 x3yz8 x3yz9 x3yz10 x3yz11 x3yz12 x3yz13 x3yz14 x3z x3z2 x3z3 x3z4 x3z5 x3z6 x3z7 x3z8 x3z9 x3z10 x3z11 x3z12 x3z13 x3z14 x2y x2y2 x2y3 x2y4 x2y5 x2y6 x2y7 x2y8 x2y8z x2y8z2 x2y8z3 x2y8z4 x2y7z x2y7z2 x2y7z3 x2y7z4 x2y6z x2y6z2 x2y6z3 x2y6z4 x2y5z x2y5z2 x2y5z3 x2y5z4 x2y4z x2y4z2 x2y4z3 x2y4z4 x2y3z x2y3z2 x2y3z3 x2y3z4 x2y3z5 x2y3z6 x2y3z7 x2y3z8 x2y3z9 x2y2z x2y2z2 x2y2z3 x2y2z4 x2y2z5 x2y2z6 x2y2z7 x2y2z8 x2y2z9 x2yz x2yz2 x2yz3 x2yz4 x2yz5 x2yz6 x2yz7 x2yz8 x2yz9 x2yz10 x2yz11 x2yz12 x2yz13 x2yz14 x2z x2z2 x2z3 x2z4 x2z5 x2z6 x2z7 x2z8 x2z9 x2z10 x2z11 x2z12 x2z13 x2z14 xy xy2 xy3 xy4 xy5 xy6 xy7 xy8 xy9 xy10 xy11 xy11z xy11z2 xy11z3 xy11z4 xy10z xy10z2 xy10z3 xy10z4 xy9z xy9z2 xy9z3 xy9z4 xy8z xy8z2 xy8z3 xy8z4 xy7z xy7z2 xy7z3 xy7z4 xy6z xy6z2 xy6z3 xy6z4 xy6z5 xy6z6 xy6z7 xy6z8 xy6z9 xy5z xy5z2 xy5z3 xy5z4 xy5z5 xy5z6 xy5z7 xy5z8 xy5z9 xy4z xy4z2 xy4z3 xy4z4 xy4z5 xy4z6 xy4z7 xy4z8 xy4z9 xy3z xy3z2 xy3z3 xy3z4 xy3z5 xy3z6 xy3z7 xy3z8 xy3z9 xy2z xy2z2 xy2z3 xy2z4 xy2z5 xy2z6 xy2z7 xy2z8 xy2z9 xyz xyz2 xyz3 xyz4 xyz5 xyz6 xyz7 xyz8 xyz9 xyz10 xyz11 xyz12 xyz13 xyz14 xz xz2 xz3 xz4 xz5 xz6 xz7 xz8 xz9 xz10 xz11 xz12 xz13 xz14 y y2 y3 y4 y5 y6 y7 y8 y9 y10 y11 y12 y13 y14 y14z y14z2 y14z3 y14z4 y13z y13z2 y13z3 y13z4 y12z y12z2 y12z3 y12z4 y11z y11z2 y11z3 y11z4 y10z y10z2 y10z3 y10z4 y9z y9z2 y9z3 y9z4 y9z5 y9z6 y9z7 y9z8 y9z9 y8z y8z2 y8z3 y8z4 y8z5 y8z6 y8z7 y8z8 y8z9 y7z y7z2 y7z3 y7z4 y7z5 y7z6 y7z7 y7z8 y7z9 y6z y6z2 y6z3 y6z4 y6z5 y6z6 y6z7 y6z8 y6z9 y5z y5z2 y5z3 y5z4 y5z5 y5z6 y5z7 y5z8 y5z9 y4z y4z2 y4z3 y4z4 y4z5 y4z6 y4z7 y4z8 y4z9 y4z10 y4z11 y4z12 y4z13 y4z14 y3z y3z2 y3z3 y3z4 y3z5 y3z6 y3z7 y3z8 y3z9 y3z10 y3z11 y3z12 y3z13 y3z14 y2z y2z2 y2z3 y2z4 y2z5 y2z6 y2z7 y2z8 y2z9 y2z10 y2z11 y2z12 y2z13 y2z14 yz yz2 yz3 yz4 yz5 yz6 yz7 yz8 yz9 yz10 yz11 yz12 yz13 yz14 z z2 z3 z4 z5 z6 z7 z8 z9 z10 z11 z12 z13 z14 |

              1       690
o42 : Matrix S  <--- S

i43 : tally apply(flatten entries basis(S),degree)

o43 = Tally{{0} => 1  }
            {1} => 3
            {10} => 63
            {11} => 69
            {12} => 73
            {13} => 71
            {14} => 66
            {15} => 53
            {16} => 38
            {17} => 23
            {18} => 12
            {19} => 3
            {2} => 6
            {3} => 10
            {4} => 15
            {5} => 21
            {6} => 28
            {7} => 36
            {8} => 45
            {9} => 54

o43 : Tally

i44 : basis(19,S)

o44 = | x14yz4 x9yz9 x4yz14 |

              1       3
o44 : Matrix S  <--- S

i45 : (x+y+z)^19

14   4          9   9         4   14
o45 = 58140x  y*z  + 923780x y*z  + 58140x y*z

o45 : S

i46 : C = res M

1      16      27      12
o46 = R  <-- R   <-- R   <-- R   <-- 0
                                      
      0      1       2       3       4

o46 : ChainComplex

i47 : C.dd_1

o47 = | x3y6 x7y4 x2y9 x2y4z5 x11y2 xy12 x6y2z5 xy7z5 xy2z10 x15 y15 x10z5 y10z5 x5z10 y5z10 z15 |

              1       16
o47 : Matrix R  <--- R

i48 : set flatten entries gens M - set flatten entries C.dd_1

6 7   10 5   5 10   5 5 5
o48 = Set {x y , x  y , x y  , x y z }

o48 : Set
```

---

## varieties / chapter.m2 — chunk 6

### Input

```macaulay2
C.dd_2
C.dd_3
A = {{1, 1, 1, 1},
           {1, 5,10,25}}
R = QQ[p,n,d,q, Degrees => transpose A]
degree d
degree q
degree(p^4*n^8*d^10*q^3)
h = basis({25,219}, R)
```

### Output

```
i49 : C.dd_2

o49 = {9}  | -y3 -x4 0   -z5 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   |
      {11} | 0   y2  0   0   0   -x4 0   0   -z5 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   |
      {11} | x   0   -y3 0   0   0   0   0   0   -z5 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   |
      {11} | 0   0   0   xy2 -y3 0   -x4 0   x5  y5  0   -z5 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   |
      {13} | 0   0   0   0   0   y2  0   0   0   0   0   0   0   -x4 0   0   -z5 0   0   0   0   0   0   0   0   0   0   |
      {13} | 0   0   x   0   0   0   0   -y3 0   0   0   0   0   0   0   0   0   -z5 0   0   0   0   0   0   0   0   0   |
      {13} | 0   0   0   0   0   0   y2  0   0   0   0   0   0   0   -x4 0   x5  0   -z5 0   0   0   0   0   0   0   0   |
      {13} | 0   0   0   0   x   0   0   0   0   0   -y3 0   0   0   0   0   0   y5  0   -z5 0   0   0   0   0   0   0   |
      {13} | 0   0   0   0   0   0   0   0   0   0   0   xy2 -y3 0   0   -x4 0   0   x5  y5  -z5 0   0   0   0   0   0   |
      {15} | 0   0   0   0   0   0   0   0   0   0   0   0   0   y2  0   0   0   0   0   0   0   -z5 0   0   0   0   0   |
      {15} | 0   0   0   0   0   0   0   x   0   0   0   0   0   0   0   0   0   0   0   0   0   0   -z5 0   0   0   0   |
      {15} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   y2  0   0   0   0   0   0   x5  0   -z5 0   0   0   |
      {15} | 0   0   0   0   0   0   0   0   0   0   x   0   0   0   0   0   0   0   0   0   0   0   y5  0   -z5 0   0   |
      {15} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   y2  0   0   0   0   0   0   0   x5  0   -z5 0   |
      {15} | 0   0   0   0   0   0   0   0   0   0   0   0   x   0   0   0   0   0   0   0   0   0   0   0   y5  0   -z5 |
      {15} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   xy2 0   0   0   0   x5  y5  |

              16       27
o49 : Matrix R   <--- R

i50 : C.dd_3

o50 = {12} | z5  0   0   0   0   0   0   0   0   0   0   0   |
      {13} | 0   z5  0   0   0   0   0   0   0   0   0   0   |
      {14} | 0   0   z5  0   0   0   0   0   0   0   0   0   |
      {14} | -y3 -x4 0   0   0   0   0   0   0   0   0   0   |
      {14} | 0   0   -y5 z5  0   0   0   0   0   0   0   0   |
      {15} | 0   0   0   0   z5  0   0   0   0   0   0   0   |
      {15} | 0   0   0   0   -x5 z5  0   0   0   0   0   0   |
      {16} | 0   0   0   0   0   0   z5  0   0   0   0   0   |
      {16} | 0   y2  0   0   -x4 0   0   0   0   0   0   0   |
      {16} | x   0   -y3 0   0   0   0   0   0   0   0   0   |
      {16} | 0   0   0   0   0   0   -y5 z5  0   0   0   0   |
      {16} | 0   0   0   -y3 0   -x4 0   0   0   0   0   0   |
      {16} | 0   0   0   0   0   0   0   -y5 z5  0   0   0   |
      {17} | 0   0   0   0   0   0   0   0   0   z5  0   0   |
      {17} | 0   0   0   0   0   0   0   0   0   -x5 z5  0   |
      {17} | 0   0   0   0   0   0   0   0   0   0   -x5 z5  |
      {18} | 0   0   0   0   y2  0   0   0   0   -x4 0   0   |
      {18} | 0   0   x   0   0   0   -y3 0   0   0   0   0   |
      {18} | 0   0   0   0   0   y2  0   0   0   0   -x4 0   |
      {18} | 0   0   0   x   0   0   0   -y3 0   0   0   0   |
      {18} | 0   0   0   0   0   0   0   0   -y3 0   0   -x4 |
      {20} | 0   0   0   0   0   0   0   0   0   y2  0   0   |
      {20} | 0   0   0   0   0   0   x   0   0   0   0   0   |
      {20} | 0   0   0   0   0   0   0   0   0   0   y2  0   |
      {20} | 0   0   0   0   0   0   0   x   0   0   0   0   |
      {20} | 0   0   0   0   0   0   0   0   0   0   0   y2  |
      {20} | 0   0   0   0   0   0   0   0   x   0   0   0   |

              27       12
o50 : Matrix R   <--- R

i51 : A = {{1, 1, 1, 1},
           {1, 5,10,25}}

o51 = {{1, 1, 1, 1}, {1, 5, 10, 25}}

o51 : List

i52 : R = QQ[p,n,d,q, Degrees => transpose A]

o52 = R

o52 : PolynomialRing

i53 : degree d

o53 = {1, 10}

o53 : List

i54 : degree q

o54 = {1, 25}

o54 : List

i55 : degree(p^4*n^8*d^10*q^3)

o55 = {25, 219}

o55 : List

i56 : h = basis({25,219}, R)

o56 = | p14n2d2q7 p9n8d2q6 p9n5d6q5 p9n2d10q4 p4n14d2q5 p4n11d6q4 p4n8d10q3 p4n5d14q2 p4n2d18q |

              1       9
o56 : Matrix R  <--- R
```

---

## varieties / chapter.m2 — chunk 7

### Input

```macaulay2
rank source h
rank source basis({100,1000}, R)
S = QQ[x, y, d, p, n, q, 
          MonomialOrder => Lex, MonomialSize => 16]
I = ideal( p - x*y, n - x*y^5, d - x*y^10, q - x*y^25)
transpose gens gb I
S' = S/I
x^10 * y^100
x^100 * y^1000
```

### Output

```
i57 : rank source h

o57 = 9

i58 : rank source basis({100,1000}, R)

o58 = 182

i59 : S = QQ[x, y, d, p, n, q, 
          MonomialOrder => Lex, MonomialSize => 16]

o59 = S

o59 : PolynomialRing

i60 : I = ideal( p - x*y, n - x*y^5, d - x*y^10, q - x*y^25)

5           10           25
o60 = ideal (- x*y + p, - x*y  + n, - x*y   + d, - x*y   + q)

o60 : Ideal of S

i61 : transpose gens gb I

o61 = {-6}  | p5q-n6     |
      {-4}  | d4-n3q     |
      {-3}  | yn2-dp     |
      {-6}  | yp4q-dn4   |
      {-4}  | yd3-pnq    |
      {-6}  | y2p3q-d2n2 |
      {-5}  | y2d2n-p2q  |
      {-7}  | y2d2p3-n5  |
      {-6}  | y3p2q-d3   |
      {-6}  | y3dp2-n3   |
      {-5}  | y4p-n      |
      {-6}  | y5n-d      |
      {-8}  | y6d2-pq    |
      {-16} | y15d-q     |
      {-7}  | xq-y5d2    |
      {-5}  | xn-y3p2    |
      {-2}  | xd-n2      |
      {-2}  | xy-p       |

              18       1
o61 : Matrix S   <--- S

i62 : S' = S/I

o62 = S'

o62 : QuotientRing

i63 : x^10 * y^100

2 6 2
o63 = d n q

o63 : S'

i64 : x^100 * y^1000

75 25
o64 = n  q

o64 : S'
```

---

## varieties / chapter.m2 — chunk 8

### Input

```macaulay2
x^39 * y^1000
weight = (5,7,13,17)
T = QQ[x, y, p, n, d, q, 
                Weights => {{1,1,0,0,0,0},{0,0,weight}},
                MonomialSize => 16]/
            (p - x*y, n - x*y^5, d - x*y^10, q - x*y^25);
x^10 * y^100
x^100 * y^1000
x^234 * y^5677
i71 :
```

### Output

```
i65 : x^39 * y^1000

25 39
o65 = y  q

o65 : S'

i66 : weight = (5,7,13,17)

o66 = (5, 7, 13, 17)

o66 : Sequence

i67 : T = QQ[x, y, p, n, d, q, 
                Weights => {{1,1,0,0,0,0},{0,0,weight}},
                MonomialSize => 16]/
            (p - x*y, n - x*y^5, d - x*y^10, q - x*y^25);

i68 : x^10 * y^100

5 2 3
o68 = p d q

o68 : T

i69 : x^100 * y^1000

60 3 37
o69 = p  n q

o69 : T

i70 : x^234 * y^5677

2 4 3 225
o70 = p n d q

o70 : T

i71 :
```

---

## varieties / test.m2 — chunk 0

### Input

```macaulay2
R = QQ[x,y,z]
curve = ideal( x^4-y^5, x^3-y^7 )
gb curve
dim curve
codim curve
degree curve
curve1 = saturate(curve,ideal(x))
curve2 = saturate(curve,curve1)
```

### Output

```
i1 : R = QQ[x,y,z]

o1 = R

o1 : PolynomialRing

i2 : curve = ideal( x^4-y^5, x^3-y^7 )

5    4     7    3
o2 = ideal (- y  + x , - y  + x )

o2 : Ideal of R

i3 : gb curve

o3 = GroebnerBasis[status: done; S-pairs encountered up to degree 11]

o3 : GroebnerBasis

i4 : dim curve

o4 = 1

i5 : codim curve

o5 = 2

i6 : degree curve

o6 = 28

i7 : curve1 = saturate(curve,ideal(x))

2       5    4   5    3
o7 = ideal (x*y  - 1, y  - x , x  - y )

o7 : Ideal of R

i8 : curve2 = saturate(curve,curve1)

3   5
o8 = ideal (x , y )

o8 : Ideal of R
```

---

## varieties / test.m2 — chunk 1

### Input

```macaulay2
curve == radical curve
curve = curve1
degree curve
curve == radical curve
surface = ideal( x^5 + y^5 + z^5 - 1)
theirunion = intersect(curve,surface)
curve*surface == theirunion
ourpoints = curve + surface
```

### Output

```
i9 : curve == radical curve

o9 = false

i10 : curve = curve1

2       5    4   5    3
o10 = ideal (x*y  - 1, y  - x , x  - y )

o10 : Ideal of R

i11 : degree curve

o11 = 13

i12 : curve == radical curve

o12 = true

i13 : surface = ideal( x^5 + y^5 + z^5 - 1)

5    5    5
o13 = ideal(x  + y  + z  - 1)

o13 : Ideal of R

i14 : theirunion = intersect(curve,surface)

6 2      7      2 5    5    5    5      2       5 5    10    5 5    9    4 5    4 5    5    4   10    10    5 5    5 5    9    4 5    4 5    5 3    8    3 5    5    5    4    3
o14 = ideal (x y  + x*y  + x*y z  - x  - y  - z  - x*y  + 1, x y  + y   + y z  - x  - x y  - x z  - y  + x , x   - y   + x z  - y z  + x  + x y  + x z  - x y  - y  - y z  - x  + y  - x  + y )

o14 : Ideal of R

i15 : curve*surface == theirunion

o15 = true

i16 : ourpoints = curve + surface

2       5    4   5    3   5    5    5
o16 = ideal (x*y  - 1, y  - x , x  - y , x  + y  + z  - 1)

o16 : Ideal of R
```

---

## varieties / test.m2 — chunk 2

### Input

```macaulay2
dim ourpoints
degree ourpoints
degree radical ourpoints
staircase = ideal leadTerm ourpoints
T = R/staircase;
basis T
use R;
anyOldPolynomial = y^5*x^5-x^9-y^8+y^3*x^5
```

### Output

```
i17 : dim ourpoints

o17 = 0

i18 : degree ourpoints

o18 = 65

i19 : degree radical ourpoints

o19 = 65

i20 : staircase = ideal leadTerm ourpoints

2   5   5   5
o20 = ideal (x*y , z , y , x )

o20 : Ideal of R

i21 : T = R/staircase;

i22 : basis T

o22 = | 1 x x2 x3 x4 x4y x4yz x4yz2 x4yz3 x4yz4 x4z x4z2 x4z3 x4z4 x3y x3yz x3yz2 x3yz3 x3yz4 x3z x3z2 x3z3 x3z4 x2y x2yz x2yz2 x2yz3 x2yz4 x2z x2z2 x2z3 x2z4 xy xyz xyz2 xyz3 xyz4 xz xz2 xz3 xz4 y y2 y3 y4 y4z y4z2 y4z3 y4z4 y3z y3z2 y3z3 y3z4 y2z y2z2 y2z3 y2z4 yz yz2 yz3 yz4 z z2 z3 z4 |

              1      65
o22 : Matrix T  <-- T

i23 : use R;

i24 : anyOldPolynomial = y^5*x^5-x^9-y^8+y^3*x^5

5 5    9    5 3    8
o24 = x y  - x  + x y  - y

o24 : R
```

---

## varieties / test.m2 — chunk 3

### Input

```macaulay2
anyOldPolynomial % ourpoints
anotherPolynomial = y^5*x^5-x^9-y^8+y^3*x^4
anotherPolynomial % ourpoints
R' = ZZ/101[x,y,z];
ourpoints' = substitute(ourpoints,R')
decompose ourpoints'
oo / (x -> <<endl) @@ print;
ideal (z - 6, y - 1, x - 1)
ooo / degree
```

### Output

```
i25 : anyOldPolynomial % ourpoints

4     3
o25 = x y - x y

o25 : R

i26 : anotherPolynomial = y^5*x^5-x^9-y^8+y^3*x^4

5 5    9    8    4 3
o26 = x y  - x  - y  + x y

o26 : R

i27 : anotherPolynomial % ourpoints

o27 = 0

o27 : R

i28 : R' = ZZ/101[x,y,z];

i29 : ourpoints' = substitute(ourpoints,R')

2       5    4   5    3   5    5    5
o29 = ideal (x*y  - 1, y  - x , x  - y , x  + y  + z  - 1)

o29 : Ideal of R'

i30 : decompose ourpoints'

2                          2             2                                         2                          2              2                                                2                          2              2                                       2                          2             2                                                 2                          2              2                                        2                          2              2                                                 2                         2              2                                         2                          2              2                                                2                          2              2                                       2                          2              2                                 3      2              2                    2       2       2              2                  3      2              2                  5      2             2
o30 = {ideal (z - 6, y - 1, x - 1), ideal (z - 14, y - 1, x - 1), ideal (z - 17, y - 1, x - 1), ideal (z + 36, y - 1, x - 1), ideal (z + 1, y - 1, x - 1), ideal (x*z - 44y*z - 22z  - 22x - 23y + 32z - 44, y  + 2y*z - 38z  + 13x + 14y - 47z - 4, x*y + 36y*z + 31z  + 18x - 31y - 13z + 11, x  - 24y*z + 32z  + 39x - 2y - 8z - 30), ideal (x*z - 44y*z - 30z  + 31x + 37y + 32z - 39, y  - 34y*z + 27z  + 13x + 14y - 9z - 4, x*y - 6y*z - 30z  + 18x - 31y + 19z + 11, x  + 4y*z - 44z  + 39x - 2y + 35z - 30), ideal (x*z - 44y*z + 31z  - 30x - 13y + 32z + 41, y  - 12y*z + 46z  + 13x + 14y - 21z - 4, x*y - 14y*z + 5z  + 18x - 31y - 23z + 11, x  + 43y*z + 41z  + 39x - 2y + 48z - 30), ideal (x*z - 44y*z + 16z  + 5x + 19y + 32z + 10, y  - 29y*z + 40z  + 13x + 14y + 25z - 4, x*y - 17y*z - 22z  + 18x - 31y + 37z + 11, x  + 45y*z - 39z  + 39x - 2y + 15z - 30), ideal (x*z - 44y*z + 5z  + 16x - 20y + 32z + 32, y  - 28y*z + 26z  + 13x + 14y - 49z - 4, x*y + y*z + 16z  + 18x - 31y - 20z + 11, x  + 33y*z + 10z  + 39x - 2y + 11z - 30), ideal (y  + 28x  - 27x*y + 46y  - 27x + y - 28, x*y  - 1, x y - 28x  + 29x*y - 28y  + 45x + y + 45, x  - 46x  + 28x*y - 27y  + 46x + y + 27, z  + 46x  - 46x*y + 8y  - 48x - 19y - 29)}

o30 : List

i31 : oo / (x -> <<endl) @@ print;
ideal (z - 6, y - 1, x - 1)

ideal (z - 14, y - 1, x - 1)

ideal (z - 17, y - 1, x - 1)

ideal (z + 36, y - 1, x - 1)

ideal (z + 1, y - 1, x - 1)

                        2                          2             2                                         2                          2              2
ideal (x*z - 44y*z - 22z  - 22x - 23y + 32z - 44, y  + 2y*z - 38z  + 13x + 14y - 47z - 4, x*y + 36y*z + 31z  + 18x - 31y - 13z + 11, x  - 24y*z + 32z  + 39x - 2y - 8z - 30)

                        2                          2              2                                       2                          2             2
ideal (x*z - 44y*z - 30z  + 31x + 37y + 32z - 39, y  - 34y*z + 27z  + 13x + 14y - 9z - 4, x*y - 6y*z - 30z  + 18x - 31y + 19z + 11, x  + 4y*z - 44z  + 39x - 2y + 35z - 30)

                        2                          2              2                                        2                          2              2
ideal (x*z - 44y*z + 31z  - 30x - 13y + 32z + 41, y  - 12y*z + 46z  + 13x + 14y - 21z - 4, x*y - 14y*z + 5z  + 18x - 31y - 23z + 11, x  + 43y*z + 41z  + 39x - 2y + 48z - 30)

                        2                         2              2                                         2                          2              2
ideal (x*z - 44y*z + 16z  + 5x + 19y + 32z + 10, y  - 29y*z + 40z  + 13x + 14y + 25z - 4, x*y - 17y*z - 22z  + 18x - 31y + 37z + 11, x  + 45y*z - 39z  + 39x - 2y + 15z - 30)

                       2                          2              2                                       2                          2              2
ideal (x*z - 44y*z + 5z  + 16x - 20y + 32z + 32, y  - 28y*z + 26z  + 13x + 14y - 49z - 4, x*y + y*z + 16z  + 18x - 31y - 20z + 11, x  + 33y*z + 10z  + 39x - 2y + 11z - 30)

        3      2              2                    2       2       2              2                  3      2              2                  5      2             2
ideal (y  + 28x  - 27x*y + 46y  - 27x + y - 28, x*y  - 1, x y - 28x  + 29x*y - 28y  + 45x + y + 45, x  - 46x  + 28x*y - 27y  + 46x + y + 27, z  + 46x  - 46x*y + 8y  - 48x - 19y - 29)

i32 : ooo / degree

o32 = {1, 1, 1, 1, 1, 6, 6, 6, 6, 6, 30}

o32 : List
```

---

## varieties / test.m2 — chunk 4

### Input

```macaulay2
S = QQ[z,y,x, MonomialOrder => Eliminate 2]
ourpoints'' = substitute(ourpoints,S)
G = gens gb ourpoints''
ideal selectInSubring(1,G)
M = staircase^3
numgens M
transpose gens M
degree M
```

### Output

```
i33 : S = QQ[z,y,x, MonomialOrder => Eliminate 2]

o33 = S

o33 : PolynomialRing

i34 : ourpoints'' = substitute(ourpoints,S)

2        5    4     3    5   5    5    5
o34 = ideal (y x - 1, y  - x , - y  + x , z  + y  + x  - 1)

o34 : Ideal of S

i35 : G = gens gb ourpoints''

o35 = | x13-1 y-x6 z5+x5+x4-1 |

              1      3
o35 : Matrix S  <-- S

i36 : ideal selectInSubring(1,G)

13
o36 = ideal(x   - 1)

o36 : Ideal of S

i37 : M = staircase^3

3 6   2 4 5   2 9   7 4     2 10     7 5   6 2 5     12   6 7   11 2   15   5 10   5 10   10 5   5 5 5   10 5   15   5 10   10 5   15
o37 = ideal (x y , x y z , x y , x y , x*y z  , x*y z , x y z , x*y  , x y , x  y , z  , y z  , x z  , y  z , x y z , x  z , y  , x y  , x  y , x  )

o37 : Ideal of R

i38 : numgens M

o38 = 20

i39 : transpose gens M

o39 = {-9}  | x3y6   |
      {-11} | x2y4z5 |
      {-11} | x2y9   |
      {-11} | x7y4   |
      {-13} | xy2z10 |
      {-13} | xy7z5  |
      {-13} | x6y2z5 |
      {-13} | xy12   |
      {-13} | x6y7   |
      {-13} | x11y2  |
      {-15} | z15    |
      {-15} | y5z10  |
      {-15} | x5z10  |
      {-15} | y10z5  |
      {-15} | x5y5z5 |
      {-15} | x10z5  |
      {-15} | y15    |
      {-15} | x5y10  |
      {-15} | x10y5  |
      {-15} | x15    |

              20      1
o39 : Matrix R   <-- R

i40 : degree M

o40 = 690
```

---

## varieties / test.m2 — chunk 5

### Input

```macaulay2
S = R/M
basis S
tally apply(flatten entries basis(S),degree)
basis(19,S)
(x+y+z)^19
C = res M
C.dd_1
flatten entries gens M - set flatten entries C.dd_1
```

### Output

```
i41 : S = R/M

o41 = S

o41 : QuotientRing

i42 : basis S

o42 = | 1 x x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x14y x14yz x14yz2 x14yz3 x14yz4 x14z x14z2 x14z3 x14z4 x13y x13yz x13yz2 x13yz3 x13yz4 x13z x13z2 x13z3 x13z4 x12y x12yz x12yz2 x12yz3 x12yz4 x12z x12z2 x12z3 x12z4 x11y x11yz x11yz2 x11yz3 x11yz4 x11z x11z2 x11z3 x11z4 x10y x10y2 x10y3 x10y3z x10y3z2 x10y3z3 x10y3z4 x10y2z x10y2z2 x10y2z3 x10y2z4 x10yz x10yz2 x10yz3 x10yz4 x10z x10z2 x10z3 x10z4 x9y x9y2 x9y3 x9y3z x9y3z2 x9y3z3 x9y3z4 x9y2z x9y2z2 x9y2z3 x9y2z4 x9yz x9yz2 x9yz3 x9yz4 x9yz5 x9yz6 x9yz7 x9yz8 x9yz9 x9z x9z2 x9z3 x9z4 x9z5 x9z6 x9z7 x9z8 x9z9 x8y x8y2 x8y3 x8y3z x8y3z2 x8y3z3 x8y3z4 x8y2z x8y2z2 x8y2z3 x8y2z4 x8yz x8yz2 x8yz3 x8yz4 x8yz5 x8yz6 x8yz7 x8yz8 x8yz9 x8z x8z2 x8z3 x8z4 x8z5 x8z6 x8z7 x8z8 x8z9 x7y x7y2 x7y3 x7y3z x7y3z2 x7y3z3 x7y3z4 x7y2z x7y2z2 x7y2z3 x7y2z4 x7yz x7yz2 x7yz3 x7yz4 x7yz5 x7yz6 x7yz7 x7yz8 x7yz9 x7z x7z2 x7z3 x7z4 x7z5 x7z6 x7z7 x7z8 x7z9 x6y x6y2 x6y3 x6y4 x6y5 x6y5z x6y5z2 x6y5z3 x6y5z4 x6y4z x6y4z2 x6y4z3 x6y4z4 x6y3z x6y3z2 x6y3z3 x6y3z4 x6y2z x6y2z2 x6y2z3 x6y2z4 x6yz x6yz2 x6yz3 x6yz4 x6yz5 x6yz6 x6yz7 x6yz8 x6yz9 x6z x6z2 x6z3 x6z4 x6z5 x6z6 x6z7 x6z8 x6z9 x5y x5y2 x5y3 x5y4 x5y5 x5y5z x5y5z2 x5y5z3 x5y5z4 x5y4z x5y4z2 x5y4z3 x5y4z4 x5y3z x5y3z2 x5y3z3 x5y3z4 x5y3z5 x5y3z6 x5y3z7 x5y3z8 x5y3z9 x5y2z x5y2z2 x5y2z3 x5y2z4 x5y2z5 x5y2z6 x5y2z7 x5y2z8 x5y2z9 x5yz x5yz2 x5yz3 x5yz4 x5yz5 x5yz6 x5yz7 x5yz8 x5yz9 x5z x5z2 x5z3 x5z4 x5z5 x5z6 x5z7 x5z8 x5z9 x4y x4y2 x4y3 x4y4 x4y5 x4y5z x4y5z2 x4y5z3 x4y5z4 x4y4z x4y4z2 x4y4z3 x4y4z4 x4y3z x4y3z2 x4y3z3 x4y3z4 x4y3z5 x4y3z6 x4y3z7 x4y3z8 x4y3z9 x4y2z x4y2z2 x4y2z3 x4y2z4 x4y2z5 x4y2z6 x4y2z7 x4y2z8 x4y2z9 x4yz x4yz2 x4yz3 x4yz4 x4yz5 x4yz6 x4yz7 x4yz8 x4yz9 x4yz10 x4yz11 x4yz12 x4yz13 x4yz14 x4z x4z2 x4z3 x4z4 x4z5 x4z6 x4z7 x4z8 x4z9 x4z10 x4z11 x4z12 x4z13 x4z14 x3y x3y2 x3y3 x3y4 x3y5 x3y5z x3y5z2 x3y5z3 x3y5z4 x3y4z x3y4z2 x3y4z3 x3y4z4 x3y3z x3y3z2 x3y3z3 x3y3z4 x3y3z5 x3y3z6 x3y3z7 x3y3z8 x3y3z9 x3y2z x3y2z2 x3y2z3 x3y2z4 x3y2z5 x3y2z6 x3y2z7 x3y2z8 x3y2z9 x3yz x3yz2 x3yz3 x3yz4 x3yz5 x3yz6 x3yz7 x3yz8 x3yz9 x3yz10 x3yz11 x3yz12 x3yz13 x3yz14 x3z x3z2 x3z3 x3z4 x3z5 x3z6 x3z7 x3z8 x3z9 x3z10 x3z11 x3z12 x3z13 x3z14 x2y x2y2 x2y3 x2y4 x2y5 x2y6 x2y7 x2y8 x2y8z x2y8z2 x2y8z3 x2y8z4 x2y7z x2y7z2 x2y7z3 x2y7z4 x2y6z x2y6z2 x2y6z3 x2y6z4 x2y5z x2y5z2 x2y5z3 x2y5z4 x2y4z x2y4z2 x2y4z3 x2y4z4 x2y3z x2y3z2 x2y3z3 x2y3z4 x2y3z5 x2y3z6 x2y3z7 x2y3z8 x2y3z9 x2y2z x2y2z2 x2y2z3 x2y2z4 x2y2z5 x2y2z6 x2y2z7 x2y2z8 x2y2z9 x2yz x2yz2 x2yz3 x2yz4 x2yz5 x2yz6 x2yz7 x2yz8 x2yz9 x2yz10 x2yz11 x2yz12 x2yz13 x2yz14 x2z x2z2 x2z3 x2z4 x2z5 x2z6 x2z7 x2z8 x2z9 x2z10 x2z11 x2z12 x2z13 x2z14 xy xy2 xy3 xy4 xy5 xy6 xy7 xy8 xy9 xy10 xy11 xy11z xy11z2 xy11z3 xy11z4 xy10z xy10z2 xy10z3 xy10z4 xy9z xy9z2 xy9z3 xy9z4 xy8z xy8z2 xy8z3 xy8z4 xy7z xy7z2 xy7z3 xy7z4 xy6z xy6z2 xy6z3 xy6z4 xy6z5 xy6z6 xy6z7 xy6z8 xy6z9 xy5z xy5z2 xy5z3 xy5z4 xy5z5 xy5z6 xy5z7 xy5z8 xy5z9 xy4z xy4z2 xy4z3 xy4z4 xy4z5 xy4z6 xy4z7 xy4z8 xy4z9 xy3z xy3z2 xy3z3 xy3z4 xy3z5 xy3z6 xy3z7 xy3z8 xy3z9 xy2z xy2z2 xy2z3 xy2z4 xy2z5 xy2z6 xy2z7 xy2z8 xy2z9 xyz xyz2 xyz3 xyz4 xyz5 xyz6 xyz7 xyz8 xyz9 xyz10 xyz11 xyz12 xyz13 xyz14 xz xz2 xz3 xz4 xz5 xz6 xz7 xz8 xz9 xz10 xz11 xz12 xz13 xz14 y y2 y3 y4 y5 y6 y7 y8 y9 y10 y11 y12 y13 y14 y14z y14z2 y14z3 y14z4 y13z y13z2 y13z3 y13z4 y12z y12z2 y12z3 y12z4 y11z y11z2 y11z3 y11z4 y10z y10z2 y10z3 y10z4 y9z y9z2 y9z3 y9z4 y9z5 y9z6 y9z7 y9z8 y9z9 y8z y8z2 y8z3 y8z4 y8z5 y8z6 y8z7 y8z8 y8z9 y7z y7z2 y7z3 y7z4 y7z5 y7z6 y7z7 y7z8 y7z9 y6z y6z2 y6z3 y6z4 y6z5 y6z6 y6z7 y6z8 y6z9 y5z y5z2 y5z3 y5z4 y5z5 y5z6 y5z7 y5z8 y5z9 y4z y4z2 y4z3 y4z4 y4z5 y4z6 y4z7 y4z8 y4z9 y4z10 y4z11 y4z12 y4z13 y4z14 y3z y3z2 y3z3 y3z4 y3z5 y3z6 y3z7 y3z8 y3z9 y3z10 y3z11 y3z12 y3z13 y3z14 y2z y2z2 y2z3 y2z4 y2z5 y2z6 y2z7 y2z8 y2z9 y2z10 y2z11 y2z12 y2z13 y2z14 yz yz2 yz3 yz4 yz5 yz6 yz7 yz8 yz9 yz10 yz11 yz12 yz13 yz14 z z2 z3 z4 z5 z6 z7 z8 z9 z10 z11 z12 z13 z14 |

              1      690
o42 : Matrix S  <-- S

i43 : tally apply(flatten entries basis(S),degree)

o43 = Tally{{0} => 1  }
            {1} => 3
            {2} => 6
            {3} => 10
            {4} => 15
            {5} => 21
            {6} => 28
            {7} => 36
            {8} => 45
            {9} => 54
            {10} => 63
            {11} => 69
            {12} => 73
            {13} => 71
            {14} => 66
            {15} => 53
            {16} => 38
            {17} => 23
            {18} => 12
            {19} => 3

o43 : Tally

i44 : basis(19,S)

o44 = | x14yz4 x9yz9 x4yz14 |

              1      3
o44 : Matrix S  <-- S

i45 : (x+y+z)^19

14   4          9   9         4   14
o45 = 58140x  y*z  + 923780x y*z  + 58140x y*z

o45 : S

i46 : C = res M

1      16      27      12
o46 = R  <-- R   <-- R   <-- R   <-- 0
                                      
      0      1       2       3       4

o46 : ChainComplex

i47 : C.dd_1

o47 = | x3y6 x7y4 x2y9 x2y4z5 x11y2 xy12 x6y2z5 xy7z5 xy2z10 x15 y15 x10z5 y10z5 x5z10 y5z10 z15 |

              1      16
o47 : Matrix R  <-- R

i48 : flatten entries gens M - set flatten entries C.dd_1

6 7   5 5 5   5 10   10 5
o48 = {x y , x y z , x y  , x  y }

o48 : List
```

---

## varieties / test.m2 — chunk 6

### Input

```macaulay2
C.dd_2
C.dd_3
A = {{1, 1, 1, 1},
           {1, 5,10,25}}
R = QQ[p,n,d,q, Degrees => transpose A]
degree d
degree q
degree(p^4*n^8*d^10*q^3)
h = basis({25,219}, R)
```

### Output

```
i49 : C.dd_2

o49 = {9}  | -y3 -x4 0   -z5 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   |
      {11} | 0   y2  0   0   0   -x4 0   0   -z5 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   |
      {11} | x   0   -y3 0   0   0   0   0   0   -z5 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   |
      {11} | 0   0   0   xy2 -y3 0   -x4 0   x5  y5  0   -z5 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   |
      {13} | 0   0   0   0   0   y2  0   0   0   0   0   0   0   -x4 0   0   -z5 0   0   0   0   0   0   0   0   0   0   |
      {13} | 0   0   x   0   0   0   0   -y3 0   0   0   0   0   0   0   0   0   -z5 0   0   0   0   0   0   0   0   0   |
      {13} | 0   0   0   0   0   0   y2  0   0   0   0   0   0   0   -x4 0   x5  0   -z5 0   0   0   0   0   0   0   0   |
      {13} | 0   0   0   0   x   0   0   0   0   0   -y3 0   0   0   0   0   0   y5  0   -z5 0   0   0   0   0   0   0   |
      {13} | 0   0   0   0   0   0   0   0   0   0   0   xy2 -y3 0   0   -x4 0   0   x5  y5  -z5 0   0   0   0   0   0   |
      {15} | 0   0   0   0   0   0   0   0   0   0   0   0   0   y2  0   0   0   0   0   0   0   -z5 0   0   0   0   0   |
      {15} | 0   0   0   0   0   0   0   x   0   0   0   0   0   0   0   0   0   0   0   0   0   0   -z5 0   0   0   0   |
      {15} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   y2  0   0   0   0   0   0   x5  0   -z5 0   0   0   |
      {15} | 0   0   0   0   0   0   0   0   0   0   x   0   0   0   0   0   0   0   0   0   0   0   y5  0   -z5 0   0   |
      {15} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   y2  0   0   0   0   0   0   0   x5  0   -z5 0   |
      {15} | 0   0   0   0   0   0   0   0   0   0   0   0   x   0   0   0   0   0   0   0   0   0   0   0   y5  0   -z5 |
      {15} | 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   xy2 0   0   0   0   x5  y5  |

              16      27
o49 : Matrix R   <-- R

i50 : C.dd_3

o50 = {12} | z5  0   0   0   0   0   0   0   0   0   0   0   |
      {13} | 0   z5  0   0   0   0   0   0   0   0   0   0   |
      {14} | 0   0   z5  0   0   0   0   0   0   0   0   0   |
      {14} | -y3 -x4 0   0   0   0   0   0   0   0   0   0   |
      {14} | 0   0   -y5 z5  0   0   0   0   0   0   0   0   |
      {15} | 0   0   0   0   z5  0   0   0   0   0   0   0   |
      {15} | 0   0   0   0   -x5 z5  0   0   0   0   0   0   |
      {16} | 0   0   0   0   0   0   z5  0   0   0   0   0   |
      {16} | 0   y2  0   0   -x4 0   0   0   0   0   0   0   |
      {16} | x   0   -y3 0   0   0   0   0   0   0   0   0   |
      {16} | 0   0   0   0   0   0   -y5 z5  0   0   0   0   |
      {16} | 0   0   0   -y3 0   -x4 0   0   0   0   0   0   |
      {16} | 0   0   0   0   0   0   0   -y5 z5  0   0   0   |
      {17} | 0   0   0   0   0   0   0   0   0   z5  0   0   |
      {17} | 0   0   0   0   0   0   0   0   0   -x5 z5  0   |
      {17} | 0   0   0   0   0   0   0   0   0   0   -x5 z5  |
      {18} | 0   0   0   0   y2  0   0   0   0   -x4 0   0   |
      {18} | 0   0   x   0   0   0   -y3 0   0   0   0   0   |
      {18} | 0   0   0   0   0   y2  0   0   0   0   -x4 0   |
      {18} | 0   0   0   x   0   0   0   -y3 0   0   0   0   |
      {18} | 0   0   0   0   0   0   0   0   -y3 0   0   -x4 |
      {20} | 0   0   0   0   0   0   0   0   0   y2  0   0   |
      {20} | 0   0   0   0   0   0   x   0   0   0   0   0   |
      {20} | 0   0   0   0   0   0   0   0   0   0   y2  0   |
      {20} | 0   0   0   0   0   0   0   x   0   0   0   0   |
      {20} | 0   0   0   0   0   0   0   0   0   0   0   y2  |
      {20} | 0   0   0   0   0   0   0   0   x   0   0   0   |

              27      12
o50 : Matrix R   <-- R

i51 : A = {{1, 1, 1, 1},
           {1, 5,10,25}}

o51 = {{1, 1, 1, 1}, {1, 5, 10, 25}}

o51 : List

i52 : R = QQ[p,n,d,q, Degrees => transpose A]

o52 = R

o52 : PolynomialRing

i53 : degree d

o53 = {1, 10}

o53 : List

i54 : degree q

o54 = {1, 25}

o54 : List

i55 : degree(p^4*n^8*d^10*q^3)

o55 = {25, 219}

o55 : List

i56 : h = basis({25,219}, R)

o56 = | p14n2d2q7 p9n8d2q6 p9n5d6q5 p9n2d10q4 p4n14d2q5 p4n11d6q4 p4n8d10q3 p4n5d14q2 p4n2d18q |

              1      9
o56 : Matrix R  <-- R
```

---

## varieties / test.m2 — chunk 7

### Input

```macaulay2
rank source h
rank source basis({100,1000}, R)
S = QQ[x, y, d, p, n, q, 
          MonomialOrder => Lex, MonomialSize => 16]
I = ideal( p - x*y, n - x*y^5, d - x*y^10, q - x*y^25)
transpose gens gb I
S' = S/I
x^10 * y^100
x^100 * y^1000
```

### Output

```
i57 : rank source h

o57 = 9

i58 : rank source basis({100,1000}, R)

o58 = 182

i59 : S = QQ[x, y, d, p, n, q, 
          MonomialOrder => Lex, MonomialSize => 16]

o59 = S

o59 : PolynomialRing

i60 : I = ideal( p - x*y, n - x*y^5, d - x*y^10, q - x*y^25)

5           10           25
o60 = ideal (- x*y + p, - x*y  + n, - x*y   + d, - x*y   + q)

o60 : Ideal of S

i61 : transpose gens gb I

o61 = {-6}  | p5q-n6     |
      {-4}  | d4-n3q     |
      {-3}  | yn2-dp     |
      {-6}  | yp4q-dn4   |
      {-4}  | yd3-pnq    |
      {-6}  | y2p3q-d2n2 |
      {-5}  | y2d2n-p2q  |
      {-7}  | y2d2p3-n5  |
      {-6}  | y3p2q-d3   |
      {-6}  | y3dp2-n3   |
      {-5}  | y4p-n      |
      {-6}  | y5n-d      |
      {-8}  | y6d2-pq    |
      {-16} | y15d-q     |
      {-7}  | xq-y5d2    |
      {-5}  | xn-y3p2    |
      {-2}  | xd-n2      |
      {-2}  | xy-p       |

              18      1
o61 : Matrix S   <-- S

i62 : S' = S/I

o62 = S'

o62 : QuotientRing

i63 : x^10 * y^100

2 6 2
o63 = d n q

o63 : S'

i64 : x^100 * y^1000

75 25
o64 = n  q

o64 : S'
```

---

## varieties / test.m2 — chunk 8

### Input

```macaulay2
x^39 * y^1000
weight = (5,7,13,17)
T = QQ[x, y, p, n, d, q, 
                Weights => {{1,1,0,0,0,0},{0,0,weight}},
                MonomialSize => 16]/
            (p - x*y, n - x*y^5, d - x*y^10, q - x*y^25);
x^10 * y^100
x^100 * y^1000
x^234 * y^5677
i71 :
```

### Output

```
i65 : x^39 * y^1000

25 39
o65 = y  q

o65 : S'

i66 : weight = (5,7,13,17)

o66 = (5, 7, 13, 17)

o66 : Sequence

i67 : T = QQ[x, y, p, n, d, q, 
                Weights => {{1,1,0,0,0,0},{0,0,weight}},
                MonomialSize => 16]/
            (p - x*y, n - x*y^5, d - x*y^10, q - x*y^25);

i68 : x^10 * y^100

5 2 3
o68 = p d q

o68 : T

i69 : x^100 * y^1000

60 3 37
o69 = p  n q

o69 : T

i70 : x^234 * y^5677

2 4 3 225
o70 = p n d q

o70 : T

i71 :
```

---

