def min_value_and_index(values):
    min_value = values[0]

    for index, value in enumerate(values):
        if value < min_value:
            min_value = value
    return min_value



def selection_sort_v1(nums):
    for i, num in enumerate(nums):
        print("------------------")
        print("find in", nums[i:])
        min_value = min_value_and_index(nums[i:])
        min_index = nums.index(min_value)
        print("value:", min_value, "index:", min_index)
        # swap
        if min_value < num:
            nums[i] = min_value
            nums[min_index] = num
        print(f"Result: {nums}")
        print("------------------")
    return nums

def selection_sort(values):
    for i in range(len(values)):
        min_index = i
        # update min_index if found min value.
        for j in range(i + 1, len(values)):
            if values[j] < values[min_index]:
                min_index = j

        # swap current value with min value and vice verca
        values[i], values[min_index] = values[min_index], values[i]

    return values


def main():
    nums = [7, 2, 5, 4, 1, 6, 0, 3]
    nums_copy = nums.copy()
    sorted_values = selection_sort(nums_copy)
    print(f"{nums}")
    print(f"{sorted_values}")

main()
