restart
R = QQ[d,t,l,u,v,j]

d = 9
t = 4
l = 5
u = 1
v = 1
j = 2

q1 = d*(2*t-2-j)+(t-1)*(u+v)+j*(l-u-v)-(t-1-j)^2 
q2 = (t-1)*(d+l)+l 
-- want q2 > q1





d = 11
t = 6
l = 9
u = 2
v = 2
j = 3

q1 = d*(2*t-2-j)+(t-1)*(u+v)+j*(l-u-v)-(t-1-j)^2 
q2 = (t-1)*(d+l)+l 

bound = (l*(t-j)/(t-1-j)) - (u+v-t+1+j)



-- d < bound <=> q2 > q1
