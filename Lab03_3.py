user_num=raw_input("Please Enter Number to be Encrypted: ")

new_num=0
length=len(user_num)
while new_num<length:
    length=length-1
    display=int(user_num[length])
    output=(display+7)%10
    print output ,
    

