class Vehicle:
    def __init__(self,plate,descrip,chasis,driverName):
        self.__plate =plate
        self.__descrip =descrip
        self.__chasis =chasis
        self.__driverName =driverName
        self.__odometer = {}
        self.__totalKms =0.0
        self.__history = None
        
    def getPlate(self):
        return self.__plate


    def getDescrip(self):
        return self.__descrip


    def getChasis(self):
        return self.__chasis


    def getDriverName(self):
        return self.__driverName

    def getOdometer(self):
        return self.__odometer


    def getTotalKms(self):
        return self.__totalKms
    def setTotalKms(self,value):
        self.__totalKms = value

    def getHistory(self):
        return self.__history
    def setHistory(self,value):
        self.__history = value

    def setOdometer(self,date,fromcity,tocity,kms):
        self.__odometer[date]=(fromcity,tocity,kms)
    def getOdometer(self):
        return self.__odometer
    def confirmOdometer(self,date):
        detailsOdo =self.__odometer.pop(date)
        print(detailsOdo)
        self.__totalKms+=detailsOdo[2]
        self.__history  +="\t "+date+" - "+detailsOdo[0]+" - "+detailsOdo[1]+" - "+str(self.__totalKms)+"\n"


    def setTotalKms(self,var):
        self.__totalKms=var
        
    def setHistory(self,var):
        self.__history=var
