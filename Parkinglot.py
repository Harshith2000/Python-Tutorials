#Imagine an parking lot with 20 parking spaces, where each parking space has an ID which is a natural number, starting with 1, 2, 3, ….upto 20. Parking space '1' is the one closest to the entrance.
#The parking space can be in three sizes: small(10 parking spaces), medium(7 parking spaces) and large slots(3 parking spaces).
#Three types of vehicles are allowed to be parked in a parking space: motorcycle(small), car(medium) and bus(large)
#A motorcycle can be parked in any small, medium or large parking spaces.
#A car can be parked in either a medium slot or a large parking spaces.
#A bus can be parked only in a large parking space.
#When a user enters the parking lot, vehicle type and vehicle ID are noted and fed as input to our system
#Our system should assign the vehicle to the nearest parking space available(if any parking space is available)
#User should be given a printed ticket with the assigned parking spot ID and his vehicle ID
class bike:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class car:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class bus:
    def __init__(self,name,id):
        self.name=name
        self.id=id
temp=[]
for i in range(1,11):
    temp.append(1)
for i in range(11,18):
    temp.append(2)
for i in range(18,21):
    temp.append(3)
def main():
    while(1):
        print("Enter the vehicle name and id")
        nam=input()
        idd=input()
        if nam=="Bike":
            for i in range(1,21):
                if((temp[i-1]==1) or (temp[i-1]==2) or (temp[i-1]==3)):
                    temp[i-1]=0
                    slot_id=i
                    break
            bik=bike(nam,idd)
            print("The vehicle is",bik.id)
            print("The slot id is",slot_id)
        if nam == "Car":
            for i in range(11, 21):
                if ((temp[i - 1] == 2) or (temp[i - 1] == 3)):
                    temp[i - 1] = 0
                    slot_id = i
                    break
            ca = car(nam, idd)
            print("The vehicle is", ca.id)
            print("The slot id is", slot_id)
        if nam == "Bus":
            for i in range(18, 21):
                if (temp[i - 1] == 3):
                    temp[i - 1] = 0
                    slot_id = i
                    break
            bu = bus(nam, idd)
            print("The vehicle id is", bu.id)
            print("The slot id is", slot_id)



if __name__ == '__main__':
    main()
