
nums = [69, 90, 15, 2, 10, 11, 41, 14, 44, 74]

def merge_sort(num):
    if len(num)>1:
        left_num = num [:len(num)//2]
        right_num = num [len(num)//2:]