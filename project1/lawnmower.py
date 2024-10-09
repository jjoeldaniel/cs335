# KEY
# 0 - white
# 1 - black


def lawnmower(disks: list[int]) -> None:
    # The list is a length of 2n
    n = len(disks) // 2

    # Each pass shifts the correct elements
    # 1 index in the correct direction, so
    # we have to pass `n` times.
    for passes in range(n):
        # If even, we move to the right end of the list
        if passes % 2 == 0:
            # Iterate through the entire length of `disks`
            for i in range(n * 2 - 1):
                # If a white and black are adjacent, swap
                # them in the correct order
                if disks[i] == 1 and disks[i + 1] == 0:
                    disks[i], disks[i + 1] = disks[i + 1], disks[i]
        # If odd, we move to the odd end of the list
        else:
            # Iterate through the entire length of `disks`
            for i in range(n * 2 - 1, 0, -1):
                # If a white and black are adjacent, swap
                # them in the correct order
                if disks[i] == 0 and disks[i - 1] == 1:
                    disks[i], disks[i - 1] = disks[i - 1], disks[i]


print("Lawnmower Algorithm")
disks = [1, 0, 1, 0, 1, 0, 1, 0]
print(disks)
lawnmower(disks)
print(disks)
