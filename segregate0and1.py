a=[0,1,0,0,1,0,1,1,0]
c=a.count(0)
for i in range(0,c+1):
	a[i]=0
for i in range(c+1,len(a)):
	a[i]=1
for i in a:
	print(i,end=" ")