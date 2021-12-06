with open("data.txt") as f:
    lines = f.read().split("\n")

    stage = 0

    def filter_oxygen(stage, oxygen_list):

        count_0 = []
        count_1 = []
        for i in oxygen_list:
            if int(i[stage]):
                count_1.append(i)
            else:
                count_0.append(i)
        new_list = count_0 if len(count_0) > len(count_1) else count_1
        print(new_list)
        if len(new_list) > 1:
            return filter_oxygen(stage + 1, new_list)
        else:
            return int(new_list[0], 2)

    
    def filter_co2(stage, co2_list):

        count_0 = []
        count_1 = []
        for i in co2_list:
            if int(i[stage]):
                count_1.append(i)
            else:
                count_0.append(i)
        new_list = count_1 if len(count_1) < len(count_0) else count_0
        print(new_list)
        if len(new_list) > 1:
            return filter_co2(stage + 1, new_list)
        else:
            return int(new_list[0], 2)

            
    oxygen = filter_oxygen(stage, lines)
    stage = 0
    co2 = filter_co2(stage, lines)

    print(oxygen * co2)
            