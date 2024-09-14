import random

class Cow:
    def __init__(self, id: int, breed: str, age_years: int, age_months: int = 0, milk_count: int = 0, is_bsod: bool = False):
        self.id = id
        self.breed = breed
        self.age_years = age_years
        self.age_months = age_months
        self.milk_count = milk_count
        self.is_bsod = is_bsod

    def milk(self) -> str:
        """Returns the type of milk produced and checks for BSOD"""
        if self.is_bsod:
            return "BSOD: Cannot produce milk"
        
        milk_type = "Regular milk"
        if self.breed == "white":
            chance_of_bsod = 0.005 * (self.age_years + self.age_months / 12)
            if random.random() < chance_of_bsod:
                self.is_bsod = True
                return "BSOD: Soy milk cannot be produced"
            milk_type = "Plain milk"
        elif self.breed == "brown":
            chance_of_bsod = 0.01 * self.age_years
            if random.random() < chance_of_bsod:
                self.is_bsod = True
                return "BSOD: Almond milk cannot be produced"
            milk_type = "Chocolate milk"
        
        self.milk_count += 1
        return milk_type

    def __str__(self):
        return f"Cow ID: {self.id}, Breed: {self.breed}, Age: {self.age_years} years {self.age_months} months, Milk Count: {self.milk_count}"

