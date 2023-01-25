print("THE VALUE:[69, 90, 15, 2, 10, 11, 41, 14, 44, 74]") 
nums = [69, 90, 15, 2, 10, 11, 41, 14, 44, 74]

def insertion_sort(nums):
    n = len(nums)

    for i in range(1,n):
        key = nums[i]
        
        j = i-1

        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

        print("The process:",nums)
    return nums


print("Sorted array is:", insertion_sort(nums))