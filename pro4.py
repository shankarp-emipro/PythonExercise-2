# Write a program which is having a class InventoryManagement.
# System should manage the quantity of purchase and sales processes.
# Users should be able to purchase the product with different prices in the same object of Inventory Management - Use a dictionary, maintain a numerical index and store product price and product quantity against it.
# Whenever the product is sold, it will start deducting the product qty whichever entry is done first in the dictionary, so qty will be deducted as FIFO (First In First Out).
# Whenever product qty is deducted change the price of that index.
# Formula -
# Once the qty from each purchase is used make sure, it is not used again, so update the dictionary accordingly.
# Program should be able to handle the valuation.
# Formula for valuation - sum of price * qty / sum of total qty.
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


def compute_subtotal(product_qty, unit_price):
    # returns - subtotal by multiplying product_qty and unit_price
    return product_qty * unit_price


class InventoryManagement:
    def __init__(self):
        # qty_and_subtotal - is a dictionary to store product qty and and its subtotal
        self.qty_and_subtotal = {}
        initial_product_qty = int(input("Enter initial product quantity:"))  # get initial product qty from user
        if initial_product_qty > 0:
            unit_price = float(input("Enter unit price:"))
            self.qty_and_subtotal = {
                1: {
                    "product_qty": initial_product_qty,
                    "product_subtotal": initial_product_qty * unit_price
                }
            }

    def get_last_product_index(self):
        # returns - last index from dictionary of qty and product
        last_index = 0
        for current_index in self.qty_and_subtotal:
            last_index = current_index
        return last_index

    def get_total_qty_of_product(self):
        # returns - sum of qty of all product
        total_qty_of_product = 0
        for qty_subtotal in self.qty_and_subtotal.values():
            total_qty_of_product += qty_subtotal.get("product_qty")
        return total_qty_of_product

    def get_total_subtotal_of_product(self):
        # returns - sum of subtotal of all products
        total_subtotal_of_product = 0
        for qty_subtotal in self.qty_and_subtotal.values():
            total_subtotal_of_product += qty_subtotal.get("product_subtotal")
        return total_subtotal_of_product

    def purchase_product(self):
        # return -
        product_qty_to_purchase = int(input("Enter product qty to purchase:"))
        unit_price = float(input("Enter unit price:"))
        if product_qty_to_purchase <= 0:
            liner()
            print("You can not purchase negative no. or zero product.")
            liner()
        else:
            self.qty_and_subtotal.update({
                self.get_last_product_index()+1: {
                    "product_qty": product_qty_to_purchase,
                    "product_subtotal": product_qty_to_purchase * unit_price
                }
            })
            liner()
            print(product_qty_to_purchase, "products purchased.")
            liner()

    def delete_record(self, index_to_delete):
        # returns -
        for index in index_to_delete:
            self.qty_and_subtotal.pop(index)

    def update_record(self, index_to_update, updated_qty, updated_subtotal):
        # returns -
        self.qty_and_subtotal.update({
            index_to_update: {
                "product_qty": updated_qty,
                "product_subtotal": updated_subtotal
            }
        })

    def sale_product(self):
        # return -
        index_to_delete = []    # empty list to store indexes to be deleted form qty_product dictionary
        index_to_update = 0     # this will hold the index of a record whose data is to be updated
        updated_qty = None      # this will hold the value which will be used to replace old qty of a particular dictionary
        updated_subtotal = None     # this will hold the value which wil be used to replace old subtotal of a particular dictionary
        sale_product_qty = int(input("Enter product qty to sale:"))
        sale_product_qty_for_msg = sale_product_qty
        if sale_product_qty <= 0:
            # user should get warning if entered value is either zero or negative
            liner()
            print("You can not sale negative no. or zero product.")
            liner()
        elif sale_product_qty <= self.get_total_qty_of_product():
            # user should get warning message if entered value is grater than available qty
            for index, qty_subtotal in self.qty_and_subtotal.items():
                if sale_product_qty > 0:
                    # above condition is to stop the loop to avoid scanning whole dictionary unnecessarily
                    if qty_subtotal.get("product_qty") - sale_product_qty <= 0:
                        # above condition checks whether sale product qty is enough or not and does the task accordingly
                        index_to_delete.append(index)   # notes down the value to be deleted
                        sale_product_qty -= qty_subtotal.get("product_qty")
                    else:
                        # if qty is more than sale product qty, below code is executed.
                        index_to_update = index
                        # below line is for getting unit price to calculate updated subtotal
                        unit_price = qty_subtotal.get("product_subtotal") / qty_subtotal.get("product_qty")
                        # updated_qty holds the updated value of quantity
                        updated_qty = qty_subtotal.get("product_qty") - sale_product_qty
                        # updated_subtotal holds the updated value of subtotal
                        updated_subtotal = updated_qty * unit_price
                        # below line is very important because it helps to break the loop running unnecessarily
                        sale_product_qty = 0
            if len(index_to_delete) > 0:
                # below line invokes the method passing the list of indexes to delete the indexes from the dictionary
                self.delete_record(index_to_delete)
            if index_to_update > 0:
                # below line invokes the method to update the required dictionary values
                self.update_record(index_to_update, updated_qty, updated_subtotal)
            liner()
            print(sale_product_qty_for_msg, "products sold.")
            liner()

        else:
            # print warning message
            liner()
            print("Not enough qty available for sale.")
            print("You need to purchase at least {qty} more products to meet the sale.".format(qty=(sale_product_qty - self.get_total_qty_of_product())))
            liner()

    def view_product_qty(self):
        # return -
        liner()
        print("Available product quantity:", self.get_total_qty_of_product())
        print(self.qty_and_subtotal)
        liner()

    def get_valuation(self):
        # returns -
        liner()
        print("Valuation: {valuation:.2f}".format(valuation=(self.get_total_subtotal_of_product() / self.get_total_qty_of_product())))
        liner()


im = InventoryManagement()

while 1:
    # return -
    print("[1] Purchase product")
    print("[2] Sale product")
    print("[3] View product qty")
    print("[4] Valuation")
    print("[5] Exit")
    ch = int(input("Select:"))      # ch - choice no. form given list
    if ch == 1:
        im.purchase_product()
    elif ch == 2:
        im.sale_product()
    elif ch == 3:
        im.view_product_qty()
    elif ch == 4:
        im.get_valuation()
    elif ch == 5:
        exit()
    else:
        liner()
        print("Invalid choice, please try again.")
        liner()
