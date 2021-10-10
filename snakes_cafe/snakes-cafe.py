"use strict"
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring

snakes_cafe_menu = [
    {
        "Appetizers": ["Cookies", "Wings", "Spring Rolls"]
    },
    {
        "Entrees": ["A Literal Garden", "Meat Tornado", "Steak", "Salmon"]
    },
    {
        "Desserts": ["Pie", "Cake", "Ice Cream"]
    },
    {
        "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
    }
]


def user_order(): 

    match_element = []

    print("""
    Welcome to the Snakes Cafe!
    Please see our menu below.

    To quit at any time, type "quit"
    """)

    for i in range(len(snakes_cafe_menu)):
        menu_type = snakes_cafe_menu[i]
        for item in menu_type:
            print("\n# *** {} *** #".format(item.upper()))
            menu_element = snakes_cafe_menu[i][item]
            for element in menu_element:
                print("- {} ".format(element))
                match_element.append(element.upper())

    user_input = ""

    while user_input != "QUIT":
        user_input = input("\n enter your order:\n> ").upper()
        if user_input in match_element:
            print("\n ------ you just order {} ------".format(user_input))
        elif user_input not in match_element and user_input != "QUIT":
            print("\n ------ please enter an exist order ------")


user_order()
