def fib(n):
	a=0
	b=1
	print(a)
	print(b)
	for i in range(n-2):
		c=a+b
		a=b
		b=c
		print(c)
n=int(input("Enter no. "))
fib(n)