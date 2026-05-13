#Name: Remi Simard
#Assignment: Password Validator
#Reflection: What did you like about this assignment?
#            I liked putting togeather all the mini check functions because they were straightforward and I got to do some more advanced string manipulation
#
#            What did you struggle with?
#            The hard part was the check_repeated_characters function to get it to log each repeated character and then spit out to the screen because I couldn't get it to format right.
#
#            How did you write your code to be efficient and reduce redundancy?
#            If there was a process or or check that would need to be done a second or third time I wrote a function for it so that you can just call the function instead of having to write it again like in the Check functions
#
#            Share exactly 2 things you learned on this assignment.
#            1. I learned how to take a string and then trim it to be used in a check with a list.
#            2. I also learned how lists can be input into a function and then returned like a variable but with more data.


#Create the allowed special characters variable for the special character check
sSpecialCharsRJS = "!@#$%^"

#Get the user's first and last name and output the stripped name
def get_full_name():
    while True:
        sNameRJS = input("Enter your full name (first and last): ").strip()
        if len(sNameRJS.split()) >= 2:
            return sNameRJS
        else:
            print("Error: Please enter at least a first and last name.")

#Get the initials from the name
def extract_initials(sNameRJS):
    lNamePartsRJS = sNameRJS.strip().split()
    sInitialsRJS = ''.join([part[0].upper() for part in lNamePartsRJS])
    return sInitialsRJS

#Ask user for password and get new as a string
def get_password():
    sPasswordRJS = input("Enter your password: ")
    return sPasswordRJS

#Check if there is an uppercase letter
def has_uppercase(sRJS):
    for c in sRJS:
        if c.isupper():
            return True
    return False

#Check if there is a lowercase letter
def has_lowercase(sRJS):
    for c in sRJS:
        if c.islower():
            return True
    return False

#Check to see if there is a digit
def has_digit(sRJS):
    for c in sRJS:
        if c.isdigit():
            return True
    return False

#Check for a special character
def has_special_char(sRJS):
    for c in sRJS:
        if c in sSpecialCharsRJS:
            return True
    return False

#Check to see if the string starts with pass
def starts_with_prohibited_prefix(sRJS):
    return sRJS.startswith('Pass') or sRJS.startswith('pass')

#Check if the password has the user's initials
def contains_initials(sRJS, sInitialsRJS):
    return sInitialsRJS.lower() in sRJS.lower()

#Check that no character appears more than one time
def check_repeated_characters(sPasswordRJS):
    dCharCountRJS = {}
    sLowerPasswordRJS = sPasswordRJS.lower()

    #Count each character (case-insensitive)
    for sCharRJS in sLowerPasswordRJS:
        if sCharRJS in dCharCountRJS:
            dCharCountRJS[sCharRJS] += 1
        else:
            dCharCountRJS[sCharRJS] = 1

    #Track repeated characters
    lRepeatedRJS = []

    for sCharRJS in dCharCountRJS:
        if dCharCountRJS[sCharRJS] > 1:
            lRepeatedRJS.append((sCharRJS, dCharCountRJS[sCharRJS]))

    #If repeats found, print required message and details
    if lRepeatedRJS:
        print("These characters appear more than once:")
        for tItemRJS in lRepeatedRJS:
            print(f"{tItemRJS[0]} appears {tItemRJS[1]} times")
        return False

    return True

#Run all the other Check Functions in one and add error messages
def validate_password(sPasswordRJS, sInitialsRJS):
    lErrorsRJS = []

    iLenRJS = len(sPasswordRJS)
    if iLenRJS < 8 or iLenRJS > 12:
        lErrorsRJS.append("Password must be between 8 and 12 characters long.")

    if starts_with_prohibited_prefix(sPasswordRJS):
        lErrorsRJS.append("Password can't start with Pass.")

    if not has_uppercase(sPasswordRJS):
        lErrorsRJS.append("Password must contain at least one uppercase letter.")

    if not has_lowercase(sPasswordRJS):
        lErrorsRJS.append("Password must contain at least one lowercase letter.")

    if not has_digit(sPasswordRJS):
        lErrorsRJS.append("Password must contain at least one digit.")

    if not has_special_char(sPasswordRJS):
        lErrorsRJS.append("Password must contain at least one special character from !@#$%^.")

    if contains_initials(sPasswordRJS, sInitialsRJS):
        lErrorsRJS.append("Password must not contain user initials.")

    if not check_repeated_characters(sPasswordRJS):
        lErrorsRJS.append("Password contains repeated characters.")

    return lErrorsRJS

#Main
def main():
    #Prompt for full name and extract initials
    sNameRJS = get_full_name()
    sInitialsRJS = extract_initials(sNameRJS)

    while True:
        #Prompt for password
        sPasswordRJS = get_password()

        #Validate password
        lErrorsRJS = validate_password(sPasswordRJS, sInitialsRJS)

        if not lErrorsRJS:
            print("Password is valid and OK to use.")
            break
        else:
            for sErrorRJS in lErrorsRJS:
                print(f"Error: {sErrorRJS}")

#Program Start
main()
