if __name__ == '__main__':
    with open(file="baidu_x_system.log",mode="r+",encoding="utf-8") as f:
        lines = f.readlines() # 将每一行数据单独放在列表中
        sum = 0
        list = []
        list1 = []
        for line in lines:
            for j in range(len(line)):
                if line[j].isspace() == True:
                    a = line[:j]
                    list1.append(a)
                    if a not in list:
                        list.append(a)
                        sum = sum + 1
                    break
        print(list1)
        print(list)

list = set(list1)
for item in list:
    print("这个IP： %s 一共访问了 %s 次" % (item,list1.count(item)))

    f.close()













