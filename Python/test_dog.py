import unittest
from dog import Dog

class TestDogMethods(unittest.TestCase):
    def test_init(self):
        name = "Doris"
        age = 15
        breed = "Poodle"
        instance_dog = Dog(name, age, breed)

        self.assertEqual(instance_dog.name, name)
        self.assertEqual(instance_dog.age, age)
        self.assertEqual(instance_dog.breed, breed)
        self.assertEqual(instance_dog.sound, "woof woof")

    def test_bark(self):
        instance_dog = Dog("Doris", 15, "Poodle")
        name, sound = instance_dog.bark()
        self.assertEqual(name, "Doris")
        self.assertEqual(sound, "woof woof")

    def test_age_in_dog(self):
        instance_dog = Dog("Doris", 15, "Poodle")
        self.assertEqual(instance_dog.age_in_dog(), 105)


if __name__ == '__main__':
    unittest.main()


"""
    def test_calculate_product_math(self):
        list_of_int = [2, 2]
        product = calculate_product_math(list_of_int)

        self.assertEqual(product == 4)
"""