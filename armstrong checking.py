number = int(input("Enter a number: "))
sum = 0
t = number
while t > 0:
   digit = t  % 10
   sum += digit ** 3
   t //= 10
if number == sum:
   print("Yes")
else:
   print("No") 
