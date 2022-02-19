# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 2/18/2022
# Description: A function named reverse_list that takes as a parameter a list and reverses the order of the elements in that list.
def reverse_list(l):
    i = 0
    j = len(l) - 1
    while i < j:
        t = l[i]
        l[i] = l[j]
        l[j] = t
        i = i + 1
        j = j - 1