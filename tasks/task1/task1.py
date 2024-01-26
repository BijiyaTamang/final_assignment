print ("BPP Pizza Price Calculator\n==========================\n")
yess=["yes","y"]
noo=["no","n"]

def nof_pizza():
    while True:
        try:
            pizzas_ordered = input("How many pizzas ordered? ")
            ordered_pizza = int(pizzas_ordered)
            if ordered_pizza<1:
                print("Please enter a positive integer!.")
                continue
            elif ordered_pizza != float(pizzas_ordered):
                print("Please enter a valid number!")
                continue
            else:
                break
        except ValueError:
            print("Please enter a number!")
            continue
    return ordered_pizza

def delivery_too():
    while True: 
        deliv=input("Is delivery required?(yes/y)or(no/n) ")
        deliver=deliv.lower()
        if deliver in yess:
            break
        elif deliver in noo:
            break  
        else:
            print("Please answer 'y/yes' or 'n/no'.")
            continue
    return deliver

def tuesday_special():
    while True:
        askt=input("Is it Tuesday? (yes/y)or(no/n) ")
        asktues=askt.lower()
        if asktues in yess:         
            break
        elif asktues in noo:         
            break
        else:
            print("Please answer 'y/yes' or 'n/no'.") 
            continue
    return asktues

def app_special():
    while True:
        app=input("Did the customer use the app? (yes/y)or(no/n) ")
        apps=app.lower()
        if apps in yess:         
            break
        elif apps in noo:         
            break
        else:
            print("Please answer 'y/yes' or 'n/no'.") 
            continue
    return apps

def calculate(ordered_pizzas, delivery, tuesday_discount, app_discount):
    price = 12
    delivery_cost = 2.5
    pizza_sum_price= ordered_pizzas * price
    if ordered_pizzas >= 5 :
        delivery_cost=0
    if tuesday_discount in yess and delivery in yess and app_discount in yess:
        total_price = (((pizza_sum_price - (50 / 100 * pizza_sum_price))-(25 / 100 *pizza_sum_price)) + delivery_cost)
    elif tuesday_discount in noo and delivery in yess and app_discount in yess:
        total_price = ((pizza_sum_price -(25 / 100 *pizza_sum_price)) + delivery_cost)

    elif tuesday_discount in yess and delivery in noo and app_discount in yess:
        total_price = ((pizza_sum_price - (50 / 100 * pizza_sum_price))-(25 / 100 *pizza_sum_price))

    elif tuesday_discount in yess and delivery in yess and app_discount in noo:
            total_price = ((pizza_sum_price - (50 / 100 * pizza_sum_price)) + delivery_cost)

    elif tuesday_discount in yess and delivery in noo and app_discount in noo:
        total_price = ((pizza_sum_price - (50 / 100 * pizza_sum_price)))

    elif tuesday_discount in noo and delivery in yess and app_discount in noo:
        total_price = (pizza_sum_price + delivery_cost)

    elif tuesday_discount in noo and delivery in noo and app_discount in yess:
        total_price = (pizza_sum_price-(25 / 100 *pizza_sum_price))

    else:
        total_price = pizza_sum_price

    return total_price

def display(overall_cost):
    print(f"\nTotal price: £{overall_cost:.2f}")

ordered_pizzas=nof_pizza()
delivery=delivery_too()
tuesday_discount=tuesday_special()
app_discount=app_special()
overall_cost = calculate(ordered_pizzas, delivery, tuesday_discount, app_discount)
display(overall_cost)
