from model.database import Database

class CowController:
    def __init__(self, db: Database):
        self.db = db

    def milk_cow(self, cow_id):
        cow = self.db.get_cow(cow_id)
        if cow:
            result = cow.milk()
            self.db.add_cow(cow)  # Save cow status after milking
            return result
        return "Cow not found"

    def reset_cow(self, cow_id):
        cow = self.db.get_cow(cow_id)
        if cow:
            cow.is_bsod = False
            cow.milk_count = 0
            self.db.add_cow(cow)
            return "Cow reset"
        return "Cow not found"

    def report(self):
        milk_counts = {
            "Plain milk": 0,
            "Chocolate milk": 0,
            "Soy milk": 0
        }
        for cow in self.db.cows:
            if not cow.is_bsod:
                milk_type = cow.milk()
                if milk_type in milk_counts:
                    milk_counts[milk_type] += 1

        total_milk = sum(milk_counts.values())
        return {
            "milk_counts": milk_counts,
            "total_milk": total_milk
        }
