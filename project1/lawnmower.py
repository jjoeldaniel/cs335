# KEY
# 0 - white
# 1 - black


def lawnmower(disks: list[int]) -> None:
    n = len(disks) // 2

    for passes in range(n):
        if passes % 2 == 0:
            for i in range(n * 2 - 1):
                if disks[i] == 1 and disks[i + 1] == 0:
                    disks[i], disks[i + 1] = disks[i + 1], disks[i]
        else:
            for i in range(n * 2 - 1, 0, -1):
                if disks[i] == 0 and disks[i - 1] == 1:
                    disks[i], disks[i - 1] = disks[i - 1], disks[i]


print("Lawnmower Algorithm")
disks = [1, 0, 1, 0, 1, 0, 1, 0]
print(disks)
lawnmower(disks)
print(disks)
