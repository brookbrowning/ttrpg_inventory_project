# Author: Brook Browning
# GitHub username: brookbrowning
# Description: This is an inventory management project (to be used when playing a ttrpg, like Dnd).
# Goals: Create inventory objects that can be customized, stored, and recalled for quick reference during gameplay


import inventory_types
import inventory_functions

my_inventory = {
'Attack': [{'name' : 'trident', 'type' : 'weapon', 'damage': '3d6', 'range' : 'melee'},
           {'name' : 'shocking grasp', 'type' : 'spell', 'damage': '1d8', 'range' : 'touch'},],
'Item' : [{'name': 'fishing pole', 'type' : 'junk'}, {'name': 'eye of anubis', 'type' : 'treasure'}]
}


# Introduction
print("Welcome! To your own personal bag of holding! A near limitless space to store:\n")
print(" - Your most precious magical artifacts")
print(" - Spell tomes and scrolls aplenty")
print(" - Other knick-knacks you've accumulated")
print("     (that you swear there's a use for)")
print("\n")

print("What would you like to do?\n Type 's' to store an item,\n Type 'r' to retrieve an item,\n "
                   "Type 'i' to view a list of inventory,\n Or type '?' if you're generally confused\n")
user_input = input("I would like to: ").lower()

if user_input == 's':
    inventory_functions.store()


