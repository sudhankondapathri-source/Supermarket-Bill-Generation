import datetime
name = input("Enter your name:")

lists = '''
    Rice          Rs 75/kg
    Sugar         Rs 50/kg
    Salt          Rs 25/kg
    Oil           Rs 175/each
    Panner        Rs 350/kg
    Vermicelli    Rs 70/kg
    Maggi         Rs 99/each
    Colgate       Rs 65/each
    Fogg perfume  Rs 135/each
    Onion         Rs 50/kg
    '''
price = 0
price_list = []
total_price = 0
final_final_price = 0
itemlist = []
quantity_list = []
P_list = []

items = {'Rice':75,'Sugar':50,'Salt':25,'Oil':175,'Panner':350,
         'Vermicelli':70,'Maggi':99,'Colgate':65,'Fogg perfume':135,'Onion':50}
option = int(input("for list of items press 1:"))
if option == 1:
  print(lists)
for i in range(len(items)):
    i_npl = int(input("if you want to buy press 1 or press 2 for exist:"))
    if i_npl == 2:
        break
    if i_npl == 1:
        item = input("Enter your items:")
        quantity = int(input("Enter quantity:"))
        if item in items.keys():
            price = quantity * (items[item])
            price_list.append((item,quantity,items,price))
            total_price += price
            itemlist.append(item)
            quantity_list.append(quantity)
            P_list.append(price)
            GST = (total_price * 5)/100
            Final_Amount = GST + total_price
        else:
            print("Sorry you entered item is not available")
    else:
        print("You entered wrong number")
    inp = input("can i bill the items Yes or No:")
    if inp == 'Yes':
        pass
        if Final_Amount != 0:
            print(26*"=","More super market",28*"=")
            print(30*"=","Hyderabad",33*"=")
            print("Name:", name,30*"","Date:",datetime.date.today())
            print(75*"-")
            print("S/No:",2*" ",'items',6*" ",'Quantity',10*" ",'price')
            for x in range(len(price_list)):
                print(x,2*' ',3*' ',itemlist[x],11*' ',quantity_list[x],15*" ",P_list[x])
            print(75*"-")
            print(50*" ",'Total Amount:','Rs',total_price)
            print("gst amount",53*" ",'Rs',GST)
            print(75*"_")
            print(50*" ",'final_amount:','Rs',Final_Amount)
            print(75*"_")
            print(75*"-")
            print(25*" ","Thanks for Visiting")
            print(75*"-")

