# searching for an item in an ordered list
# this technique uses a binary search

items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binary_search(item, itemList):
    # get the list size
    listsize = len(itemList) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx: 
        pass
        # TODO: calculate the middle point
        midPt = (lowerIdx + upperIdx) // 2

        # TODO: if item is found, return the inde
        if itemList[midPt] == item:
            return midPt

        # TODO: otherwise get the next midpoint
        if item > itemList[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt + 1

    if lowerIdx > upperIdx: 
        return None

print(binary_search(23, items))
print(binary_search(87, items))
print(binary_search(250, items))