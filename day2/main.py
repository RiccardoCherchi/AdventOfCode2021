
def main():
    with open("data.txt", "r") as f:
        data = f.read().split("\n")
        aim = 0
        forward = 0
        depth = 0
        # for i in [i for i in data]:
        #     option, value = i.split(" ")[0], int(i.split(" ")[1])
        #     if option == "forward":
        #         forward += value
        #     if option == "down":
        #         depth += value
        #     if option == "up":
        #         depth -= value 

        for i in [i for i in data]:
            option, value = i.split(" ")[0], int(i.split(" ")[1])
            if option == "forward":
                forward += value
                depth += aim * value
            if option == "down":
                aim += value
            if option == "up":
                aim -= value 

        
        print(data)
        print(forward, depth, forward * depth)
            


if __name__ == "__main__":
    main()
