n = input('Enter a number to test ')
n = int(n)
a=int(5)
d = n - 1
s = 0
while (d % 2 == 0):
   s = s + 1
   d = int(d/2)
x = a**d
x = x % n
if (x==1 or x==(n-1)):
   print("probably prime")
r = int(1)
while(r<(s-1)):
   x = x**2
   x = x%n
   if (x==1):
      print ("composite")
   if (x==(n-1)):
      print ("probably prime")
print("if nothing above is printed n is composite")