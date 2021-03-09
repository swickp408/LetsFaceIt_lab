#Juan Zavala/ Patrick Swick/ Anthony Toma/ Daeeun Yim
#LETS FACE IT
#CSE 5408
#SPRING 2021
#LAB 4


# Function to convert the date format
def convertTime(str1):

    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    
    else:

        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]


userinput = input("Enter time here in 00:00:00 PM or AM format: ")

print(convertTime(userinput))


def Validation():

    alphabets = 0
    digit = 0
    special = 0

    password = input("Enter your Password: ")
    
    if len(pw) < 7:
        print('Pw must be longer than 7')

    for i in range(len(pw)):
        if(pw[i].isalpha()):
            alphabets = alphabets + 1
        elif(pw[i].isdigit()):
            digit = digit + 1
        else:
            special = special + 1
    
    if (digit + special == 2):
        print('Password Valid')
        return True
    else:
        print('Password not Valid')
        return False

def reverse_string(x):
    return x[::-1]

    y = input("Input a string \n")
    z = reverse_string(y)
    print(z)

'''
Team Lets Face It
Patrick Swick, Dae Eun Yim, Juan Zavala, Anthony Toma
CSE 5408 Spring 2021 Lab 04
'''

def prime_number():
    prime = int(input("Enter a number \n"))
    comp = False
    comp_list = []
    
    for i in range(2, abs(prime)):
        if (prime % i == 0):
            comp = True
            comp_list.append(i)
        
            
    if (comp == True):
        print(prime, "is not prime, it is divisible by")
        for it, x in enumerate(comp_list):
            if (it < len(comp_list)-1):    
                print(x , ", ", sep = '', end='')
            else:
                print("and ", x, sep = '')
        return False
    else:
        print(prime, "is prime")
        return True
    
    
def fibonacci():
    fib = int(input("Enter a number \n"))
    count = [0]
    fib_c = 0
    
    for i in range(0, fib):
        if i == 0:
            count.append(1)
        else:
            fib_c = count[i-1]+count[i]
            count.append(fib_c)
            
    return count