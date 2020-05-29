import time
import random
import re
import pyotp


class Trek:
        
    # Creating an instance of a class.
    def __init__(self, name, email_id, number_of_seats, place, total_cost):
        self.name = name
        self.email_id = email_id
        self.number_of_seats = number_of_seats
        self.place = place
        self.total_cost = total_cost
    
    # To update the number of seats as per user's requirements.
    def add_seats(self, changed_seats, cost):
        self.number_of_seats = self.number_of_seats + changed_seats
        self.total_cost = cost * self.number_of_seats

    def remove_seats(self, changed_seats, cost):
        self.number_of_seats = self.number_of_seats - changed_seats
        self.total_cost = cost * self.number_of_seats

    
    # Confirmation of ticket booking.
    def congrats(self, name, place, total_cost, number_of_seats):
        print(f" Hey {self.name}, your booking to {self.place} has been allotted.\nThe total cost is  ₹{self.total_cost}.Total number of seats you have allotted is {self.number_of_seats}.\n To confirm the booking,kindly do the payment.\nMore details will be provided to your Email ID.")

     
    
    # Payment 
    def payment(self):
        acc_no = input("acc no:")
        cvv = input("cvv:")
        totp = pyotp.TOTP('base32secret3232', interval=60)
        OTP = totp.now()
        print("OTP code:", OTP)
        otp = input("Enter the otp:")
        totp.verify(otp)
        if totp.verify(otp) is True:
            print("The OTP provided is valid.your payment is confirmed.")
            print("Thank You for choosing Wonder Adventures!")
            print("Thank You.Visit Again.")
        else:
            print("The OTP provided is Invalid.")


# Data kept in Dictionary to simplify the access of data.
# Data kept in List for the tabulate function to display.
kar = {"Kodachadri Trek": 4150, "Tadiandamol Trek, Coorg": 3954, "Kudremukh Trek": 4878,
       "Kumara Parvatha Trek": 4014, "Dudhsagar Waterfalls Trek": 5900, "Gokarna Beach Trek & Camping": 4539}
Karnataka = [["Kodachadri Trek", "4150"], ["Tadiandamol Trek, Coorg", "3954"], ["Kudremukh Trek", "4878"],
             ["Kumara Parvatha Trek", "4014"], ["Dudhsagar Waterfalls Trek", "5900"], ["Gokarna Beach Trek & Camping", "4539"]]
headers_karnataka_treks = ["Places", "Price"]


Maharashtra = [["Trek to Plus Valley, Tamhini Ghat", "2500"], [
    "Trek to Alang, Madan and Kulang ( AMK )", "3600"], ["Trek to Sandhan Valley", "2500"]]
mah = {"Trek to Plus Valley, Tamhini Ghat": 2500,
       "Trek to Alang, Madan and Kulang ( AMK )": 3600, "Trek to Sandhan Valley": 2500}
headers_maharashtra_treks = ["Places", "Price"]


Tamil_Nadu = [["Kotagiri Trek, Ooty", "4940"], ["Trek to Canopy Hills, Vattakanal",
                                                "5706"], ["Top Station Trek - Munnar", "4428"]]
tn = {"Kotagiri Trek, Ooty": 4940, "Trek to Canopy Hills, Vattakanal":
      5706, "Top Station Trek - Munnar": 4428}

headers_tamilnadu_treks = ["Places", "Price}


ker = {"Paithalmala Trek, Kerala": 3953, "Trek to Banasura Hills, Wayanad":
       3600, "Night Trekking & Camping at Wayanad": 4600}
Kerala = [["Paithalmala Trek, Kerala", "3953"], ["Trek to Banasura Hills, Wayanad",
                                                 "3600"], ["Night Trekking & Camping at Wayanad", "4600"]]
headers_kerala_treks = ["Places", "Price"]


tables_info = [["Enquiry Name", "Sukesh Bairy"], ["Phone Number", "9686853769"], [
    "Email_id", "sukeshbairy@gmail.com"], ["Address", "Puttenahalli, Phase 7, J. P. Nagar, Bengaluru, Karnataka,560078"]]
headers_info = ["_Type_", "_Info_"]


Himachal_Pradesh = [["Trek to Malana - Chandrakhani Pass, Himachal Pradesh", "8900"], [
    "Children's Adventure Camp at Manali - Himalayas", "23250"], ["Trek to Hampta Pass and Chandratal - Himalayas", "10600"]]
h_p = {"Trek to Malana - Chandrakhani Pass, Himachal Pradesh": 8900,
       "Children's Adventure Camp at Manali - Himalayas": 23250, "Trek to Hampta Pass and Chandratal - Himalayas": 10600}
headers_himachalpradesh_treks = ["Places", "Price"]

Sikkim = [["Trek to Goechala, Sikkim", "15200"]]
si = {"Trek to Goechala, Sikkim": 15200}
headers_sikkim_treks = ["Places", "Price"]

Uttarkhand = [["Brahmatal Trek", "8800"], [
    "Pindari Glacier Trek", "13400"], ["Kedarkantha Trek - Himalaya", "8999"]]
ut = {"Brahmatal Trek": 8800,
      "Pindari Glacier Trek": 13400,  "Kedarkantha Trek - Himalaya": 8999}
headers_uttarkhand_treks = ["Places", "Price"]
