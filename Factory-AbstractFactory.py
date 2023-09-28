# Factory & Abstract Factory design pattern

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            return None

class AbstractAnimalFactory:
    def create_animal(self):
        pass

class DogFactory(AbstractAnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AbstractAnimalFactory):
    def create_animal(self):
        return Cat()

animal_factory = AnimalFactory()
animal = animal_factory.create_animal("dog")
print(animal.speak())

dog_factory = DogFactory()
animal = dog_factory.create_animal()
print(animal.speak())

cat_factory = CatFactory()
animal = cat_factory.create_animal()
print(animal.speak())
