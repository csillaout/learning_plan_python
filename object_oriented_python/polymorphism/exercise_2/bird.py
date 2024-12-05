from turtle import pen


class Bird:
    def fly(self):
        return "I can fly."

class Penguin(Bird):
    def fly(self):
        return "I cannot fly."

#create object
sparrow = Bird()
penguin = Penguin()

#use isinstance
print(isinstance(sparrow, Bird))
print(isinstance(penguin, Bird))
print(isinstance(penguin, Penguin))
print(sparrow.fly())
print(penguin.fly())
