mylist = raw_input('Enter your list: ')
mylist = [int(x) for x in mylist.split(',')]
total = 0    

print mylist
for number in mylist:    
    total += number    
print "The sum of the numbers is:", total