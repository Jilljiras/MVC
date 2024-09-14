import json
import random

def generate_cow_data(num_white, num_brown):
    cows = []
    
    # Helper function to generate random age in years and months
    def random_age():
        return {
            "age_years": random.randint(0, 10),
            "age_months": random.randint(0, 11)
        }
    
    # Generate white cows
    for _ in range(num_white):
        cow = {
            "id": random.randint(10000001, 99999999),
            "breed": "white",
            "milk_count": 0,
            "is_bsod": False,
            **random_age()
        }
        cows.append(cow)
    
    # Generate brown cows
    for _ in range(num_brown):
        cow = {
            "id": random.randint(10000001, 99999999),
            "breed": "brown",
            "milk_count": 0,
            "is_bsod": False,
            **random_age()
        }
        cows.append(cow)
    
    return cows

# Create 20 cows (10 white and 10 brown)
data = generate_cow_data(10, 10)

# Write to data.json
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Data generated and saved to 'data.json'")
