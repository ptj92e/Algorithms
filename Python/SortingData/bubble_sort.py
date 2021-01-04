# Bubble Sort algorithm

def bubbleSort(data_set):
    # TODO: start with the array length and decrement each time
    for i in range(len(data_set) - 1, 0, -1):
        for j in range(i):
            if data_set[j] > data_set[j + 1]:
                temp = data_set[j]
                data_set[j] = data_set[j + 1]
                data_set[j + 1] = temp
        print("Current state: ", data_set)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubbleSort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    main()