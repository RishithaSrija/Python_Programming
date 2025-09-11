# def apply_discount(pr,dis_per):
#     dis=(float) (pr-(dis_per*pr)/100)
#     return dis
# def add_gst(pr,gst_per=18):
#     pr=(float)(pr+(pr*gst_per/100))
#     return pr
# def generate_invoice(cart,dis_per=0,gst_per=18):
#     subtotal=0
#     print("------ INVOICE ------")
#     for k,v in cart.items():
#         print(f"{k}         :  ₹{v}")
#         subtotal=sum(values)

#     print(" ---------------------  ---------------------")
#     print("Subtotal:    {subtotal:.2f}")
#     print("After {dis_per}% discount:   ",apply_discount(pr,dis_per))
#     print("After {gst_per}% discount:   ",add_gst(pr,gst_per))


def apply_discount(pr, dis_per):
    return pr - (dis_per * pr / 100)

def add_gst(pr, gst_per=18):
    return pr + (pr * gst_per / 100)

def generate_invoice(cart, dis_per=0, gst_per=18):
    subtotal = sum(cart.values())
    print("\n------ INVOICE ------")
    for product, price in cart.items():
        print(f"{product:<15}: ₹{price:.2f}")
        subtotal += price

    print("\n-----------------------------")
    print(f"Subtotal: ₹{subtotal:.2f}")
    discounted = apply_discount(subtotal, dis_per)
    print(f"After {dis_per}% discount: ₹{discounted:.2f}")
    final_total = add_gst(discounted, gst_per)
    print(f"After {gst_per}% GST: ₹{final_total:.2f}")
    print("-----------------------------")
    print("Thank you for shopping with us!")
