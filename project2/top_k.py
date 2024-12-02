from collections import Counter


# Given an integer array nums and an integer k, return the
# k most frequent elements. You may return the answer in any order.
def topKFrequent(nums: list[int], k: int) -> list[int]:
    # Get frequency of each element
    freq = Counter(nums)

    # Sort by frequency in reverse order
    d: list[tuple[int, int]] = list(sorted(freq.items(), reverse=True, key=lambda x: x[1]))

    # Retrieve first k elements
    res: list[int] = []
    for key, _ in d:
        res.append(key)

        if len(res) == k:
            break

    return res
