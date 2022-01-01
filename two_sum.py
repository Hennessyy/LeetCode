# 21MS -- My solution
def two_sum(nums, target):
    for count, i in enumerate(nums):
        for cnt, n in enumerate(nums):
            if i + n == target:
                return [count , cnt]
        

# 18MS
def two_sum_improved(nums, target):
    
    vals = dict()

    for count , ele in enumerate(nums):
        seek = target - ele

        if seek in vals:
            print("here")
            return [vals[seek], count]
    
        vals[ele] = count

    return []






print(two_sum_improved([2,7,11,15], 9))