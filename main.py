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
