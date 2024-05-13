class Vehicle:
    def __init__(self, reg_num, model, owner):
        self.reg_num = reg_num
        self.model = model
        self.owner = owner

    def update_owner(self, new_owner):
        print(f"The {self.model} has been transfered from {self.owner} to {new_owner}")
        self.owner = new_owner

car1 = Vehicle(1, "Batmobile", "Batman")
car2 = Vehicle(2, "Shadowfax", "Gandalf")
car3 = Vehicle(672, "Nimbus", "Goku")

car1.update_owner("Robin")

class Event:
    def __init__(self, name, date, participant_count):
        self.name = name
        self.date = date
        self.participant_count = participant_count

    def add_participant(self):
        self.participant_count += 1

    def bounce_participant(self):
        self.participant_count -= 1

    def get_participant_count(self):
        return self.participant_count

mothers_day = Event("Mother's Day", "May 12", 1000000000)
mothers_day.add_participant()
print(mothers_day.get_participant_count())