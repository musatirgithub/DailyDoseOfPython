import itertools
list1 = [int(i) for i in input().split()]
list2 = [int(j) for j in input().split()]

def prod(list1, list2):
    res = list(itertools.product(list1, list2))
    for a in res:
        print(a, end=' ')

prod(list1, list2)
