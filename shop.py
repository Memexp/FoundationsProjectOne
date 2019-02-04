####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Meme's Cubcake"
signature_flavors = ["blue velvet", "red velvet", "purple velvet"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print ("Our menu:")
    for k in menu:
        print ("- \"" + k + "\" (KD " + str(menu[k]) + ")") 


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for k in original_flavors:
        print ("- \"%s\"" % k) 


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for k in signature_flavors:
        print ("- \"%s\"" % k) 


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    all_shop = menu + original_flavors + signature_flavors
    for i in order:
        for f in all_shop:
            if i != f:
                return False
            else:
                return True



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    print ("What's your order? (Enter the exact spelling of the item you want. Type 'Exit' to end your order.)")
    thewhile = True

    while thewhile == True:
        order = input()
        if order != "exit":
            order_list.append(order)
        else:
            thewhile = False


    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    print ("That'll be KD %s" % total)
    print ("This order is eligible for credit card payment.")
    print ("Thank you for shopping at %s" % cupcake_shop_name)


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for order in order_list:
        for k in menu:
            if order == k:
                total += menu[k]
        for i in original_flavors:
            if order == i:
                total += 2
        for j in signature_flavors:
            if order == j:
                total += 2.75              

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for order in order_list:
        "- %s" % order 

    accept_credit_card(get_total_price(order_list))
