class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.sound = "woof woof"

    def bark(self):
        print(self.name)
        print(self.sound)
        return self.name, self.sound

    """
    The first year of a dog's life is equal to 15 human years.
    The second year of a dog's life is equal to about nine human years.
    Each additional year is equal to about four or five human years.
    """

    def age_in_dog(self):
        return self.age * 7

if __name__ == '__main__':
    dog = Dog("Doris", 15, "Poodle")
    dog.bark()
    print(dog.age_in_dog())


"""
    def age_in_dog(self):
        if self.age <= 0:
            return "Invalid age. Please provide a positive number."
        elif self.age == 15:
            return 1
        elif self.age == 24:
            return 2
        else:
            return (self.age - 15) / 9 + 1

"""