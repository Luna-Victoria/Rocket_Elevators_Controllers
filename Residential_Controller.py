VarFloorNameList = ["SS2","SS1","RC","2","3","4","5","6","7","8"]
VarNumberOfFloor = len(VarFloorNameList)
VarElevatorList = ["Elevator 1", "Elevator 2"]
VarNumberOfElevator = 2
Elevators=[]
Floors=[]
ElevatorDirection = ["Up", "Down", "Nowhere"]
Status = ["Idle", "Stop", "Moving"]


class ClOperator:
    def __init__(self,VarNumberOfFloor,VarNumberOfElevator):
        self.Column = []
        self.Column.append(ClColumn(VarNumberOfFloor,VarNumberOfElevator))


    def CallElevator(self,CurrentFloor,Direction):
        print("I want to go " + str(Direction) +
              ". I am on floor "+str(CurrentFloor))

        Elevator = self.FindElevator(CurrentFloor,Direction)
        print(str(Elevator.Id))
        self.OperateElevator(Elevator)
        return Elevator
        self.CallElevator = []

    def OperateElevator(self, Elevator):
        if Elevator.DestinationList == []:
            Elevator.Status ="Idle"
        else:
            NextFloor = Elevator.DestinationList[0]
            if NestFloor == Elevator.Floor:
                Elevator.Status = "Stop"
                Elevator.OpenDoor()
            elif NextFloor > Elevator.Floor:
                Elevator.Status = "Moving"
                Elevator.LevelUp()
            else:
                Elevator.status = "Moving"
                Elevator.LevelDown()


    def FindElevator(self,CurrentFloor,Direction):
        for Elevator in self.Columns[0].Elevators:
            print("Elevator " + str(Elevator.Id) + ", Direction " + str(Elevator.Direction) + ", Status " + str(Elevator.Status))
            if Elevator.Floor == self.CurrentFloor and Elevator.Status == "Stop":
                return Elevator
            elif Elevator.Status == "Idle":
                return Elevator
            elif Elevator.Status == "Moving" and Elevator.Floor < self.CurrentFloor and Elevator.Direction == "Up":
                return Elevator
            elif Elevator.Status == "Moving" and Elevator.Floor > self.CurrentFloor and Elevator.Direction == "Down":
                return Elevator
            else:
                return self.IsShortestList()

    def IsShortestList(self):
           ShortestListElevator = None
           for Elevator in self.Columns[0].Elevators:

               if len(Elevator.DestinationList) < len(ShortestListElevator.DestinationList):
                ShortestListElevator = Elevator

                print("Elevator with the shortest list is " + str(shortestListElevator))
           return ShortestListElevator


    def RequestFloor(self,FloorsNumber,Elevator):
        self.Elevator.ActivateButton(FloorNumber)



class ClColumn:
    def __init__(self,VarNumberofFloor,VarNumberOfElevator):
        self.ElevatorList=[]
        self.ButtonList=[]


# Elevator
        for x in range(VarNumberOfElevator):
            self.ElevatorList.append(ClElevator(x+1, VarNumberofFloor))


# FloorButton
        for y in range(VarNumberofFloor):
            FloorButton=[]
            if y is 0:
                self.ButtonList.append(ClFloorButton(y,VarFloorNameList[y],"Up"))
            elif y is -1:
                self.ButtonList.append(ClFloorButton(y,VarFloorNameList[y],"Down"))
            else:
                self.ButtonList.append(ClFloorButton(y,VarFloorNameList[y],"Up"))
                self.ButtonList.append(ClFloorButton(y,VarFloorNameList[y],"Down"))

            self.ButtonList.append(ClFloor(y,VarFloorNameList[y],FloorButton))


class ClElevator:
    def __init__(self,Id,Floor):
        self.Id=Id
        self.Status="Idle"
        self.Floor=0
        self.Direction="NoWhere"
        self.DestinationList=[]
        self.ButtonList=[]
        self.CloseDoorButton=CloseDoorsButton
        self.OpenDoorButton=OpenDoorsButton
        self.Door=Door()
        self.ElevatorNextFloor = []



# loop that created ElevatorButton
        for x in range(VarNumberOfElevator):
            for y in range(VarNumberOfFloor):
                self.ButtonList.append(ClElevatorButton("Elevator "+str(x+1)+" Button call floor "+VarFloorNameList[y]))

def LevelDown(self):
    self.Status="GoigDown"
    NextFloor = self.DestinationList[0]
    while NextFloor != self.Floor:
        self.Floor = self.Floor -1
        self.DestinationList.remove(NextFloor)
        self.OpenDoor()


def LevelUp(self):
    self.Status="GoigUp"
    NextFloor = self.DestinationList[0]
    while NextFloor != self.Floor:
        self.Floor = self.Floor +1
        self.DestinationList.remove(NextFloor)
        self.OpenDoor()

def OpenDoor(self):
    NextFloor = self.DestinationList[0]
    if self.Status is "Moving" or "Idle":
        self.Door.Status is "Closed"
    elif self.Floor is NextFloor:
        self.Door.Status is "Opened" and self.Door.Timer is "Active"


def CloseDoor(self):
    if self.Door.Timer > 0:
        self.Door.Status="Opened"
    else:
        self.door.status = "Closed"

def ActivateButton(self, FloorNumber):
    print(str(FloorNumber)+ " is selected")
    GoActivateButton = 0
    for x in self.ButtonList:
        if x.FloorNumber == FloorNumber:
            GoActivateButton = x

    GoActivateButton.Status = "Active"

class ClFloor:
    def __init__(self,Id,Number,FloorButton):
        self.Id=Id
        self.Number = Number
        self.FloorButton = FloorButton

class ClFloorButton:
    def __init__(self,Id,FloorNumber,VarNumberOfElevator):
        self.Id=Id
        self.FloorNumber=FloorNumber
        self.VarNumberOfElevator=VarNumberOfElevator
        self.status =[]

    def setButton(self,Floor,Direction):
        x = FindButton(Floor,Direction)
        x.self.Status = "Active"

    def FindButton(self,Floor,Direcion):
        return Button()

class Door:
    def __init__(self):
        self.Status= "Closed","Opened"
        self.Timer = 3

    def SetTimer(self):
        self.Status = "Inactive"

    def Open(self):
        self.Status = "Opened"
        print("Door Status = " + str(self.Status))

    def Close(self):
        self.Status = "Closed"
        print("Door Status = " + str(self.Status))


class ClElevatorButton:
    def __init__(self,Id):
        self.Id=Id
        self.Active = False

class OpenDoorsButton:

    def __init__(self):
        self.Status = "Inactive"

class CloseDoorsButton:
    def __init__(self):
        self.Status = "Inactive"

Controller = ClOperator(10,2)
Elevator = Controller.RequestFloor(2, "Up")
Floor = Controller.RequestFloor(4,Elevator)
