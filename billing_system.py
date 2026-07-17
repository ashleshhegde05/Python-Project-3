# Billing System using OOP

class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Bill:

    def __init__(self):
        self.products = []

    def add_product(self):
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: ₹"))
        quantity = int(input("Enter Quantity: "))

        product = Product(name, price, quantity)
        self.products.append(product)

        print("Product Added Successfully!\n")

    def generate_bill(self):

        if len(self.products) == 0:
            print("No products added.")
            return

        subtotal = 0

        print("\n================ FINAL BILL ================")
        print("{:<15}{:<10}{:<10}{:<10}".format("Product", "Price", "Qty", "Total"))

        for product in self.products:
            total = product.total_price()
            subtotal += total

            print("{:<15}{:<10}{:<10}{:<10}".format(
                product.name,
                product.price,
                product.quantity,
                total
            ))

        tax = subtotal * 0.18
        grand_total = subtotal + tax

        print("--------------------------------------------")
        print("Subtotal : ₹", round(subtotal, 2))
        print("GST (18%): ₹", round(tax, 2))
        print("Grand Total: ₹", round(grand_total, 2))
        print("============================================")


bill = Bill()

while True:

    print("\n===== Billing System =====")
    print("1. Add Product")
    print("2. Generate Bill")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bill.add_product()

    elif choice == "2":
        bill.generate_bill()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")