from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition):
        super().__init__("Electronics", condition)
    
    def __str__(self):
        self.Electronics = "A gadget full of buttons and secrets."
        return self.Electronics
