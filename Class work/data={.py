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