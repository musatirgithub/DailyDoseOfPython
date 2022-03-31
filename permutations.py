from itertools import permutations

users_inp = input().split()
s = sorted(list(users_inp[0]))
k = int(users_inp[1])

perms = list(permutations(s, k))
for i in perms :
    print(''.join(i))
