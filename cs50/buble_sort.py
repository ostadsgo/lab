def bubble_sort_v1(values):
    for i in range(0, len(values)):
        for j in range(0, len(values)):
            if values[i] < values[j]:
                values[j], values[i] = values[i], values[j]

    return values


def bubble_sort(values):
    for i in range(len(values) - 1):
        for j in range(len(values) - i - 1):
            if values[j+1] < values[j]:
                values[j], values[j+1] = values[j+1], values[j]
    return values



nums = [7, 2, 5, 4, 1, 6, 0, 3]
sorted_values = bubble_sort(nums)
print(sorted_values)
