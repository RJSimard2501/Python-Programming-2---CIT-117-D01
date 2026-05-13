#Numerology.py
class Numerology:
    def __init__(self, sName, sDOB):
        self.__name = sName.upper()
        self.__dob = sDOB

    #Getters
    def getName(self):
        return self.__name

    def getBirthdate(self):
        return self.__dob

    #Private Helper
    def __reduceNumber(self, num):
        while num > 9:
            total = 0
            for digit in str(num):
                total += int(digit)
            num = total
        return num

    #Number to Character
    def __charToNumber(self, ch):
        mapping = {
            'A':1,'J':1,'S':1,
            'B':2,'K':2,'T':2,
            'C':3,'L':3,'U':3,
            'D':4,'M':4,'V':4,
            'E':5,'N':5,'W':5,
            'F':6,'O':6,'X':6,
            'G':7,'P':7,'Y':7,
            'H':8,'Q':8,'Z':8,
            'I':9,'R':9
        }
        return mapping.get(ch, 0)

    #Birth Date Functions
    def getLifePath(self):
        digits = [int(c) for c in self.__dob if c.isdigit()]
        return self.__reduceNumber(sum(digits))

    def getBirthDay(self):
        parts = self.__dob.replace('/', '-').split('-')
        day = parts[1]
        total = sum(int(d) for d in day if d.isdigit())
        return self.__reduceNumber(total)

    def getAttitude(self):
        parts = self.__dob.replace('/', '-').split('-')
        month = parts[0]
        day = parts[1]
        total = sum(int(d) for d in month + day if d.isdigit())
        return self.__reduceNumber(total)

    #Name Calculations
    def getSoul(self):
        vowels = "AEIOU"
        total = 0
        for ch in self.__name:
            if ch in vowels:
                total += self.__charToNumber(ch)
        return self.__reduceNumber(total)

    def getPersonality(self):
        vowels = "AEIOU"
        total = 0
        for ch in self.__name:
            if ch.isalpha() and ch not in vowels:
                total += self.__charToNumber(ch)
        return self.__reduceNumber(total)

    def getPowerName(self):
        total = self.getSoul() + self.getPersonality()
        return self.__reduceNumber(total)
