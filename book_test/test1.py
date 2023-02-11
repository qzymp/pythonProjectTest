# banner_current_users = ['andrew', 'carolina', 'david']
# user = 'marie'
# if user not in banner_current_users:
#     print(user.title() + ", you can post a response if you wish")

# age = 17
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")

# age = -1
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# elif age >=65:
#     price = 5
# print("Your admission cost is $" + str(price) +".")


# alien_color = 'green'
# print("Player kill one alien")
# if alien_color == 'green':
#     print("player get 5 point")
# else:
#     print('player get 10 point')

# age = 101
# if age < 2:
#     print("婴儿")
# elif age < 4:
#     print("蹒跚学步")
# elif age < 13:
#     print("儿童")
# elif age < 20:
#     print("青少年")
# elif age < 65:
#     print("成年人")
# else:
#     print("老年人")

# request_toppings = []
# if request_toppings:
#     for request_topping in request_toppings:
#         print("Adding " + request_topping + ".")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")


# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requseted_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requseted_topping in requseted_toppings:
#     if requseted_topping in available_toppings:
#         print("Add " + requseted_topping + ".")
#     else:
#         print("Sorry, we don't have " + requseted_topping + ".")
# print("\nFinished making your pizza!")


# current_users = ['admin', 'Eric', 'Jack', 'Rose', 'zhangsan']
# new_users = ['admin', 'ZhangSan', 'lisi', 'wangwu', 'zhaoliu']
#
# new_current_users = []
#
# for name in current_users:
#     new_current_users.append(name.title())
#
# if new_users:
#     for user in new_users:
#         if user.title() in new_current_users:
#             print(user + "已经被使用，需要别的用户名")
#         else:
#             print(user + "用户名未被使用")
# else:
#     print("We need find some current_users!")


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for num in nums:
#     if num == 1:
#         print(str(num) + "st")
#     elif num == 2:
#         print(str(num) + "nd")
#     elif num == 3:
#         print(str(num) + "rd")
#     else:
#         print(str(num) + "th")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])


# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + ".")
# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ".")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# # 向右移动外星人  根据外星人当前速度决定将其移动多远
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_0['x_position'] += x_increment
# print("New x-position: " + str(alien_0['x_position']))

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
# print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")


# person = {
#     'first_name': '张',
#     'last_name': '三',
#     'age': 18,
#     'city': '深圳'
# }

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi'
# }
#
# print(type(user_0.keys()))
#
# for key,value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")

# for name in favorite_languages.keys():
#     print(name.title())

# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print("  Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
#
# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

# for language in set(favorite_languages.values()):
#     print(language.title())

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)

# 创建一个用于存储外星人的空列表
# aliens = []
# 创建30个绿色的外星人
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# # 显示前面5个外星人
# for alien in aliens[:5]:
#     print(alien)
# # 显示创建了多少个外星人
# print("Total numbers of aliens: " + str(len(aliens)))

# 修改前面3个外星人，修改为黄色的、速度为中等且值10个点
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
# 显示前面5个外星人
# for alien in aliens[:5]:
#     print(alien)

# 存储所点披萨的信息
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese']
# }
# 概述所点的披萨
# print("You ordered a " + pizza['crust'] + "-crust pizza with the following toppings:")
# for topping in pizza['toppings']:
#     print("\t" + topping)

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell']
# }
# for name, languages in favorite_languages.items():
#     if len(languages) > 1:
#         print("\n" + name.title() + "'s favorite languages are:")
#         for language in languages:
#             print("\t" + language.title())
#     else:
#         print("\n" + name.title() + "'s favorite language is:")
#         for language in languages:
#             print("\t" + language.title())

users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


