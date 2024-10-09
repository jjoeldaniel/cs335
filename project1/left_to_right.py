# KEY
# 0 - white
# 1 - black


def left_to_right(disks: list[int]) -> None:
    for i in range(0, len(disks) - 1):
        for x in range(i + 1, len(disks)):
            if disks[i] == 1 and disks[x] == 0:
                disks[i], disks[x] = disks[x], disks[i]


print("Left to Right Algorithm")
disks = [1, 0, 1, 0, 1, 0, 1, 0]
print(disks)
left_to_right(disks)
print(disks)
