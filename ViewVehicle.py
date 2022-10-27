from Controllervehicle import ControllerVehicle
from Vehicleapi import getDistance
from Vehicle import Vehicle
controller = ControllerVehicle()
def readPlate():
    plate=""
    while True:
        plate = input("Enter the Plate: ")
        if(len(plate)==7):
            numPart = plate[:4]
            lettersPart = plate[4:]
            if numPart.isdigit:
                if lettersPart.isalpha:
                    break
        print("Error entering the Plate!!!")
    return plate
def addVehicle():
    plate =readPlate()
    desc = input("Enter Description: ")
    while True:
        chasis = input("Enter Chasis (17 characters): ")
        if(len(chasis)==17):
            break
        print("Error entering the Chasis (17 characters)")
    driver = input("Enter Drive: ")
    if controller.addVehicle(plate,desc,chasis,driver):
        print("Vechicle aadd successfully!!")
    else:
        print("Error adding the Vehicle. Plate already !!")
def delVehicle():
    plate =readPlate()
    if(controller.delVehicle(plate)):
        print("Vehicle deleted!!")
    else:
        print("Vehicle it's not deleted!!")
def addOdometer():
    plate =readPlate()
    date = input("Enter date [dd/mm/yyyy]: ")
    source = input("From: ")
    destination = input("To: ")
    kms = getDistance(source=source,dest=destination)/1000
    if(controller.addOdometer(plate,date,source,destination,kms)):
        print("Odometer added successfully!")
    else:
        print("Error adding odometer!")

def comfirmOdometer():
    plate =readPlate()
    date = input("Enter date [dd/mm/yyyy]: ")
    if(controller.comfirmOdometer(plate,date)):
        print("Odometer confirm successfully!")
    else:
        print("Error confirm odometer!")
def listVechicle():
    vehicles = controller.getVehicles()
    for plate,vehicle in vehicles.items():
        print("Plate:",plate)
        print("Description:",vehicle.getDescrip())
        print("Chasis:",vehicle.getChasis())
        print("Driver:",vehicle.getDriverName())
        print("Unconfirm Odometer: ")
        for date,odomete in vehicle.getOdometer().items():
            print("\t",end="")
            print(date,odomete[0],odomete[1],odomete[2],sep=" - ")
    print()
    print("TotalKms:",vehicle.getTotalKms())
    print("History:\n",vehicle.getHistory())

while True:
    print("Currently there are",controller.getNumberVehicles(),"vehicles registered!")
    print("1.- Add a vehicle")
    print("2.- Delete vehicle")
    print("3.- Add odometer")
    print("4.- Confirm odometer")
    print("5.- List vehicle")
    print("6.- Exit")
    option = int(input("Choose option: "))
    if option == 6:
        print("Good bye!")
        break
    elif option == 1:
        addVehicle()
    elif option ==2:
        delVehicle()
    elif option ==3:
        addOdometer()
    elif option ==4:
        comfirmOdometer()
    elif option == 5:
        listVechicle()
    else:
        print("The option selected it's not exist!")