start = int(input("Enter lower range: "))
end = int(input("Enter upper range: "))
 
for num in range(start + 1,end):
   
   sum = 0
 
   
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
       print(num) 
