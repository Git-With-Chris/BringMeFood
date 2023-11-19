"""
NAME: CHRIS SANTOSH JOHN
STUDENT ID: 3954428
HIGHEST POINT ATTEMPTED: DI Level Completed
PROBLEMS/UNMET REQUIREMENTS IN CODE: Could not proceed into HD level. But did attempt it.
"""


class Customer:
    cust_type = 'C'

    def __init__(self, cust_id, cust_name):
        self.cust_id = cust_id
        self.cust_name = cust_name

    def get_id(self):
        return self.cust_id

    def get_name(self):
        return self.cust_name

    def get_cust_type(self):
        return self.cust_type

    def get_service_fee(self, cost):
        pass

    def get_discount(self, cost):
        pass

    def display_info(self):
        print("Customer ID: ", self.cust_id)
        print("Customer Name: ", self.cust_name)
        print("Customer Type: ", self.cust_type)


class BronzeCustomer(Customer):
    service_fee_rate = 0.1
    cust_type = 'B'

    def __init__(self, cust_id, cust_name):
        super().__init__(cust_id, cust_name)

    @staticmethod
    def get_service_fee_rate():
        return BronzeCustomer.service_fee_rate

    def get_service_fee(self, cost):
        service_fee = cost * BronzeCustomer.service_fee_rate
        return service_fee

    def get_discount(self, cost):
        return 0

    @staticmethod
    def set_service_fee_rate(new_rate):
        BronzeCustomer.service_fee_rate = new_rate

    def display_info(self):
        print("Customer ID: ", self.cust_id)
        print("Customer Name: ", self.cust_name)
        print("Customer Type: ", self.cust_type)
        print("Service Fee Rate: ", self.get_service_fee_rate(), '\n')

    def print_receipt(self, ordered_item, item_price, item_quantity, total_cost, final_cost, registration=False):
        print(f"{ordered_item.get_name():25}", f"{item_price:20}", " (AUD) x", f"{int(item_quantity):3d}",
              f"\nService fee:{self.get_service_fee(total_cost):39}", " (AUD)",
              f"\nTotal cost:{final_cost:40}", " (AUD)", sep="")


class SilverCustomer(Customer):
    service_fee_rate = 0
    cust_type = 'S'

    def __init__(self, cust_id, cust_name):
        super().__init__(cust_id, cust_name)

    @staticmethod
    def get_service_fee_rate():
        return SilverCustomer.service_fee_rate

    def get_service_fee(self, cost):
        return 0

    def get_discount(self, cost):
        return 0

    def display_info(self):
        print("Customer ID: ", self.cust_id)
        print("Customer Name: ", self.cust_name)
        print("Customer Type: ", self.cust_type)
        print("Service Fee Rate: ", self.get_service_fee_rate(), '\n')

    def print_receipt(self, ordered_item, item_price, item_quantity, total_cost, final_cost, registration=False):
        print(f"{ordered_item.get_name():25}", f"{item_price:20}", " (AUD) x", f"{int(item_quantity):3d}",
              f"\nService fee:{self.get_service_fee(total_cost):39}", " (AUD)", sep="", end="")
        if registration:
            print(f"\nRegistration fee:{100:34}", " (AUD)", sep="", end="")
        print(f"\nTotal cost:{final_cost:40}", " (AUD)", sep="")


class GoldCustomer(Customer):
    service_fee_rate = 0
    discount_rate = 0.08
    cust_type = 'G'

    def __init__(self, cust_id, cust_name):
        super().__init__(cust_id, cust_name)

    @staticmethod
    def get_service_fee_rate():
        return GoldCustomer.service_fee_rate

    def get_service_fee(self, cost):
        return 0

    def get_discount_rate(self):
        return self.discount_rate

    def get_discount(self, cost):
        discount = round(cost * self.discount_rate, 2)
        return discount

    def set_discount(self, set_rate):
        self.discount_rate = set_rate
        return self.discount_rate

    def display_info(self):
        print("Customer ID: ", self.cust_id)
        print("Customer Name: ", self.cust_name)
        print("Customer Type: ", self.cust_type)
        print("Service Fee Rate: ", self.get_service_fee_rate())
        print("Discount Rate: ", self.get_discount_rate(), '\n')

    def print_receipt(self, ordered_item, item_price, item_quantity, total_cost, final_cost, registration=False):
        print(f"{ordered_item.get_name():25}", f"{item_price:20}", " (AUD) x", f"{int(item_quantity):3d}",
              f"\nService fee:{self.get_service_fee(total_cost):39}", " (AUD)", sep="", end="")
        if registration:
            print(f"\nRegistration fee:{300:34}", " (AUD)", sep="", end="")
        print(f"\nDiscount:{self.get_discount(total_cost):42}", " (AUD)", sep="", end="")
        print(f"\nTotal cost:{final_cost:40}", " (AUD)", sep="")


# ____________________________________________________________________________________________________________________ #
# -------------------------------------------------------------------------------------------------------------------- #


class Item:

    def __init__(self, item_id, item_name, item_price):
        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price

    def get_id(self):
        return self.item_id

    def get_name(self):
        return self.item_name

    def get_price(self):
        return self.item_price

    def display_info(self):
        print("Item ID: ", self.item_id)
        print("Item Name: ", self.item_name)
        print("Item Price: ", self.item_price)


class FoodDish(Item):
    item_type = "F"

    def __init__(self, item_id, item_name, item_price):
        super().__init__(item_id, item_name, item_price)

    def get_item_type(self):
        return self.item_type

    def display_info(self):
        print("Item ID: ", self.item_id)
        print("Item Name: ", self.item_name)
        print("Item Price: ", self.item_price)
        print("Item Type: ", self.item_type, '\n')


class Drink(Item):
    item_type = "D"

    def __init__(self, item_id, item_name, item_price):
        super().__init__(item_id, item_name, item_price)

    def get_item_type(self):
        return self.item_type

    def display_info(self):
        print("Item ID: ", self.item_id)
        print("Item Name: ", self.item_name)
        print("Item Price: ", self.item_price)
        print("Item Type: ", self.item_type, '\n')


class Banquet(Item):
    banquet_list = []
    item_type = 'B'

    def __init__(self, item_id, item_name):
        super().__init__(item_id, item_name, 0)

    def get_id(self):
        return self.item_id

    def get_name(self):
        return self.item_name

    def set_banquet_items(self, banquet_list):
        self.banquet_list = banquet_list
        self.set_price()

    def get_banquet_items(self):
        return self.banquet_list

    def set_price(self):
        total_price = 0
        for item in self.banquet_list:
            if item.get_item_type() == 'F':
                total_price += item.get_price()
        self.item_price = total_price

    def get_price(self):
        return self.item_price

    def display_info(self):
        print("Item ID: ", self.item_id)
        print("Item Name: ", self.item_name)
        print("Item Price: ", self.item_price)
        print("Item Type: ", self.item_type)
        for component in self.banquet_list:
            print("Component:", component.get_name())
        print("\n")

# ____________________________________________________________________________________________________________________ #
# -------------------------------------------------------------------------------------------------------------------- #


class Order:

    def __init__(self, customer, item, quantity):
        self.customer = customer
        self.item = item
        self.quantity = quantity

    def compute_cost(self):
        total_cost = self.item.get_price() * self.quantity
        service_fee = self.customer.get_service_fee(total_cost)
        discount = self.customer.get_discount(total_cost)
        return total_cost, service_fee, discount

    def display_order(self):
        print(self.customer.get_name(), self.item.get_name(), self.quantity, sep=', ')


# ____________________________________________________________________________________________________________________ #
# -------------------------------------------------------------------------------------------------------------------- #


class Records:
    cust_list = []
    item_list = []

    def get_cust_list(self):
        return self.cust_list

    def get_item_list(self):
        return self.item_list

    def read_customers(self, filename):
        with open(filename) as f:
            for line in f:
                line_items = line.split(", ")
                elements = []
                for element in line_items:
                    e = element.split(": ")
                    elements.append(e[1])
                # Bronze Customer.
                if elements[1] == 'B':
                    bronze_cust = BronzeCustomer(elements[0], elements[2].replace("\n", ""))
                    self.cust_list.append(bronze_cust)
                # Silver Customer.
                elif elements[1] == 'S':
                    silver_cust = SilverCustomer(elements[0], elements[2].replace("\n", ""))
                    self.cust_list.append(silver_cust)
                # Gold Customer.
                elif elements[1] == 'G':
                    gold_cust = GoldCustomer(elements[0], elements[2].replace("\n", ""))
                    gold_cust.set_discount(float(elements[3]))
                    self.cust_list.append(gold_cust)

    def read_items(self, filename):
        with open(filename) as i:
            for line in i:
                line_items = line.split(",")
                elements = []
                for element in line_items:
                    e = element.split(": ")
                    elements.append(e[1])
                # Food Dish.
                if elements[1] == 'F':
                    food_item = FoodDish(elements[0], elements[2], float(elements[3].replace("\n", "")))
                    self.item_list.append(food_item)
                # Drink.
                elif elements[1] == 'D':
                    drink_item = Drink(elements[0], elements[2], float(elements[3].replace("\n", "")))
                    self.item_list.append(drink_item)
                # Banquet.
                elif elements[1] == 'B':
                    food_count = 0
                    drink_count = 0
                    banquet_items = []
                    components = elements[3].split()
                    for component in components:
                        item = self.find_item(component)
                        banquet_items.append(item)
                        if item.get_item_type() == 'F':
                            food_count += 1
                        elif item.get_item_type() == 'D':
                            drink_count += 1
                    if food_count >= 1 and drink_count >= 1:
                        banquet = Banquet(elements[0], elements[2])
                        banquet.set_banquet_items(banquet_items)
                        self.item_list.append(banquet)
                    else:
                        print(f"Banquet: {elements[0]} is not valid. Banquet requires at least 1 Dish and 1 Drink.")

    def find_customer(self, search):
        for value in self.cust_list:
            if value.get_name() == search or value.get_id() == search:
                return value
        return None

    def find_item(self, search):
        for value in self.item_list:
            if value.get_name() == search or value.get_id() == search:
                return value
        return None

    def display_customers(self):
        for value in self.cust_list:
            value.display_info()

    def display_items(self):
        for value in self.item_list:
            value.display_info()


# ____________________________________________________________________________________________________________________ #
# -------------------------------------------------------------------------------------------------------------------- #


class Operations:
    members = Records()
    menu = Records()

    try:
        members.read_customers("customers.txt")
    except:
        print("\nThe file 'customers.txt' is not available in your local directory")
        quit()
    try:
        menu.read_items("items.txt")
    except:
        print("\nThe file 'items.txt' is not available in your local directory")
        quit()

    option = ""
    id_counter = 100
    while option != '0':

        print("Welcome to the RMIT restaurant ordering system!")
        print("#" * 55)
        print("You can choose from the following options:\n"
              "1: Order a meal\n"
              "2: Display existing customer information\n"
              "3: Display existing item information\n"
              "4: Order Meals via file\n"
              "5: Adjust the service fee rate of all bronze customers\n"
              "6: Adjust the discount rate of a gold customer\n"
              "7: Display all orders\n"
              "0: Exit the program")
        print("#" * 55)
        option = input("Choose one option: ")

        # 1: Order a meal.
        if option == '1':

            cust_name = input("Enter the name of the Customer: \n")
            item_name = input("Enter the Item: \n")
            # Invalid Response Handler for item_name.
            while not menu.find_item(item_name):
                item_name = input("Item Invalid. Please enter a valid item! \n"
                                  "Enter the Item: \n")

            item_quantity = input("Enter the  item quantity: \n")
            # Invalid Response Handler for item_quantity.
            while (not item_quantity.isdecimal()) or int(item_quantity) <= 0:
                item_quantity = input("Quantity Invalid. Please enter a valid quantity! \n"
                                      "Enter the  item quantity: \n")

            registration_fee = 0

            # Validate New Members [i.e. Members not in Record.cust_list].
            if not members.find_customer(cust_name):
                id_counter += 1
                rewards_question = input("This is a new customer.Does the customer want to join the rewards program "
                                         "[enter y or n]?\n")
                # Invalid Response Handler "y" or "n".
                while not (rewards_question == 'y' or rewards_question == 'n'):
                    rewards_question = input(
                        "Invalid Response.\nThis is a new customer.Does the customer want to join the rewards program "
                        "[enter y or n]?\n")
                # Valid Response Path for "y" and "n".
                if rewards_question == 'y':
                    member_question = input("What kind of rewards does the customer want?\n")
                    # Invalid Response Handler for "G" and "S".
                    while not (member_question == 'G' or member_question == 'S'):
                        member_question = input("Invalid Response.\nWhat kind of rewards does the customer want?\n")
                    # Valid Response Path for "G" and "S".
                    if member_question == 'G':
                        new_gold_member = GoldCustomer(id_counter, cust_name)
                        members.cust_list.append(new_gold_member)
                        registration_fee = 300
                    elif member_question == 'S':
                        new_silver_member = SilverCustomer(id_counter, cust_name)
                        members.cust_list.append(new_silver_member)
                        registration_fee = 100
                elif rewards_question == 'n':
                    new_bronze_member = BronzeCustomer(id_counter, cust_name)
                    members.cust_list.append(new_bronze_member)

            # Points at the customer making the Order.
            current_cust = members.find_customer(cust_name)

            # Validate if item is in Records.item_list and get_price() to calculate total_cost.
            if menu.find_item(item_name):
                ordered_item = menu.find_item(item_name)
                item_price = ordered_item.get_price()
                total_cost = float(item_price) * float(item_quantity)

                # Final Cost after Fees and Discount.
                final_cost = total_cost + \
                             current_cust.get_service_fee(total_cost) + \
                             registration_fee - \
                             current_cust.get_discount(total_cost)

            # Receipt Header.
            print(f"\nYour Membership Type is: {current_cust.cust_type}")
            print("\n", "*" * 55,
                  f"\nReceipt of Customer {cust_name}\n",
                  "*" * 55, sep="")

            # T0 print_receipt() depending on class.
            if registration_fee > 0:
                registration = True
            else:
                registration = False
            current_cust.print_receipt(ordered_item, item_price, item_quantity, total_cost, final_cost, registration)

        # 2: Display existing customer information.
        if option == '2':
            members.display_customers()

        # 3: Display existing item information.
        if option == '3':
            menu.display_items()

        # 4: Order Meals via file.
        if option == '4':
            orders = []
            order_file = input("Enter the order filename: ")
            try:
                with open(order_file) as k:
                    for line in k:
                        line_items = line.split(", ")
                        elements = []
                        for element in line_items:
                            e = element.split(": ")
                            if e[0] == "customer":
                                customer = members.find_customer(e[1])
                            elif e[0] == "order":
                                order_list = e[1].split()
                                item = menu.find_item(order_list[0])
                                quantity = order_list[1]
                        orders.append(Order(customer, item, quantity))
                print("Successfully placing the orders\n")
            except:
                print("Cannot load the order file. Go back to the main menu.\n")

        # Adjust the service fee rate of all bronze customers.
        if option == '5':
            new_rate = input("Set the new service rate for Bronze Customers: \n")
            BronzeCustomer.set_service_fee_rate(float(new_rate))

        # Adjust the discount rate of a gold customer.
        if option == '6':
            gold_discount_change = input("Enter name or id of gold member:\n")
            gold_member = members.find_customer(gold_discount_change)
            while not gold_member.cust_type == 'G':
                print("Enter a valid gold member")
                gold_discount_change = input("Enter name or id of gold member:\n")
                gold_member = members.find_customer(gold_discount_change)
            new_rate = input(f"Enter the new discount rate for {gold_member.get_name()}:\n")
            gold_member.set_discount(float(new_rate))
            print("Discount rate was changed successfully")

        # Display all orders
        if option == '7':
            print("Displaying all existing orders")
            for order in orders:
                order.display_order()

    # 0: Exit the program
    exit()
