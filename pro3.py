# Write a program which is having a class InventoryManagement.
# System should manage the quantity of purchase and sales processes.
# If the system is not having enough quantity during sales, the system should show a warning message “Not enough product quantities to sell”.
# Write appropriate constructor, methods to manage the sales and purchase processes.
# There should be a provision to view the available quantities.
# This should be a menu driven program, which allows to
# Purchase Product
# Sale Product
# View Available Product Quantities
# Exit
# Whenever sales take place, the system should process the quantities and then should show the available quantities.

def liner():
    # for line
    # returns -
    print("------------------------------")


class InventoryManagement:
    def __init__(self):
        initial_product_qty = int(input("Enter initial product quantity:"))  # get initial product qty from user
        self.product_qty = initial_product_qty

    def purchase_product(self):
        # return -
        purchase_product_qty = int(input("Enter product qty to purchase:"))
        if purchase_product_qty <= 0:
            liner()
            print("You can not purchase negative no. or zero product.")
            liner()
        else:
            self.product_qty += purchase_product_qty
            liner()
            print(purchase_product_qty, "products purchased.")
            liner()

    def sale_product(self):
        # return -
        sale_product_qty = int(input("Enter product qty to sale:"))
        if sale_product_qty <= 0:
            liner()
            print("You can not sale negative no. or zero product.")
            liner()
        elif sale_product_qty > self.product_qty:
            liner()
            print("Not enough product quantities to sell.")
            liner()
        else:
            self.product_qty -= sale_product_qty
            liner()
            print(sale_product_qty, "products sold.")
            liner()

    def view_product_qty(self):
        # return -
        liner()
        print("Available product quantity:", self.product_qty)
        liner()


im = InventoryManagement()

while 1:
    # return -
    print("[1] Purchase product")
    print("[2] Sale product")
    print("[3] View product qty")
    print("[4] Exit")
    ch = int(input("Select:"))  # ch - choice no. form given list
    if ch == 1:
        im.purchase_product()
    elif ch == 2:
        im.sale_product()
    elif ch == 3:
        im.view_product_qty()
    elif ch == 4:
        exit()
    else:
        liner()
        print("Invalid choice, please try again.")
        liner()
