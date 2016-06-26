from vehicle import Vehicle



class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.carry_limit = 0
        self.current_carriage_weight = None

    def has_carriage(self):
        return self.current_carriage_weight != None

    def attach_carriage(self, weight):
        if self.carry_limit >= weight:
            self.current_carriage_weight = weight
            # return True
        return self.has_carriage()

    def detach_carriage(self):
        if self.has_carriage():
            self.current_carriage_weight = None
