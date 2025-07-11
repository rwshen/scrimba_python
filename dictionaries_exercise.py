#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}


cart = []
shops = [freelancers, antiques, pet_shop]

def go_shopping(shop):
    items = {key: value for key, value in shop.items() if key != 'name'}
    shop_name = list({key: value for key, value in shop.items() if key == 'name'}.values())[0]
    buy_item = input(f'\n\nWhat item do you want to buy from {shop_name}? \n\n {(', ').join(list(items.keys()))} \n\n: ')
    if buy_item not in items.keys():
        print('This item is not in the inventory.')
    return buy_item

def make_cart(buy_item, shop, total=1000):
    if shop.get(buy_item):
        cart.append({'item': buy_item, 'price': shop[buy_item]})
        total -= shop[buy_item]
        print(f'You have ${total} left.')
        shop.pop(buy_item)
        return total

def ask_if_done():
    answer = input('\n Are you done shopping? ')
    if answer == 'yes' or answer =='Yes' or answer == 'Y':
        return True
    return False

index = 0
for shop in shops:
    item = go_shopping(shop)
    total = make_cart(item, shop)
    index += 1
    if index < len(shops):
        if ask_if_done() == True:
            break

def give_formatted_inventory(stuff):
    stuffs = ''
    total = 0
    for s in stuff: 
        stuffs += f' {s[0]},'
        total += s[1]
    return f'\n\n You have{stuffs} and it costs ${total}.\n'

# After shopping:
inventory = []
for items in cart:
    inventory.append(list(items.values()))

print(give_formatted_inventory(inventory))
    

