
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
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
    """)

    for i in range(len(snakes_cafe_menu)):
        menu_type = snakes_cafe_menu[i]
        for item in menu_type:
            print("\n {} \n  ------ ".format(item))
            menu_element = snakes_cafe_menu[i][item]
            for element in menu_element:
                print("{}".format(element))
                match_element.append(element)
    # print(str(match_element))
    user_input = ""
    user_orders = []
    while user_input != "quit":
        user_input = input('''\n ***********************************
** What would you like to order? **
***********************************
> ''').lower()
        for i in range(len(match_element)):
            comparasen = match_element[i]
            if user_input == f'{comparasen}'.lower():
                user_orders.append(match_element[i])
                counter = user_orders.count(match_element[i])
                print(
                    "\n ** {} order of {} have been added to your meal **".format(counter, match_element[i]))


if __name__ == "__main__":
    user_order()
