from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition):
        super().__init__("Decor", condition)
        
    def __str__(self):
        self.decor = "Something to decorate your space."
        return self.decor