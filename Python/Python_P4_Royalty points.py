#Calculate royalty points for a cafe where customers earn 10 points for every cup of coffee they buy

class CafeRoyaltyPoints:
    def __init__(self):
        self.points = {}

    def buy_coffee(self, phone_number, cups):
        if phone_number not in self.points:
            self.points[phone_number] = 0
        if cups > 0:
            self.points[phone_number] += cups * 10

    def check_points(self, phone_number):
        return self.points.get(phone_number, 0)

    def reset_points(self, phone_number):
        if phone_number in self.points:
            self.points[phone_number] = 0

# Create a CafeRoyaltyPoints object
cafe_loyalty = CafeRoyaltyPoints()

while True:
    phone_number = input("Enter customer's phone number (or 'q' to quit): ")
    if phone_number == 'q':
        break
    try:
        cups = int(input("Enter the quantity of drinks bought: "))
    except ValueError:
        print("Invalid input. Please enter a valid number of drinks.")
        continue
    
    cafe_loyalty.buy_coffee(phone_number, cups)
    print(f"Total Royalty Points for {phone_number}: {cafe_loyalty.check_points(phone_number)}")

# Display the final dictionary containing customer points
print("Customer Royalty Points Dictionary:", cafe_loyalty.points)

# Example usage:
# Enter customer's phone number (or 'q' to quit): 1234567890
# Enter the quantity of drinks bought: 2
# Total Royalty Points for 1234567890: 20
# Enter customer's phone number (or 'q' to quit): 9876543210
# Enter the quantity of drinks bought: 3
# Total Royalty Points for 9876543210: 30
# Enter customer's phone number (or 'q' to quit): q
# Customer Royalty Points Dictionary: {'1234567890': 20, '9876543210': 30}

