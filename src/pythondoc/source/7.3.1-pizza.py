def make_pizza(*toppings):
    """打印客户点的所有配料"""
    print(toppings)
    print("----------")
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

print("-------------------------")
