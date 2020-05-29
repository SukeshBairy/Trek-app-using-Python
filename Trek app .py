from tabulate import tabulate
from main import *

customer_details = dict()
#total_me = 30


# To check User's email ID.
def valid_email_ID(email_id):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex, email_id)):
        print("Valid Email")
    else:
        print("Invalid Email")

# Homescreen
print("-" * 30)
print("WELCOME TO WONDER ADVENTURES")
print("-" * 30)
while True:
    choice = int(input("Where do you want to visit?\n\
						1.Upcoming_Treks\n\
						2.Himachal_Treks\n\
						3.Change of number of seats\n\
						4.Contact us\n\
						5.Show Status\n\
						6.Payment\n\
						7.EXIT\n-->"))
    if choice == 1:
        sub_choice = int(input("Which place are you looking for?\n\
							  1.Karnataka\n\
							  2.Tamil Nadu\n\
							  3.Kerala\n\
							  4.Maharashtra\n\
							  5.EXIT\n-->"))
        if sub_choice == 1:
            print(tabulate(Karnataka, headers_karnataka_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1,2,3,4,5,6)\n-->"))
                place_name -= 1
                for i, j in enumerate(kar):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        valid_email_ID(email_id)
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (kar[j])
                        total_cost = cost * number_of_seats
                        t = Trek(name, email_id, number_of_seats,
                                 place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name, place, total_cost, number_of_seats)
            elif yes_no == "n":
                print("Look for another place maybe :D")
                pass
        elif sub_choice == 2:
            print(tabulate(Tamil_Nadu, headers_tamilnadu_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1,2,3)\n-->"))
                place_name -= 1
                for i, j in enumerate(tn):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        valid_email_ID(email_id)
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (tn[j])
                        total_cost = cost * number_of_seats
                        t = Trek(name, email_id, number_of_seats,
                                 place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name, place, total_cost, number_of_seats)
            elif yes_no == "n":
                print("Look for another place maybe :D")
                pass
        elif sub_choice == 3:
            print(tabulate(Kerala, headers_kerala_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1,2,3)\n-->"))
                place_name -= 1
                for i, j in enumerate(ker):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        valid_email_ID(email_id)
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (ker[j])
                        total_cost = cost * number_of_seats
                        t = Trek(name, email_id, number_of_seats,
                                 place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name, place, total_cost, number_of_seats)
            elif yes_no == "n":
                print("Look for another place maybe :D")
                pass
        elif sub_choice == 4:
            print(tabulate(Maharashtra, headers_maharashtra_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1,2,3)\n-->"))
                place_name -= 1
                for i, j in enumerate(mah):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        valid_email_ID(email_id)
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (mah[j])
                        total_cost = cost * number_of_seats
                        t = Trek(name, email_id, number_of_seats,
                                 place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name, place, total_cost, number_of_seats)
            elif yes_no == "n":
                print("Look for another place maybe :D")
                pass
        else:
            pass
    elif choice == 2:
        sub_choice = int(input("Which place are you looking for?\n\
							  1.Himachal_Pradesh,aka The Apple State\n\
							  2.Sikkim\n\
							  3.Uttarkhand, its natural beauty of the Himalayas, the Bhabhar and the Terai grasslands and savannas.\n\
							  4.EXIT\n-->"))
        if sub_choice == 1:
            print(tabulate(Himachal_Pradesh,
                           headers_himachalpradesh_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1,2,3)\n-->"))
                place_name -= 1
                for i, j in enumerate(h_p):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        valid_email_ID(email_id)
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (h_p[j])
                        total_cost = cost * number_of_seats
                        t = Trek(name, email_id, number_of_seats,
                                 place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name, place, total_cost, number_of_seats)
            elif yes_no == "n":
                print("Look for another place maybe :D")
                pass
        elif sub_choice == 2:
            print(tabulate(Sikkim, headers_sikkim_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1)\n-->"))
                place_name -= 1
                for i, j in enumerate(si):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        valid_email_ID(email_id)
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (si[j])
                        total_cost = cost * number_of_seats
                        t = Trek(name, email_id, number_of_seats,
                                 place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name, place, total_cost, number_of_seats)
            elif yes_no == "n":
                print("Look for another place maybe :D")
                pass

        elif sub_choice == 3:
            print(tabulate(Uttarkhand, headers_uttarkhand_treks, tablefmt="orgtbl"))
            yes_no = input("Do you want to book the tickets? (y/n)\n-->")
            if yes_no == "y":
                place_name = int(
                    input("Which place are you looking for?(1,2,3)\n-->"))
                place_name -= 1
                for i, j in enumerate(ut):
                    if place_name == i:
                        name = input("Enter your name:")
                        email_id = input("Enter your email ID:")
                        valid_email_ID(email_id)
                        number_of_seats = int(
                            input("How many seats you want to book?\n--> "))
                        place = j
                        cost = (ut[j])
                        total_cost = cost * number_of_seats
                        t = Trek(name, email_id, number_of_seats,
                                 place, total_cost)
                        customer_details[email_id] = t
                        t.congrats(name, place, total_cost, number_of_seats)
            elif yes_no == "n":
                print("Look for another place maybe :D")
                pass

        else:
            pass
    elif choice == 3:
        i = input("Enter your email ID:")
        if i in customer_details.keys():
            add_remove = input(
                "Do you want to add more seats(add) or remove seats(remove)?\n--> ")
            if add_remove == 'add':
                changed_seats = int(
                    input("How many new seats you want to book?\n-->"))
                cost = t.total_cost // t.number_of_seats
                t.add_seats(changed_seats, cost)
                print(f"Total number of seat bookings you have booked is {t.number_of_seats}")
                t.congrats(t.name, t.place, t.total_cost, t.number_of_seats)
            elif add_remove == 'remove':
                changed_seats = int(
                    input("How many seats do you want to remove?\n--> "))
                cost = t.total_cost // t.number_of_seats
                t.remove_seats(changed_seats, cost)
                print(f"Total number of seat bookings you have booked is {t.number_of_seats}")
                t.congrats(t.name, t.place, t.total_cost, t.number_of_seats)
        else:
            print("Email ID not found . Please try another ID.")
            pass
    elif choice == 4:
        print(tabulate(tables_info, headers_info, tablefmt="orgtbl"))

    elif choice == 5:
        email = input("Enter your email ID:")
        if email in customer_details.keys():
            table = [[t.name, t.place, t.number_of_seats, t.total_cost]]
            header = ["Name", "Place", "Seats", "Cost"]
            print(tabulate(table, header, tablefmt="orgtbl"))
    elif choice == 6:
        email_id = input("Enter your email_id:")
        if email_id == t.email_id:
            print(f"The amount to be paid is {t.total_cost}")
            no_yes = input("Do you want to proceed to pay? (y/n):")
            if no_yes == 'y':
                t.payment()
            else:
                print("It's lot easier and faster to pay this way :'(  ")
    else:
        print("THANK YOU.VISIT AGAIN.")
        break
