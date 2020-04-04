def key1(item):
    return item[0]
def key2(item):
    return item[2]
def main():
    t = int(input())
    list1 = []
    list2 = []
    for x in range(t):
        n = int(input())
        list1.clear()
        for y in range(n):
            list2 = []
            list2 =[int(z) for z in input().split(" ")]
            list2.append(y)
            list1.append(list2)
        list1.sort(key = key1)
        cam = -1
        jamie = -1
        flag = True
        for a in list1:
            entry_time = a[0]
            exit_time = a[1]
            if jamie == -1:
                jamie = exit_time
                a.append('J')
            elif entry_time >= jamie:
                jamie = exit_time
                a.append('J')
            elif entry_time < jamie and entry_time >= cam:
                cam = exit_time
                a.append('C')
            elif entry_time < cam and entry_time < jamie:
                flag = False
                break
        if flag == False:
            string = "IMPOSSIBLE"
        else:
            string = ""
            list1.sort(key = key2)
            string = string.join([a[3] for a in list1])
        print("Case #"+str(x+1)+": "+string)

main()
