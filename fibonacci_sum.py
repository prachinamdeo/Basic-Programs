def fib(n):
	sum=0
	for i in range(n+1):
		sum=sum+i
	return sum
n=int(input("Enter no. "))
sum = fib(n)
print(sum)