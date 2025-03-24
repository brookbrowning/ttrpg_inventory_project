# Author: Brook Browning
# GitHub username: brookbrowning
# Description: This is a text-based inventory management project (to be used when playing a ttrpg, like Dnd).
# Goals: Create inventory (utilizing a csv file) that can be customized, stored, and recalled for quick reference during gameplay

from inventory_functions import *

spacing = 3*'\n'

# Introduction
print("Welcome! To your own personal bag of holding! A near limitless space to store:\n")
print(" - Your most precious magical artifacts")
print(" - Spell tomes and scrolls aplenty")
print(" - Other knick-knacks you've accumulated")
print("     (that you swear there's a use for)")
print("\n")

is_empty = is_inventory_empty()
if is_empty is True:
    print("Your inventory is currently empty. Would you like to store a new item?")
    action = input("Type 'y' to store a new item. Type 'x' to exit: ").lower()

    if action == 'y':
        new_name = input("Enter the name of your new item/spell: ").lower()
        add_new_item(item_name=new_name)
else:
    exit_app = False
    while exit_app is False:
        function_choice = choose_action()
        if function_choice == 's' or function_choice == 'r':
            name = input("Please enter the name of your object/spell: ").lower()
            already_exists = name_exists(name)
            if already_exists is True:
                if function_choice == 's':
                    over_wr_choice = input("This name already exists. Would you like to overwrite? (y/n): ").lower()
                    if over_wr_choice == "y":
                        overwrite(name)
                        print("\nItem info updated:")
                        view_item(name)
                        print(spacing)
                        exit_app = continue_app()
                else:
                    print("This item's attributes are: ")
                    view_item(name)
                    print(spacing)
                    update_choice = input("Would you like to update this item?(y/n): ").lower()
                    if update_choice == "y":
                        overwrite(name)
                        print("Item info updated:")
                        view_item(name)
                    print(spacing)
                    exit_app = continue_app()
            else:
                if function_choice == "s":
                    add_new_item(name)
                    print("You added:")
                    view_item(name)
                    print(spacing)
                    exit_app = continue_app()
                else:
                    print("\nThe item name entered does not exist. Please try again.", spacing)
        elif function_choice == 'i':
            print("Your current inventory: ")
            view_inventory()
            print(spacing)
            update_choice = input("Would you like to update an item?(y/n): ").lower()
            if update_choice == 'y':
                item_name = input("Enter the name of the item you want to update: ")
                already_exists = name_exists(item_name)
                if already_exists is True:
                    overwrite(item_name)
                else:
                    print("Name entered is not in list.")
            exit_app = continue_app()
        else:
            print('This is your current inventory:')
            view_inventory()
            item_name = input('Enter the name of the item you want to delete: ').lower()
            already_exists = name_exists(item_name)
            print(f"\nYou entered {item_name.title()}")
            if already_exists is True:
                confirmation = input(f"{item_name.title()} will be permanently deleted. Are you sure you want to delete {item_name.title()}? (y/n): ")
                confirmation_choices = ['y', 'n']
                if confirmation in confirmation_choices:
                    if confirmation == 'y':
                        delete_item(item_name)
                        print(f"{item_name.title()} has been deleted.")
                    else:
                        print(f"{item_name.title()} will not be deleted.")
                else:
                    print(f"'{confirmation}' is not a valid option. Please try again.")
            else:
                print("That name is not in your inventory. Please try again.")
            exit_app = continue_app()



