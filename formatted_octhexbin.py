def print_formatted(number):
    max = len(str(bin(number))[2:])
    for i in range (1, number+1):
        print(str(i).rjust(max, ' '), str(oct(i))[2:].rjust(max, ' '), str(hex(i))[2:].upper().rjust(max, ' '), str(bin(i))[2:].rjust(max, ' '))
print_formatted(17)
