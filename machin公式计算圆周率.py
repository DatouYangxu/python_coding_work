n=int(input())
i=1
A,B=0,0
while i<=n:
    A=A+(-1)**(i-1)/((2*i-1)*5**(2*i-1))
    B=B+(-1)**(i-1)/((2*i-1)*239**(2*i-1))
    i+=1
A=eval('A')
B=eval('B')
pi=16*A-4*B
print('%.14f'%(pi))