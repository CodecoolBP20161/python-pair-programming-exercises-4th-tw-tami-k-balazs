from vehicle import Vehicle

class Car(Vehicle):
    max_ccm = 10000

    def __init__(self):
        super(Car, self).__init__()
        self.is_running = False

    def start_engine(self):
        self.is_running = True

    def stop_engine(self):
        self.is_running = False
