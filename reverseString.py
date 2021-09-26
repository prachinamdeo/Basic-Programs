s="helloWorld"
rs=""
'''
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")
print()
'''
for i in range(len(s)-1,-1,-1):
    rs=rs+s[i]
print(rs)
'''
s=rs
print(s) 
print(s is rs)
'''