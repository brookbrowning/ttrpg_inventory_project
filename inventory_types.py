
class Attack:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.damage = 0
        self.range = "melee"
        self.dictionary = {'name' : name, 'type' : self.type, 'damage': self.damage, 'range' : self.range}



class Item:
    def __init__(self, name):
        self.name = name