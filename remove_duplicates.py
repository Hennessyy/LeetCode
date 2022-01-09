def removeDuplicates(nums):
    left = 1

    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            nums[left] = nums[right]
            left += 1
        
    return left
        