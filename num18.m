i = sqrt(-1);
xinit = [0 ; 1]
A = [-0.8 0.6; -0.8 -0.8]
[eigenvector,lamda] = eig(A)
S = [3**.5 0; 0 2]
sInverse = inv(S)
SinvAS = sInverse*A*S
SinvAS(:, 1);
r = norm(SinvAS(:, 1))
tht = arg(SinvAS(1, 1) + SinvAS(2, 1)*i)
intialPosition= sInverse*xinit

#just for intializing
h = xinit;
hcircle = xinit;
hellipse = xinit;
m = [];
x = [];
y = [];
xcircle = [];
ycircle = [];
xellipse = [];
yellipse = [];


for t = 0:.05:8
  m = [cos(tht*t) -sin(tht*t); sin(tht*t) cos(tht*t)];

  f = (r**t)*S*(m)*sInverse*xinit;
  fcircle = (m)*sInverse*xinit;
  fellipse = S*(m)*sInverse*xinit;
 
  h = [h f];
  hcircle = [hcircle fcircle];
  hellipse = [hellipse fellipse];

  x = [x f(1,1)];
  y = [y f(2,1)];  
  xcircle = [xcircle fcircle(1,1)];
  ycircle = [ycircle fcircle(2,1)];  
  xellipse = [xellipse fellipse(1,1)];
  yellipse = [yellipse fellipse(2,1)];
endfor

plot(x,y,'b')
hold on
plot(xcircle,ycircle,'g')
hold on
plot(xellipse,yellipse,'r')
hold on

if(r>=1)
  disp("Unstable")
else
  disp("Stable")
endif


