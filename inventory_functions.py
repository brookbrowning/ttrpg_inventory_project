
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

    if type == 'w' or type == 's':

    else:



