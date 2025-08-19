# find method

my_str = 'tiruvanantapuram'

print(my_str.find('ananta'))
print(my_str.find('a')) # finds index of 1st occurance
print(my_str.find('krishna')) # returns -1 saying the substring is not found
print(my_str.find('ananta', 6)) # start the search from index 6
print(my_str.find('ananta', 5, 10)) # start the search from the index 5 and ends at index 9 . so it will return -1.
print(my_str.find('ananta', 5, 11)) # start from index 5 and ends at index 10 . so it return 5.


