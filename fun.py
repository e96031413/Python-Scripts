import random
a=0
p=10000
for i in range(0,p):
	x=random.uniform(-1,1)
	y=random.uniform(-1,1)
	if(x**2+y**2<=1):
		a=a+1
num=a/p*4
print(f'圓內點數:{a:4d}')
print(f'圓內點數/所有點數*4:{num:6.4f}')