from itertools import combinations
S, k = input().split()
S2 = ''.join(sorted(list(S)))

for i in range (1, int(k)+1):
    my_comb = list(combinations(S2, i))
    for item in my_comb:
        print(''.join(item))
