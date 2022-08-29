def misuma(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + misuma(L[1:])


print(misuma([1, 2, 3, 4, 5]))

input()
