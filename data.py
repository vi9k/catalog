from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Restaurant, Base, MenuItem, User
 
engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
User1 = User(name="Vinay", email = "15pa1a0470@vishnu.edu.in",
            picture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqHx9HEKprfUBgpfsgDNjaeCrXPGqwam_oAsREaXgYnt71HaDp')
session.add(User1)
session.commit()

#Menu for UrbanBurger
restaurant1 = Restaurant(user_id=1, name = "Achuth-Breakfast Center")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Pulihora",
 description = "very good at it", price = "$2.99", 
 course = "Breakfast", restaurant = restaurant1, photo='https://bit.ly/2sRPzE6')

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Dosa",
 description = "Classic indian breakfast item",
  price = "$5.50", course = "Breakfast",
   restaurant = restaurant1, photo='https://bit.ly/2JN3aGs')

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Upma",
 description = "Dish from indian subcontinent",
  price = "$3.99", course = "Breakfast",
   restaurant = restaurant1, photo='https://bit.ly/2HHoU1p')

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Vada", 
description = "Savoury fired snack item from India", 
price = "$7.99", course = "Snack", 
restaurant = restaurant1, photo='https://bit.ly/2Mkp1Dq')

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name = "Idli", 
description = "Savoury rice cake item", 
price = "$1.99", course = "Breakfast",
 restaurant = restaurant1, photo='https://i.ndtvimg.com/i/2018-01/rice-idli_620x330_71514979375.jpg')

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name = "Iced Tea",
 description = "with Lemon", 
 price = "$.99", course = "Beverage",
  restaurant = restaurant1, photo='https://bit.ly/2JMtEb8')

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name = "Bread-Item",
 description = "On texas toast with American Cheese",
  price = "$3.49", course = "Snack",
   restaurant = restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name = "Veggie Burger",
 description = "Made with freshest of ingredients and home grown spices",
  price = "$5.99", course = "Snack", restaurant = restaurant1)

session.add(menuItem8)
session.commit()




#Menu for Super Stir Fry
restaurant2 = Restaurant(user_id=1, name = "Chicken Love")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Chicken NOodle Soup",
 description = "simmed with water, usaully with various other ingrediants",
  price = "$7.99", course = "Main", restaurant = restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Buldak",
description = " a famous Korean dish made from heavily spiced chicken", 
price = "$25", course = "Main", restaurant = restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Amritsar Chicken Masala",
description = "A Punjabi Cuisine favorite", price = "$30",
 course = "Main", restaurant = restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Nepali Momo ",
 description = "", price = "", course = "",
  restaurant = restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name = "Beef Noodle Soup",
 description = "", price = "", course = "",
 restaurant = restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name = "Ramen",
 description = "", price = "", course = "",
  restaurant = restaurant2)

session.add(menuItem6)
session.commit()




#Menu for Panda Garden
restaurant3 = Restaurant(user_id=1, name = "Snack-Hits")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Punugulu",
 description = "famous streetfood from Andhra-Pradesh",
  price = "$10", course = "Sanck", restaurant = restaurant3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Stuffed Idlies",
 description = "A healthy Udipi snack",
  price = "$15", course = "Snack", restaurant = restaurant3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Pesarattu",
 description = "dosa like prep but native from Andhra-Pradesh",
  price = "$30", course = "Breakfast", restaurant = restaurant3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Stinky Tofu",
 description = "deep fried fermented tofu served with pickled cabbage.",
  price = "", course = "Main", restaurant = restaurant3)

session.add(menuItem4)
session.commit()



#Menu for Thyme for that
restaurant4 = Restaurant(user_id=1, name = "Vegetarian Cuisine ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Tres Leches Cake", 
description = "Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
 price = "", course = "", restaurant = restaurant4)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Mushroom risotto",
 description = "Portabello mushrooms in a creamy risotto", 
 price = "", course = "", restaurant = restaurant4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Honey Boba Shaved Snow",
 description = "Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
  price = "", course = "", restaurant = restaurant4)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Cauliflower Manchurian",
 description = "Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
  price = "", course = "", restaurant = restaurant4)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name = "Aloo Gobi Burrito",
 description = "Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
  price = "", course = "Snack", restaurant = restaurant4)

session.add(menuItem5)
session.commit()




#Menu for Tony's Bistro
restaurant1 = Restaurant(name = "Tony\'s")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Shellfish Tower",
 description = "", price = "", course = "", 
 restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Chicken and Rice",
 description = "", price = "", course = "", restaurant = restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Mom's Spaghetti",
 description = "", price = "", course = "", restaurant = restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
 description = "", price = "", course = "", restaurant = restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name = "Tonkatsu Ramen",
 description = "Noodles in a delicious pork-based broth with a soft-boiled egg", 
 price = "", course = "", restaurant = restaurant1)

session.add(menuItem5)
session.commit()




#Menu for Andala's 
restaurant1 = Restaurant(user_id=1, name = "Andala\'s")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Lamb Curry",
 description = "Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
  price = "", course = "", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Chicken Marsala", 
description = "Chicken cooked in Marsala wine sauce with mushrooms", 
price = "", course = "", restaurant = restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Potstickers",
 description = "Delicious chicken and veggies encapsulated in fried dough.",
  price = "", course = "", restaurant = restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Nigiri SamplerMaguro, Sake, Hamachi, Unagi, Uni, TORO!",
 description = "", price = "", course = "", restaurant = restaurant1)

session.add(menuItem4)
session.commit()




#Menu for Auntie Ann's
restaurant1 = Restaurant(user_id=1, name = "Auntie Ann\'s Diner ")

session.add(restaurant1)
session.commit()

menuItem9 = MenuItem(user_id=1, name = "Chicken Fried Steak", description = "Fresh battered sirloin steak fried and smothered with cream gravy", price = "$8.99", course = "Entree", restaurant = restaurant1)

session.add(menuItem9)
session.commit()



menuItem1 = MenuItem(user_id=1, name = "Boysenberry Sorbet",
 description = "An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
  price = "", course = "", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Broiled salmon",
 description = "Salmon fillet marinated with fresh herbs and broiled hot & fast",
  price = "", course = "", restaurant = restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Morels on toast (seasonal)",
 description = "Wild morel mushrooms fried in butter, served on herbed toast slices",
  price = "", course = "", restaurant = restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Tandoori Chicken",
 description = "Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
  price = "", course = "", restaurant = restaurant1)

session.add(menuItem4)
session.commit()




#Menu for Cocina Y Amor
restaurant1 = Restaurant(name = "Subway")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Super Burrito Al Pastor",
 description = "Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
  price = "", course = "", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Cachapa",
 description = "Golden brown, corn-based venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
  price = "", course = "", restaurant = restaurant1)

session.add(menuItem2)
session.commit()

print("added menu items!")

