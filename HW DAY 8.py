class Employee:
    def __init__(self, name, role):
        super().__init__()
        self.name = name
        self.role = role
    def display(self):
        print("name:",self.name,"role:",self.role)
class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization
    def display(self):
        print("name:",self.name,"role:",self.role,"specialization:",self.specialization)
class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style
    def display(self):
        print("name:",self.name,"role:",self.role,"yoga style:",self.yoga_style)
class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style
    def display(self):
        print("name:",self.name,"role:",self.role,"specialization:",self.specialization)
employee = Employee("Arun", "Staff")
trainer = Trainer("Rohan", "Fitness Trainer", "strength Training")
yoga_instructor = YogaInstructor("Sona", "Yoga coach", "Ashtanga Yoga")
multi_trainer = MultiTrainer("Neethu", "Multi-Trainer", "Crossfit", "power Yoga")
employee.display()
trainer.display()
yoga_instructor.display()
multi_trainer.display()




