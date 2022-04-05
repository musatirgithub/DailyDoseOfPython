def average(array):
    # your code goes here
    my_set = set(array)
    return sum(my_set)/len(my_set)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = average(arr)
    print (result)
