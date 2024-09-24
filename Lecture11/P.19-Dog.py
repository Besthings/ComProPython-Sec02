class Dog:

    species = 'manmal'

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)
    
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

mikey = Dog("Mikey", 6)

print(mikey.description())
print(mikey.speak("Gruff Gruff"))