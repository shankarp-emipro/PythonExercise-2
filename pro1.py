# Program - 1
# Write a program that contains ‘manufacturing’ class which allows product manufacturing.
# It purchases raw material from the market and produces a product.
# One should manage the raw material product to produce the actual product.
# One should manage the ratio of raw material to produce the actual product.
# Example - 2 wheels(raw material) are required to produce 1 bicycle(actual product)
# Take input from user raw material, raw material ratio qty, actual product
# While producing the actual product, if the system doesn’t have enough of its stock of raw material, it should show a warning message as “Not enough raw material available to produce the product, please do the purchase”.
# Program should be menu driven allowing to
# Purchase Raw Material Product
# Manufacture Actual Product
# Show Raw Material Quantity
# Show Actual Product Quantity
# Exit
# Following attributes and method function should be part of the class
# Appropriate constructor to set the values for raw material product, actual product, raw material ratio qty value, raw material qty
# produce() - taking no qty to be produced for actual product as argument
# display_raw_material_stock()
# display_final_product_stock()
# purchase_raw_material() - taking no of qty of raw material to be purchased

def liner():
    # for line
    # returns -
    print("------------------------------")


class Manufacture:
    def __init__(self, ratio, raw_material_qty, actual_product_qty):
        # ratio - no. of raw material to manufacture 1 product
        self.ratio = ratio
        self.raw_material_qty = raw_material_qty
        self.actual_product_qty = actual_product_qty

    def purchase_raw_material(self):
        # returns -
        purchase_raw_material_qty = int(input("Enter no. of qty to purchase:"))
        if purchase_raw_material_qty <= 0:
            liner()
            print("You can not purchase negative no. or zero product")
            liner()
        else:
            self.raw_material_qty += purchase_raw_material_qty
            liner()
            print(purchase_raw_material_qty, "raw materials purchased.")
            liner()

    def produce(self):
        # returns -
        qty_to_produce = int(input("Enter no. of qty to manufacture:"))
        if qty_to_produce <= 0:
            liner()
            print("You can not produce negative no. or zero product")
            liner()
        elif self.raw_material_qty >= self.ratio*qty_to_produce:
            self.actual_product_qty += qty_to_produce
            self.raw_material_qty -= self.ratio*qty_to_produce
            liner()
            print(qty_to_produce, "products manufactured.")
            liner()
        else:
            liner()
            print("Can not manufacture product")
            print("You need to purchase at least {raw_qty} raw material to manufacture {product_qty} product".format(raw_qty=self.ratio*qty_to_produce-self.raw_material_qty, product_qty=qty_to_produce))
            liner()

    def display_raw_material_stock(self):
        # returns -
        liner()
        print("Raw material stock:", self.raw_material_qty)
        liner()

    def display_final_product_stock(self):
        # returns -
        liner()
        print("Actual product qty:", self.actual_product_qty)
        liner()


mf = Manufacture(2, 0, 0)

while 1:
    print("[1] Purchase Raw Material Product")
    print("[2] Manufacture Actual Product")
    print("[3] Show Raw Material Quantity")
    print("[4] Show Actual Product Quantity")
    print("[5] Exit")
    ch = int(input("Select:"))  # ch - choice of no. for menu driven

    if ch == 1:
        mf.purchase_raw_material()
    elif ch == 2:
        mf.produce()
    elif ch == 3:
        mf.display_raw_material_stock()
    elif ch == 4:
        mf.display_final_product_stock()
    elif ch == 5:
        exit()
    else:
        print("Invalid choice, please try again.")
