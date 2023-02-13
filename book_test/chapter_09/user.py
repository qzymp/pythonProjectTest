class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(self.first_name.title() + self.last_name + " is " + str(self.age) + " years old.")

    def greet_user(self):
        print("Hello " + self.first_name.title() + self.last_name)

zhangsan = User('zhang', 'san', 18)
zhangsan.describe_user()
zhangsan.greet_user()

lisi = User('li', 'si', 20)
lisi.describe_user()
lisi.greet_user()