x = sum(range(1, 151))
print(x)

y = sum(i for i in range(1, 151) if i%7 ==0)
print(y)

z = sum( a for a in range(1, 151) if a%3==0 and a%4==0)
print(z)



