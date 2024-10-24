items = []

num_items = int(input('Enter the number of items to add: '))

for i in range(num_items):
    item = input('Enter item: ')
    items.append(item)

remove_item = input('Do you want to remove any items? (y/n): ')
while remove_item.lower() == 'y':
    item_to_remove = input('Enter the item you want to remove: ')
    if item_to_remove in items:
        items.remove(item_to_remove)
    else:
        print('Item not found in the list.')
    remove_item = input('Do you want to remove any more items? (y/n): ')

print('Final list of items:', items)



