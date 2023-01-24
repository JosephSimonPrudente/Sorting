
print("THE VALUE:[69, 90, 15, 2, 10, 11, 41, 14, 44, 74]")

nums = [69, 90, 15, 2, 10, 11, 41, 14, 44, 74]
def sort (nums):

    for i in range (9):
        minpos = i
        for j in range (i,10):
            if nums[j] < nums [minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

sort(nums)

print(nums)