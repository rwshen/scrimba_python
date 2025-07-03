# two lists, invite friends
# need to add two extra names when you run the code
# print out one invitation to each friend per line
# Capitalize the names

names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
name2 = input('Enter the next name: ').title()
name3 = input('Enter another friend name: ').title()
names.append(name2)
names1.append(name3)

def invite_friends(friends_array):
    for friend in friends_array: 
        print(f"{friend.title()}! You are invited to the party on Saturday.")
    

invite_friends(names)
invite_friends(names1)