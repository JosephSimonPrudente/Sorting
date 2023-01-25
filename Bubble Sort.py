print("THE VALUE:[69, 90, 15, 2, 10, 11, 41, 14, 44, 74]") 
print("                                                 ")
nums =  [69, 90, 15, 2, 10, 11, 41, 14, 44, 74]

def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp =  nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

                print("The process:",nums)

bubble_sort(nums)
print("                                                 ")
print("Sorted array is:",nums)
