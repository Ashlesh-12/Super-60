from Trainer_class import Trainer
from Trainee_class import Trainee
from Organization_class import Organization
from Topic_class import Topic
from Unit_class import Unit
from Module_class import Module
from Course_class import Course
from Training_class import Training

def main():
    org1 = Organization("Tech Academy")
    
   
    trainer1 = Trainer("John Doe", org1)
    
   
    trainee1 = Trainee("Alice")
    trainee2 = Trainee("Bob")
    
   
    topic1 = Topic("Python Basics")
    topic2 = Topic("Object-Oriented Programming")
    
    unit1 = Unit(3, [topic1])
    unit2 = Unit(2, [topic2])
    
   
    module1 = Module([unit1, unit2])
    
   
    course1 = Course([module1])
    
   
    training1 = Training(trainer1, [trainee1, trainee2], course1, 5)
   
    print("Number of Trainees:", training1.getNumOfTrainees())
    print("Training Organization Name:", training1.getTrainingOrganizationName())
    print("Training Duration (in hours):", training1.getTrainingDurationInHrs())

if __name__ == "__main__":
    main()
