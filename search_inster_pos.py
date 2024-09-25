def binarySearch(nums, target):
    front, back = 0, len(nums) - 1
    while front <= back:
        middle = (front+back) // 2
        if nums[middle] == target:
            return middle
        elif target < nums[middle]:
            back = middle - 1
        else:
            front = middle + 1
    return front

nums = [1,3,5,6]
target = 4
result = binarySearch(nums, target)
print(result)