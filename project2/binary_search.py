# Given a sorted array that can contain duplicates,
# find the first occurrence of a target element T.
def binary_search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    result = -1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            result = m  # Record the position
            r = m - 1  # Narrow the search to the left side
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return result
