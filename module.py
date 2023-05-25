#exercise1-shopping cart
def shopping_cart():
    name=None
    user_input={}
    while True:
        select = input('please select 1 to add, 2 to delete, 3 to view your cart, "q" to quit: ')
        if select == '1':
            name = input('pleas enter your name:  ')
            items = input('pleas enter the item you want to buy:  ')
            user_input[name]=items
            print(f"{items} added to {name}'s art")
        elif select == '2':
            if name in user_input:
                items = input('pleas enter the item you want to remove: ')
                if items in user_input:
                    del user_input[items]
                    print(f"{items} deleted from {name}'s cart")
                else:
                    print(f"{items} not in {name}s cart.")
            else:
                print('user is unknown')
        elif select == '3':
            if user_input:
                print('shopping list: ')
                for name,items in user_input.items():
                    print("f{name} : {items}")
            else:
                print('shopping cart is empty')
        elif select.lower() == 'q':
            if user_input:
                print('here are your items in the cart')
                for name, items in user_input.items():
                    print(f"{name}: {items}")
            else:
                print('this is nothing in your cart')
                break
shopping_cart()


# exercise2

def square(l,w):
    a= l * w
    return a
print(square(100,20))

def c_circle(d=None,r=None,pi=3.14):
    d=input('what is the diameter ? ')
    c = None
    if d is None or d == "":
        r=input('what is the radius ? ')
        c = 2 * float(r) * pi
    else:
        c = (pi) * float(d)
    return c
print(c_circle())

    





