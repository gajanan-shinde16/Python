class Product:
    count = 0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        # self.count += 1 (it will create new instance attr cllled count and will assign val of count + 1)
        Product.count += 1 # Assignment always writes to the instance (unless you explicitly use the class name).
    
    @staticmethod
    def calc_disc(price,disc):
        print(f"Discount is : {price - price * disc/100}")

p1 = Product("Phone" , 30000)
p2 = Product("Laptop" , 60000)
p3 = Product("Keyboard" , 1000)

print(Product.count)
p1.calc_disc(p1.price , 20)