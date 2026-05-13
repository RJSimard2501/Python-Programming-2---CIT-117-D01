#Name: Remi Simard
#Assignment: Numerology Classes
#Reflection: Share what you liked about this assignment?
# I liked learning how to organize logic into a class and reuse functions in that way.
#
# Share what you struggled with?
# I struggled most with properly separating vowels and consonants and reducing numbers repeatedly. Also classes were the newest thing and 
#
# Think back to a previous assignment how could rewrite it to use Python classes?
# I could rewrite almost all the previous programs by grouping the majority of the functions into a class and storing the shared data as attributes.
#
# Share exactly 2 things you learned on this assignment:
# 1. How to design and use classes with public and private methods.
# 2. How to manipulate strings and repeatedly reduce numbers using loops.

#UseNumerology.py
from Numerology import Numerology

#Validate date
def valid_date(dob):
    dob = dob.replace('/', '-')
    parts = dob.split('-')
    if len(parts) != 3:
        return False
    return all(part.isdigit() for part in parts)

#Main
def main():
    name = input("Enter your full name: ").strip()
    while name == "":
        name = input("Name cannot be empty. Enter again: ").strip()

    dob = input("Enter your birthdate (mm-dd-yyyy or mm/dd/yyyy): ")
    while not valid_date(dob):
        dob = input("Invalid format. Enter again: ")

    #Create the Numerology object after inputs are collected
    num = Numerology(name, dob)

    print("\nClient Name:", num.getName())
    print("Client DOB:", num.getBirthdate())
    print("Life Path:", num.getLifePath())
    print("Attitude:", num.getAttitude())
    print("Birthday:", num.getBirthDay())
    print("Personality:", num.getPersonality())
    print("Power Name:", num.getPowerName())
    print("Soul:", num.getSoul())

if __name__ == "__main__":
    main()

