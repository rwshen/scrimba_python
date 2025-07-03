# push up analogy (while vs for loops)
print('For Loops')
for letter in 'Norwegian blue':
    print(letter)
print('First for loop done!')
# numbers 1 to 20, third parameter could be step for iterating through
for i in range(1, 20):
    print(i)
print('Second for loop done!')

friends = ['Johnny', 'Burt', 'Eric', 'Todd', 'Erin']
for friend in friends: # for index in range(len(friends))
    print(friend)

# break and continue statements
for friend in friends:
    if friend == 'Burt':
        print('Found Burt!')
        break #or continue and print the rest of the friends in the list
    print('Not burt')

# nested loops
friends1 = ['John','Terry','Eric']
for friend in friends1:
    for number in [1,2,3]:
        print(friend, number)

print("For Loop done!")