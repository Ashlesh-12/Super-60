class Trainer:
    def __init__(self, name, organization):
        self.name = name
        self.organization = organization
        self.trainees = []

    def add_trainee(self, trainee):
        self.trainees.append(trainee)
