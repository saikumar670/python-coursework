seats={
    "u1":{'price':1029,'booking_status':true}  
    "u2":{'price':1029,'booking_status':false}
    "l1":{'price':2029,'booking_status':true}
    "l2":{'price':2029,'booking_status':false}
}
for i in seats:
    if seats[i]['booking_status']:
        print(f'***{1}***')
    else:
        print(f'{i}-{seats[i]["price"]}')
seatno=input("enter seat number:"):.upper()
if seatno in seats:
    if seats[seatno]{'booking_status':true}
    print(f'seat {seatno} is already booked')
else:
        print(f'seat {seatno} is available for booking at price {seats[seatno]["price"]}')
