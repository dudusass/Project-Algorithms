def find_duplicate(nums):
    if len(nums) <= 1 or type(nums) != list:
        return False
    nums.sort()
    for n in range(0, len(nums) - 1):
        if type(nums[n]) is not int or nums[n] < 0:
            return False
        if nums[n] == nums[n + 1]:
            return nums[n]
    return False
