class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        """
            将里程表读数设置成指定的值
            禁止将里程读表数往回调
        """
        if self.odometer_reading <= mileage:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")

    def increment_odometer(self, miles):
        """将里程表增加指定的量"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("不能为负")

    def read_odometer(self):
        """打印汽车里程信息"""
        print("This car has " + str(self.odometer_reading) + " mile on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

