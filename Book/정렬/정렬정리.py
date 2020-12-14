def swap(nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]

def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        swap(nums, i, min_index)

def insert_sort(nums):
    for i in range(len(nums)):
        for j in range(i, 0, -1):
            if nums[j] <= nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            else:
                break

nums = [1,5,7,9,3,0,6,8,3,2,1]
insert_sort(nums)
print(nums)