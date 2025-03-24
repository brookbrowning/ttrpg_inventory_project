import csv


# my_inventory = [{'name': 'trident', 'type': 'weapon', 'damage': '3d6', 'range': 'melee', 'description' : None},
#                {'name': 'shocking grasp', 'type': 'spell', 'damage': '1d8', 'range': 'touch', 'description': None}, ]
#
# with open('inventory.csv', 'w', newline='') as csvfile:
#     fieldnames = ['name', 'type', 'damage', 'range', 'description']
#     writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
#     writer.writeheader()
#     writer.writerows(my_inventory)

#f
def read_inv():
    inv = []
    with open('inventory.csv', 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            inv.append(row)
    return inv


def is_inventory_empty():
    file_size = len('inventory.csv')
    if file_size == 0:
        return True
    else:
        return False


def name_exists(name):
    my_inventory = read_inv()
    names_list = []
    for val in my_inventory:
        names_list.append(val['name'])
    if name in names_list:
        return True
    else:
        return False

def overwrite(name):
    print("overwriting")


def view_item(name):
    my_inventory = read_inv()
    for index, entry in enumerate(my_inventory):
        if entry['name'] == name:
            for key in entry:
                value = str(entry[key])
                print(key.title(), ':', value.title())


def view_inventory():
    my_inventory = read_inv()
    for index, entry in enumerate(my_inventory):
        print(index+1, entry['name'].title())


def object_type():
    """This function prompts the user to determine a 'type' for their object, which determines which attributes it has"""
    print("Enter the item type.")
    inv_type = input(" Type 'w' for weapon\n Type 's' for spell\n Type 't' for treasure\n "
                     "Or type 'u' for useless piece of crap: ").lower()
    types = ['w', 's', 't', 'u']
    if inv_type in types:
        if inv_type == 'w':
            return 'weapon'
        elif inv_type == 's':
            return 'spell'
        elif inv_type == 't':
            return 'treasure'
        else:
            return 'junk'
    else:
        print(f"You inputted {inv_type}. Please enter a valid option.")
        object_type()


def add_new_item(item_name):
    item_type = object_type()
    damage = input("Enter the amount of damage (or enter 'none'): ").lower()
    item_range = input("Enter the damage range (or enter 'none'): ").lower()
    description = input("Enter a brief description (or enter 'none'): ").lower()
    new_item = [item_name, item_type, damage, item_range, description]
    with open('inventory.csv', 'a') as infile:
        writer = csv.writer(infile)
        writer.writerow(new_item)


def continue_app():
    exit_app = input("Would you like to exit the app? (y/n): ").lower()
    answers = ['y', 'n']
    if exit_app in answers:
        if exit_app == 'y':
            return True
        else:
            return False
    else:
        print("Invalid choice.")
        continue_app()

def choose_action():
    correct_response = False
    while correct_response is False:
        print("What would you like to do?\n - Type 's' to store an item,\n - Type 'r' to retrieve an item,\n "
                           "- Type 'i' to view a list of inventory,\n - Or type 'x' to exit\n")
        user_input = input("I would like to: ").lower()
        options = ['s', 'r', 'i', 'x']
        if user_input in options:
            correct_response = True
            return user_input
        else:
            print("That is not an option, please try again\n")

