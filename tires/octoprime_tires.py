from tires.tires import Tires

class OctoprimeTires(Tires):
    def _init_ (self,tire_wear):
        self.tire_wear = tire_wear
        self.tire_need_to_service = 3.0
    
    def needs_service(self):
        for tire in self.tire_wear:
            return sum(self.tire_wear) >= self.tire_need_to_service