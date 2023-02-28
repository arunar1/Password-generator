import random

print("password generator");


lower_alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']


upper_alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']


symbols=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

digit=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



length=int(input("how many letters you need in the password  :"));

upper=int(input("Enter the no of uppercase letter :"))

lower=int(input("Enter the no of lowercase letter  :"))

special=int(input("Enter the no of special character:"))

number=int(input("Enter the no of numbers needed   :"))


#check the length of password


tot=upper+lower+special+number

passw=""

if tot==length:
    for i in range(0,upper):
        passw=passw+random.choice(upper_alphabet)
    for i in range(0,lower):
        passw=passw+random.choice(lower_alphabet)
    for i in range(0,special):
        passw=passw+random.choice(symbols)
    for i in range(0,number):
        passw=passw+random.choice(digit)
    print("\n")
    print(f"Your password : {passw}")


else:
    print("wrong length entered")





print("\nMore stronger password ")

passwd=""
countu=0
countl=0
counts=0
countd=0

if tot==length:
    while tot>=0:
        num=random.randint(1,4)
        # elif and checking the condition and checking the count
        if num==1 and countu<upper:
            countu=countu+1
            passwd=passwd+random.choice(upper_alphabet)
            tot=tot-1
           # print(passwd,num)
        elif num==2 and countl<lower:
            countl=countl+1
            tot=tot-1
            passwd=passwd+random.choice(lower_alphabet)
          #  print(passwd,num)
        elif num==3 and counts<special:
            counts=counts+1
            tot=tot-1
            passwd=passwd+random.choice(symbols)
           # print(passwd,num)
        elif num==4 and countd<number:
            countd=countd+1
            tot=tot-1
            passwd=passwd+random.choice(digit)
            #print(passwd,num)
        elif len(passwd)==length:
            print(f"\nyour password :{passwd}")
            break
        else:
            tot=tot
            
else:
    print("Entered wrong input:")



