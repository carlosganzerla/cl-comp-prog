def kth_largest(nums, k):
    nums.sort()
    return nums[len(nums) - k]


if __name__ == '__main__':
    print(kth_largest([2, 1], 2))
