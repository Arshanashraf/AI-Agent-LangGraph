# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# for player in players[:3]:
#     print(player.title())

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# print(friend_foods)

# buffets = ('Burger', 'Pizza', 'Sandwich', 'Salad', 'Steak')
# for buffet in buffets:
#     print(buffet)

# buffet = ('Burger', 'Pizza', 'Sandwich', 'Salad', 'Pasta')
# for buffet in buffets:
#     print(buffet)

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'subaru':
#         print(True)
#     else:
#         print(False)

# alien_color = ['red', 'yellow', 'green']
# for alien in alien_color:
#     if alien== 'green':
#         print("player just earned 5 point")

#     elif alien== 'yellow':
#         print("player just earned 10 points")
#     elif alien== 'red':
#         print("player just earned 50 points")

# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points..")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['x-poition'] = 0
# alien_0["y-position"] = 10
# print(alien_0)

# person = {'first_name': 'Ali', 'last_name': 'Khan', 'age': 23}
# print(person['first_name'].title() + " " + person['last_name'].title() + " age is " + str(person['age']))

# favorite_languages = {
#  'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# for name, language in favorite_languages.items():
#     print(name.title()+"'s favourite language is " + language.title())

# for name in favorite_languages.keys():
#     print(name.title())
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     if name in friends:
#         print("Hi! " + name.title() + " i see your favourite language is " + favorite_languages[name].title()+"!")

# aliens=[]
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed' : 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(aliens)
# print(...)

# print("total num of aliens:" + str(len(aliens)))
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = 10
#         alien['speed'] = 'fast'
#     print(aliens[0:3])

# pizza = {
#     'crust': 'thick',
#     'toppings' : ['mushroom' , 'extra cheese']
# }
# print("You ordered a " + pizza['crust'] + "-crust pizza" + " with the following toppings: ")

# for topping in pizza['toppings']:
#     print("\t" + topping)

# users = {
#     'aeinstein' : {
#         'first name': 'Albert',
#         'last name' : 'Einstein',
#         'location' : 'princeton'
#     },
#     'mcurie' : {
#         'first name' : 'marie',
#         'last name' : 'curie',
#         'location' : 'paris'
#     } 
# }
# for username, user_info in users.items():
#     print("\n Username: " + username)
#     full_name = user_info['first name'] + " " + user_info['last name']
#     location = user_info['location']

#     print("\t fullname: " + full_name.title())
#     print("\t Location: " + location.title())

# name = input("tell me your name:")
# print("Hello! " + name)

# age = input("How old are you? ")
# age = int(age)
# age>=18
# print(age)

# num = input("enter num: ")
# num = int(num)
# if num % 2 == 0: 
#     print("\t" + str(num) + " is Even")
# else:
#     print("\t" + str(num) + " is Odd")

# count = 1
# while count <=5:
#     print(count)
#     count += 1
##############################################
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# # active = True     #flag
# # while active:
# #     message = input(prompt)

# #     if message == 'quit':
# #         active = False
# #     else:
# #         print(message)

# while True:  #break
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go " + city.title()+ "!")

# count = 0
# while count < 10:
#     count +=1 
#     if count % 2 == 0:
#         continue
    
#     print(count)

# x = 1
# while x <= 5:
#     print(x)

# unconfirmed_users = ['alice', 'brian', 'harry']
# confirmed_users = []
# while unconfirmed_users:
#     current_users = unconfirmed_users.pop()
#     print("Verrifying users: " + current_users.title())
#     confirmed_users.append(current_users)
# print("The following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# responses = {}
# polling_active = True

# while polling_active:
#     name = input("enter name: ")
#     response = input("which mountain would you like to climb someday: ")
#     responses[name] = response
    
#     repeat = input("Would you like to add another person response (yes/no)? ")
#     if repeat == 'no':
#         polling_active = False

# print("/n--- POLL RESULT----")
# for name, response in responses.items():
#     print(name + " would you like to climb "+ response+ ".")

################################################

# def get_formatted_name(f_name, l_name):
#     full_name = f_name + " " + l_name
#     return full_name.title()
# musician = get_formatted_name("harry", "styles")
# print(musician)

# def get_formatted_name(f_name, l_name):
#     full_name = f_name + " " + l_name
#     return full_name.title()
# while True:
#     print("tell your name ")
#     print("(enter q to quit)")
#     f_name = input("Enter first name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Enter last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\tHello " + formatted_name + "!")
###############################
# def greet_users(names):
#     for name in names:
#         msg = "Hello! " + name.title() + "."
#         print(msg)
# usernames = ['Hannah', 'tyler', 'damon']
# greet_users(usernames)
############################################

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing Models: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'headphones']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)