
X = int(input())  # Number of shoes
shoes = input().split()
my_list = [int(i) for i in shoes]
my_dict = {i: my_list.count(i) for i in my_list}
N = int(input())
money = 0
for j in range(N):
    customer = input().split()
    if int(customer[0]) in my_dict.keys() and my_dict[int(customer[0])] > 0:
        my_dict[int(customer[0])] -= 1
        money += int(customer[1])

print(money)
