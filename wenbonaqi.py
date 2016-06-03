n = input()
x = 3
a1 = 1
a2 = 1
print a1,a2,
while x <= n:
    a3 = a1 + a2
    print a3,
    a1 = a2
    a2 = a3
    x += 1
#########ex###########
m = input()
b1 = 1
b2 = 1
print b1,b2,
for w in range(3,m+1):
    b3 = b1 + b2
    print b3,
    b1 = b2
    b2 = b3
