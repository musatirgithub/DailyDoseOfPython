x, y = input().split(' ')
def door_mat(m, n):
    for i in range(int((m-1)/2)):
        print(('.|.'*(2*i+1)).center(n, '-'))
    print(('WELCOME').center(n, '-'))
    for j in range(int((m-2)/2), -1, -1):
        print(('.|.'*(2*j+1)).center(n, '-'))
        

door_mat(int(x), int(y))
