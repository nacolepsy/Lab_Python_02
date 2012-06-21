a =  raw_input("Please Enter the numbers to be encrypted: ")
num= int(a)
print "Your Encrypted Numbers are:",
while num:
    dig=num%10
    
    print dig,
    num/=10
