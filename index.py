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




    

                
                    


#a = Auth()
#a.register()
#a.Login()
p=Producthandling()
#p.add_product()
#p.decrease_quantity()
#p.delete_product()
#p.update_product()
p.view_products()