class InvalidExperienceException(Exception):
    pass

class Employee:
    def __init__(self, name, age, experience):
        self._name = name
        self._age = age
        self._experience = experience
    
    # Getter and Setter for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and Setter for age
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    # Getter and Setter for experience
    def get_experience(self):
        return self._experience

    def set_experience(self, experience):
        self._experience = experience
    
    # Method to compute years of experience
    def compute_years(self):
        try:
            parts = self._experience.split('.')
            if len(parts) == 1 or len(parts[1]) == 1:
                years = int(parts[0])
                return years
            elif len(parts) == 2 and len(parts[1]) == 2 and parts[1] in ['10', '11', '12']:
                years=int(parts[0])
                years += 1
                return years
            else:
                raise InvalidExperienceException(f"Invalid experience format: {self._experience}")
        except InvalidExperienceException as e:
            print(e)

# Example usage:
employee = Employee("John Doe", 30, "5.12")
print(f"Name: {employee.get_name()}, Age: {employee.get_age()}, Experience (years): {employee.compute_years()}")

class Address:
    def __init__(self,line1,line2,city,state,pin):
        self._line1=line1
        self._line2=line2
        self._city=city
        self._state=state
        self._pin=pin
        
