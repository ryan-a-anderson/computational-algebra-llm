R=QQ[p,s,a0,a1,b0,b1]
I=ideal(((1-p)*a0+p*a1)*((1-s)*b0+s*b1),((1-p)*a0^2+p*a1^2)*((1-s)*b0^2+s*b1^2),((1-p)*a0^3+p*a1^3)*((1-s)*b0^3+s*b1^3),((1-p)*a0^4+p*a1^4)*((1-s)*b0^4+s*b1^4))
gens gb I
for i from 0 to 50 do
m_i=((1-p)*a0^i+p*a1^i)*((1-s)*b0^i+s*b1^i)
m_5%I
m_9%I
m_5//gens I
m_9//gens I

--are 3 moments sufficient?
I=ideal(((1-p)*a0+p*a1)*((1-s)*b0+s*b1),((1-p)*a0^2+p*a1^2)*((1-s)*b0^2+s*b1^2),((1-p)*a0^3+p*a1^3)*((1-s)*b0^3+s*b1^3))
m_4%I



--assume uniform distribution
R=QQ[a0,a1,b0,b1]
I=ideal((a0+a1)*(b0+b1),(a0^2+a1^2)*(b0^2+b1^2),(a0^3+a1^3)*(b0^3+b1^3),(a0^4+a1^4)*(b0^4+b1^4))
gens gb I
for i from 0 to 50 do
m_i=(a0^i+a1^i)*(b0^i+b1^i)
m_5//gens I
