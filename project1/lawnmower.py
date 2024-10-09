# KEY
# 0 - white
# 1 - black


def lawnmower(disks: list[int]) -> None:
    for i in range(0, len(disks) - 1, 2):
        if disks[i] == 1 and disks[i + 1] == 0:
            disks[i], disks[i + 1] = disks[i + 1], disks[i]

        while i > 0:
            if disks[i] == 0 and disks[i - 1] == 1:
                disks[i], disks[i - 1] = disks[i - 1], disks[i]
            i -= 1
    return


print("Left to Right Algorithm")
disks = [1, 0, 1, 0, 1, 0, 1, 0]
print(disks)
lawnmower(disks)
print(disks)
