# Calculate package shipping cost according to its weight

class Calculate_Shipment():

    def __init__(self):
        self.weight = 0
        self.unit = 0
        self.total = 0
        self.product = 0
        self.price = 0

    def obtain_weight(self):
        print("Enter the weight and units to calculate")
        while True:
            try:
                self.weight = float(input("Enter weight of product: "))
                self.unit = int(input("Enter units: "))
                if self.weight <= 0 or self.unit <= 0:
                    print("Enter only positive non-zero values")
                self.product = self.weight * self.unit
                self.total += self.product
                while True:
                    answer = input(
                        "Do you want enter more products? Yes: Y, No: N \n")
                    if answer.upper() in ('Y', 'N'):
                        break
                    else:
                        print("Yo must indicate 'Y' or 'N'")
                if answer.upper() == 'N':
                    break
            except:
                print("Please, enter a number")
        return self.total

    def calculate_price(self):
        message = "Price of your shipment is"
        if self.total < 1:
            self.price = 2
            print(message, round(self.price, 2), "€")
        elif self.total < 5:
            self.price = 5
            print(message, round(self.price, 2), "€")
        elif self.total <= 10:
            self.price = self.total * 1.10
            print(message, round(self.price, 2), "€")
        elif self.total <= 20:
            self.price = self.total * 1.25
            print(message, round(self.price, 2), "€")
        elif self.total <= 30:
            self.price = self.price * 1.5
            print(message, round(self.price, 2), "€")
        else:
            print("The maximum weight available to send is 30 Kg.")


calculator = Calculate_Shipment()
total = calculator.obtain_weight()
if isinstance(total, float) and total > 0:
    if total < 1:
        print("Total weight", round(total, 2), "gr")
    else:
        print("Total weight", total, "Kg")
calculator.calculate_price()
