#core logic
'''
n=4
print(1)
for i in range(1,n):
	print(11**i)
'''
#implementation
m=int(input())
n=m-1
i=1
print((n)*" ",1)
for j in range(n,0,-1):
	print(j*" ",end="")
	s=str(11**i)
	ns=""
	for k in s:
		ns=ns+k+" "
	print(ns)
	i+=1