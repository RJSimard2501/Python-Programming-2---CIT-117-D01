#Imports
from NumerologyLifePathDetails import NumerologyLifePathDetails

#Validate date Function
def valid_date(dob):
    dob = dob.replace('/', '-')
    parts = dob.split('-')

    if len(parts) != 3:
        return False

    #Make sure all parts are digits
    if not all(part.isdigit() for part in parts):
        return False

    #Format
    if len(parts[0]) not in [1,2] or len(parts[1]) not in [1,2] or len(parts[2]) not in [2,4]:
        return False

    return True

#Main Function
def main():
    name = input("Enter your full name: ").strip()
    while name == "":
        name = input("Name cannot be empty. Enter again: ").strip()

    dob = input("Enter your birthdate (mm-dd-yy or mm/dd/yy): ").strip()
    while not valid_date(dob):
        dob = input("Invalid format. Enter again (mm-dd-yy or mm/dd/yy): ").strip()

    #Create Object
    num = NumerologyLifePathDetails(name, dob)

    print("\nClient Name:", num.Name)
    print("Client DOB:", num.Birthdate)
    print("Life Path:", num.LifePath)
    print("Life Path Description:", num.LifePathDescription)
    print("Attitude:", num.Attitude)
    print("Birthday:", num.BirthDay)
    print("Personality:", num.Personality)
    print("Power Name:", num.PowerName)
    print("Soul:", num.Soul)

#Program Start
if __name__ == "__main__":
    main()
