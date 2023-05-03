class Car():
    """一个可以用于表示汽车的类"""
    """初始化汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
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

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()


class Battery():
    """一次模拟电动汽车的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条描述电瓶续航里程的消息"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """模拟电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()
