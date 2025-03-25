num = int(input("Enter any number:"))
sum = 0
for i in range(1,num):
    if num%i == 0 :
         print(i,end=" ")
         sum = sum + i
print(sum)
if(num==sum):
    print("Number given number ", num , " is a perfect number.")
else:
    print("Number given number ", num , " is not a perfect number.")