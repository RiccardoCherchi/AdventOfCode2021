with open("data.txt") as f:
    lines = f.read().split("\n")

    rates = []
    ellips = []

    # for i in li(nes:
    #     count_0 = 0
    #     count_1 = 0
    #     for j in i:
    #         if int(j):
    #             count_1+= 1
    #         else:
    #             count_0 += 1
    #     if count_0 > count_1:
    #         rates.append(0)
    #     else:
    #         rates.append(1))
    for i in range(0, len(lines[0])):
        count_0 = 0
        count_1 = 0
        for j in lines:
            if int(j[i]):
                count_1 += 1
            else:
                count_0 += 1
            print(count_0, count_1)
        if count_0 > count_1:
            rates.append("0")
            ellips.append("1")
        else:
            rates.append("1")
            ellips.append("0")

    
    print(int("".join(rates), 2) * int("".join(ellips), 2))

            