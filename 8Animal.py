class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat shouts")
cat=Cat()
cat.speak()
dog=Dog()
dog.speak()