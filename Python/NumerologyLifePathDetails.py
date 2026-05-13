#Name: Remi Simard #Code Name: Numerology Inheritance & Properties
#Reflection:
#What did you like about this assignment?
#I liked learning how to extend an existing class using inheritance and then making the code cleaner with properties.
#What did you struggle with?
#I struggled with pretty much all the property work because before this unit Ive never used them before. I'm just content that I got it to work.
#Explain how decorators work:
#Decorators let you change how a method behaves and the @property decorator allows you to call a method like an attribute. This makes the code cleaner because it hides the method call behind the properties
#Top 2 things you learned:
#1. How to use inheritance to add functionality to a class.
#2. How to use @property to replace getter methods.

#Imports
from Numerology import Numerology

#Life Path Details Class
class NumerologyLifePathDetails(Numerology):

    def __init__(self, name, birthdate):
        super().__init__(name, birthdate)

    #Replace Getters with properties
    @property
    def Name(self):
        return super().getName()

    @property
    def Birthdate(self):
        return super().getBirthdate()

    @property
    def LifePath(self):
        return super().getLifePath()

    @property
    def BirthDay(self):
        return super().getBirthDay()

    @property
    def Attitude(self):
        return super().getAttitude()

    @property
    def Soul(self):
        return super().getSoul()

    @property
    def Personality(self):
        return super().getPersonality()

    @property
    def PowerName(self):
        return super().getPowerName()

    #Life Path Descriptions Function
    def getLifePathDescription(self):
        descriptions = {
            1: "The Independent: Wants to work and think independently",
            2: "The Mediator: Avoids conflict and seeks harmony",
            3: "The Performer: Enjoys art, music, and attention",
            4: "The Teacher/Truth Seeker: Meant to teach and values truth",
            5: "The Adventurer: Loves travel and social interaction",
            6: "The Inner Child: Nurturing and youthful at heart",
            7: "The Naturalist: Drawn to nature and spirituality",
            8: "The Executive: Focused on success, money, and power",
            9: "The Humanitarian: Helps others and learns through hardship"
        }

        life_path_number = super().getLifePath()
        return descriptions.get(life_path_number, "Unknown Life Path")

    @property
    def LifePathDescription(self):
        return self.getLifePathDescription()
