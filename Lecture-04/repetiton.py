keep_going ="y"

while keep_going == "y" :
    sales = float(input("Enter sales amount: "))
    comm_rate  = float(input("Enter commission rate: "))
    commision = sales * comm_rate
    print('The commisione is $', format(commision, ".2f"))
    keep_going = input('Do you want to calculate another'+ \
                            " commission(Emter y for yes):")