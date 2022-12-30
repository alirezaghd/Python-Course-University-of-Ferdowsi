def read_from_db():
    try:
        products=[]
        fl=open('Store/database.csv','r')
        big_text=fl.read()
        products_list=big_text.split('\n')
        for i in range(len(products_list)):
            info=products_list[i].split(',')
            products.append( {'id':info[0],'name':info[1],'price':info[2],'count':info[3] })
    except Exception as e:
        print(e)
        products=[]

    return products

x=read_from_db()



def show_menu():
    print("Wrlcome to store")
    print("------------------")

    print('1-Add new product ')
    print('2-Search ')
    print('3-Edit ')
    print('4-Buy ')
    print('5-Remove ')
    print('6-Show all')
    print('7-Exit ')
    print("------------------")


def add():
    id = input('enter id: ')
    for key in x:
        if id == key['id']:
            print('this id is not availble')
            return
    name = input('enter name: ')
    price = input('enter price: ')
    count = input('enter count: ')
    x.append({'id': id, 'name': name, 'price': price, 'count': count})

  


def Search():
    user_input = input('Enter a id or name to search = ')
    for product in x:
        if product['id'] == user_input or product['name'] == user_input:
            print(product)
            break
    else:
        print('you product not found')




def Edit():
    show_all()
    editor = input("Enter your ID: ")

    for product in x:
        if product["id"] == editor or product["name"] == editor:
            print("sucsess")
        u_product = input("Which Part To Edit? ")
        if u_product == "id":
            id = int(input("Enter New Id: "))
            product["id"] = id
            break
        elif u_product == "name":
            name = input("Enter New Name: ")
            product["name"] = name
            break
        elif u_product == "price":
            price = input("Enter New Price: ")
            product["price"] = price
            break
        elif u_product == "count":
            count = input("Enter New Count: ")
            product["count"] = count
            break
    else:
        print("not found  this item")

def Remove():
    show_all()
    remove_item = input("Enter your ID: ")
    for product in x:
        if product["id"] == remove_item or product["name"] == remove_item:
            x.remove(product)
            print("removed")
            break
    else:
        print("not found")

def buy():
    buy_list = []
    price = int()


    while True:
        user_list = input('Do you want to continue buy ? ("y" or "n"(See shoping cart)): ')
        if user_list == 'y':
            print('Choose your product ')
            for product in x:
                print(product)
            user_input = input('enter product = ')
            for product in x:
                if product['id'] == user_input or product['name'] == user_input:
                    print(product)
                    break
            else:
                print('This product is out of stock')
                exit()
            print('We have', product['count'])
            number_user = int(input("How many do you need?"))
            c = int(product['count'])
            if number_user > c:
                print('The number of you want is out of stock please try again')
            elif number_user <= c:
                buy_list.append({'id': product['id'], 'name': product['name'], 'price': product['price'],
                                'count': number_user})
                count = int(product['count']) - number_user
                x.remove(product)
                x.append({'id': product['id'], 'name': product['name'], 'price': product['price'], 'count': str(count)})
                price += int(number_user) * int(product['price'])

        elif user_list == 'n':
            print(buy_list)
            print('Your Total cost is: ', price)
            break

        else:
            print('your input is not correct')
    
def show_all():
    for product in x:
        print(product)

while True:
    show_menu()
    Choise=int(input("Enter your activity code :"))

    if Choise==1:
        add()

    elif Choise==2:
        Search()

    elif Choise==3:
        Edit()

    elif Choise==4:
        buy()

    elif Choise==5:
        Remove()

    elif Choise==6:
        show_all()

    elif Choise == 7:
        Choise = input('Would you like to save your change ? (y or n): ')
        if Choise == 'y':
            f1 = open("Store/database.csv", "w")
            for product in x:
                f1.write(str(product['id']+','+product['name']+','+product['price']+','+product['count']))
                f1.write('\n')

            exit()