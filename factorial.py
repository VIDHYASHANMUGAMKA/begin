number = int(input("Enter a number: "))

factorial = 1


if number < 0:
   print("factorial does not exist for negative numbers")
elif number == 0:
   print("1")
else:
   for i in range(1,number + 1):
       factorial = factorial*i
   print(factorial) 
