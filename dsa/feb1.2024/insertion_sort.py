nums = [10, 2, 6, 5, 1, 3, 4]

def insertion_sort(nums):
    for i in range(1, len(nums)):
        # j = i-1
        # while nums[j] > nums[j+1] and j >= 0:
        #     nums[j], nums[j+1] = nums[j+1], nums[j]
        #     j -= 1
        for j in range(i - 1, -1, -1):
            if (nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
            else:
                break 
    return nums

insertion_sort(nums)
print(nums)