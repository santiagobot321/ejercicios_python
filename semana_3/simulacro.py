inventory = [
    {"title": "Book 1", "price": 10.0, "quantity": 100},
    {"title": "Book 2", "price": 15.0, "quantity": 50},
    {"title": "Book 3", "price": 20.0, "quantity": 30},
    {"title": "Book 4", "price": 25.0, "quantity": 10},
    {"title": "Book 5", "price": 30.0, "quantity": 5}
]


def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("\033[31mError: Type a positive number.\033[0m")
        except ValueError:
            print("\033[31mError: Type a valid character.\033[0m")
            
def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("\033[31mError: Type a positive number.\033[0m")
        except ValueError:
            print("\033[31mError: Type a valid character.\033[0m")    

def add_book():
    name_book = str(input("Write the name of the book: "))
    price_book = get_valid_float("Write the price of the book: ")
    quantity = get_valid_int("Write the quantity: ")
    inventory.append({"title": name_book,"price": price_book,"quantity": quantity})
    print(f"{name_book} has been added succesfully")
    print(inventory)

def search_book():
    name_book = str(input("Write the name of the book to search: "))
    
    for i in inventory:
        if name_book == i["title"]:
            print(f"\n\033[33m{i['title']}\033[0m price is: \033[32m${i["price"]}\033[0m and quantity is: \033[31m{i['quantity']}\033[0m")
            break
    else:
        print("Book is no in the list")
        
def update_book():
    name_book = str(input("Write the name of the book to search: "))
    for i in inventory:
        if name_book == i["title"]:
            new_price = get_valid_float("Write the new price of the book: ")
            i['price'] = new_price
    print(f"\n\033[33m{i['title']}\033[0m new price is: \033[32m${i["price"]}\033[0m")
    
def delete_book():
    name_book = str(input("Write the name of the book to search: "))
    for i in inventory:
        if name_book == i["title"]:
            inventory.remove(i)
    print(f"\n\033[32m{i['title']} has been delete succesfully\033[0m")
    print(inventory)

    
print_table = lambda: print("\n".join(f"{i['title']} | {i['price']} | {i['quantity']}" for i in inventory) +
     f"\nTotal price inventory is \033[32m${sum(i['price'] * i['quantity'] for i in inventory)}\033[0m")

    
while True:
    print("""
          1) Add a book to the inventory
          2) Search a book
          3) Update a book in the inventory
          4) Delete a book from the inventory
          5) Calculate total value of the inventory
          6) Exit
          """)
    option = int(input("Choose an option: "))
    match option:
        case 1:
            add_book()
        case 2:
            search_book()
        case 3:
            update_book()
        case 4:
            delete_book()
        case 5:
            print_table()
        case 6:
            print("\033[34mEnd...\033[0m")
            break
        case _:
            print("Choose a correct option between 1 - 6")