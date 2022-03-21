def wrap(string, max_width):
    text = ''
    for i in range(len(string)):
        if (i + 1) % 4 == 0:
            text += string[i]+'\n'
        else:
            text += string[i]
    return text
res = wrap('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4)
print(res)
