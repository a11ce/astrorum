def askText(s):
    return input(s)


def selectFrom(arr, count, displayFunc=None):
    for idx, ob in enumerate(arr):
        print("{}: ".format(idx), end="")
        print(displayFunc(ob) if displayFunc else ob)
    picked = []
    while len(picked) < count:
        p = int(input("? "))
        picked.append(arr[p])
    return picked
