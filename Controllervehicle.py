from Vehicle import Vehicle
class ControllerVehicle():
    def __init__(self):
        self.__vehicles = {} #Key --> Plate, Value --> Vehicle  --
    def getVehicles(self):
        return self.__vehicles
    def addVehicle(self,plate,descrip,chasis,driver):
        if plate in self.__vehicles:
            return False
        vehicle = Vehicle(plate,descrip,chasis,driver)
        self.__vehicles[plate]=vehicle
        return True
    def delVehicle(self,plate):
        if plate not in  self.__vehicles:
            return False
        return self.__vehicles.pop(plate) #del slft.__vehicles[plate]
    def getNumberVehicles(self):
        return len(self.__vehicles)
    def addOdometer(self,plate,date,fromcity,tocity,kms):
        if plate not in self.__vehicles:
            return False
        vehicle =self.__vehicles[plate]
        vehicle.setOdometer(date,fromcity,tocity,kms)
        return True
    def comfirmOdometer(self,plate,date):
        if plate not in self.__vehicles:
            return False
        vehicle = self.__vehicles[plate]
        if date not in vehicle.getOdometer():
            return False
        vehicle.confirmOdometer(date)
        return True