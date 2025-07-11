# open a file and how you get it (read, write, appending)
# my_file = open('greeting.txt', 'r')
# # print(my_file.read(5)) # can specify the number of characters to read

# # read line by line
# # print(my_file.readline())
# # line_by_line = line_by_line = my_file.readlines()
# line_by_line1 = my_file.read().splitlines() # better at splitting things
# # print('readlines: ',line_by_line)
# print('splitlines: ',line_by_line1)

# # always close a file
# my_file.close()

# context manager (do not need to remember to close the file)
with open('friends.csv', 'r') as f:
    friends = f.read().splitlines()
    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year = int(friend[1].strip())
        print(f'In 2030, {name} will be {2030-year} years old')


with open('greeting.txt', 'r') as f:
    for line in f: 
        print(line)
