def reverse_list(l):
    i = 0
    j = len(l) - 1
    while i < j:
        t = l[i]
        l[i] = l[j]
        l[j] = t
        i = i + 1
        j = j - 1