
def selection_sort(nums):
    for i, num in enumerate(nums):
        mn = min(nums[i:])
        mn_i = nums.index(mn)
        if mn < num:
            nums[i] = mn
            nums[mn_i] = num
    return nums


def main():
    nums = [7, 2, 5, 4, 1, 6, 0, 3]
    sorted_values = selection_sort(nums)
    print(f"Unsorted: {nums}")
    print(f"Sorted: {sorted_values}")

main()
