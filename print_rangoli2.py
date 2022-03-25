def print_rangoli(n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = alphabet[:n]
    text2 = text[::-1]
    list1 = []
    for i in range(n):
        piece = text2[:i+1]
        if i > 0 :
            piece2 = piece[::] + piece[-2::-1]
            list1.append('-'.join(piece2).center(4*n-3, '-'))
        else:
            list1.append(piece.center(4*n-3, '-'))

    for i in list1:
        print(i)
    for j in range(len(list1),1,-1):
        print(list1[j-2])
