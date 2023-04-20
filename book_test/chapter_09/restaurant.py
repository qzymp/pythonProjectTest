class Restaurant():
    def __init__(self, my_restaurant_name, cuisine_type):
        self.my_restaurant_name = my_restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.my_restaurant_name + " has " + self.cuisine_type)

    def open_restaurant(self):
        print("The " + self.my_restaurant_name + " is open")

my_restaurant = Restaurant('dapanji', 'chuancai')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant('a', 'b')
your_restaurant.describe_restaurant()

h = Restaurant('c', 'd')
h.describe_restaurant()

number_served = 0
