n1=int(input())
n2=int(input())
l=[]
x=n1 if n1>n2 else n2
i=x
while(1):
	if i%n1==0 and i%n2==0:
		lcm=i
		break
	i+=x
print(lcm)