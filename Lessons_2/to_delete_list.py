# Set list
random_list = ['one', 'two', 'to-delete', 'three', 'to-delete', 'four', 'to-delete']

# Delete word 'to-delete'
random_list = [item for item in random_list if item != 'to-delete']

# Print list
print(random_list)