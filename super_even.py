supers = []

nums1 = list(range(1000, 3001))
def super_even(list1):
    for i in list1:
        issuper = True
        for j in str(i):
            if int(j) % 2:
                issuper = False
                break
        if issuper:
            global supers
            supers.append(i)
    return supers

print(super_even(nums1))
