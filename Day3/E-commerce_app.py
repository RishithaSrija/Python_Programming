

def add_prod(value,list):
    list.append(value)
    print(f"Product {value} added to cart.")
def remove_prod(value,list):
    if value in list:
        list.remove(value)
        print(f"{value} removed from the cart.")
    else:
        print(f"{value} is not present to remove from cart.")

def search_prod(value,list):
    if value in list:
        print(f"{value} found in cart.")
    else:
        print(f"{value} not found in the cart.")
def display_prod(list):

    print("Products in the cart: ",list)
def count_prod(list):
    print("Number of products in the cart: ",len(list))
def sort_prod(list):
    list.sort()
    print(list)
def clear_prod(list):
    list.clear()
    print(list)

def e_comm():   
  cart=[]
 
  while True :
   print("Cart Operations:\n 1. Add Product\n 2. Remove Product\n 3. Search Product\n 4. Display Cart\n 5. Count Products\n 6. Sort products \n 7. Clear products \n 8. Exit")
   ch=int(input("Enter choice: "))
   match ch:
    case 1:
          pro=input(("Enter product to add: ")).strip().lower()
          add_prod(pro,cart)

    case 2:
           pro=input("Enter product to remove: ")
           remove_prod(pro,cart)
    case 3:
          pro=input("Enter product to search: ")
          search_prod(pro,cart)
    case 4:
          display_prod(cart)
    case 5:
          count_prod(cart)
    case 6:
          sort_prod(cart)
    case 7:
          clear_prod(cart)
    case 8:
          print("Exiting...")
          break
e_comm()
  

