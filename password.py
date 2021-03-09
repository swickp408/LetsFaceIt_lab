

def Validation(pw):

    alphabets = 0
    digit = 0
    special = 0

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





password = input("Enter your Password: ")

Validation(password)