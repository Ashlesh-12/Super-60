class Organization:
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    
class Trainer:
    def __init__(self,name,organization):
        self.name=name
        self.organization=organization
    def getOrganization(self):
        return self.organization.getName()
    
class Trainee():
    def __init__(self,name):
        self.name=name

class Course:
    def __init__(self,Modules):
        self.Modules=Modules
    def getModule(self):
        return self.Modules
    
class Modules:
    def __init__(self,Unit):
        self.Unit=Unit
    def getUnit(self):
        return self.Unit
    
class Unit:
    def __init__(self,Duration):
        self.Duration=Duration
    def getDuration(self):
        return self.Duration
    
class Topic:
    def __init__(self,name):
        self.name=name

class Training:
    def __init__(self,trainer,trainee,course):
        self.trainer=trainer
        self.trainee=trainee
        self.course=course
    def getNum_of_trainers(self):
        return len(self.trainee)
    def getTraining_Organization(self):
        return self.trainer.getOrganization
    def getDuration(self):
        totalDuration=0
        for m in self.course.getModule():
            for u in m.getUnit():
                totalDuration+=u.getDuration()
        return totalDuration
    
def test_main():
    org=Organization("Sahyadri")
    Trainer1=Trainer("Ashlesh",org)
    Trainee1=Trainee("Keerthan")
    Trainee2=Trainee("Sushant")
    unit1=Unit(5)
    unit2=Unit(4)
    unit3=Unit(2)
    module1=Modules([unit1,unit2,unit3])
    course1=Course([module1])
    training=Training(Trainer1,[Trainee1,Trainee2],course1)
    print("No of Trainees:",training.getNum_of_trainers())
    print("Name of the Organization:",org.getName())
    print("Duration:",training.getDuration())
    
test_main()
    