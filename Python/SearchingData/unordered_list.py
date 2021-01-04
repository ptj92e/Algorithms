# searching for an item in an unordered list
# sometimes called a Linear Search

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item, itemList):
    for i in range(0, len(items)):
        if item == itemList[i]:
            return i
    
    return None

print(find_item(87, items))
print(find_item(250, items))