products = []
def read_data():
    f = open("session8\list foroosh.txt", "r")
    for i in f :
       product = i.split(",")
       dic = {"id":product[0], "name": product[1],"price": product[2], "cout":int(product[3])}
       products.append(dic)

def show_menu():
    print("1- add")
    print("2-delete")
    print("3-search")
    print("4-buy")
    print("5-edit")
    print("6-exit")
    print("7- show products")

def add():
    id = input("enter id: ")
    name = input("enter name: ")
    price = input("enter price: ")
    cout = input("enter cout: ")
    dic = {"id": id, "name": name, "price": price, "cout": cout}

def delete():
    while True:
        welcome = int(input("welcome! 1 for delete product and 2 for back:"))
        if welcome == 1:
            key = input("enter product id or name: ")
            for product in products:
                key == product["id"] or key == product["name"]
                print(product)
                insure = int(input(" 1 for delete and 2 for back: "))
                if insure == 1:
                    x = products.remove(product)
                    print("product removed! ")
                    break
                if insure ==2:
                    print("back")
        if welcome == 2:
            break

def search():
    key = input("enter your key: ")
    for product in products:
        if key == product["id"] or key == product["name"]:
            print(product)
            break
    else:
        print("not found!! ")

def buy():
    key = input("enter product name or id: ")
    for product in products:
        if key == product["id"] or key == product["name"]:
            print(product)
            while True:
                count = int(input("enter count : "))
                if count <= product["cout"]:
                    print(" product added successfully!!")
                    new_count = product["cout"] - count
                    print("Remaining quantity in stock :", new_count)
                else:
                    print(" sorry! This number of products is not available in stock!! ")
            else:
                print(" product not found!! ")

def edit():
    user_edit = input("enter product id or name: ")
    for product in products:
        if user_edit == product["id"] or user_edit == product["name"]:
            print(product)
            insure = int(input("do you want to edit this product? 1. yes    2. no and back"))
            if insure == 1:
                question = int(input("1. edit id   2. edit name   3. edit price   4. edit count: "))
                if question == 1:
                    new_id = int(input("enter new id:"))
                    product["id"] = new_id
                    print(product)
                    print("sucessfully changed! ")
                    break

                if question == 2:
                    new_name = input("enter new name:")
                    product["name"] = new_name
                    print(product)
                    print("sucessfully changed! ")
                    break
                    
                if question== 3:
                    new_price = int(input("enter new price:"))
                    product["price"] = new_price
                    print(product)
                    print("sucessfully changed! ")
                    break

                if question == 4:
                    new_count = int(input("enter new count: "))
                    product["cout"] = new_count
                    print(product)
                    print("sucessfully changed! ")
                    break
                else:
                    print("invalid!") 

            if insure == 2:
                print("back")
                break
        else :
            print("product not found! ")  

def exit():
    pass

def show_products():
    print("id \t name \t price \t cout")
    for product in products:
        print(product["id"], "\t", product["name"], "\t" , product["price"], "\t" , product["cout"])
        # print(f'{}')

read_data()
show_menu()

user_chice = int(input("enter your choice: "))
if user_chice == 1:
    add()

elif user_chice == 2:
    delete()

elif user_chice ==3:
    search()

elif user_chice == 4:
    buy()

elif user_chice == 5:
    edit()

elif user_chice ==6:
    exit()

elif user_chice == 7:
    show_products()