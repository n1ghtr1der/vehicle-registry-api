import persistent

class Car(persistent.Persistent):
    def __init__(self, brand, model, license_plate, color):
        self.brand = brand
        self.model = model
        self.license_plate = license_plate
        self.color = color