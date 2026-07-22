keep_going ="y"

while keep_going == "y" :
    price = float(input("Enter the item's wholesale cost: "))
    keep_going = input('Do you have another item?'+ \
                            " (Emter y for yes):")
    retail_price = price*2.5
    print('The retail price is $', format(retail_price, ".2f"))
   