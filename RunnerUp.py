n = int(input())
arr = map(int, input().split())
    
list1 = sorted(arr)
list1.reverse()
    
for i in range(0, len(list1)):
    if list1[i] == list1[0]:
        continue
    else:
        print(list1[i])
        break
