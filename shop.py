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
    if order in menu or order in original_flavors or order in signature_flavors:
        return True
    else:
        return False



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    print ("What's your order? (Enter the exact spelling of the item you want. Type 'Exit' to end your order.)")

    while True:
        order = input()
        
        if is_valid_order(order) == True:
            order_list.append(order)
        elif order == "exit":
            break
        else:
            print("Your item is invalid, Please order something from the menu.")

    return order_list



def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total > 5:
        print ("This order is eligible for credit card payment.")
    else:
        print ("The order is not eligible for credit card payment.")    
    


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
        print ("- %s" % order) 
    total = get_total_price(order_list)
    print ("That'll be KD %s" % total)
    
    accept_credit_card(total)

    print ("Thank you for shopping at %s" % cupcake_shop_name)
