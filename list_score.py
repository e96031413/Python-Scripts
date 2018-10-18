import random
num_1=0
num_2=0
for i in range(1,6):
    x=random.randint(1,100)
    y=random.randint(1,100)
    print(f'No.{i:02d}\t{x:5d}\t{y:5d}')
    num_1 = num_1+x
    num_2 = num_2+y
print(f'AVG\t{num_1/5:4.2f}\t{num_2/5:4.2f}')