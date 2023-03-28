class Menu:
  def __init__(self, name, items, start_time, end_time):

    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + ' menu available from ' + str(self.start_time) + ' — ' + str(self.end_time)

  def calculate_bill(self, purchased_items):
    bill = 0
    for item in purchased_items:
      if item in self.items:
        bill += self.items[item]
    
    return bill
    
# brunch menu
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("Brunch", brunch_items, 1100, 1600)


# early bird menu
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("Early Bird", early_bird_items, 1500, 1800)

# dinner menu
dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu("Dinner", dinner_items, 1700, 2300)

# kids menu
kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00,  'apple juice': 3.00 }
kids = Menu("Kids", kids_items, 1100, 2100)

# arepa menu
arepa_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas = Menu("Take a' Arepa", arepa_items, 1000, 2000)

print(kids)
print(brunch)
print(early_bird)
print(dinner)

print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))

print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)', 'grilled ham steak with pineapple']))

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address
  
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus
menus = [brunch, early_bird, dinner, kids]  
flagship_store_address = "1232 West End Road"
new_installment_address = "12 East Mulberry Street"
flagship_store = Franchise(flagship_store_address, menus)
new_installment = Franchise(new_installment_address, menus)

arepa_address = "189 Fitzgerald Avenue"
arepa_place = (arepa_address, [arepas])

print(new_installment)

print(flagship_store.available_menus(1200))
print(new_installment.available_menus(1700))


class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepa = Business("Take a' Arepa", arepa_place)

print(arepa.franchises[1])
