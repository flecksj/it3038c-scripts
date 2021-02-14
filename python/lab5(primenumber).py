start = 1
number = int(input("Enter any number: "))
# prime number is always greater than 1

for num in range(start, number):
    prime = True 
    for i in range(2, num):
        if (num%i == 0):
            prime = False
    if prime:
         print(num, "is a prime number")




