from_num = int(input("Enter the Min Number : "))
to_num = int(input("Enter the Max Number : "))
print("Prime numbers between", from_num, "and", to_num, "are:")
for num in range(from_num,to_num + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
