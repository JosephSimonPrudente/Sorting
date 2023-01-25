print("THE VALUE:[69, 90, 15, 2, 10, 11, 41, 14, 44, 74]") 
nums = [69, 90, 15, 2, 10, 11, 41, 14, 44, 74]

def merge_sort(num):
    if len(num)>1:
        left_num = num [:len(num)//2]
        right_num = num [len(num)//2:]

        merge_sort(left_num)
        merge_sort(right_num)

        i = 0
        j= 0
        k= 0 
        while i < len(left_num) and j < len(right_num):
            if left_num[i] < right_num[j]:
                num[k] = left_num[i]
                i += 1
            else:
                num[k] = right_num[j]
                j+=1
            k+=1

        while i < len(left_num):
            num[k] = left_num[i]
            i+=1
            k+=1

        while j < len(right_num):
            num[k] = right_num[j]
            j+=1
            k+=1 
     
merge_sort(nums)
print("Sorted array is:",nums)