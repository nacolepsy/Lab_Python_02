number=12345
while number:
    dig=number%10
    print dig,
    number/=10
print "-----------------"

a =  raw_input("Please Enter the numbers to be encrypted: ")
num= int(a)
while num:
    dig=num%10
    print dig,
    num/=10
