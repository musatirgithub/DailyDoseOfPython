def merge_the_tools(string, k):
    # your code goes here
    list1 = []
    for i in range(int(len(string)/k)):
        list1.append(string[i*k:i*k+k])
    
    for item in list1:
        list2 = []
        for letter in item:
            if letter not in list2:
                list2.append(letter)
        print(''.join(list2))
            
    
print(merge_the_tools('AABCAAADA', 3))
