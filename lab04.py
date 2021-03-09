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