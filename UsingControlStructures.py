#Part II: Computer Exercises:

theInput = raw_input("Enter an integer: ")

a=int(theInput)
if a%2==0:
    print "Even"
else:
    print "Odd"

print "---------------------"

#Qusetion 6
primaySchoolAge=4
votingage=18
presidentAge=40
retirement=60
personsAge= input ("Enter your Age:")
age=int(personsAge)
if age<primaySchoolAge:
    print "Too Young"
elif age>17:
    if age==votingage or age<presidentAge:
     print "Remember to vote"
elif age>presidentAge:
    if age<presidentAge:
        print "Vote for me"
    if age<presidentAge:
        print "You can't be president"
elif age>retirement:

    print "Too old"



#Question 7
print "---------------------"
i=39
while i<40:
    print i
    if i==0:
     break
    i-=3
    
print "---------------------"

#Question 8


for i in range(6,30,1):
    if i%2!=0:
        if i%3!=0:
            if i%5!=0:
                print i
               


#Question 9
print "---------------------"
n=1

while n>0:
    n+=1
    if (79*n)%97==1:
        print "The Correct Answer is:", n
        break








