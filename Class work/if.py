# seat={
#     'l1':true,
#     'l2':false,
#     'l3':true,
#     'l4':true,
#     'l5':false,
#     'u1':false,
#     'u2':true,
#     'u3':false,
#     'u4':true,
#     'u5':true,

# }
# seatno=input("enter the seat no to check its availability:").upper()
# 
#  seatno in seats:
# if seats[seatno]:
# print("already booked.try with another number")
# else:
#    print("seat is available")












data={
    'watches':{'discount':10,'brand':['titan','fastrack']},
    'facewash':{'discount':20,'brand':['mamaearth']},
    'tops':{'discount':30,'brand':['max','netplay']},
    'jeans':{'discount':40,'brand':['highlander','holand']},
}
print(data.keys())
pro=input("enter the cat: ")
if pro in data:
        print(f'{data[pro]["discount"]}% discount is going on for this brands:{data[ pro]}')
else:
         print(f"product is out of stock.please check with our other products:{data}")











movies={
        'animal':{'kids':'false'},
        'avengers':{'kids':'true'},
        'superman':{'kids':'true'}
}
print('welcome to prime'.center(30,'='))
movie=input("enter the movie: ").title()
if movie in movies:
        if movies[movie]['kids']:
                print(f"good selection.you can watch with your family\n{movie}......")
        else:print(f"adult movie.kids are not allowed to watch{movie}......")