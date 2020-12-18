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

def quick_sort(nums, start, end):
    if start >= end:
        return
    pivot = start
    i, j = start + 1, end

    while i <= j:
        while i <= end and nums[i] <= nums[pivot]:
            i += 1
        while start < j and nums[j] >= nums[pivot]:
            j -= 1
        if i > j:
            nums[j], nums[pivot] = nums[pivot], nums[j]
        else:
            nums[i], nums[j] = nums[j], nums[i]

    quick_sort(nums, start, j-1)
    quick_sort(nums, j+1, end)

def counting_sort(nums):
    max_num = max(nums)
    num_list = [0] * (max_num+1)
    for i in nums:
        num_list[i] += 1
    for i in range(len(num_list)):
        for j in range(num_list[i]):
            print(i, end=' ')

nums = [1,5,7,9,3,0,6,8,3,2,1]
counting_sort(nums)