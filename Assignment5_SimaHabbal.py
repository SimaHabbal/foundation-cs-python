def insertionSort(list1):  # O(n^2)
    border = 1
    while border < len(list1):  # O(n), n being the length of the list
        current = border  # the index of the element we are currently dealing with
        while current > 0 and list1[current].lower() < list1[current - 1].lower():  # O(n)
            # swap the out of order elements
            list1[current], list1[current - 1] = list1[current - 1], list1[current]  # O(1)
            current -= 1
        border += 1

    print(list1)

list1 = ["aA", "b", "BD", "Bc", "D"]
insertionSort(list1)
