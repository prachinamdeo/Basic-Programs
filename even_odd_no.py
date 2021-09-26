def evenodd(n):
	if n % 2 == 0:
		return "even no."
	else:
		return "odd no."
n=int(input("Enter no. "))
res = evenodd(n)
print(res)