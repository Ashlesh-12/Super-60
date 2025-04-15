from abc import ABC, abstractmethod
import random

class Animals(ABC):
    def __init__(self, name, health_level, hunger, habitat_type):
        self._name = name
        self._health = health_level
        self._hunger = hunger
        self._habitat_type = habitat_type

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food_amount):
        pass

    def get_health(self):
        return self._health

    def get_hunger(self):
        return self._hunger

    def get_habitat_type(self):
        return self._habitat_type

    def decrease_health(self, amount):
        self._health = max(self._health - amount, 0)

    def decrease_hunger(self, amount):
        self._hunger = max(self._hunger - amount, 0)

    def increase_health(self, amount):
        self._health = min(self._health + amount, 100)

    def increase_hunger(self, amount):
        self._hunger = min(self._hunger + amount, 100)

class Lion(Animals):
    def __init__(self, name, health_level, hunger, habitat_type):
        super().__init__(name, health_level, hunger, habitat_type)

    def make_sound(self):
        print(f"{type(self).__name__} Roar!")

    def feed(self, food_amount):
        temp = self.get_hunger()
        self.decrease_hunger(food_amount * 2)
        self.increase_health(food_amount * 0.5)
        print(f"Feeding {type(self).__name__} {temp} -> {self.get_hunger()}")

class Elephant(Animals):
    def __init__(self, name, health_level, hunger, habitat_type):
        super().__init__(name, health_level, hunger, habitat_type)

    def make_sound(self):
        print(f"{type(self).__name__} Trumpet!")

    def feed(self, food_amount):
        temp = self.get_hunger()
        self.decrease_hunger(food_amount * 1.5)
        self.increase_health(food_amount * 0.3)
        print(f"Feeding {type(self).__name__} {temp} -> {self.get_hunger()}")

class Parrot(Animals):
    def __init__(self, name, health_level, hunger, habitat_type):
        super().__init__(name, health_level, hunger, habitat_type)

    def make_sound(self):
        print(f"{type(self).__name__} Squawk!")

    def feed(self, food_amount):
        temp = self.get_hunger()
        self.decrease_hunger(food_amount * 0.5)
        self.increase_health(food_amount * 0.2)
        print(f"Feeding {type(self).__name__} {temp} -> {self.get_hunger()}")

class Habitat(ABC):
    def __init__(self, type, condition, animals=None):
        self._type = type
        self._condition = condition
        self._animals = animals or []

    @abstractmethod
    def affect_animal(self, animal):
        pass

    def add_animal(self, animal: Animals):
        if animal.get_habitat_type() == self._type:
            self._animals.append(animal)
        else:
            print(f"{animal._name} doesn't belong to {self._type}")

    def get_condition(self):
        return self._condition

    def degrade(self, amount):
        self._condition = max(self._condition - amount, 0)

class Savanna(Habitat):
    def __init__(self, condition, animals=None):
        super().__init__(type(self).__name__, condition, animals)

    def affect_animal(self, animal: Animals):
        if self._condition > 50:
            animal.increase_health(5)
        else:
            animal.decrease_health(5)

class Jungle(Habitat):
    def __init__(self, condition, animals=None):
        super().__init__(type(self).__name__, condition, animals)

    def affect_animal(self, animal: Animals):
        if self._condition > 60:
            animal.increase_health(3)
        else:
            animal.decrease_health(3)

class Aviary(Habitat):
    def __init__(self, condition, animals=None):
        super().__init__(type(self).__name__, condition, animals)

    def affect_animal(self, animal: Animals):
        if self._condition > 70:
            animal.increase_health(2)
        else:
            animal.decrease_health(2)

class Staff(ABC):
    def __init__(self, name, energy):
        self._name = name
        self._energy = energy

    @abstractmethod
    def perform_task(self, target):
        pass

    def get_energy(self):
        return self._energy

    def use_energy(self, amount):
        self._energy = max(self._energy - amount, 0)

class Caretaker(Staff):
    def __init__(self, name, energy):
        super().__init__(name, energy)

    def perform_task(self, target):
        if isinstance(target, Habitat):
            target._condition = min(100, target._condition + 20)
            self.use_energy(10)
        else:
            print("Caretaker can only maintain habitats.")

class Veterinarian(Staff):
    def __init__(self, name, energy):
        super().__init__(name, energy)

    def perform_task(self, target):
        if isinstance(target, Animals):
            target.increase_health(15)
            self.use_energy(15)
        else:
            print("Veterinarian can only treat animals.")

class Sanctuary:
    def __init__(self, animals=None, habitats=None, staff=None):
        self.animals = animals or []
        self.habitats = habitats or []
        self.staff = staff or []

    def add_animal(self, animal: Animals, habitat: Habitat):
        if animal.get_habitat_type() == habitat._type:
            self.animals.append(animal)

    def add_habitat(self, habitat):
        self.habitats.append(habitat)

    def add_staff(self, staff):
        self.staff.append(staff)

    def simulate_day(self):
        for animal in self.animals:
            animal.make_sound()
            animal.increase_hunger(10)

        for habitat in self.habitats:
            habitat.degrade(10)

        for person in self.staff:
            if isinstance(person, Caretaker):
                habitat = random.choice(self.habitats)
                person.perform_task(habitat)
                print(f"Caretaker maintaining {type(habitat).__name__}")
            elif isinstance(person, Veterinarian):
                animal = random.choice(self.animals)
                if animal.get_health() < 50:
                    person.perform_task(animal)
                    print(f"Veterinarian treating {type(animal).__name__} (health < 50)")

        for animal in self.animals:
            if animal.get_hunger() > 50:
                animal.feed(20)

        print("\nAnimal Status:")
        for animal in self.animals:
            print(f"{type(animal).__name__} ({animal.get_habitat_type()}): Health {animal.get_health()}, Hunger {animal.get_hunger()}")

        print("\nHabitat Status:")
        for habitat in self.habitats:
            print(f"{type(habitat).__name__}: Condition {habitat.get_condition()}")

def main():
    animals = [Lion("Leo", 10, 20, "Savanna"), Elephant("Mirchi", 90, 20, "Jungle"), Parrot("Chichi", 70, 45, "Aviary")]
    habitats = [Savanna(50, [animals[0]]), Jungle(75, [animals[1]]), Aviary(100, [animals[2]])]
    staff = [Caretaker("Shek", 50), Veterinarian("Aadithya", 85)]

    sanctuary = Sanctuary(animals, habitats, staff)
    print("--- Day 1 ---")
    sanctuary.simulate_day()

if __name__ == "__main__":
    main()