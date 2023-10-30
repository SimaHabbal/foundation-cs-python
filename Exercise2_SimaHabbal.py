a=int(input("Enter Three integers a, b and c:"))
b=int(input())
c=int(input())
max = a
min = a
if b > max:
    max = b
if b < min:
    min = b
if c > max:
    max = c
if c < min:
    min = c
print("The maximum value is "+str(max))
print("The minimum value is "+str(min))
