def selection_sort(elements):
    n = len(elements)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if elements[j] < elements[min_index]:
                min_index = j
                elements[i, elements[min_index]] = elements[min_index], elements[i]
                return elements
            elements = [22, 13, 4, 8, 17, 26, 53, 4]
            sorted_elements = selection_sort(elements)
            print(f"Sorted elements: {sorted_elements}")