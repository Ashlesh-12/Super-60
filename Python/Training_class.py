class Training:
    def __init__(self, trainer, trainees, course, duration):
        self.trainer = trainer
        self.trainees = trainees
        self.course = course
        self.duration = duration

    def getNumOfTrainees(self):
        return len(self.trainees)

    def getTrainingOrganizationName(self):
        return self.trainer.organization.name

    def getTrainingDurationInHrs(self):
        return self.duration
























