# Program - 2
# Write a program which extends Program - 1
# Add appropriate class and perform inheritance
# Add the facility of scrapping the raw material product and actual product
# Add appropriate option in the menu for
# scrapping the raw material product
# scrapping the actual product
# Add appropriate methods to scrap the raw material product and actual product

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


class Scrap(Manufacture):
    def __init__(self, ratio, raw_material_qty, actual_product_qty):
        # ratio - no. of raw material to manufacture 1 product
        super().__init__(ratio, raw_material_qty, actual_product_qty)

    def scrap_raw_material(self):
        # returns -
        scrap_raw_material_qty = int(input("Enter qty of raw material to scrap:"))
        if scrap_raw_material_qty > self.raw_material_qty:
            liner()
            print("You can not scrap more than available quantity")
            liner()
        elif scrap_raw_material_qty <= 0:
            liner()
            print("Can not scrap negative no. quantity or zero quantity")
            liner()
        else:
            self.raw_material_qty -= scrap_raw_material_qty
            liner()
            print(scrap_raw_material_qty, "materials scrapped.")
            liner()

    def scrap_actual_product(self):
        # returns -
        scrap_actual_product_qty = int(input("Enter qty of product to scrap:"))
        if scrap_actual_product_qty > self.actual_product_qty:
            liner()
            print("You can not scrap more than available quantity")
            liner()
        elif scrap_actual_product_qty <= 0:
            liner()
            print("Can not scrap negative no. quantity or zero quantity")
            liner()
        else:
            self.actual_product_qty -= scrap_actual_product_qty
            liner()
            print(scrap_actual_product_qty, "products scrapped.")
            liner()


scrap = Scrap(2, 0, 0)

while 1:
    # returns -
    # menu method for menu driven
    print("[1] Purchase Raw Material Product")
    print("[2] Manufacture Actual Product")
    print("[3] Show Raw Material Quantity")
    print("[4] Show Actual Product Quantity")
    print("[5] Scrap the raw material")
    print("[6] Scrap the actual product")
    print("[7] Exit")
    ch = int(input("Select:"))  # ch - choice of no. for menu driven

    if ch == 1:
        scrap.purchase_raw_material()
    elif ch == 2:
        scrap.produce()
    elif ch == 3:
        scrap.display_raw_material_stock()
    elif ch == 4:
        scrap.display_final_product_stock()
    elif ch == 5:
        scrap.scrap_raw_material()
    elif ch == 6:
        scrap.scrap_actual_product()
    elif ch == 7:
        exit()
    else:
        liner()
        print("Invalid choice, please try again.")
        liner()
