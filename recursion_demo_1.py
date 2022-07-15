num = 10


def f1(index, n):
    if index == n:
        return
    print(index)
    f1(index=index + 1, n=n)


f1(index=0, n=num)
