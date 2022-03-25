def print_rangoli(size):
    def letterer(size):
        # your code goes here
        letters = []
        for i in range(size):
            letters.append(chr(97+i))
        letters.reverse()
        return letters

    def mixer(list1):
        list2 = []
        for i in range(len(list1)):
            j = 0
            k= i
            while j <= i:
                list2.append(list1[j])
                j += 1

            while k > 0:
                list2.append(list1[k-1])
                k -= 1
            list2.append('&')
        return list2

    def texter(list1):
        temp = []
        temp2 = []
        text = '-'.join(list1)
        text2 = text.strip("&")
        temp = text2.split('&')
        for i in temp:
            j = i.strip('-')
            temp2.append(j)
        return temp2


    upper = texter(mixer(letterer(size)))
    down = upper[-2:0:-1]
    down_tip = upper[0]

    for i in upper:
        print(i.center(4*size-3, '-'))
    for j in down:
        print(j.center(4*size-3, '-'))
    print(down_tip.center(4*size-3, '-'))
    
print_rangoli(4)
