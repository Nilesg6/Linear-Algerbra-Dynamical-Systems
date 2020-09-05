i = sqrt(-1)
xinit = [0 ; 1]
A = [3 -5; 1 -1]

p = 1 #lambda1 = 1+i
q = 1 #lambda2 = 1-i

r = (p**2 + q**2)**.5
tht = arg(p+q*i)

s = [0 -5; 1 -2]
m = [cos(tht) -sin(tht); sin(tht) cos(tht)]

sInverse = inv(s)
sInverse*A*s
sInverse*xinit

#just for intializing
h = xinit;
hcircle = xinit;
hellipse = xinit;

x = [];
y = [];
xcircle = [];
ycircle = [];
xellipse = [];
yellipse = [];


for t = 0:.05:8
  m = [cos(tht*t) -sin(tht*t); sin(tht*t) cos(tht*t)];

  l = (r**t)*s*(m)*sInverse*xinit;
  lcircle = (m)*sInverse*xinit;
  lellipse = s*(m)*sInverse*xinit;
 
  h = [h l];
  hcircle = [hcircle lcircle];
  hellipse = [hellipse lellipse];

  x = [x l(1,1)];
  y = [y l(2,1)];  
  xcircle = [xcircle lcircle(1,1)];
  ycircle = [ycircle lcircle(2,1)];  
  xellipse = [xellipse lellipse(1,1)];
  yellipse = [yellipse lellipse(2,1)];
endfor

plot(x,y,'b')
hold on
plot(xcircle,ycircle,'g')
hold on
plot(xellipse,yellipse,'r')
hold on




