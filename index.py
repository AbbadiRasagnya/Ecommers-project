class User:
    def __init__(self, id, name, password, is_admin):
        self.id=id
        self.name=name
        self.password=password
        self.is_admin=is_admin
    def user_details(self):
        return f"{self.id},{self.name},{self.password},{self.is_admin}\n"
class Auth:
    def register(self):
        id=input("Enter Your Id: ")
        name=input("Enter Your Name: ")
        password=input("Enter Your Password: ")
        is_admin=input("Enter Yes or No: ")
        new_user=User(id,name,password,is_admin)

        #with open("users.txt","a") as file:
            #file.write(new_user.user_details())
        with open("users.txt","r") as file:
            lines=file.readlines()
            is_Found=False
            for line in lines:
                details=line.strip().split(",")
                if details[1]==name:
                    is_Found=True
        if is_Found:
            print("User already Exist Tryy another Name")
        else:
            with open("users.txt","a") as file:
                file.write(new_user.user_details())
    def Login(self):
        name=input("Enter Your Name: ")
        password=input("Enter your Password")
        user_id=None
        with open("users.txt","r") as file:
            lines=file.readlines()
            is_Found=False
            for line in lines:
                details=line.strip().split(",")
                if details[1]==name:
                    if details[2]==password:
                        is_Found=True
        if is_Found:
            print("Login Successful!")
            return user_id
        else:
            print("Invalid Crediantials")

class Product:
    def __init__(self,id,product_name,price,quantity):
        self.id=id
        self.product_name=product_name
        self.price=price
        self.quantity=quantity
    def product_details(self):
        return f"{self.id},{self.product_name},{self.price},{self.quantity}\n"
class Producthandling:
    def add_product(self):
        id=input("Enter Your id: ")
        product_name=input("Enter product_name: ")
        price=input("Enter item price: ")
        quantity=input("Enter no of items: ")

        new_product=Product(id,product_name,price,quantity)
        #with open("products.txt","a") as file:
            #file.write(new_product.product_details())
        with open("products.txt","r") as file:
            lines=file.readlines()
            is_Found=False
            for line in lines:
                details=line.strip().split(',')
                if details[1]==product_name:
                    is_Found=True
                    break
            if is_Found:
                with open("products.txt","w") as file:
                    for line in lines:
                        details = line.strip().split(",")
                        if details[1]==product_name:
                            q = int(details[3])+int(quantity)
                            file.write(f"{details[0]},{details[1]},{details[2]},{q}\n")
                        else:
                            file.write(line)
            else:
                with open("products.txt","a") as file:
                    file.write(new_product.product_details())
    def decrease_quantity(self):
        product_name=input("Enter a product_name: ")
        with open("products.txt","r") as file:
            lines=file.readlines()
            is_Found=False
            for line in lines:
                details=line.strip().split(",")
                if details[1]==product_name:
                    is_Found=True
        
            if is_Found:
                with open("products.txt","w") as file:
                    for line in lines:
                        details=line.strip().split(",")
                        if details[1]==product_name:
                            if int(details[3])>1:
                                q=int(details[3])-1
                                file.write(f"{details[0]},{details[1]},{details[2]},{q}\n")
                        else:
                            file.write(line)
            else:
                print("Product not Found!")
    def delete_product(self):
        id=input("Enter a product id: ")
        with open("products.txt","r") as file:
            lines=file.readlines()
            is_Found=False
            for line in lines:
                details=line.strip().split(",")
                if details[0]==id:
                    is_Found=True
            if is_Found:
                with open("products.txt","w") as file:
                    for line in lines:
                        detalis=line.strip().split(",")
                        if detalis[0]!=id:
                            file.write(line)
            else:
                print("product not find!")
    def update_product(self):
        id=input("Enter product id to be updated: ")
        with open("products.txt","r") as file:
            lines=file.readlines()
            is_Found=False
            for line in lines:
                details=line.strip().split(",")
                if details[0]==id:
                    is_Found=True
            if is_Found:
                with open("products.txt","w") as file:
                    for line in lines:
                        details=line.strip().split(",")
                        if details[0]==id:
                            product_name=input(f"change {details[1]} to:")
                            price=input(f"change {details[2]} to:")
                            quantity=input(f"change {details[3]} to:")
                            file.write(f"{details[0]},{product_name},{price},{quantity}\n")
                        else:
                            file.write(line)   
            else:
                print("product not found")

    def view_products(self):
        with open("products.txt","r") as file:
            lines=file.readlines()
            
            print("-------------------------")
            for line in lines:
                details=line.strip().split(",")
                print(f"|{details[0]+(" "*(5-len(details[0])))} | {details[1]+(" "*(10-len(details[1])))}|") | {details[2]+(" "*(10-len(details[2])))} | {details[3]+(" "*(10-len(details[3])))}|")
class Cart(Producthandling):
    def _init_(self,userid):
        self.userid = userid 

    def add_to_cart(self):
        product_name = input("Enter product name: ")

        with open("products.txt","r") as file:
            lines = file.readlines()

        is_found = False
        new_product = None
        with open("products.txt","w") as file:
            for line in lines:
                details = line.strip().split(",")
                if details[1]==product_name and int(details[-1])>0:
                    q = int(details[-1])-1
                    new_product = details
                    file.write(f"{details[0]},{details[1]},{details[2]},{q}\n")
                    is_found = True 

                else:
                    file.write(line)

        if is_found:
            with open("cart.txt","r") as file:
                lines = file.readlines()

            is_found = False
            with open("cart.txt","w") as file:
                for line in lines:
                    details = line.strip().split(",")
                    if details[0]==self.userid and details[2]==product_name:
                        q = int(details[-1])+1
                        is_found = True
                        file.write(f"{details[0]},{details[1]},{details[2]},{details[3]},{q}\n")
                    else:
                        file.write(line)

            if is_found==False:
                new_product.insert(0,self.userid)
                new_product[-1]="1"
                with open("cart.txt","a") as file:
                    file.write(",".join(new_product)+"\n")
        else:
            print("Out of stock!")


    def decerease_product_quantity(self):
        product_name = input("Enter product name: ")

        with open("cart.txt","r") as file:
            lines = file.readlines()

        is_found = False
        with open("cart.txt","w") as file:
            for line in lines:
                details = line.strip().split(",")
                if details[2]==product_name and self.userid==details[0]:
                    if int(details[-1])>1:
                        q = int(details[-1])-1
                        file.write(f"{details[0]},{details[1]},{details[2]},{details[3]},{q}\n")
                    is_found = True 
                else:
                    file.write(line)

        if is_found:
            with open("products.txt","r") as file:
                lines = file.readlines()

            with open("products.txt","w") as file:
                for line in lines:
                    details = line.strip().split(",")
                    if details[1]==product_name:
                        q = int(details[-1])+1
                        file.write(f"{details[0]},{details[1]},{details[2]},{q}\n")
                    else:
                        file.write(line)
        else:
            print("Product not found in the cart.")

    def delete_product_in_cart(self):
        product_name = input("Enter product name: ")

        with open("cart.txt","r") as file:
            lines = file.readlines()

        is_found = False
        with open("cart.txt","w") as file:
            for line in lines:
                details = line.strip().split(",")
                if(details[2]==product_name and details[0]==self.userid):
                    is_found = True 
                else:
                    file.write(line)

                    

        if is_found==False:
            print("Product is not found in the cart")

    def view_cart(self):
        with open("cart.txt","r") as file:
            lines = file.readlines()

        print("-----------------------------------")
        print("|name      | price     | quantity   |")
        print("-----------------------------------")
        total = 0
        for line in lines:
            details = line.strip().split(",")
            if details[0]==self.userid:
                total+=int(details[3])*int(details[-1])
                print(f"|{details[2]+(" "(10-len(details[2])))}| {details[3]+(" "(10-len(details[3])))}| {details[4]+(" "*(10-len(details[4])))} |")

        print("-----------------------------------")
        print(f"|             toatl price: {total}  |")
        print("-----------------------------------")


def user(userId):
    while True:
        print("1) View Products")
        print("2) Add to cart")
        print("3) Decrese product quantity")
        print("4) Delete product in cart")
        print("5) View Cart")
        print("6) Logout")
        cart = Cart(userId)
        opt = input("Choose one option: ")
        if opt=="1":
            cart.view_products()
        elif opt=="2":
            cart.add_to_cart()
        elif opt=="3":
            cart.decerease_product_quantity()
        elif opt=="4":
            cart.delete_product_in_cart()
        elif opt=="5":
            cart.view_cart()
        elif opt=="6":
            break 
        else:
            print("Invalid option.")

def admin():
    while True:
        print("1) Add product")
        print("2) Decrese quantity")
        print("3) Delete product")
        print("4) Update product")
        print("5) View Products")
        print("6) Logout")
        ph = Producthandling()
        opt = input("Choose one option: ")
        if opt=="1":
            ph.add_product()
        elif opt=="2":
            ph.decerease_quantity()
        elif opt=="3":
            ph.delete_product()
        elif opt=="4":
            ph.update_product()
        elif opt=="5":
            ph.view_products()
        elif opt=="6":
            break 
        else:
            print("Invalid option")



def run():
    while True:
        print("1) Register")
        print("2) Login")
        print("3) Exit")
        opt = input("Choose one option: ")
        auth = Auth()
        if opt=="1":
            auth.register()
        elif opt=="2":
            res = auth.login()
            if res[1]=="yes":
                admin()
            else:
                user(res[0])
        elif opt=="3":
            print("Thanks for visiting! Visit again.")
            break
        else:
            print("Inavlid option.")

run()




    

                
                    


#a = Auth()
#a.register()
#a.Login()
p=Producthandling()
#p.add_product()
#p.decrease_quantity()
#p.delete_product()
#p.update_product()
p.view_products()