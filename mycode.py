coffee_menu = [
    { 
    'itemname' : 'Espresso','itemno' : 1,'price' : 5,
     },

         { 
    'itemname' : 'Latte Mocchiato','itemno' : 2,'price' : 6,
     },

         { 
    'itemname' : 'Caramel Mocchiato', 'itemno' : 3,'price' : 6,
     },
     
              { 
    'itemname' : 'Latte','itemno' : 4,'price' : 4,
     },
     
              { 
    'itemname' : 'Americano','itemno' : 5,'price' : 5,
     },
     
         { 
    'itemname' : 'Cappuccino','itemno' : 6,'price' : 4,
     },

         { 
    'itemname' : 'Cafe Latte','itemno' : 7,'price' : 5,
     },

         { 
    'itemname' : 'Flat White','itemno' : 8,'price' : 6,
     },
     
              { 
    'itemname' : 'Mocha','itemno' : 9,'price' : 4,
     },
     
              { 
    'itemname' : 'Frappiccino', 'itemno' : 10, 'price' : 5,
     },

         { 
    'itemname' : 'Chocolate Cake','itemno' : 11,'price' : 5,
     },

         { 
    'itemname' : 'Croissant','itemno' : 12,'price' : 4,
     },

         { 
    'itemname' : 'Caramel Waffles','itemno' : 13,'price' : 4,
     },
     
              { 
    'itemname' : 'Dounut','itemno' : 14,'price' : 4,
     },
     
              { 
    'itemname' : 'Burger','itemno' : 15,'price' : 6,
     },

         { 
    'itemname' : 'Sandwich','itemno' : 16,'price' : 4,
     },

         { 
    'itemname' : 'Chocolate Chip Cookie','itemno' : 17,'price' : 4,
     },

         { 
    'itemname' : 'Muffin','itemno' : 18,'price' : 4,
     },
     
              { 
    'itemname' : 'Coffee Cake','itemno' : 19,'price' :6,
     },
     
              { 
    'itemname' : 'Loaf Cake','itemno' : 20,'price' : 4,
     },
]

#printing drinks and logo
def coffee():
  print("〈〈〈〈〈〈 BATHSPA COFFEE 〉〉〉〉〉\n") 
  print("*************** DRINKS ***************")
  coffee = {
    "01. Espresso" : "5 AED", 
    "02. Latte Mocchiato" : "6 AED",
    "03. Caramel Mocchiato" : "6 AED",
    "04. Latte" : "4 AED",
    "05. Americano" : "5 AED",
    "06. Cappuccino" : "4 AED",
    "07. Cafe Latte" : "5 AED",
    "08. Flat White" : "6 AED",
    "09. Mocha" : "4 AED",
    "10. Frappiccino" : "6 AED",
}
  for item, price in coffee.items():
    print(f" {item:30}, {price}")

#printing snacks
def food():
  print("**************** FOOD ****************")
  food_items = {
    "11. Chocolate Cake" : "5 AED", 
    "12. Croissant" : "4 AED",
    "13. Caramel Waffles" : "4 AED",
    "14. Dounut" : "4 AED",
    "15. Burger" : "6 AED",
    "16. Sandwich" : "4 AED",
    "17. Chocolate Chip Cookie" : "4 AED",
    "18. Muffin" : "4 AED",
    "19. Coffee Cake" : "6 AED",
    "20. Loaf Cake" : "4 AED",
}
  for item, price in food_items.items():
    print(f" {item:30}, {price}")
  print()

def options():
  coffee()
  food()

def order():

  while True:
    
    
    options()

    amount = int(input('Please Enter the ammount to be purchase items:\n'))

    if amount <= 0:
      print('Invalid Amount\n')
      order()

    itementer = int(input('Please choose the item to be dispensed\n'))

    if itementer >= 21 or itementer <= 0:
      print('Invalid Input')
      
    items = []
    total_sum = []

    for di in coffee_menu:

          if itementer == di['itemno'] and amount <= di['price'] :
            print('Insufficient Amount\n')
            order()

          if itementer == di['itemno'] and amount >= di['price']:

            print('***************************************\n')
            print(f"You picked {di['itemname']}\n")
            print('***************************************\n')

            total_sum.append(di.get('price'))
          
            items.append(di.get('itemname'))

            print(f"Amount of {di['itemname']}\n")

            print('***************************************\n')
            print("You may now proceed a receive the following items that have been dispensed:\n")

            print(items, '\n')
            print('***************************************\n')

            total=sum(total_sum)
            print("And here is your total amount:\n\n\t", total, "AED\n")

            remaining_amount = amount - total
            print("And your change is:\n\n\t", remaining_amount, "AED\n")

            print('***************************************\n')
            print("Thank you for the purchase!\n")
            print('***************************************\n')

            break

def bathspacoffee():
  order()

bathspacoffee()