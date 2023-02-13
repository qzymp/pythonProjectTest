class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

my_dog.sit()
my_dog.roll_over()

print("My Dog's name is " + my_dog.name.title() + ".")
print("My Dog is " + str(my_dog.age) + " years old")

