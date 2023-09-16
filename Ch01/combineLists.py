def combine_lists(list1: list, list2: list) -> list:
    combinedList = []
    list = list1
    list2 = list2
    listIndex = 0
    list2Index = 0
    totalLength = (len(list) + len(list2))

    for i in range(totalLength):
        if(listIndex >= len(list)):
            for x in range(len(list2) - list2Index):
                combinedList.append(list2[list2Index])
                list2Index += 1
            break

        elif(list2Index >= len(list2)):
            for y in range(len(list) - listIndex):
                combinedList.append(list[listIndex])
                listIndex += 1
            break

        elif(list[listIndex] <= list2[list2Index]):
            combinedList.append(list[listIndex])
            listIndex += 1

        elif(list[listIndex] >= list2[list2Index]):
            combinedList.append(list2[list2Index])
            list2Index += 1


    return combinedList

print(combine_lists([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]))
print(combine_lists([3], [1, 2, 3, 4, 5]))
print(combine_lists([], []))
print(combine_lists([1, 2, 3, 4, 5], [3]))
print(combine_lists([1, 2, 3, 4, 5], [-3, -2, -1]))
print(combine_lists([0], [0, 0, 0]))