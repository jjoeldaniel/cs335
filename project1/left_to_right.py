# KEY
# 0 - white
# 1 - black


def left_to_right(disks: list[int]) -> None:
    n = len(disks) // 2
    for _ in range(n):
        for i in range(n * 2 - 1):
            if disks[i] == 1 and disks[i + 1] == 0:
                disks[i], disks[i + 1] = disks[i + 1], disks[i]


print("Left to Right Algorithm")
disks = [1, 0, 1, 0, 1, 0, 1, 0]
print(disks)
left_to_right(disks)
print(disks)
