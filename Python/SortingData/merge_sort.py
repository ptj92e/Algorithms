# Implement a merge sort with recursion

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def merge_sort(data_set):
    if len(data_set) > 1:
        mid = len(data_set) // 2
        leftarr = data_set[:mid]
        rightarr = data_set[mid:]

        # TODO: recursively break down the arrrays
        merge_sort(leftarr)
        merge_sort(rightarr)

        # TODO: now perform the merging
        i = 0 # index of the left array
        j = 0 # index of the right array
        k = 0 # index of the merged array

        # TODO: while both array have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                data_set[k] = leftarr[i]
                i += 1
            else:
                data_set[k] = rightarr[j]
                j += 1
            k += 1

        # TODO: if the left array still has values, add them
        while i < len(leftarr):
            data_set[k] = leftarr[i]
            i += 1
            k += 1

        # TODO: if the right array still has values, add them
        while j < len(rightarr):
            data_set[k] = rightarr[j]
            j += 1
            k += 1

# test merge sort with data
print(items)
merge_sort(items)
print(items)