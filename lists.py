N = int(input())
new_list = []
num = 0
pos = 0

for i in range(N):
    split_list = input().split()
    action = str(split_list[0])
    if len(split_list) >= 2:
        num = int(split_list[1])
    if len(split_list) >= 3:
        pos = int(split_list[2])

    match action:
        case "insert":
            new_list.insert(num, pos)
        case "print":
            print(new_list)
        case "remove":
            new_list.remove(num)
        case "append":
            new_list.append(num)
        case "sort":
            new_list.sort()
        case "pop":
            new_list.pop()
        case "reverse":
            new_list.reverse()  