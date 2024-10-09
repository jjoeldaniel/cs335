# KEY
# 0 - white
# 1 - black


def left_to_right(disks: list[int]) -> None:
    # The list is a length of 2n
    n = len(disks) // 2

    # Each pass shifts the correct elements
    # 1 index in the correct direction, so
    # we have to pass `n` times.
    for _ in range(n):
        # Iterate through the entire length of `disks`
        for i in range(n * 2 - 1):
            # If a white and black are adjacent, swap
            # them in the correct order
            if disks[i] == 1 and disks[i + 1] == 0:
                disks[i], disks[i + 1] = disks[i + 1], disks[i]


print("Left to Right Algorithm")
disks = [1, 0, 1, 0, 1, 0, 1, 0]
print(disks)
left_to_right(disks)
print(disks)
