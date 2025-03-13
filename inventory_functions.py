import inventory_types


def store():
    print("What would you like to store?")
    inv_type = input("Type 'w' for weapon\n Type 's' for spell\n Type 't' for treasure\n "
                     "Or type 'u' for useless piece of crap").lower()
    types = ['w', 's', 't', 'u']
    if inv_type in types:
        info(inv_type)
    else:
        return


def info(type):
    name = input("What is the name of your object/spell?:")
    #Check name in current inventory
    # if already exists, overwrite/update?
    if type == 'w' or type == 's':
        new_attack = inventory_types.Attack
        # update attack category
    else:
        # update item category
        new_item = inventory_types.Item



