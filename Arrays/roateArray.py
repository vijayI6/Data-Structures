def rotate(nums, k):
    rem = k % len(nums)
    if rem == 0:
        print(nums)
    else:
        fa = nums[:-rem]
        sa = nums[-rem:]
        res = sa + fa
        for i, value in enumerate(res):
            nums[i] = value
        print(nums)


rotate([1, 2, 3, 4, 5], 3)    # Output: [3, 4, 5, 1, 2]
